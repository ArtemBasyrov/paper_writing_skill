#!/usr/bin/env python3
"""Terminology and sentence-length check for paper sources.

Usage:
    check_terms.py --glossary plan/glossary.md --vocab templates/vocabulary/*.md \
        [--max-words 30] sources...

Reports, with file and line:
  - every forbidden alternative from the glossary
  - every outside term from the vocabulary files
  - every sentence longer than --max-words

It never edits anything.
"""

import argparse
import re
import sys


def parse_table(path):
    """Return the body rows of the first Markdown table in the file as lists of cells."""
    rows = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if all(re.fullmatch(r"-+", c) for c in cells):
                continue
            rows.append(cells)
    return rows[1:] if rows else []


def load_glossary(path):
    """Map forbidden alternative -> canonical term."""
    out = {}
    for row in parse_table(path):
        if len(row) < 4:
            continue
        term, forbidden = row[0], row[3]
        for alt in re.split(r"[;,]", forbidden):
            alt = alt.strip()
            if alt:
                out[alt.lower()] = term
    return out


def load_vocab(path):
    """Map outside term -> field term."""
    out = {}
    for row in parse_table(path):
        if len(row) < 2:
            continue
        outside = re.sub(r"\s*\(.*?\)", "", row[0]).strip()
        if outside:
            out[outside.lower()] = row[1]
    return out


def strip_tex(line):
    line = re.sub(r"(?<!\\)%.*", "", line)
    line = re.sub(r"\$[^$]*\$", " ", line)
    line = re.sub(r"\\[A-Za-z]+\*?(\[[^\]]*\])?(\{[^}]*\})?", " ", line)
    return line


def scan(path, glossary, vocab, max_words):
    findings = []
    with open(path, encoding="utf-8") as fh:
        lines = fh.readlines()
    text_lines = [strip_tex(l) for l in lines]

    for n, line in enumerate(text_lines, 1):
        low = line.lower()
        for alt, term in glossary.items():
            if re.search(r"\b" + re.escape(alt) + r"\b", low):
                findings.append((path, n, "glossary", f"'{alt}' -> use '{term}'"))
        for outside, field in vocab.items():
            if re.search(r"\b" + re.escape(outside) + r"\b", low):
                findings.append(
                    (path, n, "vocab", f"'{outside}' -> field term: {field}")
                )

    joined = " ".join(l.strip() for l in text_lines)
    for sent in re.split(r"(?<=[.!?])\s+", joined):
        words = sent.split()
        if len(words) > max_words:
            findings.append((path, 0, "length", f"{len(words)} words: {sent[:80]}..."))
    return findings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--glossary")
    ap.add_argument("--vocab", nargs="*", default=[])
    ap.add_argument("--max-words", type=int, default=30)
    ap.add_argument("sources", nargs="+")
    args = ap.parse_args()

    glossary = load_glossary(args.glossary) if args.glossary else {}
    vocab = {}
    for v in args.vocab:
        for outside, field in load_vocab(v).items():
            vocab[outside] = (
                f"{vocab[outside]} | {field}" if outside in vocab else field
            )

    findings = []
    for src in args.sources:
        findings.extend(scan(src, glossary, vocab, args.max_words))

    for path, n, kind, msg in findings:
        loc = f"{path}:{n}" if n else path
        print(f"{loc}\t{kind}\t{msg}")
    print(f"{len(findings)} findings", file=sys.stderr)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
