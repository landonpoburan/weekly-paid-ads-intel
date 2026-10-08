---
name: weekly-paid-ads-intel
description: Produce a weekly Facebook and Meta ads market-intelligence briefing covering platform incidents, advertising news, advertiser chatter, and macro conditions, with sourced implications and prioritized watch items. Use for weekly ads intel or an external market scan; excludes account-performance reporting and campaign changes.
---

# Weekly Paid Ads Intel

Turn external signals into a concise briefing explaining what changed, why advertisers should care, and what to watch next. Research public sources only. No ad account IDs, Meta API access, or delivery credentials are needed.

## Start a run

Read `config.local.json` beside this file if present, otherwise `config.example.json`. These paths are relative to this skill directory, not the working directory. User instructions override configuration. Check that the lookback is a positive integer, the timezone is usable, and source lists and archive settings have the expected shapes. If a required value is invalid, report it and request a correction rather than silently producing a misleading report. Do not edit configuration during a research run.

Use the configured timezone to establish the run date. Declare the exact lookback start and end dates and the current observation time. Defaults: seven days, US macro context. A region override requires corresponding official macro sources; do not apply US data to another market without labeling the distinction.

If the user provides non-identifying business context (region, offer type, price range, placements, API usage), use it to assess exposure. Otherwise state exposure is unknown and make actions conditional. Do not search private project files, account rosters, or credentials to fill gaps.

Use the host's available live web search and page-reading tools. An optional research connector such as Exa may improve access, but is never required. Check actual access each run: Reddit, X, and JavaScript status pages may be limited. Try an accessible alternative, disclose the gap, and continue. Never bypass access controls. If live research is unavailable, state that no current briefing can be verified and stop without inventing news.

Read [research guidance](references/research.md) for source selection and evidence rules, and use [the report template](references/report-template.md) for the output.

## Research

1. **Platform health.** Check each configured status page, including incident history for the reporting window. Prioritize Ads Manager, ad delivery, and Marketing API. Distinguish active incidents from resolved ones. Treat AI-tool availability as operational context only when included in configuration. A page that returns only a header is unavailable evidence, not proof of normal operation. Label third-party incident summaries as secondary. Use `unknown` when no usable evidence establishes status.
2. **Meta advertising news.** Search official announcements, policy updates, product changes, and developer changelogs, then credible trade coverage. Record announcement date, effective date, affected regions/products, and rollout limits separately. Highlight deadlines even if the announcement predates the window. Verify API removals and policy deadlines against official documentation; unconfirmed claims belong on a watchlist.
3. **Advertiser chatter.** Search configured communities and, when `sources.public_x_search` is true, public X posts for restrictions, delivery anomalies, learning resets, CPM/CPA volatility, and rollout experiences. Cluster overlapping reports; syndicated stories are one source. Record post dates and visible engagement only. Anecdotes indicate something to investigate, not measured industry-wide prevalence. Never infer broad performance changes from a few threads.
4. **Macro conditions.** For configured indicators, use the latest official release, its reference period, release date, units, prior comparable reading, and revision status. Monthly data may predate the lookback; label it as context rather than new news. Explain a plausible mechanism affecting purchase decisions or advertising, with explicit uncertainty. Do not predict CPA percentages or diagnose campaign performance from macro news alone.
5. **Next catalysts.** Verify release calendars and platform deadlines. List events before the next weekly run first; separate later known deadlines. Include year and timezone for timed events. Do not invent dates from a recurring calendar pattern.

## Interpret and prioritize

For each material finding, give: what changed, a direct source link, evidence class (`official`, `reported`, or `anecdotal`), confidence (`high`, `medium`, or `low`), likely ad impact, and exposure (`confirmed`, `possible`, `not applicable`, or `unknown`). Confidence describes the claim's evidence; urgency describes the practical response. An official announcement can still have uncertain ad impact.

Keep observations separate from your interpretation. A fact may justify checking conversion rate, auction costs, tracking, or a rollout setting; it does not automatically justify changing spend. Distinguish market-wide importance from the user's known exposure. Say what would confirm or weaken an interpretation.

If a prior report exists in the configured output directory, read only the most recent earlier dated report. Mark continuing items as changed, unchanged, or resolved. Do not repackage old news as a new event. No prior report is a valid first run.

End with a short numbered action/watch list, ordered by urgency:

- 🔴 red: verified urgent issue with confirmed exposure, or an urgent check to establish exposure before a near deadline.
- 🟠 orange: meaningful near-term risk or a specific verification needed.
- 🟡 yellow: context or monitoring with a clear trigger.
- 🟢 green: supportive context or no action needed.

Every action identifies who/what is affected, the recommended check, and a deadline or trigger when relevant. Avoid client names unless supplied for this run. If nothing warrants action, say `No action required; continue monitoring.` Close with one plain-language takeaway sentence. Never execute campaign changes, purchase services, or notify third parties as part of this skill.

## Save and return

Return the full Markdown briefing with source links adjacent to claims and a coverage/limitations note. Mark `complete` when required research areas have usable coverage; use `partial` when a required area is inaccessible or a material claim remains unverified. An empty but successfully checked news window can be complete. Do not equate no search results with no events.

If `archive.enabled` is true, save the same full briefing as `Ad Intelligence YYYY-MM-DD.md` under `archive.directory`. Resolve relative directories against the user's working directory, expand `~` using the host, and use an absolute path for the write. The output is ordinary Markdown usable in Obsidian, Git, or a notes folder. Do not insert personal vault links.

Preserve an existing same-day report by writing a new timestamp-suffixed file rather than overwriting it. Choose a unique suffix if necessary. Report the saved path. If saving fails, return the full briefing and describe the archive failure. A failed save must not erase research or be reported as a successful archive.

This skill performs no message delivery and installs no scheduler. Weekly recurrence is configured by the user in the host app or scheduler, following the repository README. Respect the host's approval and sandbox rules in scheduled runs.
