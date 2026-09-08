Visitors — who was in the building when

PURPOSE
Contractors, applicants, customer visits: a simple visitor book with host and check-in/out —
for the front desk overview and the question "who was here last week?".

DATA
One table "visits":
- visitor (text, required) — the guest's name
- company (text) — the guest's company
- host (reference to a person from master data) — who receives the guest
- visit_date (date, required) — the day of the visit
- checked_in (text) — arrival time, e.g. "09:30"
- checked_out (text) — leaving time
- note (text) — reason for the visit

Access: the whole team reads and edits (scope "all").

VIEWS
A table overview "Visits" with guest, company, host, date, arrival and leave. The host
reference appears as a name (the platform does this automatically).

TOOLS
The agent can create visits and record check-in/out (consequential, with approval) and query
them (read-only) — e.g. "who is in the building today?".
