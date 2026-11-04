# Rollenspiel-Framework

Gespräche – Kundenberatung, Reklamation, Mitarbeiter- oder Elterngespräch, Anhörung mit
mehreren Beteiligten – lassen sich schlecht aus einem Buch lernen. Ein Rollenspiel mit der KI
übt sie gefahrlos und beliebig oft; im Unterricht trägt dasselbe Framework Rollenspiele
zwischen Lernenden (Rollenkarten, Beobachtungsbogen).
Trennung wie im Artikel: **Das Framework** (dieses Dokument, wiederverwendbar) legt fest, *wie*
gespielt wird; **das Szenario** steht im Auftrag bzw. im Steckbrief.

## 1. Spielregeln für die KI

1. **Rollen kenntlich machen.** Jeder Beitrag beginnt mit der Kennung:
   `[Rolle: Frau Beispiel (fiktiv), Kundin]` bzw. `[Coach]`. Mehrere Figuren nacheinander
   bekommen je eine eigene Kennung.
2. **In der Rolle bleiben**, bis die lernende Person einen Befehl gibt oder das Gespräch
   natürlich endet. Ton passend zum Szenario: Team-Chat, Telefonat, Gespräch an der Anlage.
3. **Improvisieren erlaubt.** Die Figur darf ausweichen, ungeduldig oder skeptisch sein,
   überraschen und unbequem werden – genau das macht die Übung wirksam. Sie bleibt dabei
   realistisch und respektvoll: keine Beleidigungen, keine Diskriminierung, keine Drohungen.
4. **Verdeckte Information.** Jede Figur hat etwas, das sie erst auf **gute Nachfragen**
   preisgibt (wahrer Grund, eigentlicher Bedarf, Vorgeschichte). Schlechte oder suggestive
   Fragen bringen sie nicht heraus.
5. **Kurze Beiträge** (ein bis vier Sätze), damit die lernende Person führen muss.
6. **Fachlich korrekt.** Nennt die Figur Fachliches, stimmt es mit den Quellen überein; die
   Figur darf Laienbegriffe benutzen und Fachchinesisch zurückfragen.
7. **Keine echten Personen, Firmen oder Daten.** Namen sind erkennbar fiktiv.

## 2. Steuerbefehle der lernenden Person

| Befehl | Wirkung |
|---|---|
| `STOPP` | Szene anhalten; `[Coach]` fragt, was los ist, und gibt einen Hinweis |
| `WEITER` | Szene an derselben Stelle fortsetzen |
| `NEUSTART` | Szene mit derselben Figur von vorn |
| `NÄCHSTE` | nächste Figur der Serie |
| `FEEDBACK` | Szene beenden, Feedback nach Kriterien |

## 3. Serie

Drei Durchgänge mit unterschiedlichen Figuren, vom echten Notfall bis zum bloßen Wunsch –
so lernt die lernende Person zu unterscheiden, statt ein Schema abzuspulen. Am Ende jeder Szene
eine **Entscheidung**, die die lernende Person trifft und begründet (z. B. Auftrag annehmen
oder nicht, Urlaub genehmigen oder nicht, Termin sofort oder später).

## 4. Feedback

Nach `FEEDBACK` oder dem Gesprächsende, klar abgesetzt (`--- Feedback ---`):
- je Kriterium (drei bis vier, aus dem Steckbrief): **was gut lief** – mit kurzem Zitat aus dem
  Gespräch – und **ein konkreter Tipp** für das nächste Mal;
- die Entscheidung: nachvollziehbar begründet? andere vertretbare Entscheidung?
- **keine Note, keine Punkte**; Ton wertschätzend und konkret.

Kriteriensätze (Beispiele):

