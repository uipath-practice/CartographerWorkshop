# Filesystem Structure

Everything about how the project is organized on disk — folders, files, naming conventions, and where things go.

---

## Project root

```
CartographerWorkshop/
├── CLAUDE.md                          ← Auto-loaded by Claude Code every session
├── README.md                          ← Human-facing repo guide (trainer notes live here, never in docs/)
├── mkdocs.yml                         ← Site config: theme, nav, plugins, extensions
├── mkdocs.local.yml                   ← Local nav with draft exercises (gitignored, optional)
├── main.py                            ← MkDocs macros: training_url / training_tenant per COURSE_ENV
├── requirements.txt                   ← Python deps for MkDocs + plugins
├── Master/                            ← Authoritative course rules (this directory)
│   ├── README.md
│   ├── Filesystem.md
│   ├── CourseStructure.md
│   ├── Formatting.md
│   ├── Language.md
│   ├── HOWTO.md
│   └── Templates/                     ← Sample exercise pages (index, lesson, you-did-it)
├── docs/                              ← All page content
│   ├── index.md                       ← Home page
│   ├── next-steps.md                  ← Global site-level outro
│   ├── assets/
│   │   └── images/                    ← Logo, favicon, images shared across multiple pages
│   ├── stylesheets/
│   │   └── extra.css                  ← Custom CSS (do not modify without reason)
│   ├── javascripts/
│   │   └── extra.js                   ← Custom JS (external links → new tab)
│   ├── warranty-resolution/           ← Exercise: Warranty Resolution at Cobalt Ridge Automation
│   └── process-to-production/         ← Exercise: From Process to Production
├── Archive/                           ← Archived exercises and lessons (gitignored)
│   └── <exercise-slug>/              ← One folder per archived exercise
├── hooks/
│   └── split_cols.py                  ← MkDocs hook: two-column layout shorthand
├── scripts/                           ← Screenshot metadata extraction pipeline
│   ├── __main__.py                    ← Lets you run the package with python -m scripts
│   ├── extract_metadata.py            ← CLI entry point
│   ├── doc_context.py                 ← Per-exercise documentation embedding
│   ├── context_resolver.py            ← Resolves context per image
│   ├── context_ingest.py              ← Builds global RAG vector store
│   ├── llm_client.py                  ← Azure OpenAI vision API calls
│   ├── image_scanner.py               ← Discovers images needing processing
│   ├── metadata_writer.py             ← Writes JSON metadata files
│   ├── config.py                      ← Script configuration
│   ├── .env.example                   ← Template for Azure OpenAI credentials
│   ├── .env                           ← Azure OpenAI credentials (gitignored)
│   ├── requirements.txt               ← Python deps for scripts
│   └── context/
│       ├── README.md
│       └── vector_store.json          ← Global RAG embeddings (built locally, gitignored)
├── .claude/
│   └── commands/                      ← Claude Code skills
│       ├── new-exercise.md
│       ├── new-lesson.md
│       ├── publish-exercise.md
│       ├── remove-lesson.md
│       ├── remove-exercise.md
│       ├── review-lesson.md
│       └── review-exercise.md
├── .github/
│   └── workflows/
│       └── deploy.yml                 ← Auto-deploy on push to main (COURSE_ENV=prod)
├── .venv/                             ← Local Python virtual environment (gitignored)
└── site/                              ← Build output (gitignored)
```

---

## Exercise folder structure

Each exercise lives under `docs/` in its own folder.

### Single-page exercise (used in this course)

Both current exercises are single-page: `index.md` holds the full guide, with `##` sections and `### N.` numbered steps. The **Warranty Resolution at Cobalt Ridge Automation** exercise is the reference implementation:

```
docs/warranty-resolution/
├── index.md                             ← The whole exercise (ALWAYS named index.md)
├── dependencies/                        ← Downloadable files referenced by the page
│   └── Cobalt-Ridge-Warranty-Resolution-Company-Source.zip
└── index.images/                        ← All screenshots for index.md
    ├── cartographer-home-new-project-W.png
    ├── new-project-dialog-W.png
    ├── project-name-and-instructions.png
    └── ...
```

`docs/process-to-production/` follows the same pattern, with an `index.md` and an `index.images/` folder (no `dependencies/`).

### Multi-lesson exercise (option)

