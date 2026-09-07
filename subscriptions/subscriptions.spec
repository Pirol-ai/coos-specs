Subscriptions — recurring contracts and their notice periods

PURPOSE
Maintenance contracts, software subscriptions, retainers: recurring revenue and cost with a
term and a notice period. The extension answers the two questions nobody else can: what is
running, and what must be cancelled or renewed by when?

DATA
One table "contracts":
- title (text, required) — what the subscription is, e.g. "Hosting customer X"
- partner (reference to an organization from master data) — customer or vendor
- amount (number, required) — amount per interval in euros
- interval (text) — monthly, quarterly, yearly
- direction (text) — income or cost
- end_date (date) — end of term or next renewal date
- notice_weeks (number) — notice period in weeks
- status (text) — active, cancelled, ended; new entries start as "active"

Access: the whole team reads, authorized people edit (scope "all").

VIEWS
A table overview "Contracts" with title, partner, amount, interval, direction, end of term and
status. The partner reference appears as a name (the platform does this automatically).

TOOLS
The agent can create and cancel/end contracts (consequential, with approval) and query them
(read-only) — e.g. "which contracts must I cancel within the next 8 weeks?".
