# The weighted decision matrix method

Background reading for the `decision-matrix` skill.

## The core idea

A decision (or Pugh) matrix makes an implicit, gut-feel comparison explicit:

1. List the options being compared.
2. List the criteria that matter, each with a weight for how much it matters.
3. Score every option against every criterion.
4. Multiply each score by its criterion's weight, sum across criteria, and compare
   totals.

Nothing here is statistically rigorous — it's a structuring tool. Its value is forcing
two things that unstructured comparison usually skips: naming *all* the criteria that
matter (not just the loudest one), and making the relative importance of each one
explicit instead of implicit.

## Why normalize by the sum of weights

`weighted_score = Σ(weight_i × score_i) / Σ(weight_i)` keeps the total on the same 1-10
scale as the individual scores, regardless of how many criteria there are or what scale
the weights happen to use. This matters in practice because:

- It stays comparable if criteria get added or removed mid-conversation.
- A "perfect 10 across the board" option still comes out to 10, which matches
  intuition and makes it easy to sanity-check a number that looks wrong.
- It avoids criteria-count inflation, where adding more criteria (even unimportant
  ones) silently makes every score bigger, which would happen with a plain unnormalized
  sum.

## Pitfalls to watch for while running the skill

**Correlated / double-counted criteria.** "Salary" and "financial security" or
"commute time" and "work-life balance" often measure overlapping things. If two
criteria almost always move together across the options, they're effectively one
criterion with its weight counted twice — merge them or make the distinction explicit.

**Weight compression.** If every criterion ends up weighted 7-9, the weights aren't
doing any work — everything is "important," so nothing is differentially important.
Encourage genuine low weights (2-4) for things that matter but not much, so the
high weights actually mean something.

**Anchoring drift.** The biggest source of bad scores isn't bad research, it's scoring
the first couple of options against one mental anchor and later options against a
different one (e.g. getting more generous as you go). Decide what 1 and 10 mean for a
criterion *before* scoring the first option, and don't revise that anchor once you've
started scoring others against it — if you need to, go back and re-score everything
scored so far.

**False precision on subjective criteria.** Some criteria ("excitement," "gut feel,"
"culture fit") can't be researched, only judged. That's fine — but say so in the
rationale rather than presenting a guess as though it were sourced. A matrix that's
honest about which numbers are soft is more trustworthy than one that's uniformly
confident.

**Too many criteria.** Past ~10, criteria usually start restating each other and the
exercise of weighting them gets noisy rather than more accurate. Push toward
consolidating instead of listing everything that's even slightly relevant.

## Talking through a close result

When two options land within ~0.5 points of each other on a 1-10 scale, say so plainly
instead of presenting a false tiebreaker. Useful framings:

- "These are close enough that the model can't tell them apart — what does your gut
  say?"
- Point at which single criterion, if weighted slightly differently, would flip the
  order — that's usually the real crux of the decision, more useful to discuss directly
  than the final number.
- A close result after a careful matrix is itself information: it usually means either
  genuinely any reasonable choice is fine, or that an important criterion is missing
  from the list entirely. Worth asking "is there something that matters to you that
  isn't on this list?" before accepting a near-tie at face value.
