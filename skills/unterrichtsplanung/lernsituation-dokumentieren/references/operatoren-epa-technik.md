# Operatoren nach EPA Technik (Abitur Berufliches Gymnasium Technik)

Für Abiturvorschläge gilt diese Zuordnung – sie weicht in einigen Punkten von der allgemeinen
Bibliotheksliste (`operatoren-afb.md`, falls vorhanden) ab (z. B. *begründen* hier AFB II, *dokumentieren* AFB III).
Maschinenlesbar: `abitur_check.py` (Skill `abiturvorschlag-erstellen`) liest die Tabellen dieser Datei – Kopfzeilen und Komma-Listen beibehalten.
Gilt auch für Klausuren der Qualifikationsphase im BG (`klausur-erstellen`, Typ `klausur-bg`).
Abgeglichen mit der Operatorenliste des Kultusministeriums für Technik – Mechatronik (Abitur 2024,
Fassung V02): deckungsgleich. *zeichnen* verlangt dort ausdrücklich genormte Symbole, *überprüfen*
steht als „überprüfen und nachweisen“. 🔎 Vor jedem Prüfungsjahr mit der gültigen Fassung abgleichen.

**Gilt für das Fach Technik.** Für das Fach *Berufliche Informatik* hat die EPA eine eigene
Liste, in der u. a. *testen*, *erweitern*, *vervollständigen*, *erstellen*, *implementieren*,
*bezeichnen* und *kennzeichnen* Operatoren sind – siehe Abschnitt *Berufliche Informatik* am Ende.

| AFB I | AFB I/II | AFB II | AFB II/III | AFB III |
|---|---|---|---|---|
| beschreiben, nennen | berechnen, bestimmen, darstellen, erläutern, erklären, vergleichen, zeichnen | ableiten, abschätzen, auswerten, begründen, durchführen, ermitteln, konstruieren, optimieren, skizzieren, strukturieren, ordnen | analysieren, untersuchen, beurteilen, bewerten, Stellung nehmen, dimensionieren, entwickeln, entwerfen, überprüfen, nachweisen, übertragen | dokumentieren |

## Häufige Fehlzuordnungen
| Operator | richtig |
|---|---|
| begründen | nur AFB II – nie AFB I |
| dokumentieren | nur AFB III – nie AFB I oder II |
| skizzieren, ermitteln, ableiten | nur AFB II – nie AFB I |
| analysieren, beurteilen, bewerten, entwickeln, entwerfen, überprüfen | AFB II/III – nie allein AFB I |
| beschreiben, nennen | nur AFB I – nie AFB II oder III |

## Keine EPA-Operatoren (Technik)
*erstellen, kommentieren, implementieren, speichern, reduzieren, programmieren, konfigurieren,
installieren, testen, codieren, notieren, ergänzen, eintragen, ausfüllen, lesen, eingeben,
ausgeben, anpassen, erweitern, umsetzen, aufbauen, validieren, kompilieren, abbilden,
vervollständigen* – zulässig nur, wenn im Lehrermaterial als **erweiterte Operatoren mit
AFB-Zuordnung** dokumentiert („Die Operatorenliste wurde … erweitert").

**Software-, CAD- und Simulationsaufgaben:** Das KMK-Aufgabenbeispiel Ingenieurwissenschaften
(2021) verwendet für Arbeiten am PC auch *vervollständigen, erstellen, anpassen, speichern*
(Baugruppe im CAD-System). Solche Operatoren sind zulässig, wenn das Lehrermaterial sie als
erweiterte Operatoren mit AFB ausweist; die Begutachtung meldet sie dann als ⚠️ Hinweis, nicht
als Mangel. Wo möglich einen EPA-Operator voranstellen (z. B. „Entwickeln Sie … und speichern
Sie …“). Für Programmieraufgaben im BG: *entwickeln*, *entwerfen*, *überprüfen* (EPA) statt
*programmieren*, *implementieren*, *testen*.

Formulierungen ohne Operator: „Geben Sie … an" (→ Nennen/Bestimmen), „Tragen Sie … ein",
„Füllen Sie … aus", „Schreiben Sie …".

## Regeln
- Ein Operator deckt höchstens zwei aufeinanderfolgende AFB ab.
- Operatoren in Schülermaterial und Erwartungshorizont identisch.
- Arbeitsauftrag im Imperativ mit „Sie".
- Im Erwartungshorizont steht der Operator des Auftrags als substantivierter Infinitiv
  (*Berechnen der …*, *Entwickeln eines …*) – so bleiben Auftrag und Bewertung erkennbar gleich.

## Berufliche Informatik (EPA Berufliche Informatik)

Die Operatorenliste der EPA Berufliche Informatik nennt 30 Operatoren mit einem Bereich von
Anforderungsbereichen (1, 1–2, 2, 2–3, 3). Die Liste unten ist die Zuordnung der Bibliothek.
🔎 Mit der gültigen EPA-Fassung abgleichen; Fachkonferenzbeschlüsse haben Vorrang.

| AFB I | AFB I/II | AFB II | AFB II/III | AFB III |
|---|---|---|---|---|
| bezeichnen | anwenden, berechnen, beschreiben, darstellen, erläutern, ermitteln, skizzieren, vervollständigen, zeichnen | begründen, benennen, erstellen, implementieren, kennzeichnen | auswerten, bestimmen, definieren, diskutieren, dokumentieren, einordnen, entwerfen, entwickeln, erweitern, kommentieren, modellieren, testen, übertragen | beurteilen, Stellung nehmen |

- **Nicht in der Liste:** *nennen, angeben, aufzählen, vergleichen, analysieren, untersuchen,
  überprüfen, abschätzen, ableiten, optimieren, konstruieren, programmieren* – zulässig nur als
  im Lehrermaterial dokumentierter erweiterter Operator mit AFB.
- **Formatanweisungen** („Tragen Sie … in die Tabelle ein“, „Kreuzen Sie … an“) stehen **nach**
  einem Operator der Liste („**Vervollständigen** Sie das Struktogramm. Tragen Sie die Einträge
  ① bis ⑤ in die Tabelle ein.“); sie ersetzen ihn nicht.
- Der AFB einer Teilaufgabe liegt im Bereich des Operators und hängt vom Unterricht davor ab
  (*Ermitteln* 1–2: Schleife durchspielen = II; *Bestimmen* 2–3: Wert aus dem Struktogramm
  = II, alle Startwerte rückwärts = III).
- Operatoren für Lernende erklären: `klausur-erstellen`, `references/druckfassung-antwortformate.md`.
