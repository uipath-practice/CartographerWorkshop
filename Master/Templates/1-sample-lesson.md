# Building the Expense Policy Agent

!!! tip "Here is our plan for this lesson:"

    1. Create a new AI Agent in **Studio Web** and configure its input/output arguments
    2. Write system and user prompts, then add Context Grounding for policy rules
    3. Add an RPA tool for retrieving employee spending history
    4. Integrate the agent into the Maestro workflow and test the decision gateway

## Goal

Create the **Expense Policy Agent** with two tools: an IXP extraction tool for receipt data and an RPA workflow that queries employee spending history. The agent receives extracted expense data, validates each line item against company policy, and returns an approval decision with supporting details.

## Why Use an AI Agent for Policy Validation

Expense policy rules sound simple on paper — "meals under $75, flights in economy class" — but real receipts are messy. Descriptions vary ("business dinner" vs "client meal vs "team lunch"), currency conversions add ambiguity, and edge cases pile up fast.

Traditional rule-based code becomes brittle when handling these variations. Every new edge case means another if-statement, another maintenance burden.

LLMs handle this naturally. They understand that "team dinner at Ristorante Milano" is a meal expense, even if the receipt doesn't say "meal." Combined with structured policy context, the agent makes consistent decisions while handling the fuzzy reality of expense reports.

[[[
Here is the structure of the agent's inputs and outputs, as well as Tools that the agent will use:
|30|
![Agent structure diagram showing inputs, outputs, and tools](configure-agent.images/1-agent-structure.png){ .screenshot }
]]]

## Steps

### 1. Create the agent and configure arguments

[[[
In **Studio Web**, add a new Agent to your solution. Name it:
```text
Expense Policy Agent
```
|30|
![New agent created in Studio Web](configure-agent.images/2-create-agent.png){ .screenshot }
]]]

[[[
Open the **Data Manager** panel. Add the following **Input Argument** (type: String):

```css hl_lines="1"
in_ExpenseReportJSON
```
```text
JSON string containing extracted expense report data from IXP
```

For Output arguments, switch to **Editor mode** and paste the JSON schema:
|50|
![Input argument configured in Data Manager](configure-agent.images/3-arguments-input.png){ .screenshot }
]]]

[[[
![Output arguments in JSON editor mode](configure-agent.images/4-arguments-output.png){ .screenshot }
|30|
**Output** JSON schema:
```json
{
  "type": "object",
  "required": ["out_Status"],
  "properties": {
    "out_Status": {
      "type": "string",
      "description": "Approval status: 'Approved', 'Flagged', or 'Rejected'"
    },
    "out_PolicyViolations": {
      "type": "string",
      "description": "HTML summary of policy violations found, if any"
    },
    "out_TotalAmount": {
      "type": "number",
      "description": "Total expense amount in USD"
    }
  },
  "title": "Outputs"
}
```
]]]

### 2. Configure the prompts

[[[
Prompts are configured in the Agent's settings (click the wrench icon).

- **System prompt** defines the agent's role and rules — the "How."
- **User Prompt** is the specific input for each run — the "What."
|30|
![Agent settings showing prompt configuration](configure-agent.images/5-prompts.png){ .screenshot }
]]]

[[[
Enter the following **System Prompt**:
|50|

]]]

```cpp
You are an Expense Policy Validation Agent. Your responsibilities:

1. Analyze expense report data extracted from receipts using IXP.

2. Validate each line item against company travel policy:
   - Meals: maximum $75 per person per meal
   - Transportation: economy class only for flights under 6 hours
   - Lodging: maximum $250 per night in standard cities, $350 in high-cost cities
   - Miscellaneous: items over $50 require a receipt and justification

3. Check the employee's spending history using the History Lookup tool to identify patterns.

4. Provide a clear decision:
   out_Status: "Approved" if all items comply, "Flagged" if minor issues found, "Rejected" if major violations detected.
   out_PolicyViolations: HTML table listing each violation with the item, policy limit, actual amount, and recommendation.

Always double-check amounts and policy thresholds before finalizing.
```

[[[
Enter the following **User Prompt**:
|30|
```text
Review this expense report: {{in_ExpenseReportJSON}}
```
]]]

### 3. Add Context Grounding and tools

Context Grounding provides the agent with structured policy data — the approved spending limits, category definitions, and high-cost city list. Without it, the agent would hallucinate policy rules.

[[[
Click **Add context** in the Contexts section. Select **Company Travel Policy** from the available resources.

Add this description:
```text
Use this context to validate expense items against company travel and spending policy rules
```
|30|
![Selecting context source in Agent Builder](configure-agent.images/6-add-context.png){ .screenshot }
]]]

Next, add the **Employee History Lookup** tool as an RPA workflow. This tool queries past expenses to detect patterns like repeated near-limit claims.

[[[
Import the **Employee History Lookup** automation into your solution.

Click the **+** button in the Explorer and choose **Import existing**.
|50|
![Importing existing project into solution](configure-agent.images/7-import-project.png){ .screenshot }
]]]

Configure the tool's argument descriptions:

```css hl_lines="1"
in_EmployeeID
```
```text
Employee ID from the expense report header
```

```css hl_lines="1"
in_LookbackDays
```
```text
Number of days to look back for spending history (default: 90)
```

![History lookup tool configured with arguments](configure-agent.images/8-tool-configured.png){ .screenshot }

!!! warning "This simplified lookup has no error handling"
    In production, add retry logic and handle cases where the employee ID doesn't exist in the system.

### 4. Update the prompt for tools

??? tip "Review the changes"
    Here are the changes to reflect the new context and tool:
    ```diff 

    --- Original
    +++ With Context and History Tool

     1. Analyze expense report data extracted from receipts using IXP.

    -2. Validate each line item against company travel policy:
    +2. Validate each line item against company travel policy from the Travel Policy Context:
        - Meals: maximum $75 per person per meal
        ...

    -3. Check the employee's spending history using the History Lookup tool to identify patterns.
    +3. Check the employee's spending history by calling Employee History Lookup automation. Flag if total spending in the lookback period exceeds $5,000.

    ```

```cpp hl_lines="4 8" title="Update the System Prompt to reference context and tool:"
You are an Expense Policy Validation Agent. Your responsibilities:

1. Analyze expense report data extracted from receipts using IXP.

2. Validate each line item against company travel policy from the Travel Policy Context:
   - Meals: maximum $75 per person per meal
   - Transportation: economy class only for flights under 6 hours
   - Lodging: maximum $250 per night in standard cities, $350 in high-cost cities
   - Miscellaneous: items over $50 require a receipt and justification

3. Check the employee's spending history by calling Employee History Lookup automation. Flag if total spending in the lookback period exceeds $5,000.

4. Provide a clear decision:
   out_Status: "Approved" if all items comply, "Flagged" if minor issues found, "Rejected" if major violations detected.
   out_PolicyViolations: HTML table listing each violation with the item, policy limit, actual amount, and recommendation.

Always double-check amounts and policy thresholds before finalizing.
```

### 5. Integrate the agent into Maestro

[[[
In **Studio Web**, return to your **Maestro Agentic Process**. Configure the second task: set the action to **Start and wait for agent**, then select the agent from your solution.
|30|
![Agent task configured in Maestro](configure-agent.images/9-add-agent.png){ .screenshot }
]]]

Map the outputs from the previous IXP extraction task as inputs to the Agent:

![Input mapping from extraction output to agent input](configure-agent.images/10-agent-arguments.png){ .screenshot }

Configure the **Exclusive Gateway** using the agent's status output. Set **Flagged** as the default path (routes to human review):

```css
vars.outStatus.ToLower()=="approved"
```

![Gateway configuration with expression](configure-agent.images/11-exclusive-gateway.png){ .screenshot }

### 6. Test the workflow

Click **Debug** and monitor the execution. The agent should:
1. Receive the extracted expense data
2. Query the policy context
3. Call the history lookup tool
4. Return a status and any violations

![Process debug run showing agent execution](configure-agent.images/12-test-run-W.png){ .screenshot width="900" }

Review the **Execution Trace** to verify each step. If the status routes correctly through the gateway, your agent is working.

![Execution audit showing gateway routing](configure-agent.images/13-execution-audit-W.png){ .screenshot width="900" }

!!! tip "Validate the gateway routes correctly"
    Run a few times with different expense amounts. Verify that expenses under policy limits get "Approved" and route to the finance connector, while over-limit items get "Flagged" and route to human review.
