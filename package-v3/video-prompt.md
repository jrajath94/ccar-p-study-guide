# Claude Certified Architect, Professional. Video prompt for Muse

Format: numbered scenes. Each scene has a visual and a narration. Use a pitch-black background, one sans-serif typeface, white outlined shapes, and colored text only for the four roles. Use no logo, no watermark, no stock footage, no human presenter, and no on-screen credit.

Scene count: 43. Target length per scene: 20 to 30 seconds.

## Scene 1. Opening

Visual. Black screen. White title text with the course name. Four colored words appear: Key fact in blue, Decision rule in green, Exam tip in purple, Trap in red.

Narration. This course teaches one decision at a time. Watch for four colors. Blue is a key fact. Green is a decision rule. Purple is an exam tip. Red is a trap.

## Scene 2. F1 Architecture and business foundations

Visual. Black background. Draw a line diagram with white outlined boxes for: Your app, Messages API, Usage fields per response, Price per million tokens by class, Cost per request, Monthly invoice or Console report. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Architecture and business foundations. Each token class has its own price, so the cost of a request is the sum of its classes. Multiply each token class by its own rate, add the classes, then multiply by the request volume. The trap: A flat estimate that counts input tokens only looks simple, but output tokens cost more, so the estimate understates the bill.

## Scene 3. F2 LLM foundations

Visual. Black background. Draw a line diagram with white outlined boxes for: System prompt and tool definitions, Messages and tool results, Context window, 1M for listed models, Thinking and text output, max_tokens cap on output, stop_reason in the response. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. LLM foundations. The context window holds every input token and every output token of a turn, so all of them share one budget. Fit the request inside the window with room for max_tokens, then select what enters the window. The trap: A bigger window looks like the fix for missed details, but context rot means more tokens can lower recall.

## Scene 4. F3 Software and distributed systems

Visual. Black background. Draw a line diagram with white outlined boxes for: Your app with SDK client, Messages API, HTTP status and error type, Retry with backoff, Fix the request or key, Log with request-id. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Software and distributed systems. Each error type tells the caller whether a retry can help. Retry 429 and 5xx errors with a limit and backoff. Fix 400 and 401 errors first. The trap: A prompt that says try again looks like a retry policy, but the model cannot resend the request or read a retry-after header.

## Scene 5. F4 Security and identity

Visual. Black background. Draw a line diagram with white outlined boxes for: Your app or CI job, Secrets manager, API key with scope and expiry, Messages API, Workspace boundary, Key status in Admin API. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Security and identity. An API key is a bearer secret, so its scope and expiration limit the damage from a leak. Use a scoped, time-limited, identity-backed key, and store it in a secrets manager. The trap: A key in a prompt or a config file looks convenient, but the model reads the prompt and the file exposes the secret.

## Scene 6. D1.1 Business problem to Claude solution

Visual. Black background. Draw a line diagram with white outlined boxes for: Business request with outcome and constraints, Fixed rules in code, Open input queue, Claude model call, Deterministic check in code, Eval set from real inputs, Accepted result. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Business problem to Claude solution. Send fixed mapping to code and send open input to Claude only when a check in code can verify the output. (Inference) Use code for fixed mapping, and use Claude with a code check for open input. The trap: A model call for a fixed format that a rule covers. It adds cost and a failure mode, and it gives no gain. (Inference)

## Scene 7. D1.2 End-to-end architecture

Visual. Black background. Draw a line diagram with white outlined boxes for: User message, Application state and history, Messages API, Claude model with tools, Your tools and data, Trace record per stage. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. End-to-end architecture. No state persists between Messages API calls. The application resends the conversation on each call and checks each stop reason. Keep the history, the retries, and the stop reason handling in application code. The trap: A larger model or a longer prompt for a failure that no trace locates. The change treats a symptom and hides the stage that breaks. (Inference)

## Scene 8. D1.3 Architectural pattern selection

Visual. Black background. Draw a line diagram with white outlined boxes for: Your application loop, Messages API request with tools, Claude model, stop_reason check in code, Your tool code, Final answer. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Architectural pattern selection. The model asks for a tool call, and the application runs the tool and returns the result. Use a tool-use loop when the steps are known, and the model only chooses tools. The trap: A full agent for one judgment step. The agent adds planning overhead that the task does not need. (Inference)

## Scene 9. D1.4 Multi-agent orchestration

Visual. Black background. Draw a line diagram with white outlined boxes for: User task, Lead agent in primary thread, Subagent thread one, Subagent thread two, Shared sandbox and files, Lead merges results. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Multi-agent orchestration. Each subagent keeps its own conversation history, and the lead agent receives only the subagent's reported results. Delegate only independent, well-scoped work, and keep one lead agent that owns the merge. The trap: Three agents with no lead and no merge. Each agent returns output, and no one owns one coherent result. (Inference)

