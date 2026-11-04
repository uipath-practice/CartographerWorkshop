# Build your Flow with a coding agent

In the first exercise, you asked Cartographer to run two stages of the Cobalt Ridge case with **Maestro Flow**. Now you'll pick one of them and have your coding agent build it, straight from the SDD.

## 1. Create the Maestro project

1. Create an empty folder for your work, for example `{YourName}-CobaltFlow`, and open it in VS Code (**File > Open Folder**).
2. Click the **UiPath** icon in the Activity Bar. In the **UiPath Maestro** view, click **Create New** and choose **Maestro Orchestrate** from the **New Project** list.
3. Name the solution and the project with your name as a prefix, for example `{YourName}_CobaltFlow`.

The extension creates the solution, the project and a default `.flow` file, and opens the empty flow on the canvas.

!!! tip "Why the name prefix?"
    Everyone in the workshop builds in the same tenant. A `{YourName}` prefix keeps your solutions, processes and connections from colliding with your neighbour's.

## 2. Add the SDD to the folder

Copy the SDD you downloaded in [Review the SDD](review-the-sdd.md) into the folder you just opened, or unzip the example SDD there. Your coding agent reads it from there.

## 3. Pick your stage

Choose one of the two stages you assigned to **Maestro Flow** in the first exercise:

- **Asset, Entitlement and Evidence Readiness** (*Warranty Asset and Evidence Readiness Flow* in the SDD): resolves the asset, verifies the entitlement, retrieves the evidence and scores readiness before coverage is decided.
- **Cost reconciliation** (*Warranty Cost Reconciliation Flow* in the SDD): assembles the actual costs, posts and reconciles them, calculates the variance and routes anything above 20% to Finance for verification.

## 4. Ask your coding agent to build it

Send the prompt for your stage to your coding agent, then replace `{YourName}` with your name:

=== "Asset, Entitlement and Evidence Readiness"

    ```text
    Read the SDD file in this folder for the Cobalt Ridge warranty resolution process. Build only the Maestro Flow for the "Asset, Entitlement and Evidence Readiness" stage, in this project's .flow file, following that stage's section of the SDD. If an Integration Service connection or another resource the flow needs doesn't exist in my tenant, use a placeholder node and list what's missing at the end. Prefix the name of every artifact you create with {YourName}.
    ```

=== "Cost reconciliation"

    ```text
    Read the SDD file in this folder for the Cobalt Ridge warranty resolution process. Build only the Maestro Flow for the cost reconciliation stage, in this project's .flow file, following that stage's section of the SDD. If an Integration Service connection or another resource the flow needs doesn't exist in my tenant, use a placeholder node and list what's missing at the end. Prefix the name of every artifact you create with {YourName}.
    ```

The agent loads the **UiPath skills** for Maestro Flow, reads the SDD and looks up the nodes, connectors and resources available in your tenant. Then it builds the flow.

1. Keep the `.flow` file open. You can watch the nodes appear on the canvas as the agent adds them.
2. Answer the agent's questions as they come up, and approve commands as it runs them.
3. When it's done, read its summary, especially the list of placeholders and anything missing from the tenant.

!!! note "Placeholders are expected"
    The SDD names systems such as SAP S/4HANA and FieldLink. The workshop tenant doesn't have connections to all of them, so some steps stay as placeholders. That's fine: the structure of the stage, its decisions and its handoffs are what you're building today.

## 5. Make it yours

The canvas works like the one in Studio Web. Select a node to check its configuration and variables, and adjust anything the agent got wrong, either by hand or by asking the agent. For example, ask it to rename a node or to add a missing decision from the SDD.

<div class="next-page" markdown>
[Next: Validate, deploy and open it in Studio Web](validate-deploy.md){ .md-button .md-button--primary }
</div>
