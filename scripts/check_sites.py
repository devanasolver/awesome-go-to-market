#!/usr/bin/env python3
"""Check every site in data/entries.json: homepage and submission page still respond.
Prints a Markdown report. Exit code 0 always; the workflow opens an issue if the report has problems."""
import json, pathlib, urllib.request, urllib.error
root = pathlib.Path(__file__).resolve().parent.parent
entries = json.loads((root / "data/entries.json").read_text(encoding="utf-8"))
HEAD = {"User-Agent": "Mozilla/5.0 (compatible; awesome-go-to-market weekly check)"}
problems = []
for e in entries:
    for label, url in (("site", e["url"]), ("submit page", e["submit"])):
        req = urllib.request.Request(url, headers=HEAD)
        try:
            code = urllib.request.urlopen(req, timeout=30).status
        except urllib.error.HTTPError as ex:
            code = ex.code
        except Exception as ex:
            problems.append(f"- `{e['name']}` {label}: {type(ex).__name__} ({url})")
            continue
        if code >= 400:
            problems.append(f"- `{e['name']}` {label}: HTTP {code} ({url})")
if problems:
    print("Sites that need a look:\n\n" + "\n".join(problems))
else:
    print("All sites OK.")