A longer exercise can be split into an overview, numbered lessons, and a summary page. The structure below uses a fictional `expense-report-processing` exercise (see `Master/Templates/`):

```
docs/expense-report-processing/
├── index.md                             ← Overview page (ALWAYS named index.md)
├── 1-configure-extraction.md            ← Lesson 1
├── 2-build-policy-agent.md              ← Lesson 2
├── 3-configure-approval.md              ← Lesson 3
├── you-did-it.md                        ← Summary/outro page (no numeric prefix)
├── documentation.txt                    ← Links to official docs (for metadata extraction)
├── documentation.cache.json             ← Embedded doc context cache (gitignored)
├── dependencies/                        ← Downloadable files referenced by lessons
│   └── sample-expense-report.pdf
├── 1-configure-extraction.images/       ← Images for lesson 1
│   ├── 1-create-extraction-project.png
│   ├── 1-create-extraction-project.metadata.json
│   └── ...
├── 2-build-policy-agent.images/         ← Images for lesson 2
├── 3-configure-approval.images/         ← Images for lesson 3
└── you-did-it.images/                   ← Images for summary page
```

---

## Archive folder

Exercises and lessons removed with `/remove-exercise` or `/remove-lesson` are moved to `Archive/` rather than deleted. The `Archive/` folder mirrors the structure of `docs/`:

```
Archive/
└── sample-exercise/           ← Archived exercise folder (same structure as docs/)
    ├── index.md
    └── index.images/
```

The `Archive/` folder is **gitignored** — archived content is never pushed to the repository or deployed to the live site.

---

## Naming conventions

### Exercise folders

- Lowercase, hyphenated: `warranty-resolution`, `process-to-production`
- Descriptive of the business use case, not the technology

### Overview page

- **Always** `index.md` (never `0-index.md`)
- This ensures the folder URL `/exercise-slug/` serves the overview page by default
- In a single-page exercise, `index.md` is the whole exercise

### Lesson files

Only for multi-lesson exercises.

- Pattern: **`N-verb-noun.md`** — numeric prefix + descriptive action
- The numeric prefix makes reading order obvious in file explorers and IDEs
- Examples: `1-configure-extraction.md`, `2-build-policy-agent.md`, `3-configure-approval.md`
- Numbers must be sequential with no gaps (1, 2, 3... not 1, 3, 5)

### Summary/outro page

Only for multi-lesson exercises.

- `you-did-it.md` (no numeric prefix)
- Alternatively: `next-steps.md` if the exercise doesn't have a celebratory ending

### Image folders (per page)

Each page gets its own image folder named after the page file (without the `.md` extension):

| Page file | Image folder |
|------------|-------------|
| `index.md` | `index.images/` |
| `1-configure-extraction.md` | `1-configure-extraction.images/` |
| `2-build-policy-agent.md` | `2-build-policy-agent.images/` |
| `you-did-it.md` | `you-did-it.images/` |

The folder name is derived from the page filename by:
1. Removing the `.md` extension (`index.md` → `index`)
2. Appending `.images/`

This pattern keeps images organized per page and is required by the metadata extraction script.

### Image files

**Final naming convention:** Descriptive name based on image content, derived from metadata extraction.

- Lowercase, hyphenated: `new-project-dialog-W.png`, `choose-map-format-W.png`, `register-work-account.png`
- Names describe the action or UI state shown in the screenshot
- Named by the `/new-lesson` skill during metadata extraction — **do not rename manually after processing**
- Wide screenshots (full-screen, detailed layouts) append `-W`: `transformation-decisions-W.png`
- The `-W` suffix signals that the image should render at full width (see [Formatting.md](Formatting.md))
- Formats: PNG for screenshots (preferred), JPG for photos, SVG for diagrams, GIF for animations
- Single-page exercises may drop the numeric prefix, as the current exercises do; the order is set by the page itself

**Upload and processing workflow:**
1. Take screenshots and save them in the page's `.images/` folder. Names can be:
   - **Sequential numeric:** `1.png`, `2.png`, `3.png`, etc.
   - **Mac screenshot format:** `Screenshot 2026-04-07 at 3.38.16 PM.png` (automatically sorted by timestamp)
2. Run `/new-lesson` — the skill extracts metadata from each screenshot, preserving order
3. The skill renames each image based on its `step_instruction` and `ui_description` fields: `1-create-project.png`, `2-add-evidence.png`, etc.
4. Claude references the renamed images in the page markdown

