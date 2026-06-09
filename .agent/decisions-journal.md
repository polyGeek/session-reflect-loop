# Decisions Journal — Sprout

*Append-only. Every architectural or strategic decision lands here with its full reasoning, written by /reflect. Mnemosyne searches this file for decision archaeology.*

## 2026-05-22 -- Notifications via browser Push API only
**Context:** Shipping the first version of watering reminders; needed a delivery channel.
**Options:** A) Browser Push API, B) Email digests, C) Both.
**Chose:** A.
**Why:** One channel to build and debug. Email adds a template pipeline, a sender reputation problem, and an unsubscribe flow — none of which test the core idea (do reminders make people water their plants?).
**Trade-offs accepted:** Users who deny the permission prompt get nothing. Acceptable for v0.

## 2026-06-03 -- Quiet hours are per-plant, not global
**Context:** Alex kept getting a 6am reminder for the office fern on weekends.
**Options:** A) One global quiet-hours setting, B) Per-plant quiet hours, C) Per-plant with a global default.
**Chose:** B (with C noted as the likely evolution).
**Why:** The annoyance is plant-specific — the bedroom monstera and the office fern genuinely need different windows. A global setting fixes the symptom for one plant by muting all of them.
**Trade-offs accepted:** More settings UI per plant. Revisit C if users complain about repeating themselves.

## 2026-06-09 -- Reminder times stored in the user's local time, not UTC
**Context:** Reminders were firing a day early for evening waterers — scheduled "Tuesday 8pm" arrived Monday. Root cause: schedule dates stored as UTC midnight, compared against local-time now.
**Options:** A) Store UTC + convert at every comparison, B) Store local wall-clock time + timezone, C) Store UTC but compare in UTC everywhere.
**Chose:** B.
**Why:** A watering reminder means "8pm where the plant lives." Wall-clock semantics match user intent; storing UTC forces a conversion at every read and every one we forget is this bug again. C is consistent but makes "9am" drift across DST changes.
**Trade-offs accepted:** Timezone column on the schedule table; DST edge cases need explicit tests (parked as an open item).
