#!/usr/bin/env python3
"""Render publications_list.tex for inclusion in the LaTeX CV.

Run from the project root:
    python scripts/render_cv_publications.py [--output PATH]

Default output: _bibliography/publications_list.tex
Then \\input it from cv_en.tex (or short_cv.tex) with the correct relative path.
"""

import os
import re
import argparse
from pybtex.database import parse_file

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
BIB_DIR     = os.path.join(PROJECT_DIR, "_bibliography")
DEFAULT_OUT = os.path.join(BIB_DIR, "publications_list.tex")

SECTIONS = [
    ("journals.bib",    "Journals"),
    ("conferences.bib", "Conferences"),
    ("discussions.bib", "Discussions"),
    ("theses.bib",      "Theses"),
]


def get_field(entry, *names):
    for name in names:
        val = entry.fields.get(name, "")
        if val:
            return val
    return ""


def format_names(person_list):
    """Format a list of pybtex Person objects as 'F. Last, G. Last, and H. Last'."""
    formatted = []
    for p in person_list:
        initials = "".join(n[0] + "." for n in p.first_names + p.middle_names if n)
        last = " ".join(p.last_names)
        formatted.append(f"{initials} {last}" if initials else last)
    if not formatted:
        return ""
    if len(formatted) == 1:
        return formatted[0]
    return ", ".join(formatted[:-1]) + ", and " + formatted[-1]


def format_editors(entry):
    """Return 'Ed. Last, ..., editor(s)' string, or empty string."""
    eds = entry.persons.get("editor", [])
    if not eds:
        return ""
    names = format_names(eds)
    plural = "editors" if len(eds) > 1 else "editor"
    return f"{names}, {plural}"


def format_entry(entry):
    t       = entry.type.lower()
    authors = format_names(entry.persons.get("author", []))
    title   = get_field(entry, "title")
    year    = get_field(entry, "year")

    parts = []
    if authors:
        parts.append(f"{authors}.")
    parts.append(f"{title}.")

    if t == "article":
        journal = get_field(entry, "journal")
        vol     = get_field(entry, "volume")
        num     = get_field(entry, "number")
        pages   = get_field(entry, "pages")

        venue = f"\\emph{{{journal}}}"
        vol_str = ""
        if vol:
            vol_str = vol
            if num:
                vol_str += f"({num})"
        detail_parts = []
        if vol_str:
            detail_parts.append(vol_str)
        if pages:
            detail_parts.append(pages)
        if detail_parts:
            venue += f", {':'.join(detail_parts)}"
        if year:
            venue += f", {year}"
        parts.append(venue + ".")

    elif t in ("inproceedings", "proceedings"):
        booktitle = get_field(entry, "booktitle")
        volume    = get_field(entry, "volume")
        series    = get_field(entry, "series")
        pages     = get_field(entry, "pages")
        publisher = get_field(entry, "publisher")
        address   = get_field(entry, "address")
        editors   = format_editors(entry)

        in_str = "In "
        if editors:
            in_str += f"{editors}, "
        in_str += f"\\emph{{{booktitle}}}"
        if volume and series:
            in_str += f", volume {volume} of \\emph{{{series}}}"
        elif volume:
            in_str += f", volume {volume}"
        if pages:
            in_str += f", pages {pages}"

        pub_parts = []
        if address:
            pub_parts.append(address)
        if publisher:
            pub_parts.append(publisher)
        if year:
            pub_parts.append(str(year))
        if pub_parts:
            in_str += ". " + ", ".join(pub_parts)
        parts.append(in_str + ".")

    elif t in ("phdthesis", "mastersthesis"):
        kind   = "Ph.D.\\ thesis" if t == "phdthesis" else "M.Sc.\\ thesis"
        school = get_field(entry, "school")
        s = kind
        if school:
            s += f", {school}"
        if year:
            s += f", {year}"
        parts.append(s + ".")

    else:
        # misc, techreport, unpublished, etc.
        howpub = get_field(entry, "howpublished", "institution", "note")
        if howpub:
            parts.append(f"{howpub}.")
        if year:
            parts.append(f"{year}.")

    return " ".join(parts)


def year_key(kv):
    try:
        return -int(get_field(kv[1], "year"))
    except Exception:
        return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--output", default=DEFAULT_OUT,
        help="Output path for publications_list.tex "
             f"(default: {DEFAULT_OUT})"
    )
    args = parser.parse_args()

    lines = []
    total = 0

    for bib_file, section_title in SECTIONS:
        path = os.path.join(BIB_DIR, bib_file)
        if not os.path.exists(path):
            continue
        bib     = parse_file(path)
        entries = sorted(bib.entries.items(), key=year_key)
        if not entries:
            continue

        lines.append(f"\\textbf{{{section_title}}}\\begin{{itemize}}")
        for key, entry in entries:
            lines.append(f"\\item  {format_entry(entry)}")
            total += 1
        lines.append("\\end{itemize}")
        lines.append("")

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Written {args.output}  ({total} entries)")


if __name__ == "__main__":
    main()
