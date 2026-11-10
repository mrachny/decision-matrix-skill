# decision-matrix

A [Claude Code skill](https://docs.claude.com/en/docs/claude-code/skills) that turns
"I can't decide" into a researched, weighted decision matrix — the method described in
[ASQ's decision matrix guide](https://asq.org/quality-resources/decision-matrix).

Tell Claude what you're trying to decide ("which apartment should I rent," "which job
offer should I take," "help me pick a laptop"), and the skill:

1. Helps you name the **5-10 criteria** that actually matter, each with a one-line
   definition so scoring stays consistent.
2. Has you **weight** each criterion 1-10 by how much it matters to you.
3. **Researches** how well each option satisfies each criterion — using real sources,
   not vibes — and scores every option × criterion cell 1-10 with a one-sentence,
   cited rationale.
4. Computes a **weighted total** per option (normalized to stay on a 1-10 scale) and
   shows it to you as a single markdown table, sorted best to worst.
5. Builds a **self-contained, interactive HTML report** — no server, no dependencies
   beyond one web font — where you can drag the importance sliders or click an option
   to mute/unmute it from the ranking, and watch the chart and totals update live.

## Try the example

[`examples/laptop-purchase.html`](examples/laptop-purchase.html) is a filled-in example
report (download it and open it in a browser, or serve the repo with GitHub Pages).
[`examples/laptop-purchase.json`](examples/laptop-purchase.json) is the data file that
produced it — a good reference for the data shape before writing your own.

## Install

Copy this repo into a skills directory Claude Code reads from, e.g.:

```bash
git clone https://github.com/<you>/decision-matrix-skill ~/.claude/skills/decision-matrix
```

(or your project's own `.claude/skills/decision-matrix/`). Claude Code picks up
`SKILL.md` automatically and will offer to use it whenever a conversation looks like a
multi-factor decision between a handful of options.

## How it works under the hood

- `SKILL.md` — the workflow instructions Claude follows: scoping the decision,
  eliciting and defining criteria, weighting, researching and scoring each cell,
  computing totals, and building the report.
- `assets/report_template.html` — the report's engine (HTML/CSS/vanilla JS, no build
  step, no external JS dependencies). A JSON data blob is injected into it at build
  time; everything interactive — weight sliders, mute toggles, the ranked chart, the
  raw data table — runs client-side off that blob.
- `scripts/build_report.py` — validates a decision's JSON data file (ids match up,
  every score is 1-10, criteria/option counts are sane) and injects it into the
  template to produce one standalone `report.html`.
- `references/method.md` — background on the ASQ method and the scoring pitfalls
  (correlated criteria, weight compression, anchoring drift) the skill is written to
  watch for.

## License

MIT — see [LICENSE](LICENSE).
