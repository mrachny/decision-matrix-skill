# decision-matrix

Make hard decisions with a weighted decision matrix — the method from
[ASQ's decision matrix guide](https://asq.org/quality-resources/decision-matrix) —
instead of gut feel. Two ways to use it:

- **No install**: a [standalone web app](#no-install-web-app) that walks you through
  it in your browser.
- **Claude Code skill**: install it so Claude builds the whole comparison for you,
  research included.

## No-install web app

**[Try it live](https://mrachny.github.io/decision-matrix-skill/)** — no account, no
server, nothing to install. Describe your decision (or click one of the built-in
examples), review and edit the criteria and weights it proposes, and get a live
interactive ranking: drag a weight slider or mute an option and everything recomputes
instantly.

Opened inside a claude.ai Artifact with AI assist granted, it also researches and
scores every option against every criterion for you — that's what the Claude Artifact
build of this page does. The GitHub Pages copy above (and any plain download) can't
reach an LLM at all — `window.claude` only exists inside a claude.ai Artifact frame —
so it skips straight to a blank comparison you fill in by hand. Either way the
weighting math is identical; only who supplies the scores changes.

## Claude Code skill

Tell Claude what you're deciding — "which job offer should I take," "help me pick a
laptop," "which apartment should I rent" — and it will:

1. Help you pick the **5-10 criteria** that actually matter.
2. Have you **weight** each criterion (1-10) by how important it is to you.
3. **Research** every option against every criterion and score it 1-10, with a
   one-sentence cited reason for each score.
4. Compute each option's **weighted total** and show you one markdown table, ranked
   best to worst.
5. Generate a **self-contained, interactive HTML report**: drag a weight slider or
   mute an option and the ranking updates live. No server, no install, just a file
   you open in a browser.

### Try it

Open [`examples/laptop-purchase.html`](examples/laptop-purchase.html) in your browser
to see a finished report. [`examples/laptop-purchase.json`](examples/laptop-purchase.json)
is the data file behind it.

### Install

```bash
git clone https://github.com/mrachny/decision-matrix-skill ~/.claude/skills/decision-matrix
```

Claude Code loads any skill under `.claude/skills/` automatically and will reach for
this one whenever a conversation looks like a multi-option, multi-factor decision.

### How it's built

| File | Purpose |
|---|---|
| `SKILL.md` | The workflow Claude follows: scope the decision, elicit and define criteria, weight them, research + score, compute totals, build the report |
| `scripts/build_report.py` | Validates your JSON data file and renders it into one standalone `report.html` |
| `assets/report_template.html` | The report's engine — plain HTML/CSS/JS, no build step |
| `webapp/index.html` | The no-install web app — same method, no Claude Code required |
| `docs/index.html` | Exact copy of `webapp/index.html`, served by GitHub Pages (which only reads `/docs` or the repo root) — keep the two in sync if you edit one |
| `references/method.md` | ASQ method background and scoring pitfalls to avoid |

## Use it, star it

This is free to use, fork, and modify — MIT licensed, no strings attached. Every
report built with it carries a small "Built with decision-matrix" credit back to this
repo in its footer by default (set `meta.credit: false` in your data file to remove
it). If it's useful to you, a ⭐ on this repo is the best way to say so.

## License

MIT — see [LICENSE](LICENSE).
