Quotes — from draft to acceptance

PURPOSE
Small service companies write quotes and lose track of which one sits with which customer and
which is about to expire. This extension keeps a lean quote register next to the CRM: a quote
belongs to an organization from master data and moves through a clear status.

DATA
One table "quotes":
- title (text, required) — short name of the quote
- customer (reference to an organization from master data, required) — the recipient
- amount (number) — quote total in euros
- valid_until (date) — how long the quote stands
- status (text) — draft, sent, accepted, rejected; new entries start as "draft"
- note (text) — scope in keywords or special terms

Access: the whole team reads, quote writers edit (scope "all").

VIEWS
A table overview "Quotes" with title, customer, amount, valid until and status. The customer
reference should appear as a name (the platform does this automatically).

TOOLS
The agent can create quotes and change their status (both consequential, with approval) and
query them (read-only) — e.g. "which quotes expire this week?".
