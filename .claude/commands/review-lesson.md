Review a single lesson page against course standards.

## Input

The user provides a lesson identifier in one of these formats:
- `exercise-slug/lesson-file` — e.g., `expense-report-processing/3-configure-agent`
- `exercise-slug/N` — e.g., `expense-report-processing/3` (resolved to the Nth lesson file)
- Full path — e.g., `docs/expense-report-processing/3-configure-agent.md`

If the identifier is ambiguous or missing, ask the user to clarify.

---

## Step 1: Load standards

Read the following Master files to establish the review criteria:

1. `Master/CourseStructure.md` — page structure rules (lesson page section)
2. `Master/Formatting.md` — all formatting patterns
3. `Master/Language.md` — voice, tone, word choices

---

## Step 2: Read the lesson

Read the lesson `.md` file. Also read:
- The exercise's `index.md` (overview page) — for context on what this lesson covers
- The exercise's entry in `mkdocs.yml` `nav:` section — for nav label correctness

---

## Step 3: Check the lesson's image folder

List all images in the lesson's image folder (named after the lesson file **including** its numeric prefix, e.g., `1-create-agent.images/`, `2-configure-robot.images/`). Cross-reference with image references in the markdown:
- Flag images referenced in markdown but missing from disk
- Flag images on disk but not referenced in markdown (orphaned)

---

## Step 4: Run checks

Check the lesson against each category below. For each issue found, note the line number and specific problem.

### Structure checks (from CourseStructure.md)

- [ ] Page starts with `# Title` (descriptive phrase)
- [ ] Opening `!!! tip` admonition with 2–3 high-level plan items
- [ ] `## Goal` section present with 1 paragraph (2–4 sentences)
- [ ] One or more concept `##` sections before steps (if the lesson has background context)
- [ ] `## Steps` section (or descriptive heading) with numbered substeps
- [ ] No bottom navigation links (`[← Previous]` / `[Next →]`)
- [ ] No horizontal rules (`---`) used as section separators (use `##` headings instead)

### Formatting checks (from Formatting.md)

- [ ] All UI screenshots use `{ .screenshot }` class
- [ ] Wide images (`-W` suffix) use `width="900"`
- [ ] Regular images either use two-column layout or are inside numbered lists with 4-space indent
- [ ] All code blocks have a language identifier (no bare ` ``` `)
- [ ] Copyable text (prompts, field values, config) is in fenced code blocks, not inline
- [ ] Arguments documented using the `css hl_lines="1"` + `text` description pattern
- [ ] Prompt updates use the collapsible diff + highlighted code block pattern
- [ ] Two-column `[[[...|N|...]]]` delimiters are each on their own line
- [ ] Admonitions use only approved types: tip, info, note, warning
- [ ] Tables are used for comparisons/references, not for argument lists
- [ ] Internal links use relative paths
- [ ] External links use markdown syntax (no bare URLs)

### Language checks (from Language.md)

- [ ] Second person throughout ("you'll", "your", not "we'll", "the user")
- [ ] No forbidden words: "leverage", "utilize", "robust", "seamlessly", "In this section we will", "Please note that", "It is important to", "feel free to"
- [ ] Platform names bold on first appearance per page
- [ ] Acronyms defined on first use per page
- [ ] Sentences are short (one idea per sentence)
- [ ] Paragraphs are 2–4 sentences maximum
- [ ] Tone is conversational but clear — not corporate, not too casual
- [ ] Domain concepts with intentional capitalisation are preserved (Map of Work, Process Atlas, Transformation Decisions, etc.)

---

## Step 5: Report findings

Organize findings into three categories:

### Must fix
Issues that break formatting, violate hard rules, or could confuse learners:
- Missing required sections
- Broken image references
- Bare code fences
- Forbidden words
- Bottom navigation links

### Recommend
Deviations from the standard that the human author may have chosen intentionally:
- Structure differences from the template
- Image layout choices that differ from the guideline
- Missing concept sections

### Info
Minor style suggestions that are subjective:
- Sentence length in specific paragraphs
- Alternative phrasing suggestions
- Optional formatting improvements

---

## Important

- **Do not auto-fix anything.** This skill only reports findings.
- **Respect human choices.** If the author has changed the structure from the template, note it under "Recommend" but don't frame it as an error.
- **Be specific.** Include line numbers, quote the problematic text, and reference the specific rule from the Master file.
- **Skip checks that don't apply.** Not every lesson has arguments or prompt updates — don't flag their absence.

$ARGUMENTS
