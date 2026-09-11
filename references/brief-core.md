# Core brief

Every unit of the paper gets a brief before any prose is written for it.
A unit is the paper, a section, a subsection, a paragraph, a figure, or a table.
The brief is the contract the draft is written against and the reviewer checks against.

## The questions

1. **Goal.** What this unit is for. One sentence.
2. **Message.** The one claim the unit carries, written as one sentence. If it needs two sentences, split the unit.
3. **Position.** What the previous unit left open, and what the next unit needs from this one.
4. **Prerequisites.** What the reader must already hold in mind to follow the message.
5. **Source of each prerequisite.** Either a reference into the text (section, equation, figure) or the reader model. A prerequisite with no source is a gap in the paper.
6. **Evidence.** What backs the message: derived (equation), measured (number with configuration and script), cited (paper and section), or assumed (labeled as such). The script name stays in the brief. The paper text gives the number and its configuration only.
7. **Objection.** What a skeptical reader would say, and whether this unit answers it or defers it to a named unit.
8. **Medium.** Whether prose, a figure, a table, or an equation carries this message best, and why the chosen one wins. See `figures-tables.md`.

Each level adds a few questions of its own.
They are listed in `brief-levels.md`.

## Format

A brief is a fenced block in the section plan file, keyed by the unit's label.
The label is the LaTeX label the unit will have in the source, so the plan and the source can be cross-checked.

```markdown
### par:beam-center-def

- goal: define the beam center so later moments have a reference point
- message: We define the beam center as the first moment of the beam power.
- position: prev par:beam-power-split introduced the power split; next par:beam-second-moment needs a center to expand around
- prerequisites: beam power $B(\hat n)$; first moment of a function on the sphere
- sources: $B(\hat n)$ from eq:beam-power; first moment from reader model
- evidence: derived, eq:beam-center
- objection: the first moment is not unique on the sphere; answered here by restricting to the tangent plane
- medium: prose plus one equation; a figure would add nothing the equation does not say
```

## The paper is not a code manual

The paper is a self-contained unit of research.
It stands without the code, the notes, or the plan.
Script names, file paths, function names, configuration keys, and software steps do not appear in the text.
A measurement is reported with its physical configuration, not with the tool that produced it.
Where the code is the subject of the paper, it is named once with a citation and then referred to by its method, not by its file names.

## Composition rule

A parent unit's message must equal the ordered child messages, with nothing missing and nothing extra.
A child whose message is not needed by the parent is cut or moved.
A parent claim that no child carries is a gap.
The reviewer checks this rule at every level before any prose is drafted.

## Filled example

The example below is a paragraph brief and the paragraph written from it.

```markdown
### par:why-not-projection

- goal: say why the obvious alternative to the tangent plane construction fails
- message: Projecting the beam onto a plane before taking moments biases the second moment at large beam widths.
- position: prev par:beam-center-def defined the center on the tangent plane; next par:tangent-moments gives the tangent plane moments
- prerequisites: gnomonic projection; second moment of the beam
- sources: gnomonic projection from reader model; second moment from eq:beam-second-moment
- evidence: measured, 3 percent at 30 arcmin FWHM, script `moment_bias.py`
- objection: the bias is small for narrow beams; deferred to sec:results where beam widths are swept
- medium: prose with one number; a figure would show the trend but the trend is not the message here
```

> The obvious alternative is to project the beam onto a plane and take the moments there.
> This biases the second moment.
> We measure a 3 percent bias at 30 arcmin FWHM.
> Section 5 sweeps the beam width and shows where the bias becomes acceptable.
