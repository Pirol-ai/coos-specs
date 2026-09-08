Time off — request and approve absences

PURPOSE
Time-off requests otherwise travel by shout and calendar chaos. Here everyone requests their
absence, approval has a clear path, and the team sees who is away when.

DATA
One table "absences":
- title (text, required) — short reason, e.g. "Summer vacation"
- kind (text) — vacation, sick, training, other
- from_date (date, required) and to_date (date, required) — the period
- days (number) — number of working days
- status (text) — requested, approved, rejected; new entries start as "requested"
- note (text) — cover arrangement or specifics

Access: everyone sees and edits their own absences (scope "own").

VIEWS
A table overview "Absences" with reason, kind, from, to, days and status.

TOOLS
The agent can create absences (consequential, with approval) and query them (read-only) —
e.g. "how many vacation days have I requested this year?".

BUNDLED PROCESS
A published, startable process "Approve a time-off request" (category: People, description:
"From request to the team calendar") with these steps:
1. Check the request for completeness (period, cover)
2. Check team coverage in the period
3. Decide and set the status on the entry
4. Inform the requester and put the absence into the team calendar
