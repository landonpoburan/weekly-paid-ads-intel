# Report template

Adapt the length to the week's evidence. Bracketed text describes fields to fill, not facts to repeat. Omit empty tables rather than manufacturing findings. Aim for a scannable report, typically 700–1,200 words; use fewer words on a quiet week.

```markdown
---
created: YYYY-MM-DD
type: ad-intel-briefing
status: complete
headline: "One-sentence takeaway, escaped as valid YAML."
top_severity: yellow
meta_status: unknown
---

# Paid Ads Intel — YYYY-MM-DD

Window: [start date] through [end date], [timezone].
Observed: [timestamp]. Market: [region].
Exposure context: [provided business context, or unknown].

## Platform health

[Current state, relevant active/resolved incidents, incident dates, direct links,
and official versus secondary confirmation.]

## Meta advertising news

[Material changes, announcement/effective dates, rollout scope, direct sources,
evidence class, confidence, ad impact, exposure, and prior-week changes.]

## Advertiser chatter

[Clustered findings with dated direct links, evidence labels, observable engagement
if available, confidence, and coverage limitations.]

## Macro conditions

| Signal | Latest / prior | Period and release date | Evidence / source | Potential ad impact |
| --- | --- | --- | --- | --- |
| [indicator] | [same units] | [both dates] | [class, confidence, link] | [conditional mechanism] |

## Upcoming catalysts

[Verified events before next run; separate later deadlines. Link each calendar.]

## Actions and watch items

1. 🟡 [Exposure, recommended check, trigger/deadline, source or finding reference.]

Takeaway: [one sentence].

## Coverage and limitations

[Tools/source categories actually accessed, gaps, unresolved conflicts, and
whether this is a first run or a comparison with an earlier report.]
```

Frontmatter: `status` is `complete` or `partial`; `meta_status` is `operational`, `degraded`, `incident`, or `unknown`; `top_severity` is the highest action severity, or `green` when no action is required. Quote and escape the headline. These properties support Obsidian without requiring plugins or personal links. Use plain headings instead of emoji if the user prefers.
