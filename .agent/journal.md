# Journal — Sprout

*Session-by-session narrative. Written by /reflect. Mnemosyne's primary search target alongside session-doc Summaries.*

## 2026-05-22 - Watering reminders shipped
Built the reminder pipeline end to end: schedule model, a daily scheduler tick, browser push delivery. Decided to ship with Push API only (see decisions-journal). Open: no quiet hours, so early-morning reminders are a known annoyance.

## 2026-06-03 - Notification settings / quiet hours
Added per-plant quiet hours after Alex's 6am office-fern complaint. Chose per-plant over global — the annoyance is plant-specific. Designed (but did not build) a snooze action on the notification itself. Correction captured: stop assuming settings should be global; Alex consistently prefers per-item control.

## 2026-06-09 - Reminder day-early bug
Reminders fired a day early for evening schedules. Root cause was a UTC-midnight date compared against local-time now — an off-by-one that only bites east of UTC or for evening times. Fixed by storing wall-clock local time + timezone (decision journaled). Mnemosyne's session-start digest pointed straight at the 05-22 scheduler-tick design as the likely culprit, which it was. DST test coverage flagged and parked.
