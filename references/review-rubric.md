# Review rubric

The reviewer is a subagent with a fresh context.
It never sees the drafter's reasoning.
It sees only the inputs listed below and returns findings in the fixed format.

## Inputs to the reviewer

- The paper brief from `plan/paper.md`: goal, claim, carriers, and scope.
- The brief of every ancestor of the unit, down from the section. This is the chain the unit's message has to serve.
- The brief of the unit under review.
- The briefs of the previous and next unit at the same level.
- The draft of the unit, and the drafts of the previous and next unit if they exist.
- The reader model.
- The glossary and the chosen field vocabularies.
- The review log for this unit, so resolved and rejected findings are not raised again.
- The output of `scripts/check_terms.py` on the unit.
- `references/prose-style.md`.

## What the reviewer checks

Checks are run in this order, and a failure at an earlier step outranks a later one.

1. **Fidelity.** The draft delivers the brief's message, and only that message. Every sentence serves it. A sentence that serves no listed prerequisite and does not carry the message is cut.
2. **Self-containment.** The draft stands without the code, the notes, or the plan. No script name, file path, function name, or software step appears. A measurement carries its physical configuration, not its tool.
3. **Prerequisites.** Every prerequisite in the brief has its source in the text before this unit, or in the reader model. The draft does not rely on anything not in the brief.
4. **Composition.** For a parent unit, the ordered child messages reproduce the parent message with nothing missing and nothing extra. For any unit, its message serves the message of every ancestor up to the paper's claim.
5. **Position.** The draft connects to what the previous unit left open and hands the next unit what it needs.
6. **Medium.** The medium chosen in the brief is the one the draft uses, and it is still the best one. A figure whose message a sentence can state is flagged. A paragraph that lists many numbers is flagged for a table.
7. **Orphans.** Every figure and table is referenced by number from a paragraph whose message it supports. See `figures-tables.md`.
8. **Terminology.** Every named object uses its glossary name. No forbidden alternative appears. No outside-field term from the vocabulary files appears.
9. **Compression.** First the removal test on each sentence: any word, clause, or phrase whose removal leaves the meaning unchanged is dropped. Then the reviewer rewrites the unit at roughly seventy percent of its length. If the message and every listed prerequisite survive, the shorter version is proposed. If something was lost, the reviewer names what the extra words carried.
10. **Style.** The checklist at the end of `references/prose-style.md`, and the journal's language guide.

## Finding format

Each finding is one block.

```markdown
- id: R3-par:beam-center-def-2
  check: prerequisites
  severity: blocking | major | minor
  where: sentence 3
  finding: "first moment" is used but its source is the reader model, and the reader model does not list it
  proposal: define the first moment in one sentence, or add it to the reader model
```

The id is round number, unit label, and a counter.

Severity:

- **blocking**: the message is not delivered, a prerequisite has no source, an orphan figure or table, a composition gap, or a reference to code or files.
- **major**: wrong medium, a terminology violation, a compression that loses nothing.
- **minor**: style.

## Loop control

- At most five rounds per unit.
- A round ends when the drafter has applied or rejected every finding and appended the outcome to the review log.
- The loop stops early when a round returns no blocking and no major finding.
- After the last round, the open findings and the diff since round one go to the author.

A rejected finding carries a reason in the log.
The reviewer reads the log and does not raise a rejected finding again unless the draft changed in the place it pointed to.

## Reviewer prompt

The drafter spawns the reviewer with this prompt, filling the paths.

```text
You are reviewing one unit of a scientific paper.
Read, in this order: the reader model, the paper brief in plan/paper.md, the section plan, the glossary, the vocabularies, the review log, the draft.
Hold the paper's claim and the section's message in mind while reviewing the unit.
A unit that is locally sound but does not serve the section message, or a section that does not serve the paper's claim, is a composition finding.
Read references/prose-style.md, references/figures-tables.md, and references/terminology.md.
Apply the checks in references/review-rubric.md in order.
Return only findings in the finding format, most severe first, followed by your seventy percent rewrite.
Do not restate the draft.
Do not raise a finding the log marks as rejected unless the text at that place changed.
```
