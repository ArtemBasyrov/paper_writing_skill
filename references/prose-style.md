# Prose style

These rules apply to every sentence of the paper.
They are generic.
The journal's language guide and the project's own notation conventions outrank them where the two differ.

Apply them from the first draft.
A loose draft cleaned up afterwards oscillates between too terse and too long.

## Sentences

- One statement per sentence. A claim, a caveat, and a number are three sentences.
- Lead with the subject. Plain subject, verb, object. No inversion, no fronted clauses.
- Promote a trailing relative clause into its own sentence.
- Repeat the noun instead of using a pronoun when the reference could be ambiguous.
- Never drop a verb to save a word.
- Punctuation is sparse. Two plain sentences beat one joined with a colon, a semicolon, or a dash.
- Removal test. Remove a word, a clause, or a phrase. If the sentence still says the same thing, the part is dropped. Apply this to every sentence, one part at a time.

## Words

- Use the simplest word that is still exactly correct. Precision wins when the two conflict.
- Use the field's technical term when it is the precise one, and define it on first use. Do not paraphrase a precise term into vague prose.
- Repeat a word rather than reach for a synonym. Varying the vocabulary hides whether two things are the same thing. The glossary enforces this. See `terminology.md`.
- Trim intensifiers and emphasis adverbs. "deliberately", "precisely", "significantly" stay only when they carry information. "significantly" is replaced by the number.
- No filler openers. "It is important to note that", "Essentially", "As we can see".
- Do not hedge without content. "may be affected" says nothing. "changes by less than 1 percent" or "not bounded here" both say something.

## Voice

Pick one voice for the paper and keep it.
First-person plural is common in the physical sciences.
Agentless passive is common in others.
The journal's guide decides.
Whatever the voice, it narrates what was done and what was found.
It does not narrate software operation.

## What to cut

- Meta-narration. Any sentence that comments on the presentation: it justifies a presentational choice, describes how the argument is organized, or announces that the next sentence is coming. A sentence that connects to what the previous unit left open, hands the next unit what it needs, or defers an objection to a named unit is not meta-narration. It serves the brief's position or objection field and stays.
- The writer's own error correction. Text that argues against a claim the paper does not make serves the writer. Correct the claim and delete the scaffolding.
- Superseded derivations. Cut them rather than leaving them next to the replacement.
- Rhetorical questions.
- Aphoristic closers and evocative verbs. Close a paragraph on the substantive claim and stop.
- Any sentence with no consumer downstream.

## Argument order

- Derive, then state. A defining equation arrives at the end of the chain that produces it, not at the top as a hypothesis.
- Open a section by connecting to what the previous one left unresolved. Then say what this section does about it. Then give the formalism.
- Tie every referenced quantity to its symbol and its equation number.
- Define every symbol once, at the place the glossary names, and never redefine it.

## How much to explain

The reader model sets the audience.
State what problem a method solves, define every symbol on first use, motivate a design choice before giving the equation, and say why the obvious simpler alternative fails.
Prefer an extra explanatory sentence over a compressed one when the sentence supplies a listed prerequisite.

Do not belabor a one-step inference.
The test is whether the step needs a new idea or only the reader's eye.
A new idea gets a sentence.
A reading of notation just written down gets a pointer.

Naming the mechanism is the explanation.
Showing the algebra is not.
The intermediate steps of a derivation stay out of the text.
The text gives the starting expression, names what happens to it, and gives the result.
The exception is a derivation that is itself the paper's contribution.
Then the steps are the result and they are shown.

## Claims

Every claim is derived, measured, cited, or assumed, and the prose says which.

- Derived: point to the equation.
- Measured: give the number with the configuration it holds in. A number without its configuration is meaningless.
- Cited: cite what the paper proves, not the neighborhood it is in. Read the source before attaching it to a claim. If the cited result covers the case only partly, say so.
- Assumed: label it as an assumption.

A measured ratio usually holds in one regime.
Quote the scope with the number.

## Revising

- Revise the whole unit, not the sentence that was complained about.
- When the argument changes, re-read the sentences that were not touched. A unit breaks at the seam between an old setup and a new payoff.
- Every sentence must have a consumer downstream and every claim a premise upstream.

## Source formatting

One sentence per line in the source file.
A reflowed paragraph shows up as a whole-paragraph diff and hides which claim changed.
One sentence per line makes the diff and the review sentence-sized.

## Checklist

1. Does every sentence lead with its subject and carry one statement?
2. Does every sentence pass the removal test, so that no part can be dropped without changing what it says?
3. Is any sentence meta-narration, a rhetorical question, or an argument against a claim the paper does not make?
4. Does any paragraph end on a turn of phrase instead of a claim?
5. Does each defining equation arrive at the end of its derivation?
6. Is every symbol defined once and tied to its equation number where referenced?
7. Is every number quoted with the configuration and regime it holds in?
8. Was every citation read, and does it prove the claim it is attached to?
9. Can any word be replaced with a simpler one without losing precision?
10. Does every named object use its glossary name?
