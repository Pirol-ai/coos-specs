Field service — plan and close on-site visits

PURPOSE
Whoever sends technicians to customers needs the visit list: who drives where and when, what
is to be done, and what was done. Planned in the office, closed after the visit.

DATA
One table "visits":
- title (text, required) — the job, e.g. "Heating system service"
- customer (reference to an organization from master data, required) — at whose site
- technician (reference to a person from master data) — who drives
- visit_date (date, required) — the appointment
- status (text) — planned, on the way, done, postponed; new entries start as "planned"
- report (text) — what was done on site
- note (text) — address/access, materials

Access: the whole team reads, dispatch and technicians edit (scope "all").

VIEWS
A table overview "Visits" with job, customer, technician, date and status. References appear
as names (the platform does this automatically).

TOOLS
The agent can create and close visits (consequential, with approval) and query them
(read-only) — e.g. "which visits does Milan drive tomorrow?".
