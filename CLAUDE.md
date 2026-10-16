# CLAUDE.md — UiPath Cartographer Tech Workshop

Read automatically every Claude Code session in this repo. Apply all rules below.

---

## Project purpose

A GitHub Pages–hosted MkDocs site that teaches technical clients and partners to design business processes with **UiPath Cartographer**: from raw discovery evidence to a reviewed Process Definition Document (PDD), and from there to production on the UiPath Platform.

The audience knows the UiPath Platform but is new to Cartographer. The workshop is a half-day, instructor-led and hands-on.

---

## Course structure

| Page | File |
|------|------|
| Home | `docs/index.md` |
| Warranty Resolution at Cobalt Ridge Automation | `docs/warranty-resolution/index.md` |
| From Process to Production | `docs/process-to-production/index.md` |
| Next Steps | `docs/next-steps.md` |

- Each exercise is a **single page**: `index.md` holds the whole guide, with `##` sections and `### N.` numbered steps.
- Screenshots live in the page's `index.images/` folder. Downloads live in `dependencies/`.
- The Warranty Resolution page opts in to collapsible sections with `<div class="collapsible-sections" hidden></div>` right after the title. The left navigation tree's sections are collapsible on every page.

---

## Content rules

- **Never change the prompts participants paste into Cartographer or a coding agent.** Instructions around them may be reworded, the prompts themselves stay exactly as written, typos included.
- **No work-in-progress signals on the site.** No "preview", "draft", "coming soon" or "more exercises are being authored" wording in `docs/`.
- **Trainer-only material stays in `README.md`**, never in `docs/`. GitHub Pages can't restrict access.
- **Roadmap capabilities are never presented as available.** In particular, don't say Cartographer itself builds the solution; coding agents build from the SDD.
- **Use the environment variables** from `main.py` in every training-environment callout: `{{ training_url }}`, `{{ training_tenant }}`. Never hardcode a URL or tenant.

---

## Master reference files

Read the relevant file before creating or reviewing content:

| File | Covers |
|------|--------|
| `Master/Filesystem.md` | Directory and naming conventions, image folders, Archive |
| `Master/CourseStructure.md` | Page types and templates |
| `Master/Formatting.md` | Images, two-column layouts, code blocks, admonitions |
| `Master/Language.md` | Voice, tone, word choices, platform names |
| `Master/HOWTO.md` | Create, generate, publish, review and remove workflows |

---

## Quick reference (always in context)

- **Voice:** second person, short sentences, conversational. Avoid "leverage", "utilize", "seamlessly", "In this section we will", "Please note that".
- **Platform names** bold on first use per page: **UiPath Cartographer**, **Map of Work**, **Process Atlas**, **Automation Hub**, **Maestro**, **Orchestrator**, **Studio Web**, **Action Center**, **Integration Service**. Coding-agent terms: **Claude Code**, the **`uip` CLI**, **UiPath skills**.
- **Code blocks:** always fenced with a language identifier (`text` for prompts, `bash` for CLI).
- **Wide screenshots** end in `-W` and render at `width="900"`.
- **Drafts** are not added to `mkdocs.yml` nav; use `mkdocs.local.yml` to preview them.
- Run a strict build before committing.

---

## Local preview

```bash
.venv/Scripts/python.exe -m pip install -r requirements.txt
COURSE_ENV=staging .venv/Scripts/python.exe -m mkdocs serve          # author and preview
COURSE_ENV=prod    .venv/Scripts/python.exe -m mkdocs build --strict # release-equivalent check
```