## Scene 10. D1.5 Task decomposition

Visual. Black background. Draw a line diagram with white outlined boxes for: Source documents, Splitter in code, Model call for piece one, Model call for piece two, Merge and totals check in code, Validated report. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Task decomposition. Independent pieces run in parallel, and each piece gets a bounded input and a fixed output format. (Inference) Split at independent seams, and check the merged result in code. The trap: One large call over the whole input. Long inputs weaken focus on the middle parts, and one error fails the whole run. (Inference)

## Scene 11. D1.6 Business-value alignment

Visual. Black background. Draw a line diagram with white outlined boxes for: Request with prompt and expected output, Token count before send, Published price per million tokens, Claude model call, Usage fields in the response, Cost ledger by use case. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Business-value alignment. The cost of one request follows from its token counts and the published price per million tokens. Price the unit cost from the published rates, then multiply it by the expected volume. The trap: A savings claim with one term, such as labor saved, and no build or run cost. The total looks positive and leaves out cost. (Inference)

## Scene 12. D2.1 Model selection and tier trade-offs

Visual. Black background. Draw a line diagram with white outlined boxes for: Your app, Model ID chosen per task, claude-haiku-5-5 for high-volume work, claude-sonnet-5-5 for everyday work, claude-opus-5-5 for agentic coding, claude-fable-5-1 for hardest work, Eval set with the quality floor. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Model selection and tier trade-offs. Choose the lowest tier that clears a quality floor you measured on your own tasks. Pick the lowest tier that clears the measured quality floor, then tune effort on that tier. The trap: The top tier for every request looks safe, but it adds cost when evals show that a lower tier clears the floor.

## Scene 13. D2.2 System prompts, templates, and guardrails

Visual. Black background. Draw a line diagram with white outlined boxes for: Your app, System prompt: role, scope, output rules, Input screen in code, Messages API top-level system field, Claude model, Untrusted tool results and documents. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. System prompts, templates, and guardrails. The system prompt sets the role, scope, and rules, while your code enforces access (Inference). Put role and output rules in the system prompt. Put access rules in code. The trap: A rule in the system prompt looks like access control, but it is guidance that code must enforce (Inference).

## Scene 14. D2.3 Prompt techniques

Visual. Black background. Draw a line diagram with white outlined boxes for: Your app, Examples in example tags, Instructions and input in tags, Messages API, Claude model, Answer in the shown format, Eval results decide the example set. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Prompt techniques. Examples show the output pattern, so Claude copies the format, tone, and structure they show. Add 3 to 5 diverse examples in example tags, then measure the result before you add more. The trap: More examples look like more guidance, but a set that lacks variety teaches an unintended pattern.

## Scene 15. D2.4 Context and token management

Visual. Black background. Draw a line diagram with white outlined boxes for: Your app, Token counting endpoint, Messages API, Context window up to 1M tokens, Claude model, Usage fields with billed counts. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Context and token management. Every input and output token counts toward the context window, so count tokens before you send a turn. Count tokens with the model ID you will call, and budget each turn before you send it. The trap: A count from an older model looks reusable, but Claude 4.7 and later models use a newer tokenizer, so the count changes.

## Scene 16. D2.5 Reuse and prompt caching

Visual. Black background. Draw a line diagram with white outlined boxes for: Your app, Stable prefix: tools, system, documents, Messages API, Prompt cache, per workspace or organization, Claude model, Usage fields in the response. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Reuse and prompt caching. Pay full price for a stable prefix once, then read it at a fraction of the price while it stays identical. Put the breakpoint on the last block whose prefix is identical across the requests that must share the cache. The trap: A custom response cache in front of the API looks cheaper. But it adds a component, and it cannot reuse a prefix for a new question (Inference).

## Scene 17. D3.1 Tool capability scope

Visual. Black background. Draw a line diagram with white outlined boxes for: Your app builds the request, Scoped tools array for this task, Claude model picks a tool by name, Permission policy or allowlist, MCP server or local tool, Tool result enters the context. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Tool capability scope. Each attached tool is a permission, a token cost, and a selection choice, so the set should hold only what the task calls. Remove or scope each tool the task does not need before you add any monitoring. The trap: Full audit logs on a broad tool set look like the safe fix. The permission stays attached, so the next wrong call still runs.

## Scene 18. D3.2 Authentication and authorization in integrations

