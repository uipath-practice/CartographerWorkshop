Review an entire exercise against course standards. This includes all individual lesson checks plus cross-lesson coherence checks.

Use the highest available model (Opus 4.6) for this review to ensure thoroughness.

## Input

The user provides an exercise identifier:
- Exercise slug — e.g., `warranty-resolution`
- Full path — e.g., `docs/warranty-resolution/`

If the identifier is ambiguous or missing, ask the user to clarify.

---

## Step 1: Load standards

Read all Master files to establish the review criteria:

1. `Master/Filesystem.md` — folder structure, file naming, image conventions
2. `Master/CourseStructure.md` — page structure for all page types
3. `Master/Formatting.md` — all formatting patterns
4. `Master/Language.md` — voice, tone, word choices

---

## Step 2: Inventory the exercise

1. List all files in `docs/<exercise-slug>/` (markdown files, image folders, other files)
2. Read the `nav:` section for this exercise in `mkdocs.yml`
3. Read every `.md` file in the exercise folder
4. List all images in every `*.images/` folder

Build a map of:
- Which pages exist and their types (overview, lesson, summary)
- Which images exist and which are referenced
- Nav registration status for each page

---

## Step 3: Run exercise-level checks

### Filesystem checks (from Filesystem.md)

- [ ] Overview page is named `index.md`
- [ ] Lesson files follow `N-verb-noun.md` naming (numeric prefix, sequential, no gaps)
- [ ] Summary page exists (`you-did-it.md` or `next-steps.md`)
- [ ] Each lesson has a corresponding `<N-lesson-slug>.images/` folder — named after the lesson file **including** its numeric prefix (e.g., `1-create-bpmn.images/`, `2-configure-robot.images/`)
- [ ] Image files are lowercase, hyphenated, numbered
- [ ] Wide images have `-W` suffix
- [ ] `documentation.txt` exists in the exercise root
- [ ] No stale or orphaned files

### Nav checks

- [ ] All exercise pages are registered in `mkdocs.yml` nav
- [ ] Overview page label is "Overview"
- [ ] Lesson labels have numeric prefixes matching file order ("1. Title", "2. Title")
- [ ] Summary page label is "You did it!" or similar
- [ ] No pages in nav that don't exist on disk
- [ ] No pages on disk that aren't in nav (excluding non-page files)

### Overview page checks (from CourseStructure.md)

- [ ] Title is a noun phrase (exercise name)
- [ ] Bold headline present (one sentence)
- [ ] `## Overview` section with 2–3 sentences
- [ ] Step table with links to all lessons
- [ ] All step table links resolve to existing files
- [ ] Training environment callout at the bottom

### Summary page checks (from CourseStructure.md)

- [ ] Congratulations admonition present
- [ ] `## What you built` section with component table
- [ ] Component table accurately reflects what was built in the exercise
- [ ] `## Next steps` section present
- [ ] `## Keep iterating` section present
- [ ] `## Learn more` section with resource table

---

## Step 4: Run lesson-level checks on each lesson

For each lesson page, run the same checks as the `/review-lesson` skill:

### Structure checks
- Title, plan admonition, goal section, concept sections, steps section
- No bottom navigation, no misused horizontal rules

### Formatting checks
- Screenshot classes, wide image sizing, code block identifiers
- Two-column layouts, admonition types, link formats
- Argument documentation pattern, prompt update pattern

### Language checks
- Person, tense, forbidden words, platform names, acronyms
- Sentence length, paragraph length, tone

---

## Step 5: Cross-lesson coherence checks

These checks span multiple pages and ensure the exercise works as a unified whole:

- [ ] **Platform name consistency** — same names used across all pages (e.g., not "Studio Web" in one lesson and "UiPath Studio" in another)
- [ ] **Terminology consistency** — domain terms are used the same way throughout (e.g., "Purchase Order" vs "PO" should be consistent after first definition)
- [ ] **Progressive build** — each lesson builds on the previous one; no lesson references concepts not yet introduced
- [ ] **Cross-lesson links** — any links between lessons resolve correctly
- [ ] **Input/output chain** — outputs from one lesson match inputs expected in the next
- [ ] **Image quality** — no duplicate images across lessons, no images that look like they belong in a different lesson
- [ ] **Tone consistency** — similar level of formality and personality across all lessons

---

## Step 6: Image audit

For each image folder:
1. List images referenced in the lesson markdown
2. List images on disk
3. Report:
   - **Missing:** referenced in markdown but not on disk
   - **Orphaned:** on disk but not referenced in any markdown file
   - **Naming:** images that don't follow the naming convention

---

## Step 7: Report findings

Organize findings into categories, grouping by page:

### Exercise-level findings
Issues that span multiple pages or affect the exercise as a whole.

### Per-page findings
For each page (overview, lessons, summary), report:

**Must fix** — broken formatting, missing required sections, forbidden words, broken links/images
**Recommend** — structure deviations, inconsistent patterns, potential improvements
**Info** — minor style suggestions

---

## Important

- **Do not auto-fix anything.** This skill only reports findings.
- **Respect human choices.** If the author has changed structure from the template, note it under "Recommend" but don't frame it as an error. The human has reviewed these pages.
- **Be thorough but practical.** Don't report 50 instances of the same issue — group them and give a count.
- **Be specific.** Include file names, line numbers, and quote the problematic text.
- **Reference Master files.** For each finding, cite which Master file and which rule applies.
- **Use the highest model.** This review should use Opus 4.6 for maximum thoroughness and accuracy.

$ARGUMENTS
