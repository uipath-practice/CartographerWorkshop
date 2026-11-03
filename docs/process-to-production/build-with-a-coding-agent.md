# Build it with a coding agent

## 1. Get your coding agent ready

Your coding agent needs two things to build on UiPath: the **`uip` CLI** to talk to the platform, and the **UiPath skills** to know how to use it.

1. Install the CLI. This gives you the `uip` command:

    ```bash
    npm install -g @uipath/cli
    ```

2. Sign in to the workshop environment. Your coding agent reuses this session, so it acts as you on the platform:

    ```bash
    uip login --authority {{ training_authority }} -t {{ training_tenant }}
    ```

3. Install the UiPath skills for Claude Code:

    ```bash
    uip skills install --agent claude
    ```

4. Check the setup:

    ```bash
    uip login status
    uip skills list
    ```

!!! info "Sessions, identity, and security"
    The agent inherits your session and acts with your permissions. Avoid approving a blanket rule for every `uip` command, since that also covers destructive ones. Approve read and list commands as they come up instead.

## 2. Hand the SDD to the coding agent

1. Create an empty folder for the solution, for example `CobaltWarrantySolution`, and open it in Claude Code.
2. Attach the SDD you downloaded and send:

    ```text
    Here you have the SDD of the automation solution we have to build for the warranty resolution process at Cobalt Ridge Automation. Build, implement and then test the uipath solution according to the SDD and then publish it on Orchestrator. Prefix the name of every artifact you create with {YourName}.
    ```

3. Watch how it starts. The agent reads the SDD and loads the **UiPath planner** skill, which handles SDD-driven builds. The SDD carries a planner hand-off marker, so the agent knows which build path to follow. It then checks your tenant login and any existing project folder, and looks up the **Integration Service** connections it will need, before it derives the build tasks.
4. Answer its questions as they come up, and approve commands as it runs them.

!!! tip "Why the name prefix?"
    Everyone in the workshop builds in the same tenant. A `{YourName}` prefix keeps your packages, processes and agents from colliding with your neighbour's.

<div class="next-page" markdown>
[Next: Review, publish and run it](review-publish-run.md){ .md-button .md-button--primary }
</div>
