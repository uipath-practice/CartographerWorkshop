Build a complete lesson page from screenshots for the Cartographer Tech Workshop site.

**Before proceeding, read:** `Master/CourseStructure.md` (lesson page section), `Master/Formatting.md`, `Master/Language.md`, and the sample lesson template `Master/Templates/1-sample-lesson.md` (demonstrates all building blocks in context).

## Collect inputs

If any of the following are missing from the user's message, ask before proceeding:

1. **Exercise slug** — folder name of the exercise (e.g., `expense-report-processing`)
2. **Step number** — the numeric prefix (e.g., `3`)
3. **Step name** — display name for the step (e.g., "Configure Agent")
4. **Images folder path** — path to the folder containing the screenshots (e.g., `docs/expense-report-processing/3-configure-agent.images/`)
5. **Context** (optional) — any additional details: platform features used, expected inputs/outputs, business logic, or special instructions

---

## Step 1: Check documentation references, then extract metadata

**Before running extraction**, check whether `docs/<exercise-slug>/documentation.txt` exists. If it does, remind the user to add links for this lesson's topic before continuing. The extraction script reads this file and embeds the linked documentation as context — this improves metadata quality.

If the file exists but may be missing relevant links, ask the user: *"Have you added the relevant documentation links to documentation.txt for this step?"*

Once ready, run the extraction script:

```bash
python -m scripts.extract_metadata --folder <images-folder-path>
```

**Prerequisites:** `scripts/.env` must exist with Azure OpenAI credentials. See `scripts/.env.example` for the required keys. If the file is missing, stop and ask the user to set it up.

If some images already have `.metadata.json` files, the script skips those by default. Use `--force` only if explicitly requested.

After running, verify that `.metadata.json` files exist next to the images. If the script fails, report the error — do not proceed with placeholder content.

---

## Step 2: Read the metadata

Read every `.metadata.json` file in the images folder. Each file contains:
- `filename` — the image file it describes
- `ocr_text` — raw text visible in the screenshot
- `ui_description` — description of the UI state shown
- `step_instruction` — the action or concept the screenshot illustrates

Build a mental model of the full lesson: what the learner does first, what intermediate states look like, and what the final result is.

Also read the existing lesson `.md` file if it exists (it may be a stub). Note any headings or partial content that should be preserved.

Keep the metadata handy for the next step — you'll use `step_instruction` and `ui_description` to generate the descriptive image names.

---

## Step 2.5: Rename images and metadata files

Once metadata is extracted, rename the image and metadata files to meaningful names based on their content.

**Naming convention:** `N-descriptive-slug.png` and `N-descriptive-slug.metadata.json`

- `N` is the sequential order (1, 2, 3, ...)
- `descriptive-slug` is derived from the image's `step_instruction` or `ui_description` in the metadata
- Wide images append `-W` suffix: `N-descriptive-slug-W.png`

**How to generate names:**
1. Read each `.metadata.json` file in order (ascending by original filename)
2. Extract a short slug from the `step_instruction` or `ui_description` (2–4 words, hyphenated, lowercase)
3. Combine: `1-slug.png`, `2-slug.png`, etc.
4. If the image is wide (full-width, detailed UI), append `-W`: `3-slug-W.png`
5. Rename both the `.png` and `.metadata.json` files with matching names

**Example:**
- Original: `Screenshot 2026-04-07 at 3.38.16 PM.png` → `1-create-agent.png`
- Metadata: `Screenshot 2026-04-07 at 3.38.metadata.json` → `1-create-agent.metadata.json`
- Original: `Screenshot 2026-04-07 at 3.40.55 PM.png` → `2-select-conversational-type.png`
- Metadata: `Screenshot 2026-04-07 at 3.40.metadata.json` → `2-select-conversational-type.metadata.json`

After renaming, verify that each image has a matching metadata file (e.g., `1-create-agent.png` pairs with `1-create-agent.metadata.json`).

---

## Step 3: Build the lesson page

Write the complete lesson to `docs/<exercise-slug>/N-verb-noun.md`.

Follow the **Lesson Page** template in `Master/CourseStructure.md`:

1. **Title** — descriptive phrase (not "Step N — Verb Noun")
2. **Opening tip admonition** — 2–3 high-level plan items
3. **Goal section** — one paragraph, what the learner will have built
4. **Concept sections** — background needed before hands-on steps
5. **Steps section** — numbered substeps with screenshots

Reference the renamed images from Step 2.5. Apply all formatting rules from `Master/Formatting.md`:
- Screenshots use `{ .screenshot }` class
- Wide images (`-W` suffix in filename) use `width="900"`
- Regular images use two-column layout or 4-space indent inside numbered lists
- Code blocks have language identifiers
- Arguments use the `css hl_lines="1"` pattern
- Prompt updates use the collapsible diff + highlighted block pattern

Apply all language rules from `Master/Language.md`:
- Second person, short sentences, conversational tone
- Platform names bold on first appearance
- No forbidden words

Use OCR text from metadata as the source of truth for prompts and config values.

---

## Step 4: Verify

After writing the file, read it back and check:
- Every image referenced exists in the images folder
- All copyable text is in fenced code blocks
- Platform names are bold on first appearance
- No manual navigation links at the bottom
- All two-column blocks have delimiters on their own lines
- Voice matches the language rules

Report what was created and flag any screenshots that had low-confidence metadata for manual review.

Then show the direct URLs for local preview:

```
Lesson created in draft exercise — not visible in navigation until published.

Local preview (requires mkdocs serve):
  http://127.0.0.1:8000/CartographerWorkshop/<exercise-slug>/N-verb-noun/

When all lessons are ready: /publish-exercise <exercise-slug>
```

$ARGUMENTS
