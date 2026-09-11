---
name: paper-writing
description: Plan, draft, and review a scientific paper unit by unit. Every unit (paper, section, paragraph, figure, table) gets a brief before prose, a fresh-context reviewer subagent checks the draft against the brief, and a draft-review loop runs up to five rounds with a persistent log. Load when asked to plan, write, or revise a paper, a section, a figure, or a table. Standalone; carries its own prose rules and defers to the journal's language guide and the project's notation conventions.
---

# Paper writing

This skill sequences the work.
The rules for prose live in `references/prose-style.md`.
Read it before writing any text.
The journal's language guide and the project's notation conventions outrank it where they differ.

The unit of work is a unit of the paper: the paper itself, a section, a subsection, a paragraph, a figure, or a table.
Every unit gets a brief before any prose.
Every draft is reviewed against its brief by a subagent that did not write it.

## Files in the paper's project

The skill keeps its state in a `plan/` directory next to the source.

| File | Holds |
|---|---|
| `plan/reader-model.md` | who the reader is and what they know a priori |
| `plan/paper.md` | the paper brief and one brief per section |
| `plan/sec-<label>.md` | the section brief and one brief per paragraph, figure, and table |
| `plan/glossary.md` | one canonical name per object, with forbidden alternatives |
| `plan/log-<label>.md` | the review log for one section |

Templates for each are in `templates/`.

## Workflow

### 0. Setup

Fill `plan/reader-model.md` from `templates/reader-model.md`.
Choose the vocabularies from `templates/vocabulary/` and list them in `plan/paper.md`.
Read `references/brief-core.md`, `references/brief-levels.md`, and `references/prose-style.md`.

### 1. Master plan

Write the paper brief and one section brief per section in `plan/paper.md`.
Spawn a reviewer with the prompt in `references/review-rubric.md`.
The reviewer checks only composition and position at this stage.
Fix the plan before going further.
A wrong outline costs nothing here and everything after prose exists.

### 2. Section plan

For the section being written, copy `templates/section-plan.md` to `plan/sec-<label>.md`.
Write one brief per paragraph, figure, and table, in reading order.
Every figure and table brief names the paragraph that supports it.
Spawn a reviewer for composition, position, medium, and orphans.
Fix the plan.

### 3. Draft

Write each paragraph against its brief.
The message sentence goes where the brief says, first by default.
Write the caption of each figure and table from its brief.
Reference every figure and table from its supporting paragraph.
Apply `references/prose-style.md` from the first sentence.

### 4. Glossary

After the first draft of a section, list every named object and every word used for it.
Where more than one word was used, propose one canonical name and list the others as forbidden.
Write the proposal into `plan/glossary.md` and hand it to the author for correction.
Later sections extend the glossary and never rename an entry.
See `references/terminology.md`.

### 5. Review loop

For each unit, at most five rounds.

1. Run `scripts/check_terms.py` on the section source with the glossary and the vocabularies.
2. Spawn the reviewer subagent with the inputs listed in `references/review-rubric.md`.
3. Apply or reject each finding. Every rejection carries a reason.
4. Append every outcome to `plan/log-<label>.md`.
5. Re-read the previous and next unit. A change in one unit breaks the seam with its neighbors.
6. Stop if the round returned no blocking and no major finding.

### 6. Hand-off

Give the author the open findings and the diff since the first draft.
Do not run a sixth round.
Do not silently accept a finding the author has not seen after the fifth round.

## The eight questions

Every brief answers these, and the level additions in `references/brief-levels.md`.

1. Goal.
2. Message, one sentence.
3. Position: what the previous unit left open, what the next unit needs.
4. Prerequisites.
5. Source of each prerequisite: in the text, or the reader model.
6. Evidence: derived, measured, cited, assumed.
7. Objection, and whether it is answered here or deferred.
8. Medium: prose, figure, table, or equation, and why.

## Rules that hold everywhere

- The paper is a self-contained unit of research. It stands without the code, the notes, or the plan. No script names, paths, or software steps in the text.
- A unit carries one message. Two messages are two units.
- Child messages compose to the parent message with nothing missing and nothing extra.
- An explanation stays if it supplies a listed prerequisite and goes if it does not.
- One name per object and one object per name, from the glossary.
- No figure or table without a supporting paragraph that references it.
- Concise means no word that does not serve the message. It does not mean fewer explanatory sentences.
