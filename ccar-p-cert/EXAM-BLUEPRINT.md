# CCAR-P Exam Blueprint - verified research (2026-09-28)

## Verified exam identity

| Item | Verified fact |
|---|---|
| Full name | Claude Certified Architect - Professional |
| Exam code | CCAR-P |
| Vendor | Anthropic |
| Items | 63: multiple-choice and multiple-response; each item states how many responses to select |
| Duration | 120 minutes |
| Delivery | Proctored via Pearson VUE: OnVUE online or test center |
| Passing score | 720 on a scaled 100–1,000 scale (criterion-referenced: fixed standard, not a curve; 720 is NOT 72% correct) |
| Fee | US$175 |
| Validity | 12 months from award; badge issued through Credly; free renewal if done on time (non-proctored assessment), otherwise full retake |
| Prerequisites | None mandatory; recommended experience only |
| Exam guide version | v1.0, effective July 2026 |

Sources: official exam guide v1.0 (summarized in the DEV Community domain/weights article, 2026-09-27); Anthropic certification page (anthropic-partners.skilljar.com); community exam reports (dev.to "I Cleared All 4 Anthropic Claude Certifications"; LinkedIn CCAR-P walkthrough; mohittej12 flashcards repo; dnacenta/claude-certified-architect repo).

## Recommended candidate profile (from the official guide)

- Foundation in software engineering best practices (modular design, separation of concerns, scalability)
- 3+ years in systems architecture or platform engineering
- 6+ months hands-on with Claude or comparable LLM systems in production
- Experience delivering end-to-end systems from discovery through deployment
- NOT for: entry-level developers, casual users, or roles limited to isolated tasks without system-design responsibility

## The seven domains (official weights; weight x 63 = estimated items)

| # | Domain | Weight | ~Items |
|---|---|---|---|
| D1 | Solution Design & Architecture | 17% | ~11 |
| D2 | Claude Models, Prompting & Context Engineering | 13% | ~8 |
| D3 | Integration | 19% | ~12 |
| D4 | Evaluation, Testing & Optimization | 16% | ~10 |
| D5 | Governance, Safety & Risk Management | 14% | ~9 |
| D6 | Stakeholder Communication & Lifecycle Management | 14% | ~9 |
| D7 | Developer Productivity & Operational Enablement | 7% | ~4 |

No single domain exceeds 19%; six of seven sit between 13% and 19%. Score report shows percent-correct per domain.

### D1: Solution Design & Architecture (17%)
- Translate business problems into Claude-based AI solutions
- Design end-to-end architectures (input, processing, output, feedback loops)
- Select architectural patterns (workflow, agentic, augmented LLM)
- Design multi-agent systems and orchestration strategies
- Apply decomposition techniques for complex problem solving
- Align solutions to business value pillars (efficiency, transformation, productivity, cost, performance SLAs)

### D2: Claude Models, Prompting & Context Engineering (13%)
- Select Claude models based on trade-offs
- Design system prompts, templates and guardrails
- Apply prompt engineering techniques (zero-shot, few-shot, chain-of-thought)
- Optimize context windows and manage token usage
- Implement prompt reuse strategies (caching, modular prompts, Skills)

### D3: Integration (19%)
- Evaluate tool and agent configuration for capability bloat
- Analyze authentication and authorization requirements to identify security gaps
- Evaluate accuracy-latency trade-offs and justify configuration decisions
- Analyze observability challenges and select monitoring strategies at scale
- Design a RAG pipeline with appropriate chunking and indexing strategies
- Apply retrieval strategies matched to data shape and query pattern
- Evaluate connection protocols and select an integration mechanism (MCP, API/CLI, agent-to-agent)
- Evaluate progressive discovery vs. monolithic context strategy

### D4: Evaluation, Testing & Optimization (16%)
- Define evaluation metrics (accuracy, latency, cost, safety, security)
- Design evaluation datasets and test frameworks using mixed methodologies
- Conduct A/B testing and iterative improvements
- Diagnose system issues (prompt failure, hallucinations, model mismatch)
- Optimize token usage, latency and cost-performance trade-offs
- Monitor system performance using logging and observability tools

