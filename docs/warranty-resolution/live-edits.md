# Make live edits and verify them

## 1. Make the agentic edit, and use Steer

1. In the [future-state design (TO-BE)](index.images/to-be-diagram.png){ .lightbox }, find the finance human task **Post and reconcile cost**. Send:

    ```text
    "Post and reconcile cost" is listed as a human task. Change this to be conducted by an agent with human verification when variance exceeds 25% of total cost.
    ```

    ![Prompt changing Post and reconcile cost to an agent with human verification](index.images/post-and-reconcile-cost-W.png){ .screenshot width="900" }

2. Before the agent finishes thinking, change the threshold. Send:

    ```text
    actually when variance exceeds 20%
    ```

    The agent is probably halfway through a multi-step validation pass. There's no point waiting for a pass that's about to be outdated, so click **Steer** on the queued message to push your request in early.

3. The request is accepted as a refinement. The agent updates the future case design, the business rules, the agentic task list and the transformation list. Then a second agent runs an independent review of the first one's work.

!!! tip "Compliance guardrails"
    Every request is checked against known compliance rules, from regulators or from the company. If a change broke one, for example *no agent may approve any variance*, Cartographer would refuse it and explain why.

## 2. Verify the change landed everywhere

Run three checks:

1. **The TO-BE diagram.** Find the **Cost closure and quality** stage. **Post and reconcile cost** now carries an **AI agent** tag, followed by **Verify Variance** as a human action for variances over 20%. Check that nothing else in the process moved.

    [![TO-BE case map with Post and reconcile cost as an AI agent task followed by Verify variance](index.images/to-be-diagram-variance-W.png){ .screenshot width="900" }](index.images/to-be-diagram-variance-W.png){ .lightbox }

2. **Business Rules in the wiki.** The new business rule is there, and it's confirmed.

    ![Business Rules page in the wiki listing the confirmed rules](index.images/business-rules-W.png){ .screenshot width="900" }

3. **Transformation Decisions.** Your change is correctly *absent*. It was your explicit instruction, not a transformation the agent proposed.

<div class="next-page" markdown>
[Next: Generate and trace the PDD](generate-pdd.md){ .md-button .md-button--primary }
</div>
