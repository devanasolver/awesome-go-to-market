# Contributing

Thanks for helping. This list stays useful only if every entry is real, open for submissions and honestly described.

## What gets in

A site can be added if all of these are true:

1. It is **live** and **accepting submissions** right now.
2. It fits the list's niche: launching, listing, reviewing or promoting a software or AI product.
3. The entry links to the **real submission page** (submit form, vendor sign-up, advertise page), not just the homepage. Account walls are fine; say so.
4. The **cost is stated honestly**: free, paid, free-with-backlink, refund-if-rejected. Check the site itself, not a blog post about it.
5. It is **not a duplicate** of another entry.

Owners may suggest their own site. It is judged by the same rules. Say so in the pull request.

## How to add a site

1. Fork this repo.
2. Add **one** object to `data/entries.json`:
   ```json
   {
     "name": "Site name",
     "url": "https://example.com",
     "submit": "https://example.com/submit",
     "category": "directories",
     "cost": "Free + paid from $39",
     "description": "One plain sentence. What it is. Say if an account is needed.",
     "verified": "YYYY-MM-DD"
   }
   ```
   Categories: `launch`, `directories`, `stores`, `reviews`, `newsletters`, `communities`, `lists`.
3. Run `python scripts/build_readme.py` to rebuild `README.md`. Do not edit `README.md` by hand.
4. Open a pull request using the template. One site per PR.

## Writing the description

- Plain words. Short. One sentence, two at most.
- Say what it is, not how great it is. No "best", "amazing", "revolutionary".
- Repeat the site's own audience claims only with "claims" or similar.
- No affiliate or tracking links.

## Removing or fixing entries

A weekly check (GitHub Action) opens an issue when a listed site or submission page stops responding. Maintainers remove or fix those. You can also open a PR to remove a dead site or update a changed price.

## Changelog

Add a line to `CHANGELOG.md` under "Unreleased" for each change.
