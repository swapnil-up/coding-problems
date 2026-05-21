#!/usr/bin/env python3
"""Organize bookmarks.html into topic-based folders with Firefox TAGS support.

Usage:
    python3 organize_bookmarks.py

Requires:
    - bookmarks.html (your Firefox bookmark export)
    - bookmarks_config.py (your topic/domain/keyword mappings — see example)

Output:
    - bookmarks-organized.html  (all topics in one file, importable into Firefox)
    - bookmarks-{topic}.html    (individual topic files)
"""

import re
import os
import html as html_mod
import sys
from collections import defaultdict
from urllib.parse import unquote

# Import config
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    from bookmarks_config import SRC, OUT_DIR, TOPIC_ORDER, TOPIC_LABELS, \
        DOMAIN_TOPIC_MAP, KEYWORD_TAGS, FOLDER_HINTS
except ImportError:
    print("Error: bookmarks_config.py not found.")
    print("Copy bookmarks_config.example.py to bookmarks_config.py and customize it.")
    sys.exit(1)


def extract_attr(tag, attr):
    m = re.search(rf'\b{attr}="(.*?)"', tag, re.IGNORECASE)
    return m.group(1) if m else ""


def get_domain(url):
    m = re.search(r'https?://(?:www\.)?([^/]+)', url)
    return m.group(1).lower() if m else ""


def make_title(url):
    """Make a readable title from URL for bookmarks with empty titles."""
    path = unquote(url.split("?")[0])
    path = re.sub(r'https?://(?:www\.)?', '', path)
    path = re.sub(r'/$', '', path)
    parts = path.split("/")
    for part in reversed(parts):
        part = re.sub(r'[-_]', ' ', part)
        part = re.sub(r'\.[a-z]{2,4}$', '', part)
        part = part.strip()
        if part and len(part) > 3:
            return part[:80]
    return url[:80]


def classify_bookmark(href, title, folder_path, existing_tags):
    """Return (primary_topic, set_of_all_tags) for a bookmark."""
    domain = get_domain(href)
    title_lower = title.lower()

    tags = set()
    if existing_tags:
        for t in existing_tags:
            tags.add(t.strip().lower().replace(" ", "-"))

    primary = DOMAIN_TOPIC_MAP.get(domain)
    if not primary and domain:
        for known_domain, topic in DOMAIN_TOPIC_MAP.items():
            if domain.endswith("." + known_domain) or domain == known_domain:
                primary = topic
                break

    if "youtube.com" in href or "youtu.be" in href:
        primary = "youtube"
    elif "reddit.com" in href:
        primary = "reddit"

    if not primary:
        folder_lower = " ".join(f.lower() for f in folder_path)
        for topic, hints in FOLDER_HINTS.items():
            if primary:
                break
            for hint in hints:
                if hint in folder_lower:
                    primary = topic
                    break

    if not primary:
        primary = "other"

    tags.add(primary)

    for topic, pattern in KEYWORD_TAGS.items():
        if re.search(pattern, title_lower):
            tags.add(topic)

    if existing_tags:
        for t in existing_tags:
            t_clean = t.strip().lower().replace(" ", "-")
            if t_clean:
                tags.add(t_clean)

    return primary, tags


def parse_bookmarks(filepath):
    """Parse bookmarks.html file. Returns list of dicts."""
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        print("Export your Firefox bookmarks to HTML and save as bookmarks.html")
        sys.exit(1)

    with open(filepath, "r", encoding="utf-8") as f:
        html_content = f.read()

    lines = html_content.split("\n")
    bookmarks = []
    current_folder = []
    dl_depth = 0

    for line in lines:
        stripped = line.strip()

        m = re.search(r'<H3[^>]*>(.*?)</H3>', stripped)
        if m:
            folder_name = m.group(1).strip()
            current_folder.append(folder_name)

        if '<DL' in stripped:
            dl_depth += 1

        if '</DL>' in stripped:
            dl_depth -= 1
            if dl_depth < 0:
                dl_depth = 0
            if current_folder and len(current_folder) > dl_depth:
                current_folder = current_folder[:dl_depth]

        if '<A HREF=' in stripped:
            href = extract_attr(stripped, "HREF")
            title_m = re.search(r'>([^<]*)</A>', stripped)
            title = title_m.group(1) if title_m else ""
            title = html_mod.unescape(title).strip()
            if not title:
                title = make_title(href)

            bm = {
                "href": href,
                "title": title,
                "add_date": extract_attr(stripped, "ADD_DATE"),
                "last_modified": extract_attr(stripped, "LAST_MODIFIED"),
                "icon_uri": extract_attr(stripped, "ICON_URI"),
                "icon": extract_attr(stripped, "ICON"),
                "existing_tags": [
                    t.strip() for t in
                    extract_attr(stripped, "TAGS").split(",")
                    if t.strip()
                ] if extract_attr(stripped, "TAGS") else [],
                "folder_path": list(current_folder),
            }
            bookmarks.append(bm)

    return bookmarks


