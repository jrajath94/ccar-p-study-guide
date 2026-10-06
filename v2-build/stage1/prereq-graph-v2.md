# Prerequisite Dependency Graph , CCAR-P v2 (Stage 1, Oct 6, 2026)

Taught just-in-time inside the crash course (§6, §7). Each prerequisite lists what
Professional-level objective depends on it, minimum required depth, the diagnostic
probe (Stage 2), and the remediation hook.

## §7.1 Software and distributed systems

- **Required by:** V2-D1.2, V2-D1.4, V2-D3.4, V2-D3.7, V2-D4.6, V2-D7.1.
- **Minimum depth:** HTTP request/response and streaming, sync vs async, queues, events, retries with backoff, idempotency keys, timeouts, circuit breakers, timeouts vs backpressure, concurrency basics, availability vs consistency at intuition level, failure isolation (blast radius), observability (logs/metrics/traces), deployment and rollback.
- **Diagnostic:** "A downstream API flakes. Where does the retry live, and what makes a retried payment safe?" → expects: retry in the caller with idempotency key, not in the model.
- **Remediation:** micro-lesson 7.1A , one toy pipeline, three failure injections, fix at the right layer.
- **Dependents on this prereq:** §7.2 (identity rides on HTTP/OAuth), V2-D3.2.

## §7.2 Security and identity

- **Required by:** V2-D3.1, V2-D3.2, V2-D5.1, V2-D5.2, V2-D5.4, V2-D7.1.
- **Minimum depth:** authentication vs authorization, user identity vs app/service identity, service accounts, delegation, OAuth2 vs OIDC, scopes, token audience, token lifetime, tenant isolation, least privilege, secrets management (never in prompts/config), auditability, human approval as a control, enforcement point vs recommendation, sandbox boundaries, data retention/deletion basics.
- **Diagnostic:** "A tool returns payroll rows. Who decided the user may see them, and at which layer?" → expects: the tool's deterministic authorization check, before context construction.
- **Remediation:** micro-lesson 7.2A , authN/authZ/enforcement vs guidance matrix with 3 minimal pairs.
- **Dependents:** V2-D3.8 (cache isolation), V2-D5.3.

## §7.3 LLM foundations

- **Required by:** V2-D2.1,D2.5, V2-D3.5, V2-D3.6, V2-D5.2.
- **Minimum depth:** tokens and tokenization (cost unit), context window vs active context, generation and model uncertainty, hallucinations (unverifiable generation, not lying), embeddings at intuition level, retrieval vs parametric knowledge, fine-tuning concepts (what it changes, when it is the wrong answer), reasoning controls, structured outputs, tool calling mechanics, prompt injection (direct vs indirect), evaluation as a separate activity.
- **Diagnostic:** "Two answers differ only in wording. What did the model not do?" → expects: no factual computation, generation samples, it does not verify.
- **Remediation:** micro-lesson 7.3A , tokens/context/generation in one worked cost example.
- **Dependents:** all of D2, D3.5/D3.6, D5.2.
- **Key separation taught here:** theory vs controls exposed by a specific Claude model (a mechanism vs a product feature).

## §7.4 Architecture and business foundations

- **Required by:** V2-D1.1, V2-D1.6, V2-D3.3, V2-D4.1, V2-D5.3, V2-D6.1,D6.5.
- **Minimum depth:** functional vs nonfunctional requirements, constraints, acceptance criteria, stakeholder discovery, risk classification (impact × reversibility), SLOs, cost models and ROI at arithmetic level, ADRs, ownership, change management, adoption, handoff, incident response, continuous improvement.
- **Diagnostic:** "'Make it fast and accurate' , what do you ask next?" → expects: numbers. Define fast (p95 ms), define accurate (metric + threshold).
- **Remediation:** micro-lesson 7.4A , requirement→metric→threshold→owner chain on one toy scenario.
- **Dependents:** D6, D1.6, D5.3.

## §7 official prep-path prerequisites (verified availability, Oct 6, 2026)

Corroborated titles from the official Professional preparation path (Partner Academy):

1. Claude 101 , vocabulary for V2-D2.x.
2. Claude Code in Action , required depth for V2-D7.1 (project config, permissions, hooks).
3. AI Fluency: Framework & Foundations , maps to §7.3/§7.4 intuition.
4. Building with the Claude API , messages API mechanics for V2-D3 (tool loop, streaming, errors).
5. Introduction to Model Context Protocol , host/client/server, tools/resources/prompts for V2-D3.7.
6. AI Capabilities and Limitations , feeds V2-D5.2 risk identification.

Status: titles corroborated by secondary sources, availability per Partner Academy (gated). The crash course does not require completing these courses, it teaches the required depth just-in-time and points to them for depth.

## Crash-course path (shortest defensible route)

Foundations: §7.4 → §7.3 → §7.1 → §7.2 (business, then model, then systems, then security)
Core: D1 → D3 → D4 → D2 → D5 → D6 → D7 (weight order within the D1-first reading order)

## Deep-reference path

Same graph, expanded with mechanism depth, implementation examples (Messages API contracts, MCP server, RAG pipeline, eval setup), extended comparisons, and troubleshooting, out of scope for the crash course page, reserved for the companion deep reference (not this build's deliverable, but fragments are kept so it can be assembled later).
