# Figures and tables

These rules apply to every figure and table.
They are checked by the reviewer under the medium and orphan checks.

## Choice of medium

Every message has a best carrier.
The brief names it and says why the alternatives lose.

| The reader needs to | Use |
|---|---|
| Compare shapes, trends, or many points | a figure |
| Look up one or a few numbers | a table |
| Hold one or two numbers | a sentence |
| Follow a relation between symbols | an equation |

A figure that shows what one sentence can say is cut and the sentence stays.
A table with one row is a sentence.
A paragraph that lists more than three numbers of the same kind is a table.

## No orphans

Every figure and every table is referenced by number from the paragraph whose message it supports.
That paragraph is named in the figure's or table's brief under support.
The reference appears in that paragraph, at or before the sentence the figure supports.
A figure or table with no supporting paragraph is removed or given one.

## The supporting paragraph

The supporting paragraph states in prose what the reader should see.
It does not describe the axes or the layout.
It states the message and points at the figure as evidence.

> Bad: Figure 3 shows the bias as a function of beam width for three pixelizations.
> Good: The bias grows with beam width and exceeds 1 percent above 20 arcmin FWHM (Fig. 3).

## Captions

A caption has three parts, in this order.

1. **What is shown.** The first sentence names the quantity and the configuration. "Bias of the second moment as a function of beam width for three pixelizations."
2. **What each element is.** One clause per line, marker, or panel, naming it by its appearance. "The green dashed line shows the analytic prediction. Orange diamonds show the measured bias at nside 1024." Every element in the figure is named here.
3. **The message.** The last sentence is the one claim the reader should carry away, and it matches the message in the brief. "The bias exceeds 1 percent above 20 arcmin FWHM."

For a table, part two names the columns and any grouping of the rows.

## Figures

- One comparison per figure. Two comparisons are two panels or two figures.
- The falsification question in the brief must have an answer. If the figure would look the same with the message false, it does not carry the message.
- Every axis has a quantity and a unit.
- Symbols in the figure use the glossary names and the paper's notation.

## Tables

- Only the columns needed for the lookup named in the brief.
- Every number carries the configuration it was measured under, in the caption or in a column.
- Units in the header, not in every cell.
- The number the reader is expected to look up is easy to find. Sort or group the rows to make it so.
