# Service requirements: Emergency Department (ED)

The first service configuration. This file is the human-readable spec; `configs/ed.json` (week 3) is the machine-readable version and must match it. Position names follow the department's own labels. No staff names; any examples are fictional.

## Model in one paragraph

The roster is a set of named **positions** per period (e.g. `Silver AM3`). Each position has a period, an optional stream, the roles allowed to fill it, a priority, and flags (in charge, on-call). Staff are assigned to positions and see them by name. Counts are simply how many positions exist.

## Roles

Consultant (SMS), Registrar, HMO, Intern. "Resident" is this site's word for HMO.

- **In charge (IC)** is a flag on a position, not a role. AM and PM ICs must be Consultants; the Night IC is a Registrar.
- One person fills one position per shift.

## Streams

Silver, Orange, Fast (FT), SSU (Short Stay Unit), AVAO (Ambulance Victoria ambulance offload). Some positions have **no stream** (Rover, Night).

## Periods and default times

| Period | Default | Overrides |
| --- | --- | --- |
| AM | 08:00–18:00 | SSU: 07:30–17:30 |
| PM | 14:30–24:00 | Consultants: 15:00–24:00 · HMO SSU PM: 14:30–23:30 |
| Night | 23:00–09:00 | — |

A shift belongs to the day it starts.

## Positions (weekday)

Eligible roles marked "to confirm" are best guesses to check.

### AM

| Position | Stream | Eligible roles | Flags |
| --- | --- | --- | --- |
| Silver AM IC | Silver | Consultant | IC |
| Silver AM2 | Silver | Registrar (occasionally an extra Consultant) | |
| Silver AM3–AM6 | Silver | Registrar, HMO or Intern (to confirm) | |
| Orange AM IC | Orange | Consultant | IC |
| Orange AM2 | Orange | Registrar (occasionally an extra Consultant) | |
| Orange AM3–AM6 | Orange | Registrar, HMO or Intern (to confirm) | |
| AM Fast IC | Fast | Consultant | IC |
| AM Fast (1)–(3) | Fast | to confirm | |
| SSU SMS | SSU | Consultant | |
| Intern SSU AM | SSU | Intern | |
| AVAO AM | AVAO | to confirm | weekdays only |
| Rover AM | none | HMO (usually) | lowest priority |

### PM

| Position | Stream | Eligible roles | Flags |
| --- | --- | --- | --- |
| Silver PM IC | Silver | Consultant | IC |
| Silver PM2 | Silver | Registrar (occasionally an extra Consultant) | |
| Silver PM3–PM6 | Silver | Registrar, HMO or Intern (to confirm) | |
| Orange PM (on-call) | Orange | Consultant | on-call overnight |
| Orange PM2 | Orange | Registrar (occasionally an extra Consultant) | |
| Orange PM3–PM6 | Orange | Registrar, HMO or Intern (to confirm) | |
| PM Fast IC | Fast | Consultant | IC |
| PM Fast (1)–(3) | Fast | to confirm | |
| Intern PM Fast | Fast | Intern | |
| HMO SSU PM | SSU | HMO | |
| AVAO PM | AVAO | to confirm | every day |
| Rover PM | none | HMO (usually) | lowest priority |

### Night

| Position | Stream | Eligible roles | Flags |
| --- | --- | --- | --- |
| Night IC | none | Registrar | IC |
| Night2–Night6 | none | Registrar or HMO (to confirm) | |
| Night SSU | SSU | HMO | |

No Consultants or Interns on site overnight.

## Staffing levels

Positions are filled in priority order. The aim is every position filled, but that isn't always possible.

1. **Core minimum (hard):** Silver and Orange, AM and PM, each have at least 1 Consultant, 1 Registrar, 1 HMO and 1 Intern. A gap here is shown as unfilled.
2. **Remaining positions (soft, high priority):** filled whenever staff are available, lower numbers first (AM3 before AM6).
3. **Rover (soft, lowest priority):** filled only after all stream positions.

### Weekends and public holidays

- Silver and Orange: usually 3–4 people per stream. Positions IC, 2 and 3 are the weekend core; 4 if staff allow; 5–6 not used.
- Rover: sometimes.
- AVAO AM: not staffed. AVAO PM: staffed.
- Fast: to confirm.
- Public holidays use the weekend set; an admin can mark any date as weekend-like.

## On-call

`Orange PM (on-call)` works the PM shift, then is the night Registrar's first contact overnight. On-call is a flag on a position, so other services (e.g. HITH) can use it too.

## Rules

- Consultants: 50:50 AM / PM split (configurable; night share 0).
- Whoever works Orange PM (on-call) should not work an AM shift the next day (soft rule, high weight; overnight call-outs make it a fatigue risk).
- Shifts pro-rated by EFT; EFT entered by an admin only.
- Business rules first, then preferences. Some preferences are requirements (e.g. part-time only, never Fridays), set by an admin.
- Rule values (rest hours, consecutive days and nights, maximum hours): to confirm from the enterprise agreement and fatigue policy.

## Handled operationally, not on the roster

- AVAO supporting the HMO SSU PM in the evening.

## Open questions

1. Eligible roles for positions 3–6 (Silver, Orange), Fast (1)–(3), AVAO, and Night2–6.
2. Which IC is the department-wide in charge in AM and PM (Silver or Orange)?
3. Fast on weekends: how many positions?
4. Does on-call count toward hours worked?
5. Do Fast positions have their own times, or the defaults?