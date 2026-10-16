# UiPath Cartographer Tech Workshop

**Design a real business process with UiPath Cartographer, from raw discovery evidence to a reviewed PDD, and see how that design carries on all the way to production.**

!!! tip "Training Environment"
    Log in at **[{{ training_url }}]({{ training_url }})** using tenant **{{ training_tenant }}**.

## What you'll build

**Cartographer** is UiPath's agentic process-design tool. You give it a brief and the evidence a team already has, and it maps the current state, designs the future state, and writes the documentation. It asks only about real gaps, recommends an answer, and leaves the decision to you. Every fact it captures is traced back to its source.

The workshop has two exercises. The first one is fully hands-on. The second one picks up where the first leaves off.

[**Warranty Resolution at Cobalt Ridge Automation**](warranty-resolution/index.md) — Cobalt Ridge Automation handles about 7,400 warranty claims a year. A claim takes 11.4 days to resolve, and a P1 line outage keeps a customer's production down for 96 hours. Your brief: get resolution down to 3.5 days and P1 downtime down to 24 hours. You'll take the process from a blank project to a published **Process Definition Document (PDD)**. Along the way you'll build a current-state wiki with provenance on every fact, choose how to map today's process, design a future state where every change is argued against a KPI, make live edits that stay inside compliance guardrails, and publish the PDD to **Automation Hub**.

[**From Process to Production**](process-to-production/index.md) — The PDD isn't the end of the story. This exercise follows the design downstream: Cartographer turns it into a **Solution Design Document (SDD)**, a coding agent such as **Claude Code** builds and tests the solution with the **UiPath skills**, and the result runs in **Maestro** and **Orchestrator**. Runtime insights then flow back into the Map of Work, so the design keeps improving.
## Key concepts

- **UiPath Cartographer** — discovers how work really happens, then makes it ready to build. A guided, AI-powered discovery conversation turns scattered process knowledge into one living definition of how the work runs. It starts with context, asks only what's missing, reconciles your evidence and routes questions to the experts who know.
- **Map of Work** — the source of truth: one living, customer-owned definition of how the work actually runs, stored in your tenant. It holds the people, stages, systems and data, rules, exceptions, judgment and goals. Every Map of Work is versioned, has a named owner and approver, carries provenance on every fact, and uses an open, portable format, the Open Knowledge Format (OKF).
- **Process Atlas** — UiPath's library of curated, expert-attested Maps of Work for verticalized processes, organized by industry, process area and process. It covers industries such as banking, insurance, healthcare, manufacturing, telecom and utilities. You adapt a proven map instead of drawing from a blank page, and every map improves with expert reviews and live deployments.
- **Provenance** — every fact in the Map of Work is attributable. Each element carries its source and its verifier, and contradictions between sources are resolved, not averaged.
- **AS-IS and TO-BE** — the process as it really runs today, grounded in your evidence and your experts, and the agreed future process you design against your KPIs and objectives.
- **Process Definition Document (PDD)** — generated from the Map of Work for decision-makers. It describes what the process does, why, and the value it delivers.
- **Solution Design Document (SDD)** — generated from the Map of Work for developers and coding agents. It describes how to build the solution on the UiPath Platform.
- **Best-fit canvas** — Cartographer's recommendation of the **Maestro** canvas that suits the work best: Case, BPMN or Flow, with the reasoning behind it.
- **Automation Hub** — the UiPath process repository, where the PDD, the process map and the solution live together.
