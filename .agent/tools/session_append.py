#!/usr/bin/env python3
"""
Session Doc Append Tool
=======================
Mechanically appends a formatted response block to the active session doc.
Eliminates ordering errors and mid-document insertion bugs.

Why this exists: letting the agent free-edit a shared document produces five
distinct failure modes (wrong insertion point, duplicated messages, stale
reads, forgotten docs, wrong-doc writes). Mechanical append fixes the worst
of them. The agent never uses Edit/Write on the session doc — only this tool.

Usage:
    # Agent response (explicit path preferred — avoids cross-session marker collisions):
    python3 .agent/tools/session_append.py --speaker "Fern" --doc "sessions/06-June/09-Tue_example.md" <<'RESPONSE'
    Your response text here.
    RESPONSE

    # Fallback (reads .agent/.session-active marker):
    python3 .agent/tools/session_append.py --speaker "Fern" <<'RESPONSE'
    Your response text here.
    RESPONSE

    # Copy the human's terminal message into the doc:
    python3 .agent/tools/session_append.py --human --doc "sessions/06-June/09-Tue_example.md" <<'MSG'
    Terminal message here
    MSG
"""

import argparse
import os
import sys
from datetime import datetime

# Change this to your name. It's used for the speaker prompt that ends every
# appended block, so the doc is always ready for your next message.
HUMAN_NAME = "Alex"


def get_session_doc_path(explicit_path=None):
    """Get the session doc path from explicit arg or .agent/.session-active marker."""
    if explicit_path:
        if not os.path.exists(explicit_path):
            print(f"ERROR: Session doc not found: {explicit_path}", file=sys.stderr)
            sys.exit(1)
        return explicit_path

    marker = os.path.join('.agent', '.session-active')
    if not os.path.exists(marker):
        print("ERROR: No active session doc. Provide --doc PATH or run /session first.", file=sys.stderr)
        sys.exit(1)
    with open(marker, 'r') as f:
        path = f.read().strip()
    if not os.path.exists(path):
        print(f"ERROR: Session doc not found: {path}", file=sys.stderr)
        sys.exit(1)
    return path


def append_response(doc_path, speaker, content):
    """Append a formatted response block to the session doc."""
    with open(doc_path, 'r') as f:
        existing = f.read()

    existing = existing.rstrip()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    block = (
        f"\n\n===\n\n**{speaker}:**\n{timestamp}\n\n{content.rstrip()}"
        f"\n\n===\n\n**{HUMAN_NAME}:**\n\n\n"
    )

    with open(doc_path, 'w') as f:
        f.write(existing + block)

    print(f"OK: Appended {speaker}'s response to {doc_path}")


def append_human_message(doc_path, content):
    """Copy the human's terminal message into the doc (at the last speaker prompt)."""
    with open(doc_path, 'r') as f:
        existing = f.read()

    existing = existing.rstrip()
    block = f"\n\n{content.rstrip()}"

    with open(doc_path, 'w') as f:
        f.write(existing + block)

    print(f"OK: Copied {HUMAN_NAME}'s message to {doc_path}")


def main():
    parser = argparse.ArgumentParser(description='Append to active session doc')
    parser.add_argument('--speaker', type=str, help='Agent speaker name (e.g., Fern)')
    parser.add_argument('--human', action='store_true', help="Copy the human's terminal message (no speaker wrapper)")
    parser.add_argument('--doc', type=str, help='Explicit path to session doc (preferred over .session-active marker)')
    args = parser.parse_args()

    if not args.speaker and not args.human:
        print("ERROR: Must specify --speaker NAME or --human", file=sys.stderr)
        sys.exit(1)

    content = sys.stdin.read()
    if not content.strip():
        print("ERROR: No content provided on stdin", file=sys.stderr)
        sys.exit(1)

    doc_path = get_session_doc_path(args.doc)

    if args.human:
        append_human_message(doc_path, content)
    else:
        append_response(doc_path, args.speaker, content)


if __name__ == '__main__':
    main()
