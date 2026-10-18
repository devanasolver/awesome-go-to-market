#!/usr/bin/env python3
"""Build README.md from data/entries.json and data/meta.json. Run: python scripts/build_readme.py"""
import json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
meta = json.loads((root / "data/meta.json").read_text(encoding="utf-8"))
entries = json.loads((root / "data/entries.json").read_text(encoding="utf-8"))
cats = meta["categories"]
out = [meta["header"].rstrip(), ""]
out.append("## Contents\n")
for c in cats:
    out.append(f"- [{c['title']}](#{c['anchor']})")
out += ["- [How to use this list](#how-to-use-this-list)", "- [Contributing](#contributing)", ""]
for c in cats:
    out.append(f"## {c['title']}\n")
    out.append(c["blurb"] + "\n")
    items = sorted([e for e in entries if e["category"] == c["id"]], key=lambda e: e["name"].lower())
    for e in items:
        out.append(f"- [{e['name']}]({e['url']}) - {e['description']} "
                   f"**Cost:** {e['cost']}. [Submit here]({e['submit']}).")
    out.append("")
out.append(meta["footer"].rstrip())
(root / "README.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print("built", len(entries), "entries")