### D5: Governance, Safety & Risk Management (14%)
- Implement guardrails and safety controls
- Identify risks, limitations and failure modes of LLM systems
- Apply human-in-the-loop validation strategies
- Ensure compliance with regulations (e.g. GDPR, HIPAA, FedRAMP)
- Address ethical AI considerations (bias, fairness, transparency)

### D6: Stakeholder Communication & Lifecycle Management (14%)
- Conduct structured discovery and requirement gathering
- Communicate architectural decisions and trade-offs
- Manage stakeholder feedback loops and expectation alignment, including SLAs
- Document architectures and provide implementation guidance
- Support lifecycle phases (discovery, design, handoff, monitoring, iteration)

### D7: Developer Productivity & Operational Enablement (7%)
- Configure Claude tools and environments for teams (e.g. Claude Code)
- Improve developer workflows using AI-assisted tooling
- Support debugging and operational issue resolution

## How CCAR-P differs from CCAR-F (foundations tier)

| | CCAR-F | CCAR-P |
|---|---|---|
| Items / fee | 60 / $125 | 63 / $175 |
| Structure | 4 scenarios drawn from a published bank of 6 | No scenario structure described |
| Domains | 5 | 7 |
| Largest domain | Agentic Architecture & Orchestration (27%) | Integration (19%) |
| Tests | Specific configuration (stop_reason values, tool_choice, .mcp.json, CLAUDE.md levels, CLI flags) | Design decisions and trade-offs (RAG pipelines, auth gaps, eval metrics, compliance, stakeholder communication) |

Three CCAR-P domains have no CCAR-F equivalent: D4 Evaluation/Testing/Optimization, D5 Governance/Safety/Risk, D6 Stakeholder Communication/Lifecycle. Prompting is 6th of 7 domains by weight on CCAR-P. It leads nothing.

## How they ask (exam style notes)

- Scenario-based items about production design decisions and their trade-offs, not config trivia.
- Multiple-response items state exactly how many answers to select.
- "Most correct" distractors: several options are partially right; the credited answer best satisfies the stated constraint (accuracy SLA, latency budget, compliance rule, cost ceiling). Train on constraint-first reading.
- Example shape (community practice style): a contract-review assistant must hit >=95% accuracy on EACH of five contract types; overall 96% on 1,000 reviewed contracts. Correct move: measure per-type accuracy and fix weak types before go-live. Overall figures hide per-segment failures; switching models or going live on aggregate metrics are the traps.
- Result reporting: pass/fail + scaled score + percent-correct by domain.

## Key study sources

- Official CCAR-P exam guide (PDF) and Anthropic certification page, via anthropic-partners.skilljar.com
- Anthropic docs: docs.anthropic.com (Models API, tool use, prompt caching, MCP, Agent SDK, Claude Code)
- Anthropic Academy (public, free courses), usable without a partner account
- Anthropic engineering blog (anthropic.com/engineering): multi-agent systems, evals, context engineering
- modelcontextprotocol.io: MCP spec (production MCP over SSE, OAuth 2.0)
- Community: dnacenta/claude-certified-architect (deep CCAR-F guide + CCAR-P overview), cemendes/anthropic-claude-certifications (question-bank design; note its 5-domain/25-22-20-18-15 split is the author's own bank design, NOT the official blueprint), akhilmahajan96/claude-architect-exam-guide (Foundations + Professional tracks), timolabs.dev (free 20-question CCAR-P practice test, no sign-up), mohittej12/claude-certifications flashcards
- Multi-cloud deployment: Google Cloud Vertex AI (Anthropic models on Vertex), AWS Bedrock (Anthropic models), direct Anthropic API: failover/resilience patterns, Zero Data Retention (ZDR) options

## Certification family (for context)

| Code | Credential | Items | Fee | Audience |
|---|---|---|---|---|
| CCAO-F | Associate - Foundations | 60 | $99 | Business/productivity users (non-developer) |
| CCDV-F | Developer - Foundations | 53 | $125 | Engineers shipping Claude apps, agents, workflows |
| CCAR-F | Architect - Foundations | 60 | $125 | Solution architects |
| CCAR-P | Architect - Professional | 63 | $175 | Senior architects owning full solution lifecycle |

All four: 120 min, Pearson VUE proctored, 720/1,000 pass, 12-month validity, Exam Guides v1.0 effective July 2026.
