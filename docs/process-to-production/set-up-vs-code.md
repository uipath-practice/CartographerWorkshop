# Set up VS Code and the Maestro extension

You'll build your Flow in **Visual Studio Code** with the **UiPath Maestro** extension and a coding agent. This page gets all three ready and signed in to the workshop tenant.

## 1. Install VS Code and Node.js

1. Install **VS Code** version **1.110.0 or later** from [code.visualstudio.com](https://code.visualstudio.com/). If it's already installed, check your version under **Help > About** and update if needed.
2. Install **Node.js** (the LTS version) from [nodejs.org](https://nodejs.org/). npm comes with it, and the extension uses npm to install the **`uip` CLI**. Keep the installer's **Add to PATH** option selected.
3. Close VS Code completely and open it again. Its terminal doesn't see newly installed programs until VS Code restarts.
4. Open a terminal in VS Code (**Terminal > New Terminal**) and check both versions:

    ```bash
    node --version
    npm --version
    ```

    Each command prints a version number. If you get "not recognized" or "command not found", run the Node.js installer again with **Add to PATH** selected, then restart VS Code.

!!! note "Remote workspaces"
    If you work in WSL, over SSH, in Codespaces or in a dev container, install Node.js and npm on the remote host, not on your local machine.

## 2. Install the UiPath Maestro extension

The extension is published by UiPath on the **Visual Studio Marketplace**. You can install it from inside VS Code:

1. In VS Code, open the **Extensions** view (`Ctrl+Shift+X`, or `Cmd+Shift+X` on a Mac).
2. Search for **UiPath Maestro**.
3. Check that the publisher is **UiPath** and the extension ID is `uipath.uipath-maestro`, then click **Install**.
4. Reload VS Code if it asks you to.

You can also open the [extension page on the Marketplace](https://marketplace.visualstudio.com/items?itemName=uipath.uipath-maestro) and click **Install** there. When the install finishes, a **UiPath** icon appears in the Activity Bar on the left.

## 3. Sign in to the workshop tenant

1. Click the **UiPath** icon in the Activity Bar.
2. In the **Connect** section, click **Sign In**.
3. If the extension offers to install the CLI, accept. It runs `npm install -g @uipath/cli` for you.
4. Finish the sign-in in the browser window that opens. The sign-in returns to VS Code through `localhost` port 8104, so keep that port free.
5. Open the Command Palette (`Ctrl+Shift+P`, or `Cmd+Shift+P` on a Mac) and run **UiPath: Select Environment**. Keep **Cloud**.
6. Run **UiPath: Select Tenant** and pick **{{ training_tenant }}**.

### Check that the CLI is installed

The extension's **Get started** page shows a checklist at the top: **Signed in**, **CLI installed** with its version, and **AI skills**. You can also check in the terminal:

```bash
uip --version
```

If it prints a version, you're set. If you get "not recognized" or "command not found", the extension didn't install it. Install it yourself, then restart VS Code:

```bash
npm install -g @uipath/cli
```

## 4. Get your coding agent ready

The coding agent needs the **`uip` CLI** signed in to the same tenant as the extension, plus the **UiPath skills** that teach it how to build on UiPath.

1. In the VS Code terminal (**Terminal > New Terminal**), check the CLI session:

    ```bash
    uip login status
    ```

    If it isn't signed in to **{{ training_tenant }}**, sign in:

    ```bash
    uip login --authority {{ training_authority }} -t {{ training_tenant }}
    ```

2. Check the CLI tools. The CLI works through tools, one per product area. List them:

    ```bash
    uip tools list --output table
    ```

    For this exercise you need **maestro-tool** and **solution-tool**, plus **orchestrator-tool** and **integrationservice-tool** for the deploy and the connections. Install any that are missing, one at a time:

    ```bash
    uip tools install maestro
    uip tools install solution
    uip tools install orchestrator
    uip tools install integrationservice
    ```

    If any of them shows **needs update**, run `uip tools update`.

3. Install the **UiPath skills** for your coding agent. This example is for Claude Code; for another agent, change the `--agent` value (for example `cursor`, `copilot` or `codex`):

    ```bash
    uip skills install --agent claude
    ```

4. Open your coding agent. This guide uses [**Claude Code**](https://docs.claude.com/en/docs/claude-code/overview), either through its VS Code extension or by running `claude` in the VS Code terminal.

!!! info "Sessions, identity, and security"
    The agent uses your session and acts with your permissions. Approve its `uip` commands one by one as they come up, rather than allowing all of them at once.

<div class="next-page" markdown>
[Next: Build your Flow with a coding agent](build-with-a-coding-agent.md){ .md-button .md-button--primary }
</div>
