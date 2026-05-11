# /install — Neue Schicht installieren

Installiere eine neue Schicht/ein neues Modul in meinen Workspace.

## Schritte

1. Frage mich: "Welche Schicht möchtest du installieren? Bitte nenne den Ordnernamen im `module-installs/`-Verzeichnis."

2. Lies den angegebenen Ordner und alle darin enthaltenen Dateien.

3. Analysiere den Inhalt:
   - Welche neuen Commands werden hinzugefügt?
   - Welche Kontext-Dateien müssen aktualisiert werden?
   - Welche Skripte sind enthalten?
   - Welche Abhängigkeiten gibt es?

4. Erkläre mir kurz, was diese Schicht macht und was sie zu meinem Workspace beiträgt.

5. Führe die Installation durch:
   - Kopiere Commands in `.claude/commands/`
   - Kopiere Skripte in `scripts/`
   - Aktualisiere `CLAUDE.md` mit neuen Commands
   - Erstelle notwendige Kontext-Dateien

6. Bestätige die erfolgreiche Installation und erkläre die neuen Möglichkeiten.

Starte mit: "Ich schaue mir den Modul-Ordner an..."
