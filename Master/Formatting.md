# Formatting Reference

Every formatting pattern used in course pages, with examples. Organized so you can find the pattern you need quickly.

---

## Table of Contents

- [Images](#images)
- [Two-Column Layouts](#two-column-layouts)
- [Code Blocks](#code-blocks)
- [Documenting Arguments](#documenting-arguments)
- [Prompt Updates (Diff + Highlighted Block)](#prompt-updates)
- [Admonitions](#admonitions)
- [Tables](#tables)
- [Lists](#lists)
- [Horizontal Rules](#horizontal-rules)
- [Links](#links)

---

## Images

### Basic screenshot (with border and shadow)

Use `.screenshot` for all UiPath UI screenshots — it adds a subtle border and shadow.

```markdown
![Alt text describing what the screenshot shows](step-slug.images/filename.png){ .screenshot }
```

### Plain image (no styling)

```markdown
![Alt text](step-slug.images/filename.png)
```

### Screenshot with caption

```markdown
![Alt text](step-slug.images/filename.png){ .screenshot }
*Caption text shown below the image*
```

### Wide images (-W suffix)

Images ending with `-W` in the filename contain large text or detailed layouts that benefit from full-width viewing. Display at `width="900"`:

```markdown
![Alt text](step-slug.images/filename-W.png){ .screenshot width="900" }
```

Examples of wide images: full-screen app layouts, process diagrams, side-by-side document comparisons, evaluation set views.

### Standard images that need sizing

For regular screenshots that render too large without constraint:

```markdown
![Alt text](step-slug.images/filename.png){ .screenshot width="700" }
```

Common width values: `600`, `700`, `800`. Use `900` only for `-W` images.

### Images inside numbered lists

Indent 4 spaces to keep the image inside the list item (prevents numbering from resetting):

```markdown
1. Open **Agent Builder** and select **New Agent**.

    ![New Agent button in Agent Builder](step-slug.images/1-new-agent.png){ .screenshot }

2. Enter a name for your agent and click **Create**.
```

### Alt text rules

- Describe what is shown, not what to do: "Agent Builder system prompt configuration panel" (not "Click here")
- Never leave alt text empty for informational screenshots
- Decorative images may use empty alt: `![](images/divider.svg)`

### Image from shared folder

When the same image is used on multiple pages:

```markdown
![Alt text](../assets/images/filename.png){ .screenshot }
```

---

## Two-Column Layouts

Use the split-column shorthand when a screenshot and its description should sit side by side. Processed by `hooks/split_cols.py`.

### Syntax

```
[[[
left column content (markdown)
|N|
right column content (markdown)
]]]
```

Each delimiter (`[[[`, `|N|`, `]]]`) **must** be on its own line with no trailing spaces.

### Supported ratios

| Value | Split | Typical use |
|-------|-------|------------|
| `\|30\|` | 30% left / 70% right | Text left, large screenshot right |
| `\|50\|` | 50% left / 50% right | Equal weight content |
| `\|70\|` | 70% left / 30% right | Large screenshot left, text right |

### Pattern: text left, screenshot right (most common)

```
[[[
Click on **Data Manager** in the left ribbon, then click "**+**" to add a new argument.
|30|
![Data Manager panel with add button](step-slug.images/4-data-manager.png){ .screenshot }
]]]
```

### Pattern: screenshot left, text right

```
[[[
![New agent created in Studio Web](step-slug.images/2-create-agent.png){ .screenshot }
|70|
In **Studio Web**, add a new Agent to your solution and name it:
```text
Expense Policy Agent
` ` `
]]]
```

(The backticks in the right column render as a code block inside the layout.)

### When to use two-column vs. full-width

- **Regular images (no `-W` suffix):** Default to two-column layout with `|30|` — text on left, image on right
- **Wide images (`-W` suffix):** Full-width with `width="900"`, no two-column layout
- **Images that need more context:** Use `|50|` or `|70|` depending on content balance

### When NOT to use two-column

- Images inside a numbered step list (use 4-space indent instead)
- Wide screenshots that lose detail when squeezed into a column
- When the text next to the image is a single short sentence (just put text above and image below)

---

## Code Blocks

Every prompt, configuration snippet, or text the learner must copy gets a **fenced code block**. MkDocs Material adds a copy-to-clipboard button automatically.

### Rules

1. The code block contains **exactly** what the learner pastes — no explanation, no placeholder comments, no extra blank lines
2. Always include a language identifier: ` ```yaml `, ` ```json `, ` ```python `, ` ```text `, ` ```css `, ` ```cpp `, ` ```markdown `
3. Choose the identifier that produces the most readable syntax highlighting (not strict language correctness)
4. Plain prose with no keywords uses ` ```text `
5. Never leave the opening fence bare (no ` ``` ` without a language)

### With title attribute

Add a contextual label above the code block:

````markdown
```markdown title="Enter the following text in the System Prompt field:"
You are an Expense Policy Validation Agent...
```
````

### With highlighted lines

Highlight specific lines to draw attention:

````markdown
```markdown hl_lines="5 6 7 9"
Line 1 of prompt
Line 2
Line 3
Line 4
Line 5 — this will be highlighted
Line 6 — highlighted
Line 7 — highlighted
Line 8
Line 9 — highlighted
```
````

### With title AND highlighted lines

````markdown
```markdown hl_lines="3 4 5" title="Update the System Prompt:"
First line
Second line
Third line — highlighted
Fourth line — highlighted
Fifth line — highlighted
```
````

### Gateway expressions / short snippets

For short configuration expressions, use ` ```css ` for readable highlighting:

```markdown
```css
vars.outStatus.ToLower()=="approved"
` ` `
```

---

## Documenting Arguments

When documenting inputs, outputs, or arguments for agents, RPA workflows, or tools, use this highlighted code block pattern:

### Pattern

````markdown
```css hl_lines="1"
ArgumentName
```
```text
Brief description of the argument
```

```css hl_lines="1"
NextArgumentName
```
```text
Description of what this argument contains
```
````

### Example (fictional expense-policy agent)

````markdown
```css hl_lines="1"
in_EmployeeID
```
```text
Employee ID from the expense report header
```

```css hl_lines="1"
in_LookbackDays
```
```text
Number of days to look back for spending history (default: 90)
```

```css hl_lines="1"
out_Status
```
```text
Approval status: 'Approved', 'Flagged', or 'Rejected'
```
````

See [Templates/1-sample-lesson.md](Templates/1-sample-lesson.md), steps 1 and 3, for the pattern in context.

### When to use this pattern

- Agent input/output arguments
- RPA process inputs/outputs
- Tool argument descriptions
- Any list of named parameters with descriptions

Do **not** use tables for this — tables are for comparisons and references. The code block pattern is more scannable and lets learners copy individual values.

---

## Prompt Updates

When an agent's prompt needs to be updated (e.g., new tools added), use this two-part template:

### Part 1: Collapsible diff (review what changed)

````markdown
??? tip "Review the changes"
    Here are the changes that we need to apply. Review carefully:
    ```diff 

    --- Original
    +++ With [Feature/Tool Name]

    [unchanged lines for context]
    -[removed or changed FROM lines]
    +[added or changed TO lines]
    [more unchanged lines]
    ```
````

### Part 2: Full updated prompt (copy-paste)

The complete prompt with `hl_lines` highlighting only the **new or modified lines**:

````markdown
```markdown hl_lines="5 6 7 9" title="Update the System Prompt to reference the context and tool:"
Full prompt text here.
Only changed lines are highlighted.
The learner copies this entire block.
```
````

### Design intent

- **Diff section:** Collapsible (`???` not `!!!`) so learners can optionally review what changed
- **Final code block:** Full context with highlights. This is what learners copy-paste.
- **Highlighting:** Only changed lines get `hl_lines`, not the entire block
- **Title attribute:** Labels the code block contextually

### Complete example

See step 4, "Update the prompt for tools", in [Templates/1-sample-lesson.md](Templates/1-sample-lesson.md) for a complete implementation.

---

## Admonitions

| Type | Syntax | Use for |
|------|--------|---------|
| **tip** | `!!! tip "Title"` | Plan for the lesson, helpful shortcuts, contextual advice |
| **info** | `!!! info "Title"` | Training environment details (platform URL, tenant) |
| **note** | `!!! note "Title"` | General notices, placeholder for content being migrated |
| **warning** | `!!! warning "Title"` | Actions that could cause errors or data loss |

### Collapsible admonitions

Use `???` instead of `!!!` for content that is optional to read:

```markdown
??? tip "Review the changes"
    Collapsible content here — learner clicks to expand.
```

### Collapsible blocks with complex nested markdown

When collapsible content includes nested code blocks or other deeply indented markdown (e.g., a sample agent transcript with fenced code inside), use the HTML `<details>` element with the `markdown="1"` attribute instead of `???`. The `md_in_html` extension (enabled in `mkdocs.yml`) processes markdown inside it correctly:

```markdown
<details markdown="1">
<summary>Here is what the output will look like</summary>

Regular markdown here, including:

```bash
uip agent validate my-agent --output json
```

And bullet lists, bold text, etc.

</details>
```

Use `???` for simple collapsible text. Use `<details markdown="1">` when the content contains fenced code blocks — nested fences inside `???` require 4-space indentation on every line, which breaks syntax highlighting.

### Standard training environment callout

Use this exact text in exercise overview pages. Always use macros — never hardcode URLs or tenant names:

```markdown
!!! tip "Training Environment"
    Log in at **[{{ training_url }}]({{ training_url }})** and remember using tenant **{{ training_tenant }}** for this exercise.
```

Values resolve from the `COURSE_ENV` environment variable via `main.py`. Author with `COURSE_ENV=staging`; CI deploys with `COURSE_ENV=prod`.

### Standard prerequisites callout

Use this pattern at the top of setup or first-exercise overview pages, between the `## Overview` text and the step table:

```markdown
!!! info "Before you begin: prerequisites"
    Have these ready **before** the session:

    - **Prerequisite one** — brief explanation.
    - **Prerequisite two** — brief explanation.
    - **A UiPath Cloud account**. In this workshop we will use: `{{ training_url }}/{{ training_tenant }}`. Talk to your trainer if you are not invited.
```

Omit this callout for exercises where no setup is needed before starting.

### Admonitions inside content

```markdown
!!! warning "This RPA workflow is good enough only for this exercise"
    This workflow has no input validation and no exception handling.
```

Do not invent new admonition types beyond the four listed above without a clear reason.

---

## Tables

### Use tables for

- Phase/step summaries on overview pages (Step | Focus)
- Component role comparisons (Component | Role)
- Stage or journey summaries (Stage | What happens)
- Resource/link references (Resource | Description)

### Do NOT use tables for

- Lists of arguments (use the code block pattern above)
- Step-by-step instructions (use numbered lists)
- Long-form content (use sections with headings)

### Formatting rules

- Keep rows short — if a cell would wrap awkwardly, convert to a description list
- Use alignment where it helps readability: `---:` for right-aligned numbers, `:---` for left-aligned text
- Header row is required

### Example

```markdown
| Step | Focus |
| ---: | :--- |
| [**Configure Document Extraction**](1-configure-extraction.md) | Set up IXP to extract receipt data |
| [**Build the Policy Agent**](2-build-policy-agent.md) | Validate expenses against company policy rules |
```

---

## Lists

### Numbered lists

Use for sequential steps only:

```markdown
1. Open **Agent Builder** and select **New Agent**.
2. Enter a name for your agent.
3. Click **Create**.
```

### Bullet lists

Use for non-sequential items, feature lists, "you'll learn" sections:

```markdown
- Current-state wiki
- Transformation Decisions
```

### Nesting

Maximum two levels. If you need a third level, restructure as a new section.

---

## Horizontal Rules

```markdown
---
```

Use to separate:
- The header block from the body on overview/home pages
- Major top-level sections on overview and summary pages

Do **not** use within lesson pages — use `##` headings for separation instead.

---

## Links

### Internal links

Relative paths within the same exercise:

```markdown
[next lesson](3-configure-approval.md)
[evidence pack](dependencies/Cobalt-Ridge-Warranty-Resolution-Company-Source.zip)
```

Cross-exercise links:

```markdown
[From Process to Production](../process-to-production/index.md)
```

### External URLs

Always use Markdown link syntax, never bare URLs:

```markdown
[uipathlabs.uipath.com/sandboxes/new](https://uipathlabs.uipath.com/sandboxes/new)
[bpmn.uipath.com](https://bpmn.uipath.com/)
```

### No bottom navigation

Do **not** add manual navigation links at the bottom of pages:

```markdown
<!-- DO NOT ADD THIS -->
[← Previous](previous.md) | [Next →](next.md)
```

Navigation is handled by the MkDocs Material theme's sidebar (`navigation.footer` enabled in `mkdocs.yml`).
