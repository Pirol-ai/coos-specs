Approvals — requests with a clear decision

PURPOSE
Purchase over 500 euros? Training? Home-office gear? One request, one decision, one record —
instead of shouts and hallway radio. Deliberately generic for the small approvals of daily
business.

DATA
One table "requests":
- title (text, required) — what is requested
- kind (text) — purchase, training, spend, other
- amount (number) — amount in euros, if relevant
- status (text) — open, approved, rejected; new entries start as "open"
- decided_by (reference to a person from master data) — who decided
- decided_on (date) — when it was decided
- note (text) — reasoning

Access: everyone sees and edits their own requests (scope "own").

VIEWS
A table overview "Requests" with title, kind, amount, status and decision. The person
reference appears as a name (the platform does this automatically).

TOOLS
The agent can create requests (consequential, with approval) and query them (read-only) —
e.g. "which of my requests are still open?".

BUNDLED PROCESS
A published, startable process "Decide a request" (category: Admin, description: "The path of
a request from open to decided") with these steps:
1. Read the request and ask the requester if anything is unclear
2. For amounts above 500 euros, get a second opinion
3. Decide and set status, decider and date on the request
4. Inform the requester about the decision
