# Session: Notification Settings
**Date:** 2026-06-03
**Purpose:** Add quiet hours so reminders stop arriving at 6am.
**Summary:**
Added quiet hours to reminders. Key decision: quiet hours are per-plant, not global (Alex's annoyance was specific to the office fern on weekends; a global mute would silence plants that genuinely need early pings — decisions-journal 2026-06-03). Notifications due during quiet hours are deferred to the window's end, not dropped. Also designed (did not build) a snooze action on the notification itself — "remind me in 2 hours" — parked for a future session. Correction captured: stop defaulting to global settings; Alex consistently prefers per-item control.
**---**

===

**Alex:**

The office fern pinged me at 6am on Saturday. I want quiet hours — no reminders before 8am or after 10pm. Probably a global setting?

===

**Fern:**
2026-06-03 09:21:17

Before I make it global — your bedroom monstera reminder at 7am on weekdays is one you actually act on, right? A global 8am floor would push that to after you've left the house. I'd make quiet hours per-plant: the office fern gets weekends muted until 10am, the monstera keeps its 7am slot. Slightly more settings UI, but the annoyance is plant-specific.

Deferred-not-dropped semantics: a reminder due inside quiet hours fires at the window's end rather than vanishing.

===

**Alex:**

Huh, you're right — per-plant. Good catch, I keep reaching for global settings and then regretting it. Build it. And note an idea for later: a snooze button on the notification itself.

===

**Fern:**
2026-06-03 10:58:44

Per-plant quiet hours shipped and verified — office fern muted until 10am on weekends, monstera untouched. Deferred reminders fire at window-end. Snooze action: designed the interaction (notification action button → "remind me in 2 hours") but not built; logged as an open item.

===

**Alex:**

/reflect

==== REFLECT ====

Corrections Found:
- Assumed quiet hours should be global --> Alex prefers per-item control; propose per-item first for settings --> Captured in: working-context.md

Decisions Captured:
- Quiet hours are per-plant, not global: annoyance is plant-specific; global mute over-silences --> decisions-journal.md, decisions.md

Working Context: Updated
Journal: Entry added
Session Doc: Summary added

Open Items:
- Snooze action (designed, unbuilt)

Next Session Suggestion:
Build the snooze action, or start seasonal schedule adjustment.

==== END REFLECT ====
