# Data Engineering Übungsblatt 1

## Thema

Bis das Rechenzentrum wieder funktioniert wird diese Datei das Aufgabenblatt sein.

Finde eine Datenquelle für Musik- und Songdaten (Songname, Album, Interpret, Streams, Veröffentlichungsdatum, ...).

Bringe Rohdaten in Format für SQL Datenbank.

Es gibt 4 Tabellen:

- Songs,
- Künstler,
- Alben,
- "beinhaltet" (m:n Tabelle)

### Notizen

#### Access Tokens

Man muss sich ständig ein neues Access Token generieren lassen (läuft nach 1h ab).

Token muss in jede Anfrage rein.

#### Anfragen

##### Prozess

- Suche selbst Interpreten auf Spotify von denen man die Daten haben möchte
- Kopiere ihre SpotifyID in ```data_aquisition```

    Es werden dann für alle Interpreten ihre Albendaten gespeichert.

    Ein weiteres Programm übernimmt dann die AlbumID von jedem Album und lässt ein batch Skript laufen, dass für diese Alben alle Songs scraped und speichert.

- Datenbereinigung
- Einführung in Datenbank