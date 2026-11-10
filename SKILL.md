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

## 2. One-message intake — don't interview field by field

Asking "what's the decision," then "what are the options," then "what matters to
you," then the weight of each criterion one at a time, turns a 2-minute decision into
a 15-message slog. Ask for the decision, the options, and a rough sense of priorities
**together, in one message**, and give an example so the person knows how little
effort a good answer takes:

> "What are you deciding, what are the options, and what matters most to you — rough
> is totally fine, I'll turn it into a clean comparison. E.g.: *'Choosing between 3 job
> offers — Acme, Globex, and staying at my current job (Initech). I mostly care about
> pay, how much I'd grow, and not having a brutal commute.'*"

If they give you a thin answer (just the options, no priorities), that's fine — move
to step 3 and propose priorities for them instead of asking again.

## 3. Propose one editable draft — criteria, definitions, and weights together

Don't collect criteria and then separately collect weights. Research what typically
matters for *this kind* of decision (a job offer and an apartment don't share
criteria) and hand back one complete draft — 5-10 criteria, each with a one-line
definition and a suggested weight (1-10) — for the person to edit in a single pass,
rather than building it from their blank-page brainstorm or asking about each one in
turn. Push back gently (still inside this one draft, don't ask permission first) if
their own list runs past ~10 — merge or drop the ones that restate each other.

Let people answer in whatever's easiest — a number, or just "high/medium/low" (map
roughly to 9/6/3) — and accept a reply as light as "looks good" or "drop commute,
bump pay to a 10." Example of what to send:

> "Here's a draft for comparing job offers — edit any row, add/remove one, or just say
> 'looks good':
>
> | Criterion | What it means | Importance (1-10) |
> |---|---|---|
> | Pay | Total comp (salary + bonus + equity), year one | 9 |
> | Growth | How much more you'd learn/grow in this role | 8 |
> | Commute | Door-to-door time, typical day | 6 |
> | Stability | How likely the role/company still exists in 2 years | 7 |
> | Team & culture | How good the people and day-to-day feel seem | 7 |
>
> Anything to add — like health insurance, or remote flexibility?"

Two things matter more than people expect once the draft is confirmed:

- **Keep each criterion's definition**, don't let it collapse back to a bare label.
  "Growth" is ambiguous; "growth = how much more I'd learn in this role in year one"
  is scorable. Without it, your own scores will drift inconsistently across options.
- **Watch for criteria that double-count the same underlying thing** (e.g. "salary" and
  "financial security" often collapse into one factor) — merging them keeps the
  weights honest.

## 4. Lock it in and move on

One edit round is normally enough — once the person confirms (or doesn't object),
treat criteria, definitions, and weights as locked and get straight to the research in
step 5. Don't re-ask them to re-confirm numbers you already showed them; if you need to
change something later (e.g. a criterion turns out unscoreable), say what you're
changing and why rather than re-opening the whole draft for approval.

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
