Remove an entire exercise — archives all files and removes it from navigation and the home page.

**Before proceeding, read:** `Master/Filesystem.md` (exercise folder structure, nav rules).

## Collect inputs

If the exercise slug is not provided, ask for it:

1. **Exercise slug** — folder name of the exercise (e.g., `warranty-resolution`)

---

## Step 1: Scan what will be affected

Before making any changes, enumerate everything:

### Exercise folder contents

List all files and subfolders in `docs/<exercise-slug>/`:
- Count lesson `.md` files
- Count image folders and total images inside them
- Note any `documentation.txt`, `dependencies/`, `.metadata.json`, and other files

### Navigation section

Read `mkdocs.yml`. Check whether this exercise appears in the nav.
- If yes: show the full nav block verbatim.
- If no: note "Not in nav (exercise was never published)."

### Home page references

Read `docs/index.md`. Search for any links, cards, or numbered descriptions referencing `<exercise-slug>` or the exercise's display name. Show what was found verbatim.

---

## Step 2: Present findings and ask for confirmation

Output a clearly formatted summary — make removed items easy to spot:

```
EXERCISE TO REMOVE
────────────────────────────────────────────────────────────────
Exercise: docs/<exercise-slug>/

Files → Archive/<exercise-slug>/
  ✕  index.md
  ✕  <lesson-1>.md
  ✕  <lesson-2>.md
  ...
  ✕  you-did-it.md
  ✕  <step>.images/  (<N> images)
  ✕  documentation.txt
  [other files as found]

Navigation section (mkdocs.yml):
  ✕  <full nav block for this exercise, indented>
     (or: Not in nav)

Home page (docs/index.md):
  ✕  <verbatim text of the reference/card that will be removed>
     (or: No references found)
────────────────────────────────────────────────────────────────
⚠  This removes the entire exercise. All files move to Archive/.
   This action cannot be undone automatically.
────────────────────────────────────────────────────────────────
```

Then ask: **"Type `yes` to confirm removal of the entire exercise, or anything else to cancel."**

Do not proceed until the user responds. Any input other than `yes` (case-insensitive) cancels the operation — report "Removal cancelled. No changes made." and stop.

---

## Step 3: Archive the exercise folder

1. Create the archive root if needed:
   ```bash
   mkdir -p Archive
   ```

2. Move the entire exercise folder:
   ```bash
   mv docs/<exercise-slug> Archive/<exercise-slug>
   ```

---

## Step 4: Update mkdocs.yml (if the exercise was in nav)

If the exercise had a nav section, remove the entire section from `mkdocs.yml`.

---

## Step 5: Update docs/index.md

Remove any references to the exercise from the home page — links, numbered exercise descriptions, and cards. If the exercise was part of a numbered list (e.g., "Exercise 1", "Exercise 2"), renumber the remaining items to close the gap.

---

## Step 6: Verify

Run `mkdocs build`:

```bash
.venv/Scripts/python.exe -m mkdocs build
```

Report any errors. If the build passes, summarize:
- Exercise folder archived to `Archive/<exercise-slug>/`
- Nav section removed (or "was not in nav")
- Home page updated (or "had no references")
- Build passed

$ARGUMENTS
