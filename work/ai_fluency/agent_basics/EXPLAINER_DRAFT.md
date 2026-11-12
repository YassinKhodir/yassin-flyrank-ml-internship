# Workflows, agents and connectors: study draft

AI-assisted FL-05 learning draft, November 12, 2026. Not submitted.
This is written by ChatGPT/Codex for Yassin to study and rewrite. It is not presented as the student's own words or proof that the student has read the linked articles.

## Explanation

A workflow is a set of steps chosen ahead of time. Our study-notes plan has four: gather facts, draft an explanation, check the claims, then format a study card. Each step has a clear output for the next step. This makes the path easier to inspect. A person still supplies the source and checks the final card. The saved examples show the assistant following those stages. They do not prove an unattended application is running.

An agent gives the model more control over the next step. Instead of always moving down the same list, the model may decide it needs another search, use a tool, read the result, then decide what to do next. Anthropic distinguishes a fixed workflow from a model that directs its own process and tool use. More independence does not automatically make a system better. A predictable task may be easier to handle with a fixed path. [1]

The study-card pipeline is currently a workflow draft. It does not search GitHub by itself. Its instructions tell the assistant how to process a source that has already been supplied. Repeating four prompts is not enough to call it an autonomous agent. Also, drafting a card and checking that same card with the same assistant is not an independent review.

MCP means Model Context Protocol. It is a shared way for an AI application to connect to outside systems. The AI application is the host. A client inside that application communicates with a server that exposes capabilities. The server might provide access to files or another service. MCP is the connection method; it does not itself decide the goal or guarantee a correct answer. [2][3]

Three important server capabilities are tools, resources and prompts. A tool is an operation the model can request, such as fetching a repository file. A resource provides information for context, such as document content. A prompt is a reusable instruction template. These are different roles. Not every file returned by a tool is automatically an MCP resource, and not every saved instruction file is automatically a server-provided prompt. [3]

The GitHub connector gives a concrete example. In this work, the assistant fetched the saved evaluation from the actual repository, updated its stale demo status, then fetched the changed file again. The service returned the file content and its revision identifier. Plain chat without an external connection could draft a replacement paragraph, but could not verify the current repository or save a real commit. The connector was already connected; no new server installation is claimed.

This also shows why the evidence matters. Saying “I updated the file” is only a claim. A successful update response and a later read of the changed content support it. A browser screenshot of the finished GitHub page shows the result, but does not by itself show the connector call. The FL-05 brief asks for screenshots of three tasks making tool calls, so those captures remain a separate evidence requirement.

One possible agent upgrade is a read-only source finder for the study-card workflow. It could use the GitHub connector to fetch a named public file, inspect its status sections, and decide whether one more permitted file is needed to resolve a conflict. For example, an evaluation might still say the demo is missing while a newer README links the submitted demo. The agent should compare dated evidence or ask for clarification, not silently choose the easier story.

That upgrade should have limits: one repository, an allowed folder, a small tool-call limit, and no automatic publishing or email. Source text should be treated as evidence, not permission to change the task. The agent should stop when support is missing and return the unresolved question. Those are proposed controls, not features already built. Human review still matters before using the card or submitting an assignment. The remaining work is to try the accepted setup, capture the real calls, and explain the difference in the student's own words.

## Sources read for this draft
1. Anthropic, Building effective agents: https://www.anthropic.com/research/building-effective-agents
2. MCP introduction: https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro
3. MCP server concepts: https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts

Repository evidence: ../workflow/README.md and ../study_coach/EVALUATION.md.
The draft distinguishes the prepared FL-04 workflow from a finished deployed application.
