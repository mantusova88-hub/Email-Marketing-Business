# Canva Ordner-Workflow — Standing Rule

> Seit 01.10.2026 (KW40). Fest einzuhalten bei jeder neuen Content-Woche,
> ohne dass Monika erneut danach fragen muss.

## Regel

Sobald eine neue Woche mit neuen Karussellbeiträgen und neuen Instagram-Stories
beginnt:

1. Zwei neue, leere Ordner im Canva-Wurzelverzeichnis (`root`) anlegen:
   - `KW<Nummer> Karussells`
   - `KW<Nummer> Stories`
2. Jedes neu gebaute Tages-Design (Karussell bzw. Story) sofort in den
   passenden neuen Wochenordner verschieben (`move-item-to-folder`).
3. Die Designs der vorherigen Woche(n) aus den alten Ordnern in den
   bestehenden Archiv-Ordner verschieben, nicht löschen:
   - Archiv-Ordner: `FAHVVV3kAPs` (Name „Archiv", direkt im Root)
4. Die alten, jetzt leeren Wochenordner können stehen bleiben oder auf
   Wunsch von Monika gelöscht werden, aber nie einfach weiter befüllt.

## Warum

Monika will für jede Woche klar getrennte, frische Ordner für Karussell und
Story, damit alte und aktuelle Beiträge sich nicht vermischen. Alte Wochen
gehören ins Archiv, nicht gelöscht.

## Bezug zur 20-Uhr-Posting-Routine

Der nächtliche Posting-Trigger (`trig_01X3P3TsT9cjb4UjyMG72PHw`) sucht die
Tages-Designs über `list-folder-items`/`search-designs` nach Wochentag im
Titel, notfalls mit Root-Suche, falls sich Ordnernamen geändert haben. Die
aktuellen Wochenordner müssen daher immer eindeutig als „aktuell" erkennbar
sein (z. B. durch die KW-Nummer im Namen), damit die Routine dort zuerst
sucht.

## Aktueller Stand

- Archiv: `FAHVVV3kAPs`
- KW40 Karussells: `FAHWv2QkmzU`
- KW40 Stories: `FAHWv-VhKz0`
