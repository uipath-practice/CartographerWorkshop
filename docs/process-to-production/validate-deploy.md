# Validate, deploy and open it in Studio Web

Your Flow is on the canvas. Now you'll check it, run it, put it in **Orchestrator** and open it in **Studio Web**, where your team can review and own it.

## 1. Validate the Flow

1. With the `.flow` file open, run **Flow: Validate Flow** from the Command Palette (`Ctrl+Shift+V`, or `Cmd+Shift+V` on a Mac).
2. Open the **Problems** panel (**View > Problems**). Problems also appear there while you edit.
3. If anything is listed, ask your coding agent to fix it, for example:

    ```text
    Fix the validation problems in the .flow file.
    ```

Go on once validation shows no errors.

## 2. Run it and watch it work

1. Run the flow from the editor.
2. Follow the live debug view. It draws the execution as a flowchart and updates it as each node runs, so you can see which path your stage took and where a placeholder stopped it.

## 3. Package and deploy to Orchestrator

1. Run **UiPath: Switch Deploy Target** and choose the workshop folder your trainer gives you.
2. Run **UiPath: Package & Deploy**. The extension builds a `.uipx` solution package and uploads it to Orchestrator.

The deployment is activated automatically, so your process is ready to run as soon as the command finishes.

!!! note "Two steps instead of one"
    **UiPath: Package** and **UiPath: Deploy** run the same two steps separately, if you want to check the package before you upload it.

## 4. Find it in Orchestrator

1. Sign in at **[{{ training_url }}]({{ training_url }})** and open **Orchestrator** in the **{{ training_tenant }}** tenant.
2. Open the folder you deployed to. Your `{YourName}` process is listed under **Automations > Processes**.

## 5. Open it in Studio Web

To edit and review the Flow in the browser, upload the solution to **Studio Web**:

1. In the VS Code terminal, go to your **solution** folder, the one that holds the `.uipx` solution, not the project folder inside it.
2. Upload it:

    ```bash
    uip solution upload "<path to your solution folder>"
    ```

    If you upload the same solution again later, add `--force` to replace the earlier upload.

3. Open **Studio Web** from **[{{ training_url }}]({{ training_url }})** and find your `{YourName}` solution.
4. Open the Flow project. It's the same flow you built in VS Code, on the same canvas, ready for your team.

!!! tip "Why this matters"
    The SDD from Cartographer became a working Flow in Orchestrator, and the same Flow is open for review in Studio Web. Nobody retyped the design along the way.

<div class="next-page" markdown>
[Next: Close the loop](close-the-loop.md){ .md-button .md-button--primary }
</div>