def deduplicate(bookmarks):
    """Deduplicate by URL, keeping the one with the longest title + most attrs."""
    seen = {}
    for bm in bookmarks:
        url = bm["href"]
        if url in seen:
            existing = seen[url]
            existing_score = len(existing["title"]) + len(existing["add_date"]) + len(existing["icon"])
            new_score = len(bm["title"]) + len(bm["add_date"]) + len(bm["icon"])
            if new_score > existing_score:
                seen[url] = bm
            existing["existing_tags"] = list(
                set(existing["existing_tags"] + bm["existing_tags"])
            )
        else:
            seen[url] = bm
    return list(seen.values())


def render_a_tag(bm, all_tags):
    """Render a <DT><A ...>Title</A> line with TAGS attribute."""
    attrs = [f'HREF="{bm["href"]}"']
    if bm["add_date"]:
        attrs.append(f'ADD_DATE="{bm["add_date"]}"')
    if bm["last_modified"]:
        attrs.append(f'LAST_MODIFIED="{bm["last_modified"]}"')
    if bm["icon_uri"]:
        attrs.append(f'ICON_URI="{bm["icon_uri"]}"')
    if bm["icon"]:
        attrs.append(f'ICON="{bm["icon"]}"')
    tag_list = sorted(all_tags) if all_tags else []
    if tag_list:
        attrs.append(f'TAGS="{",".join(tag_list)}"')
    title = html_mod.escape(bm["title"])
    return f'        <DT><A {" ".join(attrs)}>{title}</A>'


def build_topic_tree(bookmarks):
    """Organize bookmarks into topic-based folder hierarchy."""
    topic_bms = defaultdict(list)
    for bm in bookmarks:
        primary, all_tags = classify_bookmark(
            bm["href"], bm["title"], bm["folder_path"], bm["existing_tags"]
        )
        bm["_primary"] = primary
        bm["_tags"] = all_tags
        topic_bms[primary].append(bm)
    return topic_bms


def write_topic_file(topic_bms, topic, filepath):
    """Write a single topic file."""
    label = TOPIC_LABELS.get(topic, topic.replace("-", " ").title())
    lines = [
        '<!DOCTYPE NETSCAPE-Bookmark-file-1>',
        '<!-- This is an automatically generated file. -->',
        '<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">',
        f'<TITLE>{label}</TITLE>',
        f'<H1>{label}</H1>',
        '<DL><p>',
    ]

    bms = topic_bms.get(topic, [])

    if topic == "reddit":
        subreddits = defaultdict(list)
        for bm in bms:
            m = re.search(r'reddit\.com/r/([^/]+)', bm["href"])
            sub = m.group(1) if m else "Other"
            subreddits[sub].append(bm)
        for sub in sorted(subreddits.keys()):
            lines.append(f'    <DT><H3 ADD_DATE="0">r/{sub}</H3>')
            lines.append('    <DL><p>')
            for bm in sorted(subreddits[sub], key=lambda x: x["title"].lower()):
                lines.append(render_a_tag(bm, bm["_tags"]))
            lines.append('    </DL><p>')
    elif topic == "youtube":
        for bm in sorted(bms, key=lambda x: x["title"].lower()):
            lines.append(render_a_tag(bm, bm["_tags"]))
    else:
        for bm in sorted(bms, key=lambda x: x["title"].lower()):
            lines.append(render_a_tag(bm, bm["_tags"]))

    lines.append('</DL><p>')
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return len(bms)


