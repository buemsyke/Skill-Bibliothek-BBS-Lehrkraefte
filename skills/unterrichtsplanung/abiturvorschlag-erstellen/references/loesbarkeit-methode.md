# Lösbarkeits- und Richtigkeitsprüfung je Teilaufgabe

Zwei Fragen je Teilaufgabe:
- **A Lösbarkeit:** Hat der Prüfling alle nötigen Informationen, um die Aufgabe in der
  vorgesehenen Zeit fachlich zu lösen?
- **B Richtigkeit:** Ist die Musterlösung im Erwartungshorizont fachlich korrekt?

Methode aus der Gutachtenpraxis der Fachberatung (GutachtenAbiturklausur), verallgemeinert.

## Regeln (verbindlich)
1. **Konfidenz < 75 → „unklar"** (Lehrkraft prüft persönlich, kein Befund).
2. Verweist die Aufgabe auf Abbildung, Datenblatt, Schaltbild oder Programmausdruck, dessen
   Inhalt nicht als Text vorliegt → **„nicht_pruefbar"**.
3. Musterlösung leer oder bruchstückhaft → Richtigkeit **„nicht_pruefbar"**.
4. Lieber „nicht_pruefbar" als raten.
5. Begründung kurz und konkret, mit Bezug auf die Aufgabe; Rechnungen **nachrechnen**.
6. Mehrere „nicht_pruefbar" in einer Aufgabe → Hinweis, dass digitale/grafische Anlagen
   bereitgestellt bzw. beschrieben werden müssen (S.2/S.3).

## Ergebnisschema je Teilaufgabe

```json
{
  "teilaufgabe": "1.3",
  "loesbarkeit": "ja | nein | unklar | nicht_pruefbar",
  "loesbarkeit_konfidenz": 0,
  "loesbarkeit_begruendung": "…",
  "fehlende_information": ["…"],
  "richtigkeit": "ja | nein | unklar | nicht_pruefbar",
  "richtigkeit_konfidenz": 0,
  "richtigkeit_begruendung": "…",
  "fehler_in_loesung": ["…"]
}
```

Im Gutachten erscheint daraus die Tabelle *Teilaufgabe | Lösbarkeit | Richtigkeit | Begründung |
Konfidenz*; „nein" mit Konfidenz ≥ 75 wird zum Befund (Kriterium 4.1/4.2 bzw. E.4).

## Typische fachliche Fehlermuster (Prüfschwerpunkte)

**Steuerungstechnik:** gegenseitige Verriegelung bei Drehrichtungsumkehr; Endlagenschalter;
Stopp/Not-Halt in allen Zuständen wirksam; Wertetabellen konsistent; Schaltbilder ohne Text
→ nicht_pruefbar.

**Netzwerke:** Netzadresse = IP AND Maske; Broadcast = Netz OR NOT Maske; private Bereiche
10/8, 172.16/12, 192.168/16; nutzbare Hosts 2ⁿ − 2; RAID 5 ≥ 3 Platten, Nutzkapazität
(n−1)·Plattengröße; WPA2/WPA3 statt WEP; Maske in Folgeaufgaben konsistent.

**Software/Datenbanken:** Syntax; Algorithmus passt zur Aufgabe; SQL-Strings zusammensetzen →
Injection-Risiko (Prepared Statements); `hashCode()` ist kein kryptografischer Hash;
Synchronisation bei geteiltem Zustand.

**Messtechnik:** Kennlinie linear interpolieren (falls nicht anders angegeben); Einheiten
konsistent; A/D-Wandler 2ⁿ Stufen, LSB = U_ref/2ⁿ.

**Metalltechnik/Mechatronik:** Passungen (Höchst-/Mindestspiel bzw. -übermaß aus Grenzabmaßen);
Schnittdaten aus Tabellen (Werkstoff, Schneidstoff); Kräfte F = p·A·η; Festigkeit mit
Sicherheitszahl; Prüfmittel passend zur Toleranz; Sicherheitsregeln bei Instandhaltung
(Stillsetzen, gegen Wiedereinschalten sichern). Normangaben nur mit Fundstelle.

**Kaufmännische Tabellenkalkulation:** relative/absolute Bezüge; Rundung; SVERWEIS mit
genauer Übereinstimmung; Datumsfunktionen; Ergebnis plausibel zur Datentabelle.
