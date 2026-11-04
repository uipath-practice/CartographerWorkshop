# Optional: build the whole case

You built one stage. If you're ahead of the clock, or you want to try the full path after the workshop, a coding agent can build the whole Cobalt Ridge case from the same SDD. This page gives you the pointers. It isn't a step-by-step exercise.

## The skills involved

The `uip skills install` command you ran earlier already installed these **UiPath skills**. Your coding agent loads them on its own when the task calls for them:

| Skill | What it does |
| :--- | :--- |
| `uipath-planner` | Reads the SDD and turns it into a design and a list of build tasks across UiPath products. |
| `uipath-maestro-case` | Builds the **Maestro** case plan (`caseplan.case`) and resolves the tenant resources it needs. |
| `uipath-maestro-flow` | Builds the Flow stages, the same skill you used in this exercise. |
| `uipath-solution` | Packs, publishes and deploys the solution. |

## How to start

1. Create a new empty folder, open it in VS Code and copy the SDD into it.
2. Ask your coding agent, for example:

    ```text
    Create a uipath maestro case project using the SDD file in this folder. Prefix the name of every artifact you create with {YourName}.
    ```

3. Let it plan first. Read the task list it derives from the SDD before it starts building, and answer its questions.

## Tips

- **Give it time.** A whole case has many stages, agents, human tasks and connections. Expect a long run with many tool calls.
- **Reuse your Flow.** Tell the agent about the Flow you already built, so it links that stage instead of building it again.
- **Review in Studio Web.** The VS Code extension shows Flow on a canvas. Review the case plan in Studio Web after you upload or deploy the solution.
- **Expect gaps.** As with your Flow, connections that don't exist in the tenant become placeholders or questions. Check the agent's list of what's missing.
- **Watch your usage.** A full build consumes far more of your AI usage allowance than a single Flow.

<div class="next-page" markdown>
[Next: Next steps](../next-steps.md){ .md-button .md-button--primary }
</div>
