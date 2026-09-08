Contract register — running contracts and their deadlines

PURPOSE
Rent, leasing, insurance, framework agreements: every company holds a dozen contracts, and the
notice period always comes to mind two weeks too late. The register keeps partner, term and
notice period in one place.

DATA
One table "contract_register":
- title (text, required) — the contract, e.g. "Office lease Main Street"
- partner (reference to an organization from master data) — the contract partner
- kind (text) — rent, leasing, insurance, framework, other
- start_date (date) — contract start
- end_date (date) — contract end or next renewal
- notice_weeks (number) — notice period in weeks
- status (text) — active, cancelled, ended; new entries start as "active"
- note (text) — where the document lives, specifics

Access: the whole team reads, admin edits (scope "all").

VIEWS
A table overview "Contracts" with title, partner, kind, end, notice period and status. The
partner reference appears as a name (the platform does this automatically).

TOOLS
The agent can query the register (read-only) and create/cancel contracts (consequential, with
approval) — e.g. "which contracts must be cancelled by end of quarter?".
