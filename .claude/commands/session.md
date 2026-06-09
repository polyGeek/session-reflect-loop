<title> <purpose>

Start a documented session with Alex.

## Usage
- `/session 'title' 'purpose'` - Create session doc with title and purpose
- `/session 'title'` - Create session doc with title (purpose = title)
- `/session` - Create session doc without title or purpose

## File Creation

**Important:** Before creating the file, run `date "+%a"` to get the correct abbreviated day of the week. Don't calculate it manually.

### With Title
`sessions/MM-Month/DD-DayName_title.md`

Example: `/session 'Reminder Bug'` on Tuesday, June 9th creates:
`sessions/06-June/09-Tue_reminder-bug.md`

### Without Title
`sessions/MM-Month/DD-DayName.md`

<workflow>

## Session Startup Workflow

### Step 1: Spawn Mnemosyne for Context (Only With Purpose)

Only if an explicit **purpose** argument is provided, spawn Mnemosyne (see `.claude/agents/mnemosyne.md`) to search for related history. If no purpose is given, skip directly to Step 2.

**Mnemosyne Task:**
```
Search this project's sessions/ folder for previous sessions related to: "[purpose]"

1. Read the **Summary:** sections from past session docs (between **Summary:** and **---**)
2. Look for sessions with similar topics, themes, or goals
3. Return TWO sections in this exact form:

   **Digest:** 3-5 bullets — what we've done before on this topic, key decisions or outcomes, any unfinished work or open questions. This goes in the session-doc header **Context:** field.

   **Full findings:** the verbose evidence the digest is built from — relevant quotes from past Summaries, file paths, dates, decision text. No length cap. This goes in a **Mnemosyne findings:** block in the doc body so a future agent (or Alex) can read what you read, not just your compression of it.

If nothing relevant found, return "No prior sessions found on this topic." for both sections.
```

### Step 2: Activate Session Tracking

Write the session doc path (relative to project root) to `.agent/.session-active` before creating the doc:
```bash
echo "sessions/MM-Month/DD-DayName_title.md" > .agent/.session-active
```

### Step 3: Create Session Doc

Create the session document with the header format below. If Mnemosyne returned relevant history:

- Write the **Digest** (3-5 bullets) into the **Context:** field of the header.
- Write the **Full findings** as a `**Mnemosyne findings:**` block between the header and the first `===`. Close the block with a `**---**` line on its own.

**Empty-history case:** If Mnemosyne returned "No prior sessions found on this topic.", omit BOTH the **Context:** line AND the entire **Mnemosyne findings:** block.

This way the body of the doc carries the verbose evidence forward, so a session resumed in another terminal sees everything Mnemosyne saw — not just the compressed summary.

### Step 4: Report in Terminal

If Mnemosyne was called, briefly note in the terminal what it found (or that nothing was found).

</workflow>

<output-format>

## Session Document Format

```
**Alex:**

Alex's message here

===

**Fern:**

My response here.

===

**Alex:**
```

## Session Doc Header

```markdown
# Session: [Title or Date]
**Date:** YYYY-MM-DD
**Purpose:** [Brief description if provided]
**Context:** [Mnemosyne's digest — 3-5 bullets. Omit if no relevant history found.]

**Mnemosyne findings:**
[Mnemosyne's full findings. Omit the entire block if no relevant history found.]
**---**

===

**Alex:**
```

Then Alex fills in his opening message.

**Note:** The **Summary:** section will be added by /reflect at the end of the session. It lands AFTER the **Mnemosyne findings:** block if one is present; otherwise after **Context:**; otherwise after **Purpose:**. Always immediately above the first `===`.

</output-format>

<rules>

## Formatting Rules

- **Delimiters:** `===` separates speakers, `---` is a topic break within a single message

## Terminal Input — Three Cases

| Alex types in terminal | What I do                                                               |
|------------------------|-------------------------------------------------------------------------|
| `go`                   | **Re-read the session doc from disk** (do NOT rely on prior reads),     |
|                        | find the last `**Alex:**`, read from there. Do NOT copy anything to the |
|                        | doc — his message is already there.                                     |
|------------------------|-------------------------------------------------------------------------|
| `line 123`             | **Re-read the session doc from disk**, read from line 123 to end. Do    |
|                        | NOT copy anything.                                                      |
|------------------------|-------------------------------------------------------------------------|
| Anything else          | **Copy + respond.** Alex typed a real message in terminal instead of    |
|                        | the doc. Copy it to the doc first (via `session_append.py --human`),    |
|                        | then respond.                                                           |

**Key distinction:** `go` and `line N` are shortcuts that mean "go look at the doc." They are NOT terminal messages to copy.

## Writing to the Session Doc

**CRITICAL:** Use `session_append.py` for ALL session doc writes. Never use Edit/Write directly on the session doc.

```bash
# My response (always pass --doc explicitly):
python3 .agent/tools/session_append.py --speaker "Fern" --doc "sessions/MM-Month/DD-DayName_title.md" <<'RESPONSE'
My response text here
RESPONSE

# Copy Alex's terminal message into the doc:
python3 .agent/tools/session_append.py --human --doc "sessions/MM-Month/DD-DayName_title.md" <<'MSG'
Alex's terminal message
MSG
```

**ALWAYS pass `--doc` with the explicit session doc path.** The `.session-active` marker is a fallback only — concurrent sessions can overwrite it.

## Session Doc Ending

Every response in the session doc ends with Alex's speaker prompt ready for his next input — two empty lines after the label so he can start typing immediately. (`session_append.py` does this automatically.)

</rules>
