Expenses — submit, approve, reimburse

PURPOSE
Employees submit business expenses (travel, meals, materials), a manager approves, accounting
reimburses. No receipt scanner, no bookkeeping depth — just the path of an expense from
"submitted" to "reimbursed", cleanly traceable.

DATA
One table "expenses":
- title (text, required) — what was bought or paid
- expense_date (date, required) — when the expense occurred
- amount (number, required) — amount in euros
- category (text) — e.g. travel, meals, materials, software, other
- status (text) — submitted, approved, rejected, reimbursed; new entries start as "submitted"
- note (text) — context, e.g. occasion or project

Access: everyone sees and edits their own expenses (scope "own").

VIEWS
A table overview "Expenses" with title, date, amount, category and status.

TOOLS
The agent can create expenses (consequential, with approval) and query them (read-only) —
e.g. "my open expenses" or "the total of my expenses this month".
