# Terminology

"Simple" in this skill means consistent and field-appropriate, not short.
Three things enforce it: the glossary, the field vocabularies, and the terminology script.

## Glossary

The glossary is one row per named object in the paper.

| Term | Symbol | Defined in | Forbidden alternatives |
|---|---|---|---|
| beam center | $\hat c$ | eq:beam-center | centroid, beam centroid, central point |

Rules:

- One name per object. The name is used everywhere, including captions, axis labels, and the abstract.
- No synonyms. Varying the word for the same object makes the reader ask whether two things are the same thing.
- One object per name. If two objects share a name, one of them is renamed.
- The symbol is defined once, at the place named in the table, and never redefined.

## How the glossary is built

The glossary is proposed from the first draft, not written up front.
After the first draft of a section, the drafter lists every named object and every word used for it.
Where more than one word was used, the drafter proposes one and lists the others as forbidden.
The author corrects the proposal.
Later sections extend the glossary and do not rename existing entries.

## Field vocabularies

A vocabulary file maps terms from outside the field to the field's own term.
The paper picks one or more vocabularies in its master plan.
The shipped ones are in `templates/vocabulary/`.

| Outside term | Field term | Note |
|---|---|---|
| loss function | objective function | a statistics paper does not use machine learning vocabulary for estimation |

An outside term is allowed when the paper is about the outside method itself.
Then it is defined on first use and entered in the glossary.

## Over-explanation

An explanation stays if it supplies a prerequisite listed in the brief.
It goes if it does not.
This is the whole test.
The default reader is set by the reader model, so the brief and not the drafter's taste decides what needs explaining.

## The script

`scripts/check_terms.py` takes the glossary, the vocabulary files, and the source files.
It reports every forbidden alternative and every outside term with file and line.
It also reports sentences longer than a word limit.
Its output goes to the reviewer as one input.
It never edits text.
