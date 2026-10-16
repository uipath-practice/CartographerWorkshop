Scaffold a new exercise for the Cartographer Tech Workshop site.

**Before proceeding, read:** `Master/Filesystem.md`, `Master/CourseStructure.md`, `Master/Language.md`, and the sample templates in `Master/Templates/` (overview, lesson, summary).

## Collect inputs

If any of the following are missing from the user's message, ask for them before proceeding:

1. **Exercise slug** — lowercase, hyphenated folder name (e.g., `expense-report-processing`). Infer from the display name if not provided.
2. **Display name** — title as it appears in the nav (e.g., "Expense Report Processing")
3. **One-paragraph description** — what the learner will build and which platform products they'll use
4. **Steps** — list of step names with brief descriptions (e.g., "1. Upload Report — robot retrieves PDFs from a storage bucket")

---

## Draft mode — exercise is hidden until published

New exercises are created in **draft mode**. They are accessible via direct URL but do NOT appear in the navigation menu or on the home page. This prevents learners from seeing work-in-progress content.

When the exercise is ready, run `/publish-exercise <slug>` to add it to the navigation and home page.

---

## What to create

### 1. Folder structure

Follow the conventions in `Master/Filesystem.md`:

- `docs/<exercise-slug>/` — exercise folder
- `docs/<exercise-slug>/<N-step-slug>.images/.gitkeep` — one image folder per lesson, named after the lesson file without the `.md` extension (e.g., `1-create-agent.images/`)

After creating the files, add the exercise to `mkdocs.local.yml` so it appears in the navigation during local preview. Use `[Unpublished]` in the section title to distinguish it from published exercises:

```yaml
  - Exercise Display Name [Unpublished]:
    - Overview: <exercise-slug>/index.md
    - 1. Lesson Title: <exercise-slug>/1-verb-noun.md
    - 2. Lesson Title: <exercise-slug>/2-verb-noun.md
    - You did it!: <exercise-slug>/you-did-it.md
```

Serve locally with: `.venv/Scripts/python.exe -m mkdocs serve -f mkdocs.local.yml`
- `docs/<exercise-slug>/documentation.txt` — documentation reference file

**`documentation.txt` template:**

```markdown
# Documentation References — <Display Name>

Add a link here for each new set of screenshots you upload to this exercise.
The metadata extraction script reads this file and embeds the linked documentation
as context for image analysis. New links are fetched and embedded automatically
on the next run; previously embedded links are not re-fetched.

## Links

<!-- Add URLs below, one per line, prefixed with - -->
```

---

### 2. Exercise overview page — `docs/<exercise-slug>/index.md`

Follow the **Overview Page** template in `Master/CourseStructure.md`. Key points:

- `# Title` is a noun phrase — the exercise name
- Bold headline: one sentence describing what the learner builds
- `## Overview` names platform products (bold on first use)
- Step table with links to lesson files
- Training environment callout at the bottom

---

### 3. Lesson stub pages — `docs/<exercise-slug>/N-verb-noun.md`

File names follow the pattern in `Master/Filesystem.md`: numeric prefix + verb-noun slug.

Use this stub structure for each lesson page:

```markdown
# Descriptive Lesson Title

!!! tip "Here is our plan:"

    1. [First action — infer from the step description]
    2. [Second action]
    3. [Third action if applicable]

## Goal

One short paragraph: what the learner will have built or configured by the end of this step.

## Steps

<!-- Add step-by-step instructions with screenshots here -->
```

Apply the language rules from `Master/Language.md` — second person, short sentences, conversational tone.

---

### 4. Summary page — `docs/<exercise-slug>/you-did-it.md`

Follow the **Summary Page** template in `Master/CourseStructure.md`.

**For the Learn more table:** Read `docs/<exercise-slug>/documentation.txt` and extract URLs. If no URLs yet, leave a placeholder row.

---

## Verify

After creating all files, run `mkdocs build` to check for errors:

```bash
.venv/Scripts/python.exe -m mkdocs build
```

MkDocs will warn that the new pages are not in the navigation — this is expected and intentional. Report the warning text so the user knows it's normal.

If the build passes, summarize what was created (files and image folders), then show the direct URLs for local preview:

```
Exercise is in draft mode — not visible in navigation.

Local preview (requires mkdocs serve):
  Overview:  http://127.0.0.1:8000/CartographerWorkshop/<exercise-slug>/
  Lesson 1:  http://127.0.0.1:8000/CartographerWorkshop/<exercise-slug>/1-verb-noun/
  Lesson 2:  http://127.0.0.1:8000/CartographerWorkshop/<exercise-slug>/2-verb-noun/
  ...

When ready to publish: /publish-exercise <exercise-slug>
```

$ARGUMENTS
