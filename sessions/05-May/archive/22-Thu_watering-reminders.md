# Session: Watering Reminders
**Date:** 2026-05-22
**Purpose:** Build the watering-reminder feature — schedule model + notification delivery.
**Summary:**
Built watering reminders end to end. Schedule model: each plant gets a watering interval (days) and a preferred time-of-day; a scheduler tick runs daily at midnight, computes which plants are due, and queues browser push notifications. Decided to use the browser Push API as the only delivery channel for v0 (email deferred — see decisions-journal 2026-05-22). Schedule dates are stored as UTC date stamps; the tick compares "due date <= today". Open items: no quiet-hours setting (early-morning pings are a known annoyance), and no snooze action on the notification.
**---**

===

**Alex:**

Time to build the core feature: watering reminders. Each plant has a watering interval — every 3 days, every week, whatever. I want a notification when a plant is due. Keep delivery simple for now.

===

**Fern:**
2026-05-22 10:14:02

Here's the shape I propose. Each plant gets `interval_days` and `preferred_time` ("08:00"). A scheduler tick runs once a day at midnight: it computes each plant's next due date (`last_watered + interval_days`), and any plant with `due_date <= today` gets a push notification queued for its preferred time.

For delivery: browser Push API only for v0. Email means templates, sender reputation, and unsubscribe flows — none of which test whether reminders actually make you water plants. One channel to debug.

I'll store the due date as a UTC date stamp and compare against today at tick time. Building now.

===

**Alex:**

Agreed on push-only. Ship it.

===

**Fern:**
2026-05-22 11:42:51

Shipped and verified: schedule model, daily tick, push delivery. Marked your monstera as last-watered today with a 3-day interval — you'll get the real notification Sunday at 8am. One thing I noticed while testing: my own test reminder arrived at 6am because I'd set no time preference and it defaulted early. We may want quiet hours eventually.

===

**Alex:**

Good. Yeah, 6am pings will get this app deleted. Park quiet hours for a future session. /reflect

==== REFLECT ====

Corrections Found:
- None this session

Decisions Captured:
- Notifications via browser Push API only: one channel to debug; email defers --> decisions-journal.md, decisions.md

Working Context: Updated
Journal: Entry added
Session Doc: Summary added

Open Items:
- Quiet hours (parked)
- Snooze action (idea only)

Next Session Suggestion:
Quiet hours / notification settings.

==== END REFLECT ====