The numeric prefix in the final name is derived from the image order, and the descriptive slug comes from the image content — it ensures metadata extraction processes images in the correct order, then each image is renamed with a meaningful name once its content is understood.

### Metadata files

- Same name as the image with `.metadata.json` appended: `1-create-project.metadata.json`
- Generated by `scripts/extract_metadata.py`, not created manually
- Contains: `filename`, `ocr_text`, `ui_description`, `step_instruction`

### Documentation references file

- **`documentation.txt`** — one per exercise, in the exercise root folder
- Contains links to official UiPath docs relevant to that exercise
- Read by the metadata extraction script for RAG context
- Format: one URL per line, optionally prefixed with `-`
- Optional: the current exercises don't have one yet. Add it before running `/new-lesson` on an exercise.

### Dependencies folder

- `dependencies/` — downloadable files referenced by the page (e.g., the evidence pack `.zip`, `.bpmn` files, sample data)
- Only create when the exercise has downloadable artifacts

---

## Nav registration (mkdocs.yml)

### Draft vs. published exercises

New exercises created with `/new-exercise` start as **drafts** — their files exist in `docs/` but they are not listed in `mkdocs.yml`. Drafts are accessible via direct URL but invisible in the navigation menu and on the home page.

Run `/publish-exercise <slug>` when the exercise is ready for learners. That skill adds the nav section and home page card.

### Published nav structure

A single-page exercise is one nav entry. This is the current `nav:` section:

```yaml
nav:
  - Home: index.md
  - Warranty Resolution at Cobalt Ridge: warranty-resolution/index.md
  - From Process to Production: process-to-production/index.md
  - Next Steps: next-steps.md
```

A multi-lesson exercise lists every page in its own section:

```yaml
nav:
  - Home: index.md
  - Exercise Display Name:
    - Overview: exercise-slug/index.md
    - 1. Lesson One Title: exercise-slug/1-verb-noun.md
    - 2. Lesson Two Title: exercise-slug/2-verb-noun.md
    - 3. Lesson Three Title: exercise-slug/3-verb-noun.md
    - You did it!: exercise-slug/you-did-it.md
  - Next Steps: next-steps.md
```

Rules:
- Exercise display name matches the `# Title` in `index.md` (a shortened form is fine when the title is long, e.g. `Warranty Resolution at Cobalt Ridge`)
- Overview page uses label: `Overview`
- Lesson labels have numeric prefixes: `1. Configure Document Extraction`, `2. Build the Policy Agent`
- Summary page: `You did it!`
- New exercises go before `- Next Steps: next-steps.md`

---

## Config files — do not change without reason

| File | What it controls | Notes |
|------|-----------------|-------|
| `mkdocs.yml` | Theme, nav, plugins, extensions | Theme: Material, palette: deep orange primary / orange accent. `site_url` must match the GitHub Pages URL (`https://uipath-practice.github.io/CartographerWorkshop/`). |
| `main.py` | `{{ training_url }}`, `{{ training_tenant }}`, `{{ env_label }}` macros | Profile picked by the `COURSE_ENV` variable (`staging` \| `prod`, default `prod`) |
| `docs/stylesheets/extra.css` | Image borders, two-column grids, admonition colours, typography | UiPath brand colours and layout classes |
| `docs/javascripts/extra.js` | External links open in new tab | Tiny script, rarely needs changes |
| `hooks/split_cols.py` | `[[[...|N|...]]]` shorthand → HTML grid | Processes markdown before MkDocs renders |

---

## Local commands

Commands run from the repo root with the repo's own virtual environment (`.venv/`). On Windows, call it as `.venv/Scripts/python.exe -m mkdocs`; with the environment activated, plain `mkdocs` works too.

Preview the site locally (served at `http://127.0.0.1:8000/CartographerWorkshop/`):
```bash
COURSE_ENV=staging .venv/Scripts/python.exe -m mkdocs serve
```

Preview locally with draft exercises visible in the navigation:
```bash
COURSE_ENV=staging .venv/Scripts/python.exe -m mkdocs serve -f mkdocs.local.yml
```

Build check before committing:
```bash
COURSE_ENV=prod .venv/Scripts/python.exe -m mkdocs build --strict
```

Run metadata extraction for an exercise:
```bash
.venv/Scripts/python.exe -m scripts.extract_metadata --folder docs/<exercise-slug>/
```
