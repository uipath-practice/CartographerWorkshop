# Course Structure

How courses are organized into pages, and what each page type contains. Includes full templates for each page type.

Reference implementation: **Warranty Resolution at Cobalt Ridge Automation** exercise (`docs/warranty-resolution/`).

---

## Page types

An exercise can take one of two shapes.

### Single-page exercise (used in this course)

Both exercises in this course are single-page: `docs/warranty-resolution/index.md` and `docs/process-to-production/index.md`. The whole guide lives in `index.md`. Each part of the exercise is a `##` section, and the hands-on steps inside it are `### N.` substeps. The page is registered in the nav as one entry.

```
# Title                           ← Exercise name (noun phrase)
!!! tip "Plan admonition"         ← 3–4 high-level actions for the whole exercise
## Goal                           ← One paragraph: what the learner will have built
## Concept Section(s)             ← Background, e.g. "How Cartographer works"
## Prerequisites                  ← Optional: setup steps and prerequisites callout
## Part One                       ← One section per part of the exercise
  ### 1. Substep heading
  ### 2. Substep heading
## Part Two
  ### 1. Substep heading
  ### ...
## Optional: ...                  ← Optional extra section for fast learners
Training environment callout      ← Standard tip admonition (always use macros)
```

Each `##` part follows the lesson rules below (concept first, then numbered substeps). Substep numbering restarts at `1.` in each `##` section. There is no separate summary page — the site-level wrap-up lives in `docs/next-steps.md`.

### Multi-lesson exercise (option)

For a longer exercise, split it into three page types in this order:

| Page type | File | Purpose |
|-----------|------|---------|
| **Overview** | `index.md` | What the exercise is about, what you'll build, links to all lessons |
| **Lesson** (1–N) | `N-verb-noun.md` | Theory + hands-on steps for one part of the exercise |
| **Summary** | `you-did-it.md` | Congratulations, what you built, next steps, learn more |

The rest of this file describes the multi-lesson page types. The same content rules apply to the matching parts of a single-page exercise.

---

## 1. Overview Page

The overview page is the entry point for an exercise. It should be short and scannable — a learner glances at it and knows what they're getting into.

### Structure

```
# Title                           ← Exercise name (noun phrase)
**Headline**                      ← One sentence: what the learner builds
## Overview                       ← 2–3 sentences + platform features used
Prerequisites callout             ← Standard info admonition (omit if no setup needed)
Step table                        ← Table with links to each lesson
Training environment callout      ← Standard tip admonition (always use macros)
```

### Content rules

- **Title** — The exercise name as a noun phrase. Examples: "Warranty Resolution at Cobalt Ridge Automation", "From Process to Production"
- **Headline** — Bold, one sentence describing what the learner builds. Example: "Take a warranty process from a blank Cartographer project to a published PDD."
- **Overview** — 2–3 sentences. Names the key platform features (bold on first use). Explains the business case briefly.
- **Steps table** — One row per lesson. Columns: `Step` (right-aligned, linked) and `Focus` (left-aligned, brief description). Links use relative paths to lesson files.
- **Training environment** — Standard callout at the bottom (see template).

### Template

````markdown
# Exercise Name

**One sentence describing what the learner builds in this exercise.**

## Overview

Two to three sentences about the business process and what platform features are used. Bold platform names on first appearance: **Cartographer**, **Automation Hub**, **Maestro**, **Orchestrator**.

!!! info "Before you begin: prerequisites"
    Have these ready **before** the session:

    - **Prerequisite one** — brief explanation.
    - **Prerequisite two** — brief explanation.
    - **A UiPath Cloud account**. In this workshop we will use: `{{ training_url }}/{{ training_tenant }}`. Talk to your trainer if you are not invited.

| Step | Focus |
| ---: | :--- |
| [**Lesson One Title**](1-verb-noun.md) | Brief description of what the learner does |
| [**Lesson Two Title**](2-verb-noun.md) | Brief description |
| [**Lesson Three Title**](3-verb-noun.md) | Brief description |

!!! tip "Training Environment"
    Log in at **[{{ training_url }}]({{ training_url }})** and remember using tenant **{{ training_tenant }}** for this exercise.
````

### Real example (Warranty Resolution at Cobalt Ridge Automation — opening)

