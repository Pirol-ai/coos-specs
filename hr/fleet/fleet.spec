Fleet — vehicles, drivers and deadlines

PURPOSE
Plate, driver, inspection, mileage: the four things a small business must know about its
vehicles — in one place instead of a spreadsheet nobody finds.

DATA
One table "vehicles":
- title (text, required) — the vehicle, e.g. "VW Crafter van"
- plate (text, required) — the license plate
- driver (reference to a person from master data) — regular driver
- inspection_due (date) — next inspection due date
- mileage (number) — current mileage
- status (text) — in service, in workshop, deregistered; new entries start as "in service"
- note (text) — damage, accessories, fuel card

Access: the whole team reads, fleet owners edit (scope "all").

VIEWS
A table overview "Vehicles" with vehicle, plate, driver, inspection due, mileage and status.
The driver reference appears as a name (the platform does this automatically).

TOOLS
The agent can query vehicles (read-only) and update mileage/status (consequential, with
approval) — e.g. "which vehicles are due for inspection in the next 60 days?".
