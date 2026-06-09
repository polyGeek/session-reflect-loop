# Session: Reminder Day-Early Bug
**Date:** 2026-06-09
**Purpose:** Reminders are firing a day early for evening watering schedules — find and fix.
**Context:**
- Reminder pipeline built 2026-05-22: daily scheduler tick at midnight computes due plants (`due_date <= today`); due dates stored as UTC date stamps; delivery via browser Push API only.
- Quiet hours added per-plant 2026-06-03; deferred-not-dropped semantics (a reminder due inside quiet hours fires at window-end). Snooze action designed but unbuilt.
- Standing preference: Alex favors per-item control over global settings (correction captured 2026-06-03).
- No prior session has touched timezone handling; the 05-22 doc notes due dates are "stored as UTC date stamps" and compared to "today" at tick time — likely relevant to a day-boundary bug.

**Mnemosyne findings:**
**Watering reminders — foundational build (2026-05-22):**
- File: `sessions/05-May/archive/22-Thu_watering-reminders.md`
- From the Summary: "Schedule dates are stored as UTC date stamps; the tick compares 'due date <= today'." Scheduler tick runs daily at midnight. Push API only (decision journaled 2026-05-22).
- From the conversation: "I'll store the due date as a UTC date stamp and compare against today at tick time."

**Notification settings / quiet hours (2026-06-03):**
- File: `sessions/06-June/archive/03-Wed_notification-settings.md`
- Quiet hours are per-plant; reminders due inside quiet hours are deferred to window-end, not dropped. If the day-early bug interacts with quiet-hour deferral, this is the spec.
- Correction on record: "stop defaulting to global settings; Alex consistently prefers per-item control."

**Decision history (`.agent/decisions-journal.md`):** entries 2026-05-22 (Push only) and 2026-06-03 (per-plant quiet hours). No timezone-related decision exists yet — if this bug forces one, it's new ground.
**---**
**Summary:**
Fixed the day-early reminder bug. Root cause: due dates were stored as UTC midnight date stamps while the scheduler tick compared them against local "today" — for evening schedules east of UTC the comparison crossed a day boundary, so "Tuesday 8pm" fired Monday. Considered three fixes (convert-at-read, store local wall-clock + timezone, all-UTC comparison); chose storing the user's local wall-clock time plus timezone, because a watering reminder means "8pm where the plant lives" (decision journaled 2026-06-09). Migrated existing schedules, added day-boundary tests for UTC+0/+10/-7, verified the monstera fires Tuesday. Mnemosyne's session-start digest pointed at the 05-22 UTC-date-stamp design as the likely culprit, which it was. Open: no DST-transition test coverage — flagged and parked.
**---**

===

**Alex:**

Something's off with reminders. My neighbor is testing the app from Sydney and her "Tuesday 8pm" watering reminder arrived on Monday. Mine are fine. A day early, consistently, for her evening schedules.

===

**Fern:**
2026-06-09 09:32:18

The digest at the top of this doc already points at the suspect: the 05-22 build stores due dates as UTC date stamps and compares them to "today" at tick time. Sydney is UTC+10 — her Tuesday-8pm local is Tuesday 10am UTC, but a due date stored as UTC midnight Tuesday is already `<= today` when her Monday-midnight local tick runs. You don't see it because you're close enough to UTC that the boundary doesn't cross for your times.

Confirmed by reproduction: set a test plant to UTC+10 with an evening preferred time — reminder queued a day early, exactly as she reports.

Three ways to fix it: (A) keep UTC storage and convert at every comparison, (B) store the user's local wall-clock time plus timezone, (C) go all-UTC including the comparison. I recommend B. A reminder means "8pm where the plant lives" — wall-clock semantics match what the user asked for, and option A means every future comparison we forget to convert is this bug again. C is internally consistent but makes "8pm" drift when DST shifts.

===

**Alex:**

B makes sense. Do it — and make sure her existing schedule migrates, don't make her re-enter it.

===

**Fern:**
2026-06-09 11:07:45

Done and verified:

- Schedules now store wall-clock time + timezone; the tick compares in the plant's own timezone.
- Migrated all existing schedules in place — your neighbor's plants kept their settings, nothing to re-enter.
- Added day-boundary tests for UTC+0, UTC+10, and UTC-7 evening schedules; all green. Reproduced the original bug against the old code path to confirm the test actually catches it.
- Her monstera now queues for Tuesday 8pm Sydney time. Yours are unchanged.

One honest gap: DST transitions aren't covered by tests yet. "8pm" stays 8pm across a DST change with the new model (that's why we chose it), but I'd want explicit tests before I call it bulletproof. Flagging it as an open item rather than scope-creeping this session.

===

**Alex:**

Good call. Park the DST tests. /reflect

==== REFLECT ====

Corrections Found:
- None this session

Decisions Captured:
- Reminder times stored in the user's local time, not UTC: wall-clock semantics match user intent; convert-at-read invites repeat bugs --> decisions-journal.md, decisions.md

Working Context: Updated
Journal: Entry added
Session Doc: Summary added

Open Items:
- DST-transition test coverage (parked)
- Snooze action (still unbuilt, from 06-03)

Next Session Suggestion:
Seasonal schedule adjustment, or the snooze action.

==== END REFLECT ====
