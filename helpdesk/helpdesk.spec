Helpdesk — incidents and requests as tickets

PURPOSE
Customer requests and incidents need a number, a priority and an owner — otherwise the inbox
rules. A lean ticket register with a due date, without SLA science.

DATA
One table "tickets":
- title (text, required) — the issue in one line
- customer (reference to an organization from master data) — who reports it
- priority (text) — low, normal, high, critical; new entries start as "normal"
- status (text) — new, in progress, waiting on customer, solved; new entries start as "new"
- assignee (reference to a person from master data) — who works it
- due (date) — promised reaction/solution date
- note (text) — the thread in keywords

Access: the whole team reads and edits (scope "all").

VIEWS
A table overview "Tickets", grouped by status, with issue, customer, priority, assignee and
due date. References appear as names (the platform does this automatically).

TOOLS
The agent can create tickets, assign them and set status (consequential, with approval) and
query them (read-only) — e.g. "which critical tickets are open?".

BUNDLED PROCESS
A published, startable process "Handle a critical ticket" (category: Service, description:
"Standard flow for a critical incident") with these steps:
1. Take the ticket, set priority to critical and assign an owner
2. Call the customer with a status within one hour
3. Fix the incident or provide a workaround
4. Document the solution on the ticket and set status to solved
5. Follow up with the customer after two days
