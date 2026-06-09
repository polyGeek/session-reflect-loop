# /reflect Command

<reflect_command>
  <purpose>End-of-session reflection ensuring continuity, corrections captured, and learnings preserved.</purpose>
  <principle>Correct once, never again.</principle>

  <config>
    <agent_name>Fern</agent_name>
    <human_name>Alex</human_name>
    <working_context_file>.agent/working-context.md</working_context_file>
    <journal_file>.agent/journal.md</journal_file>
    <decisions_file>.agent/decisions.md</decisions_file>
    <decisions_journal_file>.agent/decisions-journal.md</decisions_journal_file>
    <decisions_word_limit>500</decisions_word_limit>
    <correction_targets>
      - working-context.md: If project-specific and recent
      - CLAUDE.md: If it's a fundamental rule or permanent preference
    </correction_targets>
  </config>

  <workflow>

    <step_1>
      <name>Correction Scan</name>
      <critical>CAPTURE LEARNINGS</critical>
      <purpose>Identify corrections {{human_name}} made so {{agent_name}} doesn't repeat mistakes</purpose>
      <review_for>
        - Explicit corrections: "no, actually...", "that's not right..."
        - Assumption failures: Things assumed that turned out wrong
        - Better approaches: When {{human_name}} showed a better way
        - Pattern violations: When an established convention wasn't followed
      </review_for>
      <for_each_correction>
        1. Note what was done wrong
        2. Note the correct approach
        3. Determine capture location (per config correction_targets)
      </for_each_correction>
    </step_1>

    <step_2>
      <name>Session Review</name>
      <purpose>Mental review before writing anything</purpose>
      <review>
        - What did we accomplish?
        - What decisions were made?
        - What's still open or pending?
        - Any new patterns or preferences established?
      </review>
    </step_2>

    <step_3>
      <name>Decision Capture</name>
      <purpose>Capture architectural/strategic decisions</purpose>
      <for_each_decision>
        1. Append to decisions-journal with full reasoning:
           ## YYYY-MM-DD -- [Decision Title]
           **Context:** What prompted the decision
           **Options:** A, B, C
           **Chose:** [Winner]
           **Why:** The reasoning
           **Trade-offs accepted:** What we gave up
        2. Update decisions.md -- add one-liner, archive stale ones
        3. Check word limit -- compress if over config limit
      </for_each_decision>
      <when_to_skip>If no architectural or strategic decisions were made</when_to_skip>
    </step_3>

    <step_4>
      <name>Update Working Context</name>
      <file>Per config working_context_file</file>
      <update_with>
        1. Current State -- project status now
        2. Active Priorities -- focus for next session
        3. Recent Decisions -- key choices this session
        4. Open Items -- unfinished work or pending questions
      </update_with>
    </step_4>

    <step_5>
      <name>Update Journal</name>
      <file>Per config journal_file</file>
      <condition>Add entry if session included significant decisions, insights, or anything too detailed for working-context</condition>
      <format>
        ## YYYY-MM-DD - Brief Topic
        [What happened, what was decided, what was learned]
      </format>
      <when_to_skip>Routine sessions with nothing notable</when_to_skip>
    </step_5>

    <step_6>
      <name>Apply Corrections</name>
      <condition>If corrections were found in Step 1</condition>
      <actions>
        1. Update the appropriate file(s) identified in Step 1
        2. For CLAUDE.md changes, show {{human_name}} what's being added
        3. Confirm corrections are captured for future sessions
      </actions>
    </step_6>

    <step_7>
      <name>Generate Session Summary</name>
      <condition>If a session doc exists for this session</condition>
      <actions>
        Spawn a sub-agent to generate a summary:
        - Read the full session document
        - Capture: what was discussed, key decisions, outcomes, open items
        - Keep concise but complete
        - Format as plain text (no markdown headers)

        Insert summary into the session doc header. Position: immediately ABOVE the first `===`. Insert it AFTER the **Mnemosyne findings:** block if one is present; otherwise after **Context:**; otherwise after **Purpose:**.

        **Summary:**
        [Generated summary]
        **---**
      </actions>
    </step_7>

    <step_8>
      <name>Append Reflect Output to Session Doc</name>
      <condition>If a session doc exists for this session</condition>
      <actions>
        Append the formatted ==== REFLECT ==== block (per <output_format> below) to the END of the session doc.
      </actions>
    </step_8>

    <step_9>
      <name>Surface Open Items</name>
      <condition>If there is unfinished work</condition>
      <actions>
        - List clearly in terminal
        - Ensure captured in working-context
        - Suggest next steps if appropriate
      </actions>
    </step_9>
  </workflow>

  <output_format>
    **Where to output:** If a session doc exists, append the reflect output to the END of the session doc.

    ==== REFLECT ====

    Corrections Found:
    - [What went wrong] --> [Correct approach] --> [Captured in: location]
    (or "None this session")

    Decisions Captured:
    - [Decision]: [Brief rationale] --> [files updated]
    (or "None this session")

    Working Context: [Updated / No changes needed]
    Journal: [Entry added / Skipped]
    Session Doc: [Summary added / N/A]

    Open Items:
    - [Any unfinished work]

    Next Session Suggestion:
    [What to tackle next]

    ==== END REFLECT ====
  </output_format>

  <rules>
    <correct_once>
      If {{human_name}} corrects something, capture it permanently so:
      1. Future sessions start with that knowledge
      2. The same mistake never happens again
      3. The correction becomes persistent memory
    </correct_once>
    <verification>
      - Were corrections scanned and captured?
      - Is working-context updated?
      - Does the session doc have its Summary?
    </verification>
  </rules>

</reflect_command>
