# paper-writing

A skill for planning, drafting, and reviewing a scientific paper one unit at a time.

A unit is the paper, a section, a subsection, a paragraph, a figure, or a table.
Every unit gets a brief before any prose is written.
A reviewer with a fresh context checks each draft against its brief.
A draft, review, draft loop runs for at most five rounds and keeps a log so findings are not re-litigated.

## Install

Copy or symlink this directory into your agent's skills directory.
For Claude Code:

```bash
ln -s /path/to/paper_writing_skill ~/.claude/skills/paper-writing
```

## Layout

| Path | Contents |
|---|---|
| `SKILL.md` | the workflow |
| `references/brief-core.md` | the eight questions every unit answers |
| `references/brief-levels.md` | extra questions per level |
| `references/review-rubric.md` | what the reviewer checks and how it reports |
| `references/figures-tables.md` | medium choice, no orphans, captions |
| `references/terminology.md` | glossary and field vocabularies |
| `references/prose-style.md` | sentence-level rules |
| `templates/` | plan, glossary, log, reader model, and vocabulary templates |
| `scripts/check_terms.py` | terminology and sentence-length check |

## Adapting

Three things are meant to be replaced per paper or per field:

- `templates/reader-model.md` sets who the reader is and what they know.
- `templates/vocabulary/` holds field vocabularies. Two examples are shipped, for astrophysics and statistics. Add your own.
- `references/prose-style.md` holds the sentence-level rules. They are one author's preferences. Edit them to yours, and the journal's language guide and the project's notation conventions outrank them where they differ.
