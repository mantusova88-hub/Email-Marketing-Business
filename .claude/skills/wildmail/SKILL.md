---
name: wildmail
description: Wild Mail (ActiveCampaign) einrichten und automatisieren — Listen, Tags, Automationen, Kampagnen, Formulare. Nutze diesen Skill bei "Wild Mail", "ActiveCampaign", "Automation", "Tag", "Liste", "Segment", "Autoresponder einrichten", "Kampagne anlegen", "Kontakte", "Formular".
---

# wildmail — Monikas E-Mail-Plattform

**Wild Mail basiert auf ActiveCampaign.** Technisch identisch — deshalb passen
ActiveCampaign-Anleitungen und die ActiveCampaign-Anbindung direkt.

Das ist das Tool, das Monika ihren Kundinnen beibringt. Ihr eigenes Setup
muss vorbildlich sein — sie zeigt es im Zweifel her.

---

## 1. Grundprinzip: Tags statt Listen

Der häufigste Anfängerfehler: für jedes Thema eine neue Liste.
Das führt zu Chaos, Doppel-Kontakten und doppelten Kosten.

**Richtig:**
- **Eine Hauptliste** („Newsletter")
- **Tags** für alles Weitere: Herkunft, Interesse, Kaufstatus

### Tag-Schema für Monika

| Präfix | Zweck | Beispiele |
|---|---|---|
| `quelle-` | Woher kam sie? | `quelle-starter-guide`, `quelle-instagram`, `quelle-ads` |
| `interesse-` | Wofür interessiert sie sich? | `interesse-automation`, `interesse-technik` |
| `kunde-` | Was hat sie gekauft? | `kunde-checkliste`, `kunde-nischengenerator` |
| `status-` | Wo steht sie? | `status-neu`, `status-aktiv`, `status-inaktiv` |

**Regel:** Tag-Namen immer klein, mit Bindestrich, nie umbenennen
(bricht laufende Automationen).

---

## 2. Die Basis-Automationen

### A) Willkommens-Automation
```
Trigger:  Tag "quelle-starter-guide" wird vergeben
   ↓
Mail 1:   sofort — Freebie ausliefern
Warten:   2 Tage
Mail 2:   Monikas Geschichte
Warten:   2 Tage
Mail 3:   Quick Win
Warten:   2 Tage
Mail 4:   Das größte Missverständnis
Warten:   2 Tage
Mail 5:   Angebot (Mini-Produkt)
   ↓
Tag setzen: "status-aktiv"
```
Inhalte → Skill `emails`

### B) Kauf-Automation
```
Trigger:  Kauf in Systeme.io (oder Tag "kunde-…")
   ↓
Mail:     Produkt ausliefern + Erwartung setzen
Warten:   3 Tage
Mail:     "Kommst du klar?" — echte Frage, lädt zur Antwort ein
Warten:   7 Tage
Mail:     Nächster sinnvoller Schritt
```

### C) Reaktivierung
```
Trigger:  seit 90 Tagen keine Mail geöffnet
   ↓
Mail 1:   "Liest du noch mit?"
Mail 2:   bestes Stück Content nochmal
Mail 3:   "Ich räume auf — bleib oder geh"
   ↓
Wenn keine Reaktion: Tag "status-inaktiv" → aus dem Hauptversand nehmen
```

> 💡 Inaktive Kontakte kosten Geld und drücken die Öffnungsrate.
> Aufräumen ist kein Verlust — es ist Hygiene.

---

## 3. Zustellbarkeit — die Basics

Ohne das landet alles im Spam:

- [ ] **Absender-Domain authentifiziert** (SPF, DKIM, DMARC) — bei Wild Mail einrichtbar
- [ ] **Echte Absenderadresse** (`monika@…`, nicht `noreply@`)
- [ ] **Physische Adresse im Footer** (rechtlich Pflicht)
- [ ] **Abmeldelink** in jeder Mail — sichtbar, nicht versteckt
- [ ] **Double Opt-in** aktiv (DSGVO-Pflicht in Deutschland!)
- [ ] Keine Spam-Wörter im Betreff („GRATIS!!!", „100% garantiert")
- [ ] Regelmäßig senden — lange Pausen schaden mehr als seltene Mails

---

## 4. Was ich über die Anbindung tun kann

Die ActiveCampaign-Anbindung erlaubt mir direkt:

| Tun | Tools |
|---|---|
| Kontakte anlegen/aktualisieren, taggen | `create_or_update_contact`, `add_tag_to_contact` |
| Listen & Tags verwalten | `create_list`, `create_contact_tag` |
| Kampagnen ansehen & bearbeiten | `list_campaigns`, `update_campaign` |
| Automationen ansehen, Kontakte hinzufügen | `list_automations`, `add_contact_to_automation` |
| Custom Fields anlegen | `create_contact_custom_field` |

### Grenzen — ehrlich benennen
- ❌ **Keine Aggregate.** Durchschnittliche Öffnungsrate, Gesamtumsatz, Conversion —
  das muss Monika im Dashboard ablesen. Ich rate nicht und rechne nichts zusammen.
- ❌ Automationen können nicht komplett neu **gebaut** werden — ich liefere den
  Bauplan, Monika klickt ihn zusammen (oder ich führe sie Schritt für Schritt).

---

## 5. Wenn ich eine Anleitung schreibe

Monikas Tech-Level und das ihrer Kundinnen: **Technik macht Angst.**

**Deshalb:**
- Jeder Klick einzeln beschrieben — „Klicke oben links auf **Kontakte**"
- Button-Beschriftungen **fett** und wörtlich zitieren
- Nach jedem Abschnitt: „Das solltest du jetzt sehen: …"
- Niemals „einfach", „nur kurz", „selbsterklärend" schreiben
- Wenn etwas schiefgehen kann: vorher sagen, was zu tun ist

Vorbild für den Ton: `reference/systeme-io-verkaufsseite.md` — genau so.

Fertige Anleitungen nach `reference/` speichern, damit Monika sie
auch ihren Kundinnen geben kann.
