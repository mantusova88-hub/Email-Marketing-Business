# Claude Code – Projekt-Kontext

Dieses Repository ist das zentrale Arbeitsverzeichnis für das **Email Marketing Business**.

## Startverzeichnis

Immer in `/home/user/Email-Marketing-Business` starten.

## Projektstruktur

```
Email-Marketing-Business/
├── 01_Kunden/          # Kundenprojekte mit je eigenem Unterordner
├── 02_Kampagnen/       # Vorlagen, aktive & archivierte Kampagnen
├── 03_Inhalte/         # Texte, Bilder, Banner, Logos
├── 04_Listen/          # E-Mail-Listen, Segmente, Blacklists
├── 05_Analyse/         # Berichte, KPIs, A/B-Tests
├── 06_Automatisierungen/ # Workflows, Trigger, Sequenzen
├── 07_Finanzen/        # Rechnungen, Angebote, Übersichten
├── 08_Rechtliches/     # DSGVO, Verträge, Einwilligungen
├── 09_Tools_Zugaenge/  # API-Keys, Dokumentation
└── 10_Ressourcen/      # Schulungen, Best Practices
```

## Wichtige Regeln

- Neuen Kunden immer als Unterordner in `01_Kunden/<Kundenname>/` anlegen
- Abgeschlossene Kampagnen nach `02_Kampagnen/Archiv/` verschieben
- API-Keys und Passwörter **nicht** in Dateien im Klartext speichern
- DSGVO-Einwilligungsnachweise in `08_Rechtliches/Einwilligungen/` ablegen
