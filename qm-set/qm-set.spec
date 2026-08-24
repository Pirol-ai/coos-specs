QM-Set — Audits und Qualitätsprozesse für kleine Dienstleister

ZWECK
Ein leichtgewichtiges Qualitätsmanagement: interne Audits planen und dokumentieren, und die zwei
Standardprozesse mitliefern, die jedes QM lebendig machen (Kunden-Onboarding, Reklamation).

DATEN
Eine Tabelle "audits":
- title (Text, Pflicht) — worum es in dem Audit geht
- audit_date (Datum) — wann es stattfindet/stattfand
- auditor (Verweis auf eine Person aus den Stammdaten) — wer es durchführt
- status (Text) — z. B. geplant, läuft, abgeschlossen
- findings (Text) — die Feststellungen in Kurzform

Zugriff: jeder sieht und pflegt seine eigenen Audits (scope "own").

ANSICHTEN
Eine Tabellen-Übersicht "Audits" mit allen Spalten. Die Referenz auf den Auditor soll als Name
erscheinen (macht die Plattform automatisch).

WERKZEUGE
Der Agent soll Audits anlegen (folgenreich, mit Freigabe) und abfragen (nur lesend) können.

MITGELIEFERTE PROZESSE
Siehe process.md — beide Prozesse gehören zur Extension und werden bei der Installation als
veröffentlichte, startbare Prozesse angelegt. Jeder Prozess trägt eine Kategorie und eine kurze
Beschreibung, damit die Prozess-App sie sauber gruppiert und erklärt.
