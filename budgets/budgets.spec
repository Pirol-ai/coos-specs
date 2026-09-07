Budgets — yearly budgets by category at a glance

PURPOSE
How much is planned for what this year, and how much is already spent? This extension keeps
budget lines (e.g. marketing, training, tooling) with planned and actual amounts — deliberately
a simple self-report, not bookkeeping.

DATA
One table "budget_lines":
- title (text, required) — the budget line, e.g. "Marketing 2026"
- year (number, required) — the year, e.g. 2026
- planned (number, required) — planned amount in euros
- spent (number) — spent so far, maintained by hand
- owner (reference to a person from master data) — who owns the line
- note (text) — what counts into this line

Access: the whole team reads, owners edit (scope "all").

VIEWS
A table overview "Budget lines" with title, year, planned, spent and owner. The person
reference should appear as a name (the platform does this automatically).

TOOLS
The agent can query budget lines (read-only) and update the spent amount (consequential,
with approval) — e.g. "book 500 euros onto marketing".
