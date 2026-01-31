#!/usr/bin/env python3
import argparse
import re
from urllib.parse import urlparse
from pathlib import Path

REQUIRED_FIELDS = {"type", "title", "authors", "venue", "date", "urls", "filename"}

TYPE_TO_SECTION = {
    "conference": "Conference",
    "workshop": "Workshop",
    "poster": "Poster",
    "phd": "PhD Dissertation",
    "dissertation": "PhD Dissertation",
    "thesis": "Master Thesis",
    "master": "Master Thesis",
}

def split_top_level(s, sep):
    parts = []
    buf = []
    depth = 0
    quote = None
    prev = ""
    for ch in s:
        if quote:
            if ch == quote and prev != "\\":
                quote = None
        else:
            if ch in ("'", '"'):
                quote = ch
            elif ch in "{[":
                depth += 1
            elif ch in "}]":
                depth -= 1
            elif ch == sep and depth == 0:
                parts.append("".join(buf).strip())
                buf = []
                prev = ch
                continue
        buf.append(ch)
        prev = ch
    if buf:
        parts.append("".join(buf).strip())
    return parts

def unquote(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in ("'", '"'):
        return v[1:-1]
    return v

def parse_inline_mapping(s):
    inner = s.strip()[1:-1].strip()
    if not inner:
        return {}
    items = split_top_level(inner, ",")
    out = {}
    for item in items:
        if not item:
            continue
        if ":" not in item:
            raise ValueError(f"Invalid mapping item: {item}")
        k, v = item.split(":", 1)
        out[k.strip()] = unquote(v.strip())
    return out

def parse_inline_yaml(line):
    data = {}
    pairs = split_top_level(line.strip(), ";")
    for pair in pairs:
        if not pair:
            continue
        if ":" not in pair:
            raise ValueError(f"Invalid pair: {pair}")
        key, value = pair.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value.startswith("{") and value.endswith("}"):
            data[key] = parse_inline_mapping(value)
        else:
            data[key] = unquote(value)
    return data

def validate_date(date_str):
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
        raise ValueError("date must be in YYYY-MM-DD format")

def sanitize_filename(name):
    return re.sub(r"[^a-zA-Z0-9._-]+", "_", name).strip("_") or "publication"

def normalize_bold_html(s):
    return s.replace("<b>", "<strong>").replace("</b>", "</strong>")

def build_citation(authors, title, venue):
    authors = normalize_bold_html(authors)
    return (
        f"{authors}, "
        f"<strong>{title}</strong>, "
        f"<i>{venue}</i>."
    )

def normalize_site_link(url, base_url):
    if not url:
        return url
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        return url
    base = urlparse(base_url)
    if parsed.netloc == base.netloc:
        path = parsed.path or ""
        query = f"?{parsed.query}" if parsed.query else ""
        fragment = f"#{parsed.fragment}" if parsed.fragment else ""
        return f"{{{{ site.url }}}}{{{{ site.baseurl }}}}{path}{query}{fragment}"
    return url

def build_publication_md(data, slug, base_url):
    title = data["title"]
    venue = data["venue"]
    date = data["date"]
    authors = data["authors"]
    urls = data.get("urls", {}) or {}
    paper = normalize_site_link(urls.get("paper", ""), base_url)
    code = normalize_site_link(urls.get("code", ""), base_url)
    slides = normalize_site_link(urls.get("slides", ""), base_url)

    citation = build_citation(authors, title, venue)

    link_lines = []
    if paper:
        link_lines.append(f"[[paper]]({paper})")
    if code:
        link_lines.append(f"[[code]]({code})")
    if slides:
        link_lines.append(f"[[slides]]({slides})")

    links_block = "\n".join(link_lines)

    return f"""---
title: "{title}"
collection: publications
permalink: /publications/{slug}
excerpt: ""
date: {date}
venue: "{venue}"
citation: '{citation}'
---

{links_block}
"""

def insert_into_publications_md(md_path, section, entry):
    lines = md_path.read_text().splitlines()
    header = f"## {section}"
    try:
        idx = lines.index(header)
    except ValueError:
        raise ValueError(f"Section not found: {header}")

    insert_at = idx + 1
    if insert_at < len(lines) and lines[insert_at].strip() == "":
        insert_at += 1

    lines.insert(insert_at, entry)
    lines.insert(insert_at + 1, "")
    md_path.write_text("\n".join(lines) + "\n")

def main():
    parser = argparse.ArgumentParser(description="Add a publication from inline YAML.")
    parser.add_argument("--input", "-i", required=True, help="Inline YAML (one line)")
    parser.add_argument("--base-url", default="https://sekwonlee.github.io")
    args = parser.parse_args()

    data = parse_inline_yaml(args.input)
    missing = REQUIRED_FIELDS - set(data.keys())
    if missing:
        raise SystemExit(f"Missing fields: {', '.join(sorted(missing))}")

    validate_date(data["date"])

    pub_type = str(data["type"]).strip().lower()
    section = TYPE_TO_SECTION.get(pub_type, pub_type.title())

    publications_dir = Path("_publications")
    pages_md = Path("_pages/publications.md")

    slug = sanitize_filename(data["filename"])
    pub_path = publications_dir / f"{slug}.md"
    if pub_path.exists():
        raise SystemExit(f"File already exists: {pub_path}")

    publication_md = build_publication_md(data, slug, args.base_url)
    pub_path.write_text(publication_md)

    authors = normalize_bold_html(data["authors"])
    entry = (
        f'{authors}, '
        f'<strong>[<font color="navy">"{data["title"]}"</font>]'
        f'({{ site.url }}{{ site.baseurl }}/publications/{slug})</strong>, '
        f'<i>{data["venue"]}</i>.'
    )
    insert_into_publications_md(pages_md, section, entry)

    print(f"Created _publications/{slug}.md and updated _pages/publications.md")

if __name__ == "__main__":
    main()