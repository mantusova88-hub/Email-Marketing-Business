## Wöchentlicher Listenhygiene-Check

### Kontext
Saubere E-Mail-Listen = bessere Zustellbarkeit = mehr Umsatz.
Dieser Agent prüft jeden Sonntag die Liste auf Problemkontakte.

API-Zugangsdaten in `.env`:
- AC_API_URL, AC_API_KEY

### Schreibregeln
- Zahlen konkret — keine ungefähren Angaben
- Empfehlung immer mit Begründung
- Entscheidung liegt bei dir — Agent macht Vorschlag, du entscheidest

### Aufgabe

1. **Bounce-Analyse**:
   - GET /api/3/contacts?filters[bounced]=1
   - Hard Bounces zählen → sofort löschen empfehlen
   - Soft Bounces zählen → beobachten empfehlen

2. **Inaktive Kontakte finden**:
   - Kontakte ohne Öffnung in 90 Tagen
   - Kontakte ohne Klick in 180 Tagen
   - Anzahl ausgeben

3. **Re-Engagement-Check**:
   - Gibt es eine aktive Re-Engagement-Automation?
   - Wenn nein → Empfehlung erstellen

4. **Spam-Risiko prüfen**:
   - Unsubscribe-Rate der letzten 30 Tage
   - Wenn > 0.5% → Warnung

5. **Report mit Entscheidungsvorschlägen**:

```
🧹 Listenhygiene Report — [DATUM]

📊 Aktuelle Listengröße: X Kontakte

🔴 Sofort handeln:
• X Hard Bounces → löschen? [Ja / Nein]
• X Spam-Markierungen → löschen? [Ja / Nein]

🟡 Diese Woche entscheiden:
• X Soft Bounces (3+ mal) → löschen oder warten?
• X Inaktive (90+ Tage) → Re-Engagement oder löschen?

🟢 Alles OK:
• Unsubscribe-Rate: X% (Ziel: < 0.5%)

💡 Empfehlung:
• [Konkreter nächster Schritt]
```

6. **Report speichern** unter:
   `outputs/reports/[DATUM]-listenhygiene.md`
