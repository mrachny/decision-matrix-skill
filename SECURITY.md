# Security

## What's actually in this repo

Worth stating plainly, since it's the real basis for any security claim here:

- **No backend, no database, no user accounts.** The two deliverables are a Claude
  Code skill (text instructions plus a small Python script that reads a JSON file and
  writes one HTML file — it doesn't reach the network or start any other program) and
  a client-side web app (plain HTML/CSS/JS, no framework, no build step).
- **Zero third-party dependencies.** No `npm`/`pip` packages beyond the Python
  standard library. Nothing to patch, nothing pulled in from someone else's registry.
- **No secrets.** Nothing in this repo talks to an API key, a token, or a credential
  of any kind.
- **Data stays with whoever runs it.** The web app (`webapp/index.html` /
  `docs/index.html`) only ever writes to the viewer's own browser (`localStorage`) and,
  inside a claude.ai Artifact with AI assist granted, sends text to Claude under that
  viewer's own account and consent. Nothing is sent anywhere else, and nothing is
  shared between viewers.

## Automated scanning

- **[CodeQL](.github/workflows/codeql.yml)** runs on every push and pull request
  against `main`, plus weekly, analyzing both the JavaScript (embedded in the HTML
  files) and the Python build script for known vulnerability patterns.
- **[OpenSSF Scorecard](.github/workflows/scorecard.yml)** runs weekly and on every
  push to `main`, publishing an objective score (branch protection, pinned actions,
  static analysis coverage, and more) to the public Scorecard API.
- GitHub's built-in secret scanning and Dependabot alerts are on by default for this
  public repo.

None of this is a substitute for review — it's automated pattern-matching, not a
guarantee. Treat the badges in the README as "actively and openly checked," not as
"certified secure."

## Known issue classes already addressed

- An earlier version built a few UI strings (the "close call" note, the results
  ribbon, chart tag chips, group headers) by concatenating user- or data-supplied
  labels directly into `innerHTML`. Free-text fields (option and criterion names) are
  user-editable in the web app, so this was a real HTML/script-injection risk, not
  theoretical. Fixed by rebuilding all of these with `textContent` / `createTextNode`
  / `setAttribute`, so label content is always treated as text, never markup. See the
  commit history for specifics.

## Reporting a vulnerability

Please open a [GitHub issue](https://github.com/mrachny/decision-matrix-skill/issues)
describing the problem. For anything you'd rather not post publicly first, use
GitHub's [private vulnerability reporting](https://github.com/mrachny/decision-matrix-skill/security/advisories/new)
instead. There's no bug bounty — this is a free, hobby-maintained project — but real
reports will get a real response and a fix.
