# Weekly Paid Ads Intel

A reusable AI skill that turns Facebook and Meta advertising news, advertiser chatter, platform health, and macro conditions into a weekly briefing explaining the implications for advertisers.

It answers: **What changed? Could it affect me? What should I check or watch this week?**

Built from an existing weekly research workflow, with the private account infrastructure removed. The default report covers US macro conditions and Meta advertising. Sources, region, timezone, business context, and archive location are configurable.

## What you get

- Current platform health and relevant recent incidents.
- Meta product, policy, and API changes with effective dates and rollout scope.
- Clustered advertiser chatter labeled as anecdotal evidence.
- Latest macro readings and cautious explanations of possible ad impact.
- Upcoming releases and deadlines, prioritized actions, and a short takeaway.
- Direct source links, confidence labels, coverage gaps, and changes since the prior report.
- A dated Markdown report usable in Obsidian or any notes folder.

This is an instruction-based skill. Your AI assistant performs the research using its web tools. It does not run by itself, scrape in the background, pull account metrics, or change campaigns. The installer copies files; a host app or scheduler supplies weekly execution.

## Requirements

- An authenticated AI assistant that supports local `SKILL.md` skills, with live web search and page access enabled.
- Write access to an output folder if you want archived reports.
- Python 3.9+ only if using the optional installer. Manual installation needs no Python.

No Meta access token, ad account ID, Telegram bot, or paid research connector is required. Your assistant or optional connectors may have their own usage charges. Exa can help with source access if already available; native research tools are sufficient, with gaps disclosed.

## Install

Download or clone this repository. Run the commands from its root. Start with a dry run:

```bash
python3 scripts/install.py --target codex --project /absolute/path/to/your-project --dry-run
python3 scripts/install.py --target codex --project /absolute/path/to/your-project
```

For Claude Code:

```bash
python3 scripts/install.py --target claude --project /absolute/path/to/your-project
```

The existing project directory must exist. The script installs into `.agents/skills/weekly-paid-ads-intel` for Codex or `.claude/skills/weekly-paid-ads-intel` for Claude Code. It refuses to overwrite an existing skill and generates a separate `config.local.json` from the public defaults. It does not alter host settings or permissions.

For another supported assistant or a tool-specific personal directory, explicitly provide the parent skill directory:

```bash
python3 scripts/install.py --target custom --destination /absolute/path/to/skills
```

Follow your host's directory conventions. Current Codex repository discovery uses `.agents/skills`; an existing tool-local convention can be selected with `--destination`. No central sync directory or shared agent hub is required. See the [official Codex skill documentation](https://learn.chatgpt.com/docs/build-skills) and [Claude Code skill documentation](https://code.claude.com/docs/en/skills).

**Manual installation:** copy only `skills/weekly-paid-ads-intel/` into your host's skill directory. Optionally copy `config.example.json` to `config.local.json` inside the installed skill. Keep the references alongside `SKILL.md`. If the skill does not appear, restart your assistant and check its discovery paths.

## Configure

Edit `config.local.json` in the installed skill, leaving `config.example.json` as the shareable defaults. Without a local file, the skill uses the example configuration.

| Setting | Purpose |
| --- | --- |
| `lookback_days` | News and chatter window, default 7. |
| `timezone` | IANA timezone, default `UTC`; set your own for weekly dates. |
| `market` | Macro region, default `US`. For other markets, replace the macro source list too. |
| `exposure_context` | Non-identifying details such as region, offer type, price range, or API usage. Empty means unknown exposure. |
| `archive.enabled` | Whether to save the full Markdown report. |
| `archive.directory` | Output folder. Relative paths resolve against the run's working directory. |
| `sources.platform_status` | Status pages to check; optional AI-provider status can be added here. |
| `sources.platform_news` | Starting points for official Meta news and policy research. |
| `sources.ad_chatter_subreddits` | Communities to search when accessible. |
| `sources.public_x_search` | Whether to include accessible public X posts. |
| `sources.macro_signals` | Indicators and official source entrypoints. |

For Obsidian, set `archive.directory` to your own vault folder. Reports use ordinary Markdown and lightweight frontmatter; no plugins are required. No credentials belong in either configuration file.

## Make the briefing apply to your ads

Give the skill a short description of how you advertise. It uses that context to explain which developments affect your setup, which might matter, and which you can ignore. The more specific your context, the more useful the action items become.