def write_combined_file(topic_bms, filepath):
    """Write one big file with all topics as top-level folders + TAGS."""
    lines = [
        '<!DOCTYPE NETSCAPE-Bookmark-file-1>',
        '<!-- This is an automatically generated file. -->',
        '<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">',
        '<TITLE>Organized Bookmarks</TITLE>',
        '<H1>Bookmarks Menu</H1>',
        '<DL><p>',
    ]

    for topic in TOPIC_ORDER:
        if topic not in topic_bms or not topic_bms[topic]:
            continue
        label = TOPIC_LABELS.get(topic, topic.replace("-", " ").title())
        lines.append(f'    <DT><H3 ADD_DATE="0">{label}</H3>')
        lines.append('    <DL><p>')

        bms = topic_bms[topic]
        if topic == "reddit":
            subreddits = defaultdict(list)
            for bm in bms:
                m = re.search(r'reddit\.com/r/([^/]+)', bm["href"])
                sub = m.group(1) if m else "Other"
                subreddits[sub].append(bm)
            for sub in sorted(subreddits.keys()):
                lines.append(f'        <DT><H3 ADD_DATE="0">r/{sub}</H3>')
                lines.append('        <DL><p>')
                for bm in sorted(subreddits[sub], key=lambda x: x["title"].lower()):
                    lines.append(render_a_tag(bm, bm["_tags"]))
                lines.append('        </DL><p>')
        elif topic == "youtube":
            for bm in sorted(bms, key=lambda x: x["title"].lower()):
                lines.append(render_a_tag(bm, bm["_tags"]))
        else:
            for bm in sorted(bms, key=lambda x: x["title"].lower()):
                lines.append(render_a_tag(bm, bm["_tags"]))

        lines.append('    </DL><p>')

    all_tags_used = set()
    for bm_list in topic_bms.values():
        for bm in bm_list:
            all_tags_used.update(bm["_tags"])
    lines.append('    <DT><H3 ADD_DATE="0">All Tags Used</H3>')
    lines.append('    <DL><p>')
    for tag in sorted(all_tags_used):
        count = sum(
            1 for bm_list in topic_bms.values()
            for bm in bm_list if tag in bm["_tags"]
        )
        lines.append(f'        <DT><A HREF="about:blank" TAGS="{tag}">{tag} ({count} bookmarks)</A>')
    lines.append('    </DL><p>')

    lines.append('</DL>')

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def generate_stats(topic_bms):
    """Print statistics."""
    total = sum(len(bms) for bms in topic_bms.values())
    print(f"\nTotal bookmarks: {total}")
    print(f"{'Topic':<35} {'Count':>6} {'%':>6}")
    print("-" * 47)
    for topic in TOPIC_ORDER:
        if topic in topic_bms:
            count = len(topic_bms[topic])
            pct = count / total * 100
            print(f"{TOPIC_LABELS.get(topic, topic):<35} {count:>6} {pct:>5.1f}%")

    all_tags = set()
    tag_counts = defaultdict(int)
    for bm_list in topic_bms.values():
        for bm in bm_list:
            all_tags.update(bm["_tags"])
            for t in bm["_tags"]:
                tag_counts[t] += 1
    print(f"\nUnique tags: {len(all_tags)}")
    print(f"{'Tag':<25} {'Count':>6}")
    print("-" * 32)
    for tag, cnt in sorted(tag_counts.items(), key=lambda x: -x[1])[:25]:
        print(f"{tag:<25} {cnt:>6}")


def main():
    print(f"Reading: {SRC}")
    bookmarks = parse_bookmarks(SRC)
    print(f"Found {len(bookmarks)} raw bookmarks.")

    bookmarks = deduplicate(bookmarks)
    print(f"Deduped to {len(bookmarks)} unique bookmarks.")

    print("Classifying...")
    topic_bms = build_topic_tree(bookmarks)
    generate_stats(topic_bms)

    combined_path = os.path.join(OUT_DIR, "bookmarks-organized.html")
    print(f"\nWriting: {combined_path}")
    write_combined_file(topic_bms, combined_path)

    for topic in TOPIC_ORDER:
        if topic not in topic_bms or not topic_bms[topic]:
            continue
        fname = f"bookmarks-{topic}.html"
        fpath = os.path.join(OUT_DIR, fname)
        count = write_topic_file(topic_bms, topic, fpath)
        print(f"  {fname}: {count} bookmarks")

    print("\nDone!")


if __name__ == "__main__":
    main()