Visual. Black background. Draw a line diagram with white outlined boxes for: End user signs in, Your app holds the OAuth flow, Per-user vault credential store, Messages API or agent session, Remote MCP server, Upstream system with its own access list. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Authentication and authorization in integrations. A remote MCP server authorizes the call from an OAuth token that the client sends for that server, so the token must name the user. Give each server a per-user credential when the audit must name the person who asked. The trap: A shared service key with a user name in the prompt looks like attribution. The system cannot verify a name that the user typed.

## Scene 19. D3.3 Accuracy and latency trade-offs

Visual. Black background. Draw a line diagram with white outlined boxes for: Your app sends the request, Model and effort chosen per task, Claude Haiku 5.5 at low effort, Larger Claude model at higher effort, max_tokens caps the output, p95 latency and quality score per stage. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Accuracy and latency trade-offs. Latency rises with model size, output length, and effort, so choose the smallest model and effort that pass the quality target. Pick the smallest model and effort level that passes the measured quality target and the latency target. The trap: A bigger model looks like the accuracy fix. It adds time per call and can break the latency target.

## Scene 20. D3.4 Observability at scale

Visual. Black background. Draw a line diagram with white outlined boxes for: Your app starts the run span, Claude SDK spans, Claude API spans with destination, Model run and tool spans, OTLP collector or partner platform, Trace view with token counts. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Observability at scale. A trace records each step of one run with a shared trace ID, so you can rebuild the run from the spans. Trace each hop that calls a model or a tool, and tie the hops to one trace ID. The trap: More prompt logs or longer retention keeps the blind spot. The logs hold no tool or retrieval hop.

## Scene 21. D3.5 The RAG pipeline

Visual. Black background. Draw a line diagram with white outlined boxes for: Your app, Retriever step in your code, Your index of chunks, Messages API request, Claude model, Citation blocks in the response. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. The RAG pipeline. Pass retrieved text as search result blocks so Claude attaches a source and title to each cited claim. Return retrieved text as search result blocks when the answer needs verifiable source attribution. The trap: A prompt that asks the model to list sources in plain text looks simple. The names are not tied to retrieved blocks, so you cannot check them. (Inference)

## Scene 22. D3.6 Retrieval strategies

Visual. Black background. Draw a line diagram with white outlined boxes for: User query, Metadata filter for source, date, and access, Keyword index for exact terms, Vector index for meaning, Rank fusion of both lists, Merged candidate list. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Retrieval strategies. Pick the matcher that fits the query shape, and merge the candidates from both matchers. Use keyword match for exact terms, semantic match for paraphrases, and filters for access. (Inference) The trap: A single semantic index looks sufficient. Exact codes often fail to match in vector space, so the codes go unfound. (Inference)

## Scene 23. D3.7 Integration mechanisms

Visual. Black background. Draw a line diagram with white outlined boxes for: Your app, Messages API with mcp_servers, Claude model, Remote MCP server over HTTP, Backend system behind the server, OAuth bearer token. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Integration mechanisms. Connect a remote MCP server from the Messages API, so the API calls its tools without a client in your code. Use the MCP connector when a Messages API request needs tool calls on a remote MCP server. The trap: The connector looks like full MCP support. Only tool calls work, so resources and prompts need another path.

## Scene 24. D3.8 Progressive discovery and monolithic context

Visual. Black background. Draw a line diagram with white outlined boxes for: Your app with the full catalog, Messages API request, Tool search tool, Tool reference blocks, Claude model, Deferred tool definitions. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Progressive discovery and monolithic context. Load only the tools that a request needs, found by a search tool over the full catalog. Defer tool definitions when the catalog reaches 10 or more tools, or when definitions exceed 10k tokens. The trap: Shorter tool descriptions look cheaper. The full schemas still load on each call, so the token cost stays high. (Inference)

## Scene 25. D4.1 Evaluation metrics

Visual. Black background. Draw a line diagram with white outlined boxes for: Business goal and success criteria, Held-out eval set, System under test on Claude, Grader: code, LLM, or human, Per-case grades, Primary metric, guards, and thresholds. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Evaluation metrics. A metric measures the goal only when it names the goal and a threshold before tuning starts. Make the business outcome the primary metric, and keep proxy scores as diagnostics. The trap: A fluency or length score that rises while task success stays flat. The score looks better, but it does not measure the goal.

## Scene 26. D4.2 Evaluation datasets and frameworks

Visual. Black background. Draw a line diagram with white outlined boxes for: Real task traffic, Representative cases, Edge cases: empty, long, or unclear input, Versioned eval set, Eval runner, System under test on Claude. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Evaluation datasets and frameworks. An eval set measures the system well only when its cases match the real task distribution. Build the eval set from production traffic, and add edge cases that production contains. The trap: A set built only from easy, clean examples. The score is high, but it does not predict production behavior.

