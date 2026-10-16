# Language and Tone

How to write course content that is clear, approachable, and consistent. With examples.

---

## Audience

Technical clients and partners who know the UiPath Platform but are new to Cartographer. Assume no prior Cartographer knowledge — explain each concept the first time it appears. They're here to learn by doing.

---

## Voice

### Person and tense

- **Second person** throughout: "you'll configure", "your agent", "open the panel"
- **Present tense** for descriptions: "Cartographer builds the current-state wiki", "the agent updates the future case design"
- **Future tense** for instructions: "you'll add a connection", "in the next step you'll configure"

### Register

Conversational and approachable. Warm, lively, with personality. Not stiff corporate tone, not casual slang. Think: a knowledgeable colleague walking you through something they find genuinely interesting.

**Good:** "Luckily, you can import them all at once by switching to JSON editor mode."
**Good:** "There's no point waiting for a pass that's about to be outdated, so click **Steer** on the queued message to push your request in early."
**Good:** "The future-state pass runs for several minutes. A good moment for a coffee."

**Too formal:** "It should be noted that the aforementioned functionality enables users to import arguments simultaneously."
**Too casual:** "Just yeet the JSON in there and you're golden lol."

### Humour

Humour is welcome — it makes the content more engaging and memorable. Use it sparingly and naturally:

- Light asides and self-aware comments are good: "A good moment for a coffee."
- Wry observations about real-world complexity work well: "It gets attached to an email, someone rebuilds it as a slide, and the developer who finally builds the automation never sees the evidence behind it."
- Visual jokes (e.g., an illustration with a generated quote) add personality
- Do not force humour where it doesn't fit — technical accuracy always comes first
- Avoid jokes that require cultural context the audience may not share

### Sentence length

Short. One idea per sentence. If a sentence runs more than two lines on screen, split it.

**Good:** "Every fact in the Map of Work is attributable. Each element carries its source and its verifier."

**Too long:** "Provenance is a mechanism that makes every fact in the Map of Work attributable, so that each element carries both the source it came from and the person who verified it, which means contradictions between sources can be resolved instead of being averaged away."

### Paragraphs

Two to four sentences maximum. After four sentences, start a new paragraph or use a list.

---

## Word choices

### Words and phrases to avoid

| Avoid | Use instead |
|-------|------------|
| "leverage" | "use" |
| "utilize" | "use" |
| "robust" | (describe what makes it strong instead) |
| "seamlessly" | (describe the actual integration) |
| "In this section we will" | (just start doing it) |
| "Please note that" | (just state the fact) |
| "It is important to" | (just state why) |
| "feel free to" | (just say "you can") |
| "As mentioned earlier" | (just restate if needed) |

### Transitions that work

These keep the conversational flow without being filler:

- "Next, ..." / "Now ..."
- "Let's ..." (for collaborative framing)
- "Here's what changes:" / "Here's the structure:"
- "Done." (for a satisfying end to a configuration step)
- "Time to give it a try" / "Time to move on"

### Platform names

Bold on **first appearance per page**, plain text after. Always use the exact name:

| Correct | Incorrect |
|---------|-----------|
| **UiPath Cartographer** / **Cartographer** | cartographer, CartoGrapher |
| **Map of Work** | map of work, Map Of Work |
| **Process Atlas** | process atlas, ProcessAtlas |
| **Automation Hub** | automation hub, AutomationHub |
| **Agent Builder** | Agent builder, agent-builder |
| **Maestro** | maestro, Maestro™ |
| **IXP** (Intelligent eXtraction & Processing) | IXP (define on first use) |
| **Action Center** | action center, ActionCenter |
| **Studio Web** | studio web, Studio web |
| **Data Fabric** | data fabric |
| **Integration Service** | integration service |
| **Orchestrator** | orchestrator |

### Acronyms

Define on first use per page:

```markdown
**Process Definition Document (PDD)**
```

After the first mention, use just the acronym: PDD.

---

## Capitalisation

### Domain concepts

Capitalised mid-sentence nouns are acceptable when they match UI labels or are domain terms used consistently. Do not lowercase them:

- Map of Work, Transformation Decisions, Business Rules, Pain Points (when they match Cartographer page or panel names)
- AS-IS, TO-BE (always upper case, hyphenated)
- User decision, Approval mode (when referring to specific UI fields)

### Headings

- `# Title` and `## Section` — title case or sentence case, be consistent within a page
- `### N. Substep heading` — sentence case: "1. Create the agent and configure arguments"

---

## Content principles

### Don't remove explanatory content

Paragraphs that give context or motivation are not "filler." When reviewing or editing:

- Rephrase awkward sentences — don't delete the paragraph
- Preserve all technical explanations and background context
- Only remove genuinely redundant content (exact same paragraph verbatim in two places)

### Describing the same scenario in more than one place is acceptable

A concept may appear in the overview, be explained in a concept section, and then referenced in the steps. This is intentional reinforcement, not duplication.

### Don't over-stub

Only add `!!! note "Content migration in progress"` placeholder blocks when real source content exists but hasn't been transferred yet. Don't add stubs to sections that are intentionally left as future work by the author.

---

## Examples from real courses

### Good opening tip (Warranty Resolution at Cobalt Ridge Automation)

```markdown
!!! tip "Here is our plan for this exercise:"

    1. Create a **Cartographer** project, give it the business brief, and check what it already knows.
    2. Feed it the evidence a real team would have and review the current state (AS-IS) it builds.
    3. Design the future state (TO-BE), make a live edit, and verify it landed everywhere.
    4. Generate the **PDD**, trace your edits inside it, and publish it to **Automation Hub**.
```

### Good conversational transition (Warranty Resolution — "Make live edits and verify them")

> "The agent is probably halfway through a multi-step validation pass. There's no point waiting for a pass that's about to be outdated, so click **Steer** on the queued message to push your request in early."

### Good "why this matters" aside (Warranty Resolution — "Design the future state")

> "This is the artifact that answers the big question: does the tool tie changes to business value, or does it just redraw the diagram?"

### Good concise ending (Warranty Resolution — "Optional: ask a teammate")

The section ends with one short paragraph on what happens next: the colleague's answer lands back in your conversation, ready for you to accept. No summary paragraph needed — the result speaks for itself.

### Good framing of the business case (From Process to Production)

> "In most organizations, a process document is where the work stops being visible."
