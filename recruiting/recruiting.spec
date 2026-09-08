Recruiting — move applications through the pipeline

PURPOSE
Whoever fills three positions at once loses applicants in mail inboxes. This extension moves
every application through fixed phases — from received to hired or declined.

DATA
One table "applications":
- candidate (text, required) — the applicant's name
- position (text, required) — the role, e.g. "Service technician"
- source (text) — where it came from, e.g. referral, job board, unsolicited
- phase (text) — received, screening, interview, offer, hired, declined;
  new entries start as "received"
- interview_date (date) — next interview date
- owner (reference to a person from master data) — who drives the process
- note (text) — impression and next steps

Access: the whole team reads, HR edits (scope "all").

VIEWS
A table overview "Applications", grouped by phase, with candidate, position, source, date and
owner. The person reference appears as a name (the platform does this automatically).

TOOLS
The agent can create applications and advance the phase (consequential, with approval) and
query them (read-only) — e.g. "who is in interviews this week?".
