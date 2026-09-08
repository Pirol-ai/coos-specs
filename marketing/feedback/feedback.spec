Customer feedback — collect it and take it seriously

PURPOSE
After projects and jobs, feedback arrives — on the phone, by mail, in meetings. Here it lands
structured: with a rating, a source, and the question whether someone must follow up.

DATA
One table "feedback":
- customer (reference to an organization from master data, required) — from whom
- received (date, required) — when it arrived
- rating (number) — rating 1 to 5
- source (text) — e.g. phone, email, meeting, survey
- text (text, required) — the feedback in their words
- follow_up (text) — needed, done, not needed; new entries start as "needed"

Access: the whole team reads and edits (scope "all").

VIEWS
A table overview "Feedback" with customer, date, rating, source and follow-up. The customer
reference appears as a name (the platform does this automatically).

TOOLS
The agent can create feedback entries (consequential, with approval) and query them
(read-only) — e.g. "where is follow-up still needed?" or "this quarter's average rating?".
