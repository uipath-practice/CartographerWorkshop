# Expense Report Processing

**Automate expense report review using IXP extraction, an AI Agent for policy validation, and human approval in Action Center.**

## Overview

**UiPath Maestro** orchestrates the end-to-end expense review process — from document intake through AI-powered policy checks to human approval for flagged items. This exercise uses **IXP** (Intelligent eXtraction & Processing) to extract structured data from uploaded receipts, then an AI Agent to validate each line item against company travel policy.

!!! info "Before you begin: prerequisites"
    Have these ready **before** the session:

    - **Prerequisite one** — brief explanation.
    - **Prerequisite two** — brief explanation.
    - **A UiPath Cloud account**. In this workshop we will use: `{{ training_url }}/{{ training_tenant }}`. Talk to your trainer if you are not invited.

| Step | Focus |
| ---: | :--- |
| [**Configure Document Extraction**](1-configure-extraction.md) | Set up IXP to extract receipt data from uploaded expense reports |
| [**Build the Policy Agent**](2-build-policy-agent.md) | Create an AI Agent that validates expenses against company policy rules |
| [**Configure Human Approval**](3-configure-approval.md) | Route flagged expenses to a manager in Action Center for review |
| [**Connect to Finance System**](4-connect-finance.md) | Push approved reports to the finance system via Integration Service |

!!! tip "Training Environment"
    Log in at **[{{ training_url }}]({{ training_url }})** and remember using tenant **{{ training_tenant }}** for this exercise.
