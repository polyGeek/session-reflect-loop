# Working Context — Sprout

*Fern reads this at the start of every session. /reflect refreshes it at the end.*

## Current State
Sprout v0.4 live at sprout-demo.web.app. Core loop (add plant → set schedule → get reminders) works. Reminder notifications shipped 2026-05-22; per-plant quiet hours shipped 2026-06-03. Reminder day-early bug fixed 2026-06-09.

## Active Priorities
1. Seasonal schedule adjustment (water less in winter) — next feature, not yet specced
2. Reminder snooze action — designed in the 06-03 session, not built

## Recent Decisions
- Reminder times stored in the user's local time, not UTC (2026-06-09 — see decisions.md)
- Quiet hours are per-plant, not global (2026-06-03)

## Open Items
- Snooze action (designed, unbuilt)
- No test coverage yet for DST transitions — flagged 2026-06-09, parked
