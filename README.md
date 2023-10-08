# Data Engineering Spotify

## Thema

Das Herunterladen von Spotify Song-, Alben- und Künstlerdaten und Representieren dieser in einer MySQL Datenbank.
Ziel sind Auswertungen basierend auf dieser Datenbank aber dieses Repository beschäftigt sich mit der Datenbeschaffung und Datenpersistenz.

## Prozess

Das gesamte Programm kann `main.py` ausgeführt werden.

Der Prozess ist in 3 Bestandteile gegliedert.

### Datenbeschaffung

Datenbeschaffung läuft über die Spotify API. Auf diese wird über Bash Scripte im `scripts` Ordner zugegriffen.

### Datenbereinigung

Die Daten werden in der `data_pipeline` vorverarbeitet. Es werden Datenstrukturen aufgelöst, hierbei werden Dupletten erstellt die sich nur in dem aufgelösten Attribut unterscheiden. Es werden auch unrelevante Attribute gelöscht.

Zuletzt werden alle Daten aus einer Datenquelle(Songs, Artists, Albums) in je einem neuen Dokument `complete_data.json` zusammengefügt und die alten Daten gelöscht.

### Datenpersistierung

Für Datenbankschema siehe `schema.png`.

Die Daten müssen noch bearbeitet werden um der 3. Normalform zu folgen und Redundanzen zu vermeiden bzw. aufzulösen.

Einfügen der Daten in die Datenbank läuft über generierte Insert Statements basierend auf den Daten.




