Rentals — lend equipment without paper chaos

PURPOSE
Whoever lends devices, tools or rooms needs two things: a catalog of the items and a register
of who has what from when to when — including deposit and return status.

DATA
Two tables.
Table "items":
- title (text, required) — the item, e.g. "Epson projector"
- category (text) — e.g. tech, tools, rooms
- daily_rate (number) — daily rate in euros
- deposit (number) — usual deposit in euros
- note (text) — condition, accessories

Table "loans":
- item (reference to an entry from "items", required) — what is lent out
- customer (reference to an organization from master data) — to whom
- from_date (date, required) and to_date (date, required) — the period
- deposit_paid (number) — deposit taken
- status (text) — reserved, out, returned, overdue; new entries start as "reserved"

Access: the whole team reads and edits (scope "all").

VIEWS
Two table overviews: "Items" (title, category, daily rate, deposit) and "Loans" (item,
customer, from, to, status). References appear as names (the platform does this).

TOOLS
The agent can create loans and change their status (consequential, with approval) and query
both (read-only) — e.g. "what is currently out and overdue?".