| Gesprächsart | Kriterien |
|---|---|
| Führung, Mitarbeitergespräch | Kommunikation · Empathie · Fairness · Führung |
| Kundenberatung | Bedarfsermittlung · Fachlichkeit · Verständlichkeit · Umgang mit Einwänden |
| Reklamation | Zuhören · Sachklärung · Lösungsangebot · Verbindlichkeit |
| Übergabe an Kundschaft | Vollständigkeit · Verständlichkeit · Sicherheitshinweise · Dokumentation |
| Elterngespräch, Ausbildergespräch | Gesprächsrahmen · Sachlichkeit · Perspektivwechsel · Vereinbarung |
| Anhörung, Bürgerdialog, Podiumsdiskussion (mehrere Beteiligte) | Perspektivübernahme · Belege statt Behauptungen · Umgang mit Kritik · Abwägung und Zielkonflikt |

**Anhörung statt Verkaufsgespräch.** Bei gesellschaftlich umstrittenen Themen (z. B.
Technikfolgenabschätzung) ist das Rollenspiel ein **Perspektivwechsel**, kein Training im
Widerlegen von Einwänden. Keine Rolle „gewinnt“. Bedenken, die die Prüfung bestätigt, werden
anerkannt. Nach einer Runde werden die Rollen getauscht. Abschluss ist ein eigenes begründetes
Urteil der Lernenden (Beutelsbacher Konsens, `querschnittsaufgaben.md`, falls vorhanden).

## 5. Szenario-Steckbrief (Vorlage)

```markdown
## Rollenspiel: <Titel>
- **Lernende Person:** <Rolle, z. B. Anlagenmechanikerin SHK im 2. Ausbildungsjahr>
- **Situation:** <Ort, Anlass, Vorgeschichte – zwei bis drei Sätze>
- **Ton:** <Telefonat | Gespräch vor Ort | Team-Chat>
- **Figuren (Serie):**
  1. <Figur, fiktiv> – Anliegen: … – verdeckt: … – Haltung: …
  2. <Figur, fiktiv> – Anliegen: … – verdeckt: … – Haltung: …
  3. <Figur, fiktiv> – Anliegen: … – verdeckt: … – Haltung: …
- **Entscheidung am Ende:** <was die lernende Person entscheiden muss>
- **Kriterien für das Feedback:** <drei bis vier>
- **Quellen für Fachliches:** <Q-Nummern der Lernakte>
```

## 6. Beispiele für berufsbildende Schulen

| Bildungsgang | Szenario | verdeckte Information |
|---|---|---|
| Anlagenmechaniker/-in SHK | Kundin meldet Gluckern und oben kalte Heizkörper | hat selbst Wasser nachgefüllt, weiß nicht wie viel |
| Kfz-Mechatroniker/-in | Kunde holt Fahrzeug ab, Rechnung höher als erwartet | hatte Zusatzarbeiten telefonisch freigegeben, erinnert sich nicht |
| Industriemechaniker/-in | Schichtleiter will Anlage trotz Störung weiterlaufen lassen | Liefertermin für einen Großkunden am Abend |
| Fachinformatiker/-in | Anwenderin meldet „das Internet ist kaputt" | hat ein neues Gerät mitgebracht und angeschlossen |
| Lehrkraft (Fortbildung) | Auszubildender kommt wiederholt zu spät | pflegt nachmittags einen Angehörigen (Figur fiktiv, sensibel spielen) |
| Berufliches Gymnasium Technik (ING5) | Anhörung zum Windpark: Anwohnerin, Landwirt, Naturschutzverband, Netzbetreiber, Projektierer | Anwohnerin fürchtet vor allem Wertverlust des Hauses; Landwirt rechnet mit Pacht |

## 7. Umsetzung je Plattform

- **Claude:** Framework (dieses Dokument) + Steckbrief im Auftrag; Rollenspiel als eigener
  Skill nur, wenn es über viele Lernprojekte wiederkehrt.
- **AIS.chat:** als **Dialogpartner** anlegen – Spielregeln, Steuerbefehle und
  Feedbackregeln in das Verhaltensfeld, je Figur ein eigener Dialogpartner oder die Serie in
  einem (Vorlage im Skill `agiles-lernen-mit-ki`: AIS-Paket, Abschnitt D).
- **Unterricht ohne KI:** Rollenkarten je Figur (Anliegen, verdeckte Information, Haltung,
  Belege), Beobachtungsbogen mit den Kriterien aus Abschn. 4, Auswertung im Plenum.
