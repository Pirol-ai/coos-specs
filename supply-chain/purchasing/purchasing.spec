Purchasing — orders from request to delivery

PURPOSE
Not a procurement suite, but the order register of a small business: what did we request or
order from which supplier, what does it cost, and has it arrived?

DATA
One table "orders":
- title (text, required) — what is ordered, in one line
- supplier (reference to an organization from master data, required) — the supplier
- amount (number) — order value in euros
- order_date (date) — when it was ordered
- expected (date) — when delivery is expected
- status (text) — requested, ordered, delivered, cancelled; new entries start as "requested"
- note (text) — line items in keywords

Access: the whole team reads, buyers edit (scope "all").

VIEWS
A table overview "Orders" with title, supplier, value, ordered on, expected and status. The
supplier reference appears as a name (the platform does this automatically).

TOOLS
The agent can create orders and advance their status (consequential, with approval) and query
them (read-only) — e.g. "what is ordered but not yet delivered?".
