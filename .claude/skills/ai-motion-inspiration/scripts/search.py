#!/usr/bin/env python3
"""Search the Awesome AI Motion catalog.

Usage:
  search.py [QUERY ...] [--category C] [--with-prompt] [--with-code]
            [--model M] [--max-seconds N] [--sort bookmarks|recent] [--limit N]
  search.py --show ID        # full record, including the prompt text
  search.py --stats          # counts by category / prompt status
"""
import argparse, json, os, sys
from collections import Counter

CATALOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "catalog.json")
CATEGORIES = ["product", "education", "motion", "characters", "interactive", "stories", "music"]


def load():
    with open(CATALOG, encoding="utf-8") as f:
        return json.load(f)["cases"]


def score(case, terms):
    if not terms:
        return 1
    fields = {
        "title": 4, "titleZh": 2, "summary": 2, "prompt": 1, "author": 3, "model": 2, "category": 2,
    }
    total = 0
    for t in terms:
        hit = 0
        for name, weight in fields.items():
            v = case.get(name) or ""
            if t in str(v).lower():
                hit += weight
        if not hit:
            return 0
        total += hit
    return total


def brief(c):
    tags = [c["category"], f'{c["durationSec"]}s', f'prompt:{c["promptStatus"]}']
    if c.get("codeUrl") or any(r.get("kind") == "code" for r in c.get("resources", [])):
        tags.append("code")
    lines = [f'[{c["id"]}] {c["title"]}  ({", ".join(tags)}; bookmarks {c.get("bookmarks") or 0})',
             f'    {c["summary"]}',
             f'    {c["author"]} · {c.get("model") or "model n/a"} · {c["gallery"]}']
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="*")
    ap.add_argument("--category", choices=CATEGORIES)
    ap.add_argument("--with-prompt", action="store_true", help="only works whose full public prompt is included")
    ap.add_argument("--with-code", action="store_true", help="only works with a public source-code link")
    ap.add_argument("--model")
    ap.add_argument("--max-seconds", type=int)
    ap.add_argument("--sort", choices=["relevance", "bookmarks", "recent"], default="relevance")
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--show")
    ap.add_argument("--stats", action="store_true")
    a = ap.parse_args()
    cases = load()

    if a.show:
        for c in cases:
            if c["id"] == a.show:
                print(json.dumps(c, ensure_ascii=False, indent=2))
                return
        sys.exit(f"no case {a.show}")

    if a.stats:
        print("total", len(cases))
        print("by category", dict(Counter(c["category"] for c in cases)))
        print("by prompt status", dict(Counter(c["promptStatus"] for c in cases)))
        return

    terms = [t.lower() for t in a.query]
    out = []
    for c in cases:
        if a.category and c["category"] != a.category:
            continue
        if a.with_prompt and not c.get("prompt"):
            continue
        if a.with_code and not (c.get("codeUrl") or any(r.get("kind") == "code" for r in c.get("resources", []))):
            continue
        if a.model and a.model.lower() not in (c.get("model") or "").lower():
            continue
        if a.max_seconds and c["durationSec"] > a.max_seconds:
            continue
        s = score(c, terms)
        if s:
            out.append((s, c))

    key = {
        "relevance": lambda x: (x[0], x[1].get("bookmarks") or 0),
        "bookmarks": lambda x: x[1].get("bookmarks") or 0,
        "recent": lambda x: x[1].get("publishedAt") or "",
    }[a.sort]
    out.sort(key=key, reverse=True)
    print(f"{len(out)} match(es); showing {min(len(out), a.limit)}\n")
    for _, c in out[: a.limit]:
        print(brief(c) + "\n")


if __name__ == "__main__":
    main()
