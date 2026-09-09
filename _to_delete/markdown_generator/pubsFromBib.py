#!/usr/bin/env python
# coding: utf-8

"""
Publications markdown generator for Academic Pages (academicpages.github.io)

Reads BibTeX files and generates one Markdown file per publication in
../_publications/, ready for Jekyll to render on the Publications and CV pages.

Usage:
    cd markdown_generator
    python pubsFromBib.py

BibTeX files are expected in ../_bibliography/:
    ../_bibliography/journals.bib
    ../_bibliography/conferences.bib
    ../_bibliography/discussions.bib
    ../_bibliography/theses.bib

To regenerate after adding publications, simply re-run this script.
The 'category' field in each Markdown file maps to publication_category in _config.yml:
    manuscripts  -> Journal Articles
    conferences  -> Conference Papers
    books        -> Books (theses, discussions)
"""

from pybtex.database.input import bibtex
import pybtex.database.input.bibtex
from time import strptime
import string
import html
import os
import re

# ---------------------------------------------------------------------------
# Configuration: map bib files to their venue key and publication category
# ---------------------------------------------------------------------------
publist = {
    "journal": {
        "file":         "../_bibliography/journals.bib",
        "venuekey":     "journal",
        "venue-pretext": "",
        "category":     "manuscripts",   # matches _config.yml publication_category
    },
    "proceeding": {
        "file":         "../_bibliography/conferences.bib",
        "venuekey":     "booktitle",
        "venue-pretext": "In the proceedings of ",
        "category":     "conferences",
    },
    "discussion": {
        "file":         "../_bibliography/discussions.bib",
        "venuekey":     "journal",
        "venue-pretext": "",
        "category":     "manuscripts",
    },
    "thesis": {
        "file":         "../_bibliography/theses.bib",
        "venuekey":     "school",
        "venue-pretext": "",
        "category":     "books",
    },
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
}

def html_escape(text):
    """Produce HTML entities within text."""
    return "".join(html_escape_table.get(c, c) for c in text)


def get_authors(entry):
    """Return a formatted author string from a pybtex entry."""
    parts = []
    for author in entry.persons.get("author", []):
        first = " ".join(author.first_names) if author.first_names else ""
        last  = " ".join(author.last_names)  if author.last_names  else ""
        parts.append(f"{first} {last}".strip())
    return ", ".join(parts)


# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------
output_dir = "../_publications"
os.makedirs(output_dir, exist_ok=True)

for pubsource, meta in publist.items():
    bib_path = meta["file"]
    if not os.path.isfile(bib_path):
        print(f"[SKIP] Bib file not found: {bib_path}")
        continue

    parser  = bibtex.Parser()
    bibdata = parser.parse_file(bib_path)

    for bib_id in bibdata.entries:
        pub_year  = "1900"
        pub_month = "01"
        pub_day   = "01"

        b = bibdata.entries[bib_id].fields

        try:
            pub_year = str(b["year"])

            if "month" in b:
                m = str(b["month"])
                if len(m) < 3:
                    pub_month = ("0" + m)[-2:]
                elif m not in range(12):
                    try:
                        pub_month = "{:02d}".format(strptime(m[:3], '%b').tm_mon)
                    except ValueError:
                        pub_month = "01"
                else:
                    pub_month = str(m)

            if "day" in b:
                pub_day = str(b["day"])

            pub_date   = f"{pub_year}-{pub_month}-{pub_day}"
            raw_title  = b["title"].replace("{", "").replace("}", "").replace("\\", "")
            clean_title = raw_title.replace(" ", "-")
            url_slug   = re.sub(r"\[.*\]|[^a-zA-Z0-9_-]", "", clean_title).replace("--", "-")
            md_filename = f"{pub_date}-{url_slug}.md".replace("--", "-")
            html_filename = f"{pub_date}-{url_slug}".replace("--", "-")

            # Authors
            author_str = get_authors(bibdata.entries[bib_id])

            # Venue
            venuekey = meta["venuekey"]
            venue_raw = b.get(venuekey, "")
            venue = meta["venue-pretext"] + venue_raw.replace("{", "").replace("}", "").replace("\\", "")

            # Citation string
            citation = f'{author_str}, "{html_escape(raw_title)}." {html_escape(venue)}, {pub_year}.'

            # --- Build YAML front matter ---
            md = f'---\ntitle: "{html_escape(raw_title)}"\n'
            md += f"collection: publications\n"
            md += f"category: {meta['category']}\n"
            md += f"permalink: /publication/{html_filename}\n"

            note = b.get("note", "")
            if len(str(note)) > 5:
                md += f"excerpt: '{html_escape(str(note))}'\n"
                has_note = True
            else:
                has_note = False

            md += f"date: {pub_date}\n"
            md += f"venue: '{html_escape(venue)}'\n"

            # Prefer 'url' field; fall back to 'pdf'
            paper_url = b.get("url", b.get("pdf", ""))
            has_url = len(str(paper_url)) > 5
            if has_url:
                md += f"paperurl: '{paper_url}'\n"

            md += f"citation: '{html_escape(citation)}'\n"
            md += "---\n"

            # --- Body ---
            if has_note:
                md += f"\n{html_escape(str(note))}\n"

            if has_url:
                md += f"\n[Download paper]({paper_url}){{:target=\"_blank\"}}\n"
            else:
                query = html.escape(clean_title.replace("-", "+"))
                md += f"\nUse [Google Scholar](https://scholar.google.com/scholar?q={query}){{:target=\"_blank\"}} for full citation\n"

            out_path = os.path.join(output_dir, os.path.basename(md_filename))
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(md)

            print(f"OK  {bib_id}: \"{raw_title[:70]}{'...' if len(raw_title)>70 else ''}\"")

        except KeyError as e:
            title_preview = b.get("title", bib_id)[:50]
            print(f"WARN Missing field {e} in {bib_id}: \"{title_preview}\"")
            continue

print("\nDone. Markdown files written to _publications/")
