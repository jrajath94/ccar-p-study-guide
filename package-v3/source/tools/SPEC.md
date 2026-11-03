# Unit drafting spec (read all of it before you write)

You draft study units for the Claude Certified Architect, Professional course.
Write one JSON file per unit to /home/claude/work/units/<UNIT_ID>.json (example: D2.5.json).

## Sources (strict)
1. Product facts come ONLY from the official docs mirror: /home/claude/work/docs/pages/
   - Page index (file | title): /home/claude/work/docs/index.txt
   - File name to URL: replace "__" with "/", add "https://", drop ".md".
     Example: platform.claude.com__docs__en__build-with-claude__prompt-caching.md
     -> https://platform.claude.com/docs/en/build-with-claude/prompt-caching
   - Use Grep on the pages folder to find facts. Read the lines before you cite them.
2. Repo lesson text (prior study build, NOT an official source): /home/claude/work/repo/<lesson>.txt
   Use it for scope, scenarios, and teaching order. Never copy a number from it unless the official docs confirm it.
   General architecture practice from the repo (SLOs, ADRs, A/B tests, idempotency) is allowed with label "Inference".
3. Do not use the web. Do not invent a URL. Every URL must be an official docs URL that exists in the mirror.
4. If a figure, limit, default, date, or name is not in the docs, write "Not in source." and put the claim in not_in_source.

## Writing rules (ASD-STE100 style). The lint enforces most of them.
- One meaning for each word. Same term every time. Keep technical terms from the docs (cache_control, tool_use, MCP).
- Procedures: imperative, one instruction per sentence, max 20 words.
- Descriptions: max 25 words per sentence. One topic per sentence.
- No contractions. No semicolons. No em dash or en dash. Use a period or a comma.
- No word ending in -ing used as a verb or gerund ("by caching" -> "with the cache", "using X" -> "with X", "when calling" -> "when you call").
  Technical nouns from the docs (caching, streaming, routing, logging, extended thinking) are allowed.
- No perfect tense (has been, have used). Active voice.
- Never write: delve, leverage, unlock, robust, seamless, nuanced, pivotal, landscape, realm, tapestry, underscore,
  harness, foster, groundbreaking, cutting-edge, game-changing, holistic, multifaceted, "It is important to note",
  "When it comes to", "At its core", "Not only".
- No emoji. No praise. No summary lines.
- Label a claim that the docs do not settle: end the sentence with " (Inference)" or " (Guess)".
- Never write exam question text, an answer letter, or a question ID. Write generic wording patterns only.

## Native services (official docs names; use these exact names)
Amazon Bedrock, Claude Platform on AWS, Claude Models on Google Cloud (Google managed), Claude Models on Google Cloud (Anthropic managed), Microsoft Foundry.
The exam guide list of native services is not available. Mark the fact that the exam covers these services as Inference in the domain notes, not in each unit.
For each component, cover timeouts, quotas, permissions, and data flow on these platforms ONLY where the docs say something. Else write "Not in source."

## JSON schema (all keys required, use [] or "Not in source." when empty)
{
  "id": "D2.5",
  "domain": "D2",
  "title": "Reuse and prompt caching",                      // short, sentence case
  "task_statement": "Apply prompt reuse and caching to cut cost and latency. (Inference: wording from secondary sources)",
  "components": [ COMPONENT, ... ],                          // 1 to 3 components per unit
  "decision_flow": "flowchart TD\n  A{Same prefix on many calls?} -->|Yes| B[...]\n ...",   // Mermaid. Decision tree for the unit. Labels in STE. No semicolons, no quotes, no parentheses inside labels.
  "cheatsheet": "flowchart LR\n ...",                        // Mermaid. Labels only, max 12 nodes, no sentences.
  "patterns": [ {"wording": "the option with the least operational overhead", "answer_type": "managed feature over custom build",
                 "rule": "Pick the managed feature that meets the stated constraint and no more.", "traps": ["Custom cache layer in front of the API"]} ],   // 2 to 4 generic wording patterns
  "console_steps": [ {"step": "Open the Usage page in the Claude Console.", "url": "<official page that shows this step>", "screenshot": null} ],   // only steps the docs show. If the docs show no console step for this unit, use [] and add "Console steps: Not in source." to not_in_source.
  "not_in_source": ["..."],
  "sources": ["https://platform.claude.com/docs/en/..."]
}

COMPONENT =
{
  "name": "Prompt caching",
  "first_principle": "One sentence.",
  "architecture": {                     // drawn as SVG by the build. 3 to 8 nodes. Groups: client, claude, cloud, data, control.
     "nodes": [{"id": "app", "label": "Your app", "group": "client"}, ...],
     "edges": [{"from": "app", "to": "api", "label": "request with cache_control"}, ...]
  },
  "steps": ["Step 1 sentence.", ...],   // how it works, 3 to 7 steps, one step per sentence
  "pros": [...], "cons": [...],         // 2 to 4 each
  "use_when": [...], "do_not_use_when": [...],   // 2 to 4 each
  "constraints": [ {"family": "cost", "choice": "Cache the stable prefix with a 5-minute TTL.", "combination": "Add a 1-hour TTL when calls arrive less often than every 5 minutes."} ],
       // families: latency, cost, quota, data location, isolation, governance, scale, skill, operations. Cover each family that applies (min 4). combination may be "".
  "native_services": [ {"service": "Amazon Bedrock", "text": "...", "url": "..."} ],   // one entry per service that the docs mention for this component. If none, one entry {"service": "All", "text": "Not in source.", "url": ""}
  "exam_tie": "D2.5. One or two sentences on what the exam tests here. (Inference)",
  "trap": "The wrong choice that looks right, and why it is wrong.",
  "decision_rule": "One sentence rule.",
  "exam_tip": "One sentence.",
  "key_facts": [ {"text": "Cache reads cost 0.1 times the base input price.", "url": "https://platform.claude.com/docs/en/build-with-claude/prompt-caching", "label": "Fact"} ],   // 3 to 8. Every number goes here with its URL.
  "not_in_source": [...]
}

## Example component (quality bar)
See /home/claude/work/units/_EXAMPLE.json. Match its density and style.

## Self-check (required)
After you write each file, run:  python3 /home/claude/work/tools/lint.py /home/claude/work/units/<ID>.json
Fix every issue. Repeat until it prints 0 issues, or until only -ing warnings on true technical nouns remain.
Then report: unit IDs written, lint result for each, and any doc gaps.