The current exercises are single-page, so the opening of `index.md` carries the plan and goal for the whole exercise instead of a step table:

````markdown
# Warranty Resolution at Cobalt Ridge Automation

!!! tip "Here is our plan for this exercise:"

    1. Create a **Cartographer** project, give it the business brief, and check what it already knows.
    2. Feed it the evidence a real team would have and review the current state (AS-IS) it builds.
    3. Design the future state (TO-BE), make a live edit, and verify it landed everywhere.
    4. Generate the **PDD**, trace your edits inside it, and publish it to **Automation Hub**.

## Goal

By the end of this exercise you'll have taken one process from a blank project to a published Process Definition Document (PDD). You'll have a current-state wiki with provenance on every fact, a future-state design where every change is tied to a specific KPI, and a PDD that carries your own edits. That PDD is everything a Solution Design Document (SDD) needs.
````

---

## 2. Lesson Page

Lesson pages are the core of the course. Each one teaches background concepts and then walks the learner through hands-on steps. In a single-page exercise, each `##` part of `index.md` plays the role of a lesson.

### Structure

```
# Title                           ← Descriptive phrase (see rules below)
!!! tip "Plan admonition"         ← 2–3 high-level actions for this lesson
## Goal                           ← One paragraph: what the learner will have built
## Concept Section(s)             ← 1+ sections covering theory and background
## Steps                          ← Numbered step-by-step instructions with screenshots
  ### 1. Substep heading
  ### 2. Substep heading
  ### ...
```

### Content rules

**Title:**
- A descriptive phrase, not a generic "Step N" label
- Can vary in style: "Set up the project and check its knowledge", "Design the future state", "Make live edits and verify them"
- Should convey what the lesson is about at a glance

**Plan admonition (tip):**
- Opens the page immediately after the title
- Lists 2–3 high-level actions the learner will take
- Title text can vary: "Here is our plan for this lesson:", "Here is our plan for this exercise:", "Let's start!", "What you'll do"
- Use a numbered list inside

```markdown
!!! tip "Here is our plan for this lesson:"

    1. Create the agent and configure its arguments.
    2. Configure testing and build an evaluations dataset.
    3. Add the agent to the Maestro workflow.
```

**Goal section:**
- One paragraph, 2–4 sentences
- Describes what the learner will have *built* by the end (not what they will *do*)
- Second person: "you'll have configured", "your agent will be able to"

**Concept sections:**
- One `##` section per key concept or background needed before hands-on steps
- Explain *why* this approach was chosen, how a platform feature works, what inputs/outputs to expect
- Keep each section short: 2–4 sentences per paragraph
- These are not optional filler — they provide the context a first-time learner needs

**Steps section:**
- Use `## Steps` as the section heading (or a descriptive heading like "Design the future state")
- Use `### N. Descriptive substep heading` for each substep
- Number substeps sequentially: `### 1. Create the project and give it the brief`, `### 2. Ask what it already knows, before uploading anything`
- Each substep has action text followed by screenshots
- Steps are numbered with `1. 2. 3.` inside the prose, not bullet points
- Screenshots sit inside numbered lists with 4-space indent to preserve numbering

**What NOT to include:**
- No bottom navigation links (`[← Previous]` / `[Next →]`) — the MkDocs sidebar handles this
- No horizontal rules (`---`) within lesson pages — use `##` headings for separation
- No `!!! note "Content migration in progress"` unless migrating real content that hasn't been transferred yet

### Template

````markdown
# Descriptive Lesson Title

!!! tip "Here is our plan for this lesson:"

    1. First high-level action the learner will take
    2. Second high-level action
    3. Third action (if applicable)

## Goal

One paragraph describing what the learner will have built or configured by the end of this lesson. Keep it to 2–4 sentences. Use second person and future tense.

## Background Concept

Background explanation that the learner needs before starting the hands-on steps. Why this approach matters, how the platform feature works, what to expect.

Keep paragraphs short — 2–4 sentences maximum.

## Steps

### 1. First substep heading

Action text explaining what to do.

[[[
Additional context or instructions.
|30|
![Alt text describing what the screenshot shows](step-slug.images/1-filename.png){ .screenshot }
]]]

### 2. Second substep heading

More action text.

![Alt text](step-slug.images/2-filename.png){ .screenshot }

### 3. Third substep heading

