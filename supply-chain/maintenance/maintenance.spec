Maintenance — machines and their service dates

PURPOSE
Every machine has a service rhythm, and somebody has to remember it. This extension keeps the
machine list with last and next service date and ships the standard process for a service.

DATA
One table "machines":
- title (text, required) — the machine, e.g. "Compressor hall 1"
- serial (text) — serial or inventory number
- responsible (reference to a person from master data) — who owns the maintenance
- last_service (date) — last service
- next_service (date) — next due service
- interval_months (number) — service interval in months
- status (text) — in operation, in maintenance, retired; new entries start as "in operation"

Access: the whole team reads, responsibles edit (scope "all").

VIEWS
A table overview "Machines" with machine, responsible, last and next service and status. The
person reference appears as a name (the platform does this automatically).

TOOLS
The agent can query machines (read-only) and advance service dates (consequential, with
approval) — e.g. "which services are due in the next 30 days?".

BUNDLED PROCESS
A published, startable process "Perform machine service" (category: Operations, description:
"Standard flow of a planned machine service") with these steps:
1. Align the service date with the responsible person
2. Take the machine out of operation and secure it
3. Perform the service per manufacturer spec and note findings
4. Put the machine back into operation and verify function
5. Record the service date on the machine and set the next due date