Save your ongoing context in `exposure_context` inside the installed skill's `config.local.json`. This is a list of plain-language descriptions, so no new fields or account connections are needed. You can also supply context in the run prompt for a one-off briefing.

Useful details to include:

| Detail | Example | Why it helps |
| --- | --- | --- |
| Customer geography | US customers; nationwide delivery | Determines which regional changes and macro signals matter. |
| Business and offer | Ecommerce; discretionary home goods; $50–$150 orders | Helps interpret buying behavior and price sensitivity. |
| Conversion path | Ad → product page → online checkout | Helps identify where a platform change could affect conversion. |
| Campaign goals | Sales campaigns optimized for purchases | Makes recommendations relevant to the outcome you measure. |
| Audiences and placements | Prospecting and retargeting; Facebook and Instagram feeds/Reels | Helps assess exposure to targeting and placement changes. |
| Measurement | Pixel and Conversions API through an ecommerce platform integration | Helps identify relevant tracking changes and checks. |
| Technical dependencies | Uses Ads Manager; no custom Marketing API integration | Helps distinguish relevant API changes from announcements you can ignore. |
| Current concerns | Watching cold-traffic conversion rate and retargeting frequency | Gives the briefing specific questions to investigate. |

Only include details you know. Write `unknown` for uncertain settings; the skill should recommend a check rather than assume your setup.

### Example: an ecommerce business

Replace the existing `exposure_context` list with your own details. This snippet is a property inside the full configuration file, not a complete replacement for the file:

```json
"exposure_context": [
  "US ecommerce business selling discretionary home goods",
  "Typical orders are $50–$150; purchases happen on our own website",
  "Meta Sales campaigns optimized for purchases",
  "Uses prospecting and retargeting on Facebook and Instagram feeds and Reels",
  "Uses Pixel and Conversions API through an ecommerce platform integration",
  "Operates through Ads Manager; no custom Marketing API integration",
  "Primary measures: purchase CPA, ROAS, and website conversion rate",
  "Current concern: whether weaker purchase conversion warrants investigation"
]
```

Prefer a walkthrough? Give your assistant this prompt and answer its questions:

```text
Help me personalize weekly-paid-ads-intel for my advertising setup.
Ask me about customer geography, business model, offer and pricing, conversion
path, campaign goals, audiences, placements, tracking, API usage, and current
concerns. Ask one question at a time and accept unknown answers.
Then save a concise profile in exposure_context in the installed skill's
config.local.json, preserving the other settings. Do not request account IDs,
credentials, client names, or access to ad accounts.
```

### Example: an agency with several types of clients

Use anonymous profile labels in the same list so the briefing can assess different exposures separately:

```json
"exposure_context": [
  "Profile A: US ecommerce; $50–$150 products; purchase optimization; website checkout",
  "Profile B: US local services; lead optimization; Meta instant forms; appointments booked by phone",
  "Both profiles use Ads Manager; neither uses a custom Marketing API integration",
  "For each priority finding, identify Profile A, Profile B, both, or neither as potentially affected"
]
```

Keep the profiles concise and update them when your offers, markets, tracking, or campaign setup changes. Weekly runs read this local configuration automatically.

### What personalized interpretation looks like

The following examples are hypothetical, not current news or a generated live report:

| If the research finds… | With the example context above, the briefing could explain… |
| --- | --- |
| A confirmed upcoming removal from a Marketing API endpoint | “Your supplied setup uses Ads Manager with no custom API integration. Direct exposure to that endpoint removal appears unlikely; confirm whether a third-party tool depends on it.” |
| An officially reported decline in consumer confidence | “Your discretionary ecommerce offers could face more purchase hesitation. Watch checkout conversion and purchase lag; this release alone does not establish the cause of a CPA increase.” |
| A verified rollout affecting Meta instant forms | “Profile B may be affected because it uses instant forms. Check whether the rollout is enabled and test lead submission through to booking. Profile A uses website checkout, so that specific form change does not appear directly relevant.” |

To request that style of output explicitly:

```text
Run weekly-paid-ads-intel using my exposure_context. For each priority finding,
explain whether it affects my setup, why, what to check, and the deadline or
trigger. Separate confirmed exposure from possible or unknown exposure.
Include a short "What this means for my ads" summary in the briefing.
```

