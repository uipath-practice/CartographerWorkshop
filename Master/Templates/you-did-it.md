# You did it!

!!! tip "Congratulations!"

    You've built a complete expense report processing automation — from receipt extraction through policy validation to human approval.

---

## What you built

The process is now complete: it extracts data from uploaded receipts, validates each item against company travel policy, routes flagged expenses to a manager for review, and pushes approved reports to the finance system. All orchestrated by Maestro.

| Component | Role |
|-----------|------|
| **IXP extraction** | Reads receipt data from uploaded expense report PDFs |
| **AI Agent** | Validates each line item against travel policy and spending history |
| **Human task** | Presents flagged items in Action Center for manager review |
| **API connector** | Pushes approved reports to the finance system via Integration Service |

This is a production-pattern process. The same design — Extraction → Agent → Human → API — applies to a wide range of document processing scenarios.

---

## Next steps

### 1. Publish and run your process

Publish to your **Personal Workspace** and run it like any other UiPath process — it triggers extraction, agent, and human tasks automatically, in the right sequence.

- Open your solution in **Studio Web**
- Publish to your **Personal Workspace**
- Trigger a run from **Orchestrator** or **Maestro**
- Watch the execution trace end-to-end from the **Maestro** dashboard:

![Maestro dashboard showing running process instances](you-did-it.images/maestro-dashboard.png){ .screenshot width="900" }

### 2. Explore Maestro analytics

After a few runs, head over to **Maestro** to explore execution details:

- Transaction-level execution details
- End-to-end process flow visualization
- Exception and escalation rates

![Maestro analytics heatmap](you-did-it.images/maestro-analytics.png){ .screenshot width="900" }

---

## Keep iterating

**Improve the agent prompt**

- The current prompt may miss edge cases — shared meal receipts split across attendees, for example.
- Modify the system prompt and re-test with the same receipts.
- Measure how the approval decision changes.

**Test the boundaries**

- Submit an expense right at the policy limit ($74.99 meal) and observe the decision.
- Submit a report with a missing receipt and check the escalation path.

**Expand the process**

- Add a second document type (e.g., mileage reimbursement forms).
- Introduce a VIP approval path for expenses over $1,000.
- Connect the rejection path to an automated notification email.

The skills you practiced here — document extraction, prompt engineering, agentic orchestration, human-in-the-loop design, API integration — are the building blocks of modern enterprise automation. Keep experimenting. Change the prompts. Break things. Fix them. That's how it sticks.

---

## Learn more

| Resource | Description |
|----------|-------------|
| UiPath Academy | Official learning paths for Agent Builder and Maestro |
| UiPath Documentation | API references, platform guides, release notes |
| UiPath Community | Forum for questions, shared automations, and tips |
