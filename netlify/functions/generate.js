const https = require('https');

exports.handler = async (event) => {
  const headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Content-Type': 'application/json'
  };

  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 200, headers, body: '' };
  }

  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, headers, body: JSON.stringify({ error: 'Method not allowed' }) };
  }

  try {
    const { prompt, systemPrompt, apiKey } = JSON.parse(event.body);

    // API key: env variable (secure, production) or client fallback (dev/legacy)
    const key = process.env.ANTHROPIC_API_KEY || apiKey;
    if (!key) {
      return {
        statusCode: 401,
        headers,
        body: JSON.stringify({ error: 'Kein API-Key konfiguriert. Bitte ANTHROPIC_API_KEY in den Netlify-Umgebungsvariablen hinterlegen.' })
      };
    }

    const requestBody = JSON.stringify({
      model: 'claude-sonnet-4-6',
      max_tokens: 2500,
      ...(systemPrompt ? { system: systemPrompt } : {}),
      messages: [{ role: 'user', content: prompt }]
    });

    return new Promise((resolve) => {
      const options = {
        hostname: 'api.anthropic.com',
        path: '/v1/messages',
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-api-key': key,
          'anthropic-version': '2023-06-01',
          'Content-Length': Buffer.byteLength(requestBody)
        }
      };

      const req = https.request(options, (res) => {
        let data = '';
        res.on('data', (chunk) => { data += chunk; });
        res.on('end', () => {
          try {
            const parsed = JSON.parse(data);
            if (res.statusCode !== 200) {
              resolve({
                statusCode: res.statusCode,
                headers,
                body: JSON.stringify({ error: parsed.error?.message || 'API Fehler' })
              });
            } else {
              resolve({ statusCode: 200, headers, body: data });
            }
          } catch (e) {
            resolve({ statusCode: 500, headers, body: JSON.stringify({ error: 'Parse error' }) });
          }
        });
      });

      req.on('error', (err) => {
        resolve({ statusCode: 500, headers, body: JSON.stringify({ error: err.message }) });
      });

      req.write(requestBody);
      req.end();
    });

  } catch (err) {
    return { statusCode: 500, headers, body: JSON.stringify({ error: err.message }) };
  }
};
