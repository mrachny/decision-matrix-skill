---
name: decision-matrix
description: >
  Walk someone through a weighted decision matrix (the ASQ method) to choose between
  real options with multiple competing factors — job offers, apartments, cities,
  vendors, degrees, cars, hires, tools, vacation spots, anything where "just pick the
  cheapest one" isn't good enough. Elicits the top 5-10 criteria that actually matter,
  weights them, researches how well each option satisfies each criterion (1-10, with a
  cited rationale per cell), computes weighted totals, and produces both a markdown
  table and a self-contained interactive HTML report where weights and included
  options can be adjusted live. Use this whenever someone is stuck comparing options,
  asks "which one should I pick" / "help me decide between X and Y" / "A or B?", wants
  a pros-and-cons comparison that involves more than one factor, or explicitly mentions
  a decision matrix, weighted scoring, comparison table, or Pugh matrix. Also trigger
  when someone pastes a list of options and asks you to "rank" or "score" them.
---

# Decision Matrix

A weighted decision matrix turns "I can't decide" into a defensible, inspectable
number — but the number is only as good as the criteria, weights, and research behind
it. Your job is the thinking (what matters, how much, how well does each option
actually measure up), not just filling in a table. The HTML report at the end is a
by-product of doing that thinking well, not the point of the exercise.

## 1. Check the decision actually fits this method

This method shines when there are **2-8 discrete options** and **several criteria that
pull in different directions** (cheaper vs. nicer, faster vs. safer). It's overkill or
the wrong tool when:

- There's really only one factor that matters ("which is cheaper") — just answer that.
- It's a yes/no call, not a choice among alternatives.
- The option space is effectively unbounded (e.g. "where should I live" with no
  shortlist yet) — help the person narrow to a shortlist first, *then* run the matrix
  on the shortlist.

If it fits, say so briefly and move on — don't make the person justify using a decision
matrix to you.

## 2. Name the decision and collect options

Get one sentence naming the actual decision and, if relevant, the deadline or stakes.
Then collect the options (2-8). If someone hands you a huge list, help them cut it to a
shortlist first (e.g. "which 5 of these 20 apartments are even worth scoring?") rather
than scoring all 20 — scoring quality drops once there are too many cells to research
properly.

## 3. Collect and define the criteria (5-10)

