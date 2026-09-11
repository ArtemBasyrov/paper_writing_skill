# Level additions to the core brief

Every unit answers the core questions in `brief-core.md`.
Each level adds the questions below.

## Paper

- **Claim.** The one claim the paper exists to make. This is the paper's message and the root of the composition rule.
- **Carriers.** Which section carries which piece of the claim.
- **Scope.** What is explicitly out of scope, so the reviewer does not flag its absence.
- **Skim path.** What a reader who reads only the abstract, the figures, and the conclusions takes away. This must be the claim.
- **Reader model.** Who the reader is and what they know a priori. Written once in `reader-model.md` and referenced from every brief's sources.

## Section and subsection

- **Question.** The question the section answers. A section that answers no question is a container and is dissolved into its neighbors.
- **Capability.** What the reader can do after this section that they could not before.
- **Children.** The ordered list of child units whose messages compose to this section's message.

## Paragraph

- **Single message.** Confirm the paragraph carries exactly one message. A paragraph with two messages is two paragraphs.
- **Message sentence.** Where in the paragraph the message sentence sits. The default is first.

## Figure

- **Glance.** What the reader should see within a few seconds of looking.
- **Comparison.** What is being compared to what.
- **Support.** The label of the paragraph whose message this figure supports. A figure without one is an orphan and is not allowed.
- **Falsification.** What the figure would look like if the message were false. If nothing in the figure would change, the figure does not carry the message.
- **Alternative.** Whether a sentence or a table would carry the message better.

## Table

- **Lookup.** The single number or comparison the reader is expected to look up.
- **Columns.** Which columns are necessary for that lookup. Every other column is cut.
- **Support.** The label of the paragraph whose message this table supports. A table without one is an orphan and is not allowed.
- **Alternative.** Whether a figure or a sentence would carry the message better.
