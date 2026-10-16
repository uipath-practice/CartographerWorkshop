Remove a single lesson from an exercise — archives files, removes it from navigation, and updates the overview step table.

**Before proceeding, read:** `Master/Filesystem.md` (naming conventions, nav rules) and `Master/CourseStructure.md` (overview page — step table structure).

## Collect inputs

If any of the following are missing, ask before proceeding:

1. **Exercise slug** — folder name of the exercise (e.g., `expense-report-processing`)
2. **Lesson identifier** — any of:
   - File name without extension: `2-configure-robot`
   - Numeric index: `2` (resolved to the Nth lesson file alphabetically by prefix)
   - Full path: `docs/expense-report-processing/2-configure-robot.md`

---

## Step 1: Scan what will be affected

Before making any changes, enumerate everything:

### Files to archive

1. The lesson `.md` file: `docs/<exercise-slug>/<lesson-file>.md`
2. The lesson's image folder and all its contents: `docs/<exercise-slug>/<lesson-file-without-extension>.images/`
   - Count images and `.metadata.json` files separately.
   - If the image folder doesn't exist, note that.

### Navigation entry

Read `mkdocs.yml`. Check whether this lesson appears in the nav.
- If yes: show the exact nav line that will be removed.
- If no: note "Not in nav (exercise not yet published with `/publish-exercise`)" — the lesson will still be archived.

### Overview page (step table)

Read `docs/<exercise-slug>/index.md`. Find the step table row that links to this lesson and show it verbatim.

### Cross-references in other lesson pages

Search all other `.md` files in `docs/<exercise-slug>/` for links to the lesson file (e.g., `](<lesson-file>.md)`). List every occurrence found.

---

## Step 2: Present findings and ask for confirmation

Output a clearly formatted summary — make removed items easy to spot:

```
LESSON TO REMOVE
────────────────────────────────────────────────────────────────
Lesson:   docs/<exercise-slug>/<lesson-file>.md
Images:   docs/<exercise-slug>/<lesson-file-without-extension>.images/  (<N> images, <M> metadata files)

Files → Archive/<exercise-slug>/
  ✕  <lesson-file>.md
  ✕  <lesson-file-without-extension>.images/  (<N> files)

Navigation (mkdocs.yml):
  ✕  "<nav label>" → <exercise-slug>/<lesson-file>.md
     (or: Not in nav — exercise not yet published)

Overview step table (index.md):
  ✕  <verbatim row from the step table>

Remaining lessons after removal:
  <list the lessons that will stay, in order>

⚠  Remaining lesson nav labels and step table will be renumbered to close the gap.
   Lesson filenames are NOT renamed — their URLs stay the same.

Cross-references in other lessons:
  <list of file:line occurrences, or "None found">
────────────────────────────────────────────────────────────────
```

Then ask: **"Type `yes` to confirm removal, or anything else to cancel."**

Do not proceed until the user responds. Any input other than `yes` (case-insensitive) cancels the operation — report "Removal cancelled. No changes made." and stop.

---

## Step 3: Archive the files

1. Create the archive directory:
   ```bash
   mkdir -p Archive/<exercise-slug>
   ```

2. Move the lesson `.md` file:
   ```bash
   mv docs/<exercise-slug>/<lesson-file>.md Archive/<exercise-slug>/
   ```

3. Move the image folder (if it exists):
   ```bash
   mv "docs/<exercise-slug>/<lesson-file-without-extension>.images" "Archive/<exercise-slug>/<lesson-file-without-extension>.images"
   ```

---

## Step 4: Update mkdocs.yml (if the lesson was in nav)

If the lesson had a nav entry:
- Remove that nav entry from `mkdocs.yml`.
- Renumber the remaining lesson nav labels to be sequential: if lessons 1, 3, 4, 5 remain, their labels become `1.`, `2.`, `3.`, `4.`. **Do not rename the actual files.**

---

## Step 5: Update the exercise overview page

In `docs/<exercise-slug>/index.md`:
- Remove the step table row that linked to the removed lesson.
- Renumber the remaining rows so that step numbers are sequential again.

---

## Step 6: Verify

Run `mkdocs build`:

```bash
.venv/Scripts/python.exe -m mkdocs build
```

Report any errors. If the build passes, summarize:
- Files archived to `Archive/<exercise-slug>/`
- Nav entry removed (or "was not in nav")
- Overview step table updated
- Build passed

If cross-references were found in Step 1, remind the user: "The following files still link to the removed lesson — review and update them manually: [list]."

$ARGUMENTS
