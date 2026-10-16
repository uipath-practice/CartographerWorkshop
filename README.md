# UiPath Cartographer Tech Workshop

A hands-on learner's handbook for **UiPath Cartographer**. Participants take a real business process from raw discovery evidence to a reviewed, published Process Definition Document (PDD), then follow the design all the way to production on the UiPath Platform.

The site is built with [MkDocs](https://www.mkdocs.org/) and the [Material](https://squidfunk.github.io/mkdocs-material/) theme, and is published to GitHub Pages.

## The course

| Page | What participants do |
|------|----------------------|
| **Home** | Overview of the workshop and the key concepts: Cartographer, Map of Work, Process Atlas, provenance, PDD, SDD and the best-fit canvas. |
| **Warranty Resolution at Cobalt Ridge Automation** | The core hands-on exercise. Create a Cartographer project from a business brief, add the evidence pack, review the AS-IS, design the TO-BE, make live edits inside the compliance guardrails, then generate, trace and publish the PDD to Automation Hub. |
| **From Process to Production** | The journey from Discover to Improve, and a hands-on path from the PDD to an SDD, a coding-agent build with the UiPath skills, and a running solution in Maestro and Orchestrator. |
| **Next Steps** | Ways to keep building after the workshop. |

## How it works

```
docs/*.md  →  MkDocs builds HTML  →  GitHub Actions  →  gh-pages  →  GitHub Pages
```

| Path | Purpose |
|------|---------|
| `docs/` | Published page content: one folder per exercise, with `index.md`, an `index.images/` folder and any downloads in `dependencies/` |
| `docs/stylesheets/extra.css` | UiPath brand styling, the journey strip, cards, stat tiles and the collapsible sections |
| `docs/javascripts/extra.js` | Collapsible page sections and collapsible sections in the left navigation tree |
| `mkdocs.yml` | Site configuration and the **published** navigation |
| `mkdocs.local.yml` | Optional local-only navigation for work-in-progress pages (gitignored) |
| `main.py` | Training-environment variables (`{{ training_url }}`, `{{ training_tenant }}`) used in the pages |
| `Master/` | Authoring rules and page templates |
| `.claude/commands/` | Authoring slash commands for Claude Code |
| `hooks/` | MkDocs hook for the two-column layout shorthand |
| `scripts/` | Screenshot metadata extraction pipeline used when writing lessons from screenshots |
| `.github/workflows/deploy.yml` | Builds and deploys the site to GitHub Pages on every push to `main` |

## Local preview

Requires Python 3.

```bash
# 1. Create a virtual environment and install the dependencies
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt     # Windows
# .venv/bin/python -m pip install -r requirements.txt           # macOS / Linux

# 2. Preview locally with live reload
COURSE_ENV=staging .venv/Scripts/python.exe -m mkdocs serve
# open http://127.0.0.1:8000/CartographerWorkshop/

# 3. Release-equivalent build check
COURSE_ENV=prod .venv/Scripts/python.exe -m mkdocs build --strict
```

In PowerShell, set the variable first with `$env:COURSE_ENV = "staging"`.

## Publishing

Every push to `main` triggers the **Deploy site** workflow, which builds the site with `COURSE_ENV=prod` and publishes it to the `gh-pages` branch. GitHub Pages serves that branch at https://uipath-practice.github.io/CartographerWorkshop/.

## Trainer notes (internal)

These notes stay in the README on purpose. GitHub Pages can't restrict access, so anything meant only for trainers must never go into `docs/`.

### Training environment

| Organization URL | Tenant |
|---|---|
| https://staging.uipath.com/uipathlabsworkshop | `Fusion_Cartographe_20260921_ocrw` |

The values live in `main.py`. Pages always use the `{{ training_url }}` and `{{ training_tenant }}` variables, so changing the environment is a one-file edit.

### Participant machines

- **Live workshop:** each participant connects to the workshop VM. The evidence pack sits on the VM desktop in the **Cobalt Ridge Industrial Equipment Warranty Resolution-FUSION** folder.
- **Self-paced (UiPath internal):** create a UiPath Studio & Robot sandbox from the **Internal Enablement Workshop** template on [uipathlabs.uipath.com](https://uipathlabs.uipath.com/sandboxes/new).
- **Own machine:** participants with the latest Cartographer build can download the evidence pack from the exercise page (`docs/warranty-resolution/dependencies/`).

### The evidence pack

The pack contains eight evidence files plus two files participants must **not** attach:

- `00_START_HERE_BA-notes.md` — background for the facilitator.
- `meta-DO-NOT-FEED-TO-AGENT.txt` — the evaluation notes for the exercise. It describes what a strong analysis should find, so treat it as an answer key and don't walk participants through it before they finish.

### Before each training

- [ ] Confirm every participant can sign in to the training tenant.
- [ ] Confirm the VMs show the evidence folder on the desktop.
- [ ] Run the knowledge-check prompt once on the tenant to confirm Cartographer and its Process Knowledge are available.
