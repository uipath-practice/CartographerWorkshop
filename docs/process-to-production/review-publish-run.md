# Review, publish and run it

## 1. Review what was built in Studio Web

Open **Studio Web** and find your solution. You should recognise the TO-BE you designed in Cartographer, now executable:

- The **Maestro** process, with its stages, decisions and handoffs.
- The **AI agents**, each with a system prompt that describes its role. Open one and check that it matches the role in your design. The variance agent from the first exercise is a good one to look at.
- The **human-in-the-loop** tasks, such as the high-variance verification you added live.
- Any **RPA** workflows or integrations behind the system tasks.

Check that **Validation issues** shows zero before you go any further.

## 2. Publish the process and the solution

Publishing puts each piece where it belongs:

| What | Where it goes |
| :--- | :--- |
| **Process documentation and map** | **Process Repository** in Automation Hub, linked to the Map of Work |
| **Solution** | **Studio Web** |
| **Deployment** | **Orchestrator** and **Maestro** |

Open your Cobalt Ridge entry in Automation Hub. Under **Documentation**, the process map now sits next to your PDD and SDD, not in a slide or an email. Open the map to see the model the solution runs.

## 3. Run it and watch it work

1. Start a test run of the process in Maestro and follow the instance as it moves through the stages.
2. Open **Action Center** when a human task comes up, and complete it.

!!! tip "Going further"
    Your coding agent can build more than the process. Ask it for a simple warranty desk for the Cobalt Ridge operations team: one screen with every case, its status and its handoffs, built on the same solution.

<div class="next-page" markdown>
[Next: Close the loop](close-the-loop.md){ .md-button .md-button--primary }
</div>