Continue the hands-on steps until the lesson goal is achieved.
````

### Real example excerpt (from warranty-resolution/index.md)

````markdown
## Capture and review the AS-IS

### 1. Add the evidence

The evidence pack is the kind of material a team already has: process flows from two departments, a process-owner interview, a workshop transcript, an executive brief, a systems architecture draft and a printed claim record.

[[[
1. On the VM desktop, open the **Cobalt Ridge Industrial Equipment Warranty Resolution-FUSION** folder. It holds the evidence files.
2. Attach the files listed below and send them with this prompt:
|50|
![VM desktop with the Cobalt Ridge Industrial Equipment Warranty Resolution-FUSION folder](index.images/vm-desktop-evidence-folder.png){ .screenshot }
]]]

### 3. Check the provenance on a captured item

Open **Pain Points** and expand **Sources and Metadata** at the top of the page.

You can see which agent captured each item and when, the source documents and the exact sections it came from, and the file metadata. This provenance stays attached for the whole life of the Map of Work.

![Pain Points page with the Sources and Metadata panel expanded](index.images/pain-points-provenance-W.png){ .screenshot width="900" }
````

---

## 3. Summary Page (you-did-it.md)

The summary page celebrates completion and gives the learner directions for what to do next. It belongs to multi-lesson exercises; single-page exercises end with their last `##` section and the training environment callout.

### Structure

```
# You did it!
!!! tip "Congratulations!"          ← One-line celebration
---
## What you built                   ← Summary + component table
---
## Next steps                       ← Publish, explore results
  ### 1. First next step
  ### 2. Second next step
---
## Keep iterating                   ← Suggestions for extending the exercise
---
## Learn more                       ← Resource table
```

### Content rules

- **Congratulations admonition** — One sentence summarizing what was built
- **What you built** — 2–3 sentences, then a component/role table
- **Next steps** — Practical steps: publish, run, explore dashboards
- **Keep iterating** — 2–3 suggestions for extending or improving the exercise
- **Learn more** — Table with links to documentation, academy, community. Pull links from `documentation.txt` in the exercise folder.

### Template

````markdown
# You did it!

!!! tip "Congratulations!"

    You've built a complete [one-line description of what they built].

---

## What you built

Two to three sentences summarizing the end-to-end process and what makes it work.

| Component | Role |
|-----------|------|
| **Component 1** | What it does in this exercise |
| **Component 2** | What it does |
| **Component 3** | What it does |

---

## Next steps

### 1. Publish and run your process

Brief instructions on publishing and triggering a run.

### 2. Explore the results

What to look at after a successful run — dashboards, logs, outputs.

---

## Keep iterating

**Improve the agent prompt**

- Suggestion for how to iterate on the prompt.

**Test the boundaries**

- Suggestion for edge case testing.

**Expand the process**

- Suggestion for extending with new capabilities.

---

## Learn more

| Resource | Description |
|----------|-------------|
| Resource Name | One-sentence description |
````

### Complete example

Neither current exercise has a `you-did-it.md`. See [Templates/you-did-it.md](Templates/you-did-it.md) for a complete page that follows this structure.

---

## Home Page (docs/index.md)

The home page is the site-wide entry point. It lists all available exercises.

### Structure

```
# Site Title
**Bold subtitle**
Training environment callout
## What you'll build               ← 2–3 sentences framing all exercises
Exercise links                     ← Bold link + short description for each exercise
## Key concepts                    ← Glossary of platform terms
```

When adding a new exercise, add a link and brief description under the exercise links section. Match the format of existing entries:

```markdown
[**Warranty Resolution at Cobalt Ridge Automation**](warranty-resolution/index.md) — Two to four sentences on the business case and what the learner builds.
```

---

## Global Outro (docs/next-steps.md)

A standalone page at the site level that wraps up the entire workshop. Structure is similar to `you-did-it.md` but covers all exercises, not just one.

---

## Generation vs. Review

**When generating new content** (creating an exercise or lesson from scratch):
- Follow the templates above exactly
- Include all required sections
- Use placeholder content for sections you can't fill yet

**When reviewing existing content** (human has already written or edited the page):
- Assume the human's structural choices are intentional
- Flag deviations from the standard but do not rewrite without confirmation
- Focus on formatting, language, and consistency rather than restructuring