### Add recent observations when helpful

For a one-off run, you can paste a short, anonymous performance observation with its date range, such as: “Over the past seven days, purchase CPA rose while CPM stayed roughly flat; checkout conversion declined.” Ask which external developments are worth investigating alongside it.

That helps focus the watch items. It does not prove that a news event caused the change. The skill does not retrieve account metrics or diagnose account performance, and it should not recommend automatic budget changes from external news alone.

You do not need to share account IDs, access tokens, raw customer data, or client names. Keep your local profile and personalized reports out of the public repository.

## Run it

In Codex:

```text
Use $weekly-paid-ads-intel to research the past seven days and save the briefing.
```

In Claude Code:

```text
/weekly-paid-ads-intel
```

You can add context or override defaults in the same prompt:

```text
Run weekly-paid-ads-intel for US ecommerce advertisers selling $50–$150 products.
Prioritize delivery incidents, policy rollouts, and purchase behavior.
Use the last seven days and explain what needs checking this week.
```

Default archive: `reports/market-intel/Ad Intelligence YYYY-MM-DD.md` beneath the run's working directory. A same-day rerun creates a timestamp-suffixed version so prior observations are preserved. Archive failures are reported in chat; source-access failures produce a partial report. Without live web tools, the assistant stops instead of inventing a current briefing.

## Run weekly

After a successful manual run, configure a weekly task in your assistant's supported scheduler. Choose a stable working directory, your timezone, and a time such as Monday at 09:00. Use this task prompt:

```text
Use weekly-paid-ads-intel to research the past seven days using its configuration.
Read the latest earlier report in the configured archive folder if available.
Use my exposure_context to explain what changed, which parts of my advertising
setup could be affected, and what to check or watch next. Distinguish confirmed,
possible, and unknown exposure. Include a short "What this means for my ads" summary.
Save the complete sourced Markdown report. Disclose coverage and save failures.
Do not modify campaigns or send messages.
```

The installer does not register a weekly task. Scheduler and connector availability depend on the host. Confirm a scheduled run has live research tools, can write the archive, and actually produces a report. A task that works interactively may not have the same tools when unattended.

For CLI automation, use your host's documented noninteractive mode and your own cron/launchd/task scheduler. Use absolute working, output, executable, and log paths. Preserve normal permission controls; do not add permission-bypass flags to make scheduling work. On macOS, unattended jobs may be denied access to Documents/iCloud folders; use a scheduler-accessible working/output folder and inspect the real job log after a scheduled cycle.

## Privacy and publishing

The public package contains no account inventory, API credentials, delivery IDs, private reports, personal paths, or messaging integration. The repository ignores local config and its default reports. The installed skill also carries an ignore rule for its local config. For reports saved in a different project, add that output folder to that project's `.gitignore` yourself; the installer does not edit project ignore rules. `.gitignore` does not protect files that are already tracked, files force-added to Git, or output written elsewhere.

Before publishing your fork, inspect the complete staged diff and Git history, including custom config, attachments, and reports. Run a secret scanner suited to your Git host. If a secret was ever committed, remove it from history and rotate it before publishing. Keep private business context out of shared reports.

This package intentionally separates research from delivery. If you add email, Slack, or Telegram later, make it an explicitly authorized integration and preserve the full local archive before sending.

## Repository layout

```text
README.md
LICENSE
scripts/install.py
skills/weekly-paid-ads-intel/
  SKILL.md
  LICENSE
  config.example.json
  agents/openai.yaml
  references/research.md
  references/report-template.md
```

## Improvements worth considering

1. Try several real weekly runs before adding integrations. Check source links, date accuracy, access gaps, and whether action items actually helped.
2. For stronger reproducibility, add a structured evidence log recording claim, URL, dates, scope, and confidence, once you know which fields you use.
3. Add regional source presets if you routinely serve other markets. Changing only the region label is insufficient.
4. Add delivery as a separate optional module with explicit authorization and duplicate-send protection.
5. If you later want an in-app marketplace install, package this folder as a host-specific plugin. Direct skill installation keeps this release simple.

## License

Licensed under the [MIT License](LICENSE). Copyright (c) 2026 Landon Poburan. You may use, modify, and redistribute this skill, including commercially, subject to preserving the copyright and license notice. The skill folder includes its own copy of the license so standalone installations retain the notice.