## Scene 27. D4.3 A/B tests and iteration

Visual. Black background. Draw a line diagram with white outlined boxes for: Incoming tasks or users, Consistent assignment rule, Arm A: current prompt or model, Arm B: candidate prompt or model, Primary metric per arm, Ship, roll back, or iterate. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. A/B tests and iteration. A control arm shows whether the change, and not the traffic mix, caused the measured difference. Assign each unit to one arm, and compare the arms on the primary metric with a stated threshold. The trap: A full rollout that compares the week before with the week after. The traffic mix changed, so the difference does not show the effect of the change.

## Scene 28. D4.4 Diagnosis at the correct layer

Visual. Black background. Draw a line diagram with white outlined boxes for: Previous response id, Current request with diagnostics object, Messages API fingerprint comparison, cache_miss_reason type, Fix at the changed block, Cache read token count. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Diagnosis at the correct layer. The earliest divergence in a request explains the miss, so find that divergence before any other fix. Find the earliest changed block in the prefix, and move the variable content after the breakpoint. The trap: A bigger model tier to recover a lower hit rate. The tier change adds cost, and the prefix still changes on every request.

## Scene 29. D4.5 Optimization under quality floors

Visual. Black background. Draw a line diagram with white outlined boxes for: Unattended job queue, Batch request set, Message Batches API, Batch processing queue, Batch results for 29 days, Quality floor check. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Optimization under quality floors. Work that no user waits for can trade latency for a lower token price. Send unattended work to the batch interface, and keep any request a user waits for synchronous. The trap: Streaming a nightly job to cut its latency. Streaming changes the timing of the first token, and the job still pays the synchronous price.

## Scene 30. D4.6 Production monitoring

Visual. Black background. Draw a line diagram with white outlined boxes for: Your app, Messages API, Token counts per request, Usage and Cost API, Dashboard cache between polls, Cost per completed task line. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Production monitoring. Spend becomes a quality signal only when it is divided by completed tasks in the same view. Show spend next to completed tasks, and alert on the per-task line. The trap: A dashboard of total tokens with no completed-task count. Total spend looks normal while the outcome rate falls.

## Scene 31. D5.1 Guardrails and safety controls

Visual. Black background. Draw a line diagram with white outlined boxes for: End user message, Your app, Harmlessness screen on a lightweight model, Messages API, Email, web page, or file content, Verdict log and stop reason. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Guardrails and safety controls. A prompt is guidance. Code checks user input and labels third-party content before the model acts on it. Screen untrusted text before the main call, and keep third-party content in tool_result blocks. The trap: A stricter system prompt as the only control. The model can still follow an injected instruction, and no code stops the action.

## Scene 32. D5.2 Risks and failure modes

Visual. Black background. Draw a line diagram with white outlined boxes for: Source documents, Your app, Claude extracts exact quotes, Claude drafts answer from quotes, Citation check in application code, Reader sees verified claims. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Risks and failure modes. A claim that cites a quote from the source is checkable, and a claim without a quote is removed. Require a source quote for each claim, and remove each claim that has none. The trap: A larger model looks like the fix for unsupported claims. The docs describe quotes, permission to abstain, and citations for the same risk.

## Scene 33. D5.3 Human-in-the-loop validation

Visual. Black background. Draw a line diagram with white outlined boxes for: Agent proposes action, Managed Agents session paused for approval, Arguments, policy, and sources, Reviewer decision, Tool runs after approval, Decision record. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Human-in-the-loop validation. A person approves an action before it runs when the action cannot be undone. Use pre-action approval when the action cannot be undone. The trap: Approval on every action, even at high volume, which stalls the queue. The stakes decide the review shape.

## Scene 34. D5.4 Regulatory compliance and data controls

Visual. Black background. Draw a line diagram with white outlined boxes for: Your app, Messages API, ZDR setting per organization, Feature data kept if needed, Console playground, outside ZDR, Compliance API activity feed. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Regulatory compliance and data controls. The retention arrangement decides how long Anthropic keeps prompts and responses, so it is a design input and not a policy note. Enable ZDR per organization, and confirm feature coverage before regulated data reaches the API. The trap: A team believes ZDR covers every product in the account. The Console, Managed Agents, and claude.ai chat sit outside ZDR.

## Scene 35. D5.5 Responsible AI

Visual. Black background. Draw a line diagram with white outlined boxes for: User content, Your app, Written policy and labeled examples, Claude classifier call, Schema-constrained verdict, Human review for uncertain items. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Responsible AI. Claude classifies user content against a written policy and labeled examples, so the policy text is the control. Put the moderation policy and examples in the prompt, and constrain the verdict with a schema. The trap: A custom classifier looks cheaper, but each policy change then needs new labels and code. (Inference)

