Events — happenings and their registrations

PURPOSE
Customer event, training, open house: the event itself and its registration list belong
together — including capacity and attendance status.

DATA
Two tables.
Table "events":
- title (text, required) — the event
- event_date (date, required) — when it happens
- location (text) — where
- capacity (number) — maximum seats
- status (text) — planned, open, full, past, cancelled; new entries start as "planned"

Table "registrations":
- event (reference to an entry from "events", required) — which event it belongs to
- person_name (text, required) — who registers
- company (reference to an organization from master data) — from which company
- status (text) — registered, confirmed, cancelled, attended; new entries start as "registered"
- note (text) — e.g. dietary wish or plus-one

Access: the whole team reads and edits (scope "all").

VIEWS
Two table overviews: "Events" (title, date, location, capacity, status) and "Registrations"
(event, name, company, status). References appear as names (the platform does this).

TOOLS
The agent can create registrations and set statuses (consequential, with approval) and query
both (read-only) — e.g. "how many confirmations does the summer party have?".
