# Generate the SDD

## 1. Ask for the SDD

Once the PDD looks good, generate the Solution Design Document (SDD):

```text
Generate the SDD.
```

The first clarifying question asks how you want the generation itself to run, meaning how often it should pause for you along the way:

- **Autonomous** generates the full SDD and only interrupts for hard blockers.
- **Interactive** pauses at the summary, architecture and final SDD checkpoints instead.

Either is a valid choice. Interactive gives you more control points, and Autonomous trades them for speed.

![Clarifying question asking whether to run the SDD generation autonomously or interactively](index.images/sdd-generation-mode-W.png){ .screenshot width="900" }

![SDD clarifying questions answered in the conversation](index.images/sdd-clarifications-W.png){ .screenshot width="900" }

## 2. Bring in Maestro Flow while it runs

While the SDD is being generated, send this prompt and click **Steer** to push it in early:

```text
I would also like to orchestrate one of the stages using Maestro Flow. Which one would be better fitted?
```

![Maestro Flow question steered into the running SDD generation](index.images/sdd-steer-flow.png){ .screenshot width="700" }

Cartographer recommends the stages that fit **Maestro Flow** best and explains why. Choose the ones you prefer. For example:

```text
Update the SDD to USE Maestro Flow for both "Asset, Entitlement and Evidence Readiness" AND the cost-reconciliation
```

![Cartographer recommending stages for Maestro Flow, followed by the update request](index.images/flow-suggestions.png){ .screenshot width="700" }

## 3. Refine the SDD, or bring your own template

The SDD isn't final until it works for you. Read it, and ask for changes the same way you shaped the TO-BE. You can even hand Cartographer your own SDD template and ask it to follow that structure.

1. Download the example template, or use your own team's template:

    [**Download the SDD template (.docx)**](dependencies/SDD-Template.docx){ .md-button download="SDD-Template.docx" }

2. Attach the template and send:

    ```text
    Can we modify the SDD cause it's not very easy to read. Would you be able to follow the attached template?
    ```

3. Be specific about what's missing. For example:

    ```text
    The current SDD doesn't contain the diagram nor process overview, activities, artefacts (suggested projects, possible assets and storage buckets), integrated components, error handling, triggers, project structure, testing strategy and next steps. I would expect to see the 2 Flow processes detailed here too
    ```

## 4. Publish the PDD and SDD

1. Choose to publish both documents to **Automation Hub** if you're prompted. If you aren't, ask Cartographer to do it, for example:

    ```text
    upload the PDD and SDD to Automation Hub
    ```

    ![Cartographer publishing the PDD and SDD to Automation Hub](index.images/publish-pdd-and-sdd-W.png){ .screenshot width="900" }

2. Cartographer verifies the upload and gives you links to the new entry in Automation Hub. The confirmation lists the process ID and the document IDs for the PDD and the SDD, and offers two follow-ups: **Show me the published Automation Hub record** and **Download the published PDD and SDD**.

    ![Confirmation listing the Automation Hub process ID and the PDD and SDD document IDs](index.images/automation-hub-published-ids.png){ .screenshot width="700" }

    ![The new Cobalt Ridge Warranty Resolution entry in Automation Hub](index.images/automation-hub-entry-W.png){ .screenshot width="900" }

<div class="next-page" markdown>
[Next: Ask a teammate (optional)](ask-a-teammate.md){ .md-button .md-button--primary }
</div>
