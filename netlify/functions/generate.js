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
    const { prompt, apiKey } = JSON.parse(event.body);

    const requestBody = JSON.stringify({
      model: 'claude-opus-4-5',
      max_tokens: 2500,
      messages: [{ role: 'user', content: prompt }]
    });

    return new Promise((resolve) => {
      const options = {
        hostname: 'api.anthropic.com',
        path: '/v1/messages',
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-api-key': apiKey,
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
