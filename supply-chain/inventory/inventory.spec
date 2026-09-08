Inventory — stock and minimums without a scanner

PURPOSE
A light stock register for consumables and small parts: what sits where, how much is there,
and where is stock below minimum? Maintained by hand, meant for the weekly look, not for
booking runs.

DATA
The app is called "Inventory". One table "stock":
- title (text, required) — the article, e.g. "Cable ties 200mm"
- location (text) — storage location, e.g. "Shelf B2"
- quantity (number, required) — current stock
- unit (text) — pieces, meters, packs
- min_quantity (number) — minimum stock that triggers reordering
- note (text) — supplier or article number

Access: the whole team reads and edits (scope "all").

VIEWS
A table overview "Stock" with article, location, quantity, unit and minimum.

TOOLS
The agent can query stock (read-only) and adjust quantities (consequential, with approval) —
e.g. "take 5 cable ties off stock" or "what is below minimum?".
