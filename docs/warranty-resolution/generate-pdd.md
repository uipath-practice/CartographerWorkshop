# Generate the PDD and trace it

## 1. Generate and download the PDD

1. Ask for the process document. Wait for it to generate and for the independent review to finish.

    ![Cartographer generating the PDD](index.images/generate-pdd-W.png){ .screenshot width="900" }

2. Download it as Word and open it.

    ![Downloading the generated PDD as a Word document](index.images/download-pdd-W.png){ .screenshot width="900" }

The document opens with the problem statement and the objectives the project was given. You'll spot two objectives that were added mid-session: the 20% variance rule was taken up as an objective in its own right. Then come the expected value, acceptance targets, scope boundaries, the current flow with its metrics, and the impact of each pain point.

![PDD in Word showing the problem statement and objectives](index.images/pdd-problem-statement-W.png){ .screenshot width="900" }

## 2. Trace your own edits in the PDD

1. Scroll to the target flow and the **What Changes AS-IS to TO-BE** table.

    Every task in every stage has a type. That's the to-do list for the SDD. The What Changes table ties each change to the goal it serves and the metric it moves.

    ![PDD target flow table for the cost reconciliation stage](index.images/pdd-target-flow-W.png){ .screenshot width="900" }

2. Keep scrolling. You'll find the business rules (including the one you added live), the data model entities, a data dictionary lifted from the claim form, integrations, RACI, exceptions, human-in-the-loop and **Action Center** tasks, the compliance and regulatory matrix, and the KPI acceptance criteria.
3. Find both of your edits: the 20% variance rule, and the task you expanded earlier.

!!! tip "Why this matters"
    The PDD carries everything an SDD needs, each item traced back to the evidence and to the KPI it moves. That's what you'll build the SDD from next.

<div class="next-page" markdown>
[Next: Generate the SDD](generate-sdd.md){ .md-button .md-button--primary }
</div>
