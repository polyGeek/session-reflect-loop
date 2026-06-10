# The /session + /reflect Loop — Sample Kit

A working sample of the session-doc workflow described in [The Conversation Is the Asset](https://polygeek.com/posts/the-conversation-is-the-asset.html).

The premise: the most valuable output of an AI coding session isn't the code — it's the conversation. The decisions, the corrections, the reasoning. By default it all evaporates when the context window ends. This loop keeps it, in plain markdown files you own.

## What's in here

This repo is a miniature, fully worked example. The fictional setup: a developer named **Alex**, an AI agent named **Fern**, and a plant-care web app called **Sprout**.

```
.claude/
  commands/
    session.md        # /session — start a documented session
    reflect.md        # /reflect — the end-of-session ritual
  agents/
    mnemosyne.md      # the memory-retrieval sub-agent
.agent/
  tools/
    session_append.py # mechanical append tool for safe doc writes
  working-context.md  # the agent's short-term memory (read at session start)
  decisions.md        # active decisions, one-liners
  decisions-journal.md# full decision history with reasoning (append-only)
  journal.md          # session-by-session narrative history
sessions/
  05-May/archive/22-Thu_watering-reminders.md   # a past session (completed, summarized)
  06-June/archive/03-Wed_notification-settings.md # another past session
  06-June/09-Tue_reminder-day-early-bug.md      # ★ the worked example — full lifecycle
```

## Start with the worked example

Open [`sessions/06-June/09-Tue_reminder-day-early-bug.md`](sessions/06-June/09-Tue_reminder-day-early-bug.md). It shows one complete session, end to end:

1. **The header** — created by `/session`, including the **Context:** digest and **Mnemosyne findings:** block that the memory agent seeded before any work began. The findings cite the two archived sessions in this repo — go check; the citations resolve.
2. **The conversation** — Alex and Fern alternating, separated by `===` delimiters. Alex writes in the file from any editor; Fern responds in the file via `session_append.py`.
3. **The Summary** — prepended to the header by `/reflect` when the session ended, between `**Summary:**` and `**---**` delimiters. This is what makes the archive searchable: Mnemosyne reads only these blocks when triaging history.
4. **The REFLECT block** — appended at the very end: corrections captured, decisions journaled, memory files updated.

## How a session runs

```
/session 'reminder bug' 'reminders firing a day early'
        │
        ├─ Mnemosyne (sub-agent) searches past session Summaries,
        │  returns a digest + full findings → seeded into the new doc's header
        │
        ▼
  You write in the doc, type `go` in the terminal.
  The agent re-reads the doc from disk, responds — in the doc.
  Repeat until done.
        │
        ▼
/reflect
        ├─ scans the session for corrections → permanent files ("correct once, never again")
        ├─ journals decisions with reasoning
        ├─ refreshes working-context.md for the next session
        └─ prepends a Summary to the doc → the archive grows by one searchable entry
```

## Adapting this to your project

**You don't need to copy this repo.** The fastest way to adopt the loop is to hand the URL to your agent and let it do the adapting — that's the whole point of the workflow. Open Claude Code in your project and start a discussion:

```
Read https://github.com/polyGeek/session-reflect-loop and the article it's based on.
I want to apply this session-doc SOP to this project. Look at how my project is
organized, then propose adapted versions of the /session and /reflect commands,
the memory agent, and the .agent/ memory files. Ask me about anything that
should be different here.
```

The agent reads the sample, maps it onto your project's shape, and you refine it together — in what will probably be your first session doc.

If you'd rather do it by hand:

1. Copy `.claude/` and `.agent/` into your project root.
2. Rename the agent: search-and-replace `Fern` with your agent's name, `Alex` with yours (also the `HUMAN_NAME` constant in `session_append.py`).
3. Create a `sessions/` folder. Run `/session 'title' 'purpose'` in Claude Code.
4. End every session with `/reflect`. The first few summaries feel like overhead; around week two, Mnemosyne starts opening your sessions with history you'd forgotten you had.

## Honest footnotes

- This is the trimmed teaching version. Our production reflect commands have grown project-specific steps (documentation sync, rules databases, automation scans) — yours will too. Let it evolve; the commands are just markdown.
- `session_append.py` exists because we found five distinct ways an agent can botch writing to a shared document (wrong insertion point, duplication, stale reads, forgotten docs, wrong-doc writes). Mechanical append fixes the worst of them. Don't let the agent free-edit the session doc.
- The archive only pays off if the Summary format stays consistent. Machine-parseable delimiters (`**Summary:**` … `**---**`) are load-bearing.