Ask what matters to the person, and propose a draft list tailored to this *specific*
kind of decision (a job offer and an apartment don't share criteria) so they're editing
your draft rather than brainstorming from zero. Push back gently if they list more than
~10 — criteria beyond that tend to be restatements of each other and just dilute the
weights. Two things matter more than people expect:

- **Give each criterion a one-sentence definition**, not just a label. "Growth" is
  ambiguous; "growth = how much more I'd learn in this role in year one" is scorable.
  Without this, scores drift inconsistently across options.
- **Watch for criteria that double-count the same underlying thing** (e.g. "salary" and
  "financial security" often collapse into one factor) — merging them keeps the
  weights honest.

## 4. Weight each criterion (1-10)

Ask directly: "On a 1-10 scale, how important is **[criterion]** to you, independent of
how any option scores on it?" If someone is unsure, propose a weight based on what
they've already told you and let them correct it — don't silently assume. Weights
don't need to sum to anything in particular; the formula below normalizes for that.

## 5. Research and score every option × criterion cell (1-10)

This step is where the real work is, and where an agent earns its keep over a
plain template. For each cell:

- **Actually research it** — use search/tools to find the relevant fact (price, spec,
  rating, salary data, review, policy) before scoring. Don't invent a precise-sounding
  number from vibes.
- **Anchor the scale consistently within a criterion.** Decide what 1 and 10 mean for
  *this* criterion (e.g. "10 = cheapest among these options" or "10 = meets every
  must-have") before scoring the first option, and hold that anchor across every option
  so scores are comparable. Write that anchor down once per criterion in your own notes.
- **Give a one-sentence rationale per cell**, naming the fact or source behind the
  number. This rationale is what makes the report trustworthy and is shown in the HTML
  report's "why" toggle.
- **Say when you're guessing.** Some criteria are genuinely subjective (e.g.
  "excitement," "gut feel") or under-documented. Score those from the person's own
  stated judgment, and flag in the rationale that it's subjective/unverified rather than
  presenting it with false precision. Never fabricate a source.

## 6. Compute the weighted total

For each option: `weighted_score = Σ(weight_i × score_i) / Σ(weight_i)`, a normalized
1-10 average. This is the same normalization used in the ASQ decision matrix method
(https://asq.org/quality-resources/decision-matrix) and keeps the total on the same
1-10 scale as the inputs, which makes it easy to sanity-check.

## 7. Deliver the markdown table first

Before building the HTML, show the result in the chat as **one table**: options as
rows sorted best-to-worst, criteria as columns (score only, to keep it readable), and a
final weighted-total column. Follow it with 2-3 sentences naming the top option, the
runner-up, and the single biggest factor separating them — and flag it plainly if the
top two are close enough that the "winner" is really a toss-up.

## 8. Build the interactive HTML report

Write a JSON data file matching the schema below, then run:

```bash
python3 scripts/build_report.py data.json report.html
```

This injects your data into `assets/report_template.html`'s engine and writes a single
self-contained `report.html` (no server, no external resources besides one Google Font
— it works by double-clicking the file). The script validates the data and fails with
a specific message if something's missing or out of range.

### Data schema

```json
{
  "meta": {
    "title": "Which apartment should I rent?",
    "subtitle": "Comparing 4 listings in the same neighborhood",
    "description": "One or two short, plain sentences of context. Shown under the title.",
    "direction": "ltr",
    "credit": "Decision matrix by <your name>",
    "credit_url": "https://github.com/mrachny/decision-matrix-skill"
  },
  "criteria": [
    { "id": "rent", "label": "Monthly rent", "description": "10 = cheapest of the four, 1 = most expensive.", "weight": 9 }
  ],
  "options": [
    { "id": "optA", "label": "Elm St apartment", "included": true }
  ],
  "scores": { "optA": { "rent": 7 } },
  "notes": { "optA": { "rent": "₪5,200/mo, the second-cheapest of the four (source: listing)." } }
}
```

- `meta.direction` is `"ltr"` or `"rtl"`; omit for `"ltr"`.
- The report footer shows a small "Generated with a decision matrix" attribution line
  by default. `meta.credit` / `credit_url` override its text/link; set `meta.credit`
  to `false` if the person explicitly doesn't want any attribution line.
- `criteria[].description` and `notes` are optional but strongly recommended — they
  become the "why" text shown in the report. A criterion or cell with no description
  just shows no rationale, which is fine for a quick draft but weakens the report.
- `options[].included` (default `true`) sets the report's starting mute state.
- Every score must be a number from 1-10. The build script checks this and the id
  consistency between `criteria`/`options`/`scores` before writing anything.

Tell the person where the file is and that it opens directly in any browser — weights
and the mute toggles recompute the ranking live, nothing is sent anywhere, and nothing
is saved unless they keep the file.

## 9. Invite a sensitivity check

Close by pointing out that the report is meant to be played with, not just read: if
toggling off the shakiest-feeling criterion or nudging a weight flips the winner, that's
real signal that the decision is close and worth more thought (or that the differences
don't matter and they should just go with gut feel / cost / whichever is easiest to
reverse). If the ranking is robust to that kind of poking, that's useful signal too.

## Reference files

- `references/method.md` — background on the ASQ method, common scoring pitfalls
  (correlated criteria, weight compression, anchoring drift), and how to talk through
  a tie with the person.
- `assets/report_template.html` — the report engine. You shouldn't need to edit this by
  hand; everything customizable flows through the JSON data file.
- `scripts/build_report.py` — builds the report; run `python3 scripts/build_report.py
  --help`-style usage shown above.
- `examples/laptop-purchase.json` — a filled-in example data file if you want to see a
  complete one before writing your own.
