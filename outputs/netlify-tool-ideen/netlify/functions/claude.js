exports.handler = async function (event) {
  const JSON_HEADERS = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
  };

  // CORS preflight
  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 200, headers: JSON_HEADERS, body: '' };
  }

  if (event.httpMethod !== 'POST') {
    return {
      statusCode: 405,
      headers: JSON_HEADERS,
      body: JSON.stringify({ error: 'Methode nicht erlaubt.' }),
    };
  }

  const apiKey = process.env.ANTHROPIC_API_KEY;
  if (!apiKey) {
    return {
      statusCode: 500,
      headers: JSON_HEADERS,
      body: JSON.stringify({
        error: 'API-Key nicht konfiguriert. Bitte ANTHROPIC_API_KEY in den Netlify Umgebungsvariablen setzen.',
      }),
    };
  }

  let branche;
  try {
    const body = JSON.parse(event.body || '{}');
    branche = (body.branche || '').trim();
  } catch {
    return {
      statusCode: 400,
      headers: JSON_HEADERS,
      body: JSON.stringify({ error: 'Ungültige Anfrage. Bitte erneut versuchen.' }),
    };
  }

  if (!branche) {
    return {
      statusCode: 400,
      headers: JSON_HEADERS,
      body: JSON.stringify({ error: 'Bitte eine Branche angeben.' }),
    };
  }

  try {
    const response = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'anthropic-version': '2023-06-01',
        'x-api-key': apiKey,
      },
      body: JSON.stringify({
        model: 'claude-sonnet-4-6',
        max_tokens: 2000,
        system:
          'Du bist ein Experte für digitale Produkte und Tool-Entwicklung. ' +
          'Antworte AUSSCHLIESSLICH mit einem validen JSON-Array. ' +
          'KEIN Markdown, KEINE Backticks, KEIN Text vor oder nach dem Array. ' +
          'Nur das rohe JSON-Array.',
        messages: [
          {
            role: 'user',
            content:
              `Erstelle 5 innovative digitale Tool-Ideen für die Branche: "${branche}".\n` +
              'Diese Tools sollen Selbständige oder Unternehmen in dieser Branche für ihre Kunden entwickeln können.\n\n' +
              'Antworte NUR mit diesem JSON-Array:\n' +
              '[\n' +
              '  {\n' +
              '    "name": "Tool-Name",\n' +
              '    "beschreibung": "Was das Tool macht und welches Problem es löst (2-3 Sätze)",\n' +
              '    "zielgruppe": "Wer das Tool nutzt",\n' +
              '    "marktpotenzial": "Marktgröße und Wachstumschance",\n' +
              '    "monetarisierung": "Wie damit Geld verdient werden kann",\n' +
              '    "schwierigkeit": "Leicht / Mittel / Fortgeschritten / Komplex"\n' +
              '  }\n' +
              ']',
          },
        ],
      }),
    });

    if (!response.ok) {
      const errBody = await response.json().catch(() => ({}));
      const msg = errBody?.error?.message || `API-Fehler: HTTP ${response.status}`;
      return {
        statusCode: response.status,
        headers: JSON_HEADERS,
        body: JSON.stringify({ error: msg }),
      };
    }

    const data = await response.json();
    const raw = data?.content?.[0]?.text || '';
    const match = raw.match(/\[[\s\S]*\]/);

    if (!match) {
      return {
        statusCode: 500,
        headers: JSON_HEADERS,
        body: JSON.stringify({
          error: 'Die KI-Antwort konnte nicht verarbeitet werden. Bitte erneut versuchen.',
        }),
      };
    }

    const tools = JSON.parse(match[0]);

    return {
      statusCode: 200,
      headers: JSON_HEADERS,
      body: JSON.stringify({ tools }),
    };
  } catch (err) {
    return {
      statusCode: 500,
      headers: JSON_HEADERS,
      body: JSON.stringify({
        error: `Serverfehler: ${err.message || 'Unbekannter Fehler'}`,
      }),
    };
  }
};