## Scene 36. D6.1 Structured discovery

Visual. Black background. Draw a line diagram with white outlined boxes for: Stakeholder requirement, Success criterion with metric and threshold, Evaluation set from real task distribution, Claude model under test, Grading: code, LLM, or human, Measured result against threshold. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Structured discovery. A requirement becomes testable only when it has a metric, a threshold, and a named scope. Convert each adjective into a metric, a threshold, and an owner before design. The trap: Design built on adjectives such as fast looks efficient, but no one can test it, so the team builds to a guessed bar. (Inference)

## Scene 37. D6.2 Trade-off communication

Visual. Black background. Draw a line diagram with white outlined boxes for: Your app, Response usage fields, Per token prices by model, Cost per completed task, Invoice on the chosen platform. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Trade-off communication. Compare options on cost per completed task, because the completed task is the unit that you pay for. Compare options on cost per completed task, and write the price date beside the figure. The trap: The lowest per-token price looks cheapest, but a model that needs more tokens or rounds can cost more per completed task.

## Scene 38. D6.3 Feedback and expectation alignment

Visual. Black background. Draw a line diagram with white outlined boxes for: Production requests, Messages API, Usage report by model and workspace, Cost report in USD by day, Scheduled read with cached result, Review against threshold. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Feedback and expectation alignment. Usage data arrives after a short delay, so the feedback loop reads aggregates on a schedule. Read usage and cost aggregates on a schedule, and compare each total with its threshold. The trap: One response at a time looks precise, but it does not show the trend across workspaces. (Inference)

## Scene 39. D6.4 Architecture documentation

Visual. Black background. Draw a line diagram with white outlined boxes for: Decision and date, Alternatives and rejections, Trade-offs and assumptions, Evidence link to eval run, Current owner, Review criteria. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Architecture documentation. A record that a successor can read preserves the decision after the original people leave. (Inference) Record each decision with its alternatives, owner, evidence, and review criteria when you make it. (Inference) The trap: A full new evaluation looks thorough, but it repeats evidence that the record already holds. (Inference)

## Scene 40. D6.5 Lifecycle phases

Visual. Black background. Draw a line diagram with white outlined boxes for: Discovery: requirements and owners, Design: priced options and records, Handoff: runbooks and alert owners, Monitoring: triggers and usage data, Iteration: tune or re-architect. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Lifecycle phases. Each phase closes only when its artifact exists, so later work cannot replace earlier work. (Inference) When a later phase fails, return to the earliest skipped gate. (Inference) The trap: More dashboards look like progress, but they measure a design that has no requirements. (Inference)

## Scene 41. D7.1 Team configuration for Claude Code

Visual. Black background. Draw a line diagram with white outlined boxes for: Managed settings from the organization, Committed .claude/settings.json, Personal .claude/settings.local.json, User settings in home folder, Claude Code session. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Team configuration for Claude Code. One committed settings file gives every clone the same permissions and hooks, and personal files hold the exceptions. Use a permission rule or a hook for a control, and use CLAUDE.md for a convention. The trap: A CLAUDE.md note that asks the agent not to read secret files. The docs call CLAUDE.md context, not enforced configuration, so only a deny rule blocks the read.

## Scene 42. D7.2 AI-assisted workflows with Claude Code

Visual. Black background. Draw a line diagram with white outlined boxes for: CI job or script, claude -p run, Tools and allowed tools flags, JSON result with session ID and cost, Exit status and test step. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. AI-assisted workflows with Claude Code. A print mode run returns a result and an exit status, so a script can decide whether the job passes. Restrict each scripted run with --tools, approve only those tools, and check the exit status before the job passes. The trap: An --allowedTools list read as a tool restriction. The flag only auto-approves the listed tools. To restrict which tools exist, use --tools, and bypass mode belongs only in isolated environments.

## Scene 43. D7.3 Diagnosis and operational resolution

Visual. Black background. Draw a line diagram with white outlined boxes for: Developer terminal, claude doctor and /doctor, Running session, /status, /hooks, /mcp, /context, Debug log from claude --debug. Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.

Narration. Diagnosis and operational resolution. Read the loaded state before you change a setting, a hook, or a server, because a file on disk can differ from what loaded. Run the built-in check that matches the symptom before you change the setting or the code. The trap: A CLAUDE.md edit meant to make a hook run. Hooks run from settings files, and a guidance note never starts a hook, so the check is the hook configuration and the debug log.
