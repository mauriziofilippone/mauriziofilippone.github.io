#!/usr/bin/env python3
"""Parse bib files and render a publications.md page.

Run from the project root:
    python scripts/render_publications.py
"""

import os
import re
from pybtex.database import parse_file, BibliographyData

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)

BIB_DIR  = os.path.join(PROJECT_DIR, "_bibliography")
OUTPUT   = os.path.join(PROJECT_DIR, "_pages", "publications.md")
BIBS_DIR = os.path.join(PROJECT_DIR, "files", "bibs")

SECTIONS = [
    ("journals.bib",      "Journal Articles"),
    ("conferences.bib",   "Conference Papers"),
    ("discussions.bib",   "Discussions"),
    ("theses.bib",        "Theses"),
]

os.makedirs(BIBS_DIR, exist_ok=True)

def get_field(entry, *names):
    for name in names:
        val = entry.fields.get(name, "")
        if val:
            return val
    return ""

def format_authors(persons):
    """Format as 'F. Last, G. Last, and H. Last' using initials."""
    authors = []
    for p in persons.get("author", []):
        initials = "".join(n[0] + "." for n in p.first_names + p.middle_names if n)
        last = " ".join(p.last_names)
        if initials:
            authors.append(f"{initials} {last}")
        else:
            authors.append(last)
    if not authors:
        return ""
    if len(authors) == 1:
        return authors[0]
    return ", ".join(authors[:-1]) + ", and " + authors[-1]

def format_venue(entry):
    t = entry.type.lower()
    if t == "article":
        venue = get_field(entry, "journal")
        vol   = get_field(entry, "volume")
        num   = get_field(entry, "number")
        pages = get_field(entry, "pages")
        parts = [venue]
        if vol:
            parts.append(vol)
            if num:
                parts[-1] += f"({num})"
        if pages:
            parts.append(pages)
        return ", ".join(p for p in parts if p)
    elif t in ("inproceedings", "proceedings"):
        return get_field(entry, "booktitle")
    elif t in ("phdthesis", "mastersthesis"):
        kind = "Ph.D. thesis" if t == "phdthesis" else "M.Sc. thesis"
        school = get_field(entry, "school")
        return f"{kind}, {school}" if school else kind
    else:
        return get_field(entry, "journal", "booktitle", "howpublished")

def clean(s):
    """Strip LaTeX markup and convert accented characters to Unicode."""
    accent_map = {}
    for cmd, pairs in [
        ('"',  [('a','ä'),('o','ö'),('u','ü'),('A','Ä'),('O','Ö'),('U','Ü'),('e','ë'),('i','ï')]),
        ("'",  [('a','á'),('e','é'),('i','í'),('o','ó'),('u','ú'),('A','Á'),('E','É'),('I','Í'),('O','Ó'),('U','Ú'),('c','ć'),('n','ń'),('s','ś'),('z','ź')]),
        ('`',  [('a','à'),('e','è'),('i','ì'),('o','ò'),('u','ù')]),
        ('^',  [('a','â'),('e','ê'),('i','î'),('o','ô'),('u','û')]),
        ('~',  [('n','ñ'),('N','Ñ'),('a','ã'),('o','õ')]),
        ('v',  [('c','č'),('s','š'),('z','ž'),('C','Č'),('S','Š'),('Z','Ž')]),
        ('c',  [('c','ç'),('C','Ç')]),
    ]:
        for letter, uni in pairs:
            accent_map[(cmd, letter)] = uni

    def replace_accent(m):
        cmd, letter = m.group(1), m.group(2).strip('{}')
        return accent_map.get((cmd, letter), letter)

    s = re.sub(r"\\(['\"`^~vcr])\{([a-zA-Z])\}", replace_accent, s)
    s = re.sub(r"\\(['\"`^~vcr])([a-zA-Z])", replace_accent, s)

    s = re.sub(r'\{\\[a-zA-Z@]+\s*\}', '', s)
    s = re.sub(r'\\[a-zA-Z@]+\{([^}]*)\}', r'\1', s)
    s = re.sub(r'\{([^}]*)\}', r'\1', s)
    s = re.sub(r'\{([^}]*)\}', r'\1', s)
    s = re.sub(r'[{}]', '', s)
    s = re.sub(r'\\&', '&', s)
    s = re.sub(r'\\-', '-', s)
    s = re.sub(r'\\,', ' ', s)
    s = re.sub(r'~', ' ', s)
    s = re.sub(r'--+', '–', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()

def write_bib_file(key, entry):
    """Write a single .bib file for the given entry and return its web path."""
    single = BibliographyData(entries={key: entry})
    bib_path = os.path.join(BIBS_DIR, f"{key}.bib")
    single.to_file(bib_path, bib_format="bibtex")
    return f"/files/bibs/{key}.bib"

lines = []
lines.append("---")
lines.append("layout: single")
lines.append("permalink: /publications/")
lines.append("author_profile: true")
lines.append("---")
lines.append("")

bib_count = 0

for bib_file, section_title in SECTIONS:
    path = os.path.join(BIB_DIR, bib_file)
    if not os.path.exists(path):
        continue

    bib = parse_file(path)
    entries = list(bib.entries.items())

    def year_key(kv):
        try:
            return -int(get_field(kv[1], "year"))
        except:
            return 0
    entries.sort(key=year_key)

    if not entries:
        continue

    lines.append(f"## {section_title}")
    lines.append("")

    for key, entry in entries:
        authors  = clean(format_authors(entry.persons))
        title    = clean(get_field(entry, "title"))
        venue    = clean(format_venue(entry))
        year     = get_field(entry, "year")
        url      = get_field(entry, "url", "pdf")
        code     = get_field(entry, "code")
        bib_path = write_bib_file(key, entry)
        bib_count += 1

        cite = f"{authors}. **{title}**."
        if venue:
            cite += f" *{venue}*."
        if year:
            cite += f" {year}."
        if url:
            cite += f" \\[[link]({url})\\]"
        if code:
            cite += f" \\[[code]({code})\\]"
        cite += f" \\[[bib]({bib_path})\\]"

        lines.append(f"- {cite}")

    lines.append("")

with open(OUTPUT, "w") as f:
    f.write("\n".join(lines))

print(f"Written {OUTPUT}")
print(f"Lines: {len(lines)}, bib files: {bib_count}")
