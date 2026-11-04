# Review the SDD

!!! info "Before you begin: prerequisites"
    Have these ready **before** you start:

    - **The first exercise, finished:** your Cobalt Ridge project, with the PDD and the SDD published to Automation Hub.
    - **VS Code 1.110.0 or later** and **Node.js:** you'll install the UiPath Maestro extension on the next page.
    - **A coding agent:** this guide uses [**Claude Code**](https://docs.claude.com/en/docs/claude-code/overview).
    - **Access to the workshop environment:** in this workshop we use `{{ training_url }}/{{ training_tenant }}`. Talk to your trainer if you haven't received an invitation.

## 1. Open the SDD you generated

Go back to your Cobalt Ridge project in **Cartographer**. At the end of the first exercise, Cartographer turned your TO-BE into a Solution Design Document (SDD): a solution architecture on the UiPath Platform, built around **Maestro** case orchestration, with the **Maestro Flow** stages you chose and the AI agents, human-in-the-loop tasks and integrations your design calls for. Now it's time to check it before anything gets built.

1. Open **Solution design (SDD)** in the left navigation. Walk the table of contents: process overview, diagram, activities, gateways and events, data objects, integrated components, error handling, triggers, project structure, testing strategy and next steps.
2. Read the summary in the conversation. It lists the status, the template validation result, the architecture, what the SDD covers, the result of an independent review, and any open items. Open items are tagged **[SME REVIEW]** so you know exactly what still needs a human answer.

## 2. Mark it as reviewed and download it

1. Cartographer deliberately leaves the build hand-off open until you approve the design. Mark the SDD as **reviewed** in the document panel.
2. Click **Download** to save the SDD. You'll hand this file to the coding agent.

!!! note "No SDD, or yours is incomplete?"
    Download the example SDD from the Cobalt Ridge run and start from it. It's a Markdown file, ready for your coding agent, with both Maestro Flow stages included.

    [**Download the example SDD (.zip)**](dependencies/Cobalt-Ridge-Warranty-Resolution-SDD.zip){ .md-button download="Cobalt-Ridge-Warranty-Resolution-SDD.zip" }

!!! tip "Why this matters"
    The build never starts from an unreviewed design. A person signs off on the SDD before any coding agent touches it.

<div class="next-page" markdown>
[Next: Set up VS Code and the Maestro extension](set-up-vs-code.md){ .md-button .md-button--primary }
</div>
