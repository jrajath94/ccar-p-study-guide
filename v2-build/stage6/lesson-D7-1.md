# Lesson D7-1: team configuration (V2-D7.1)

## 1. Problem this lesson solves

A team of eight shares a repo. One developer's Claude Code has
`Bash(rm -rf:*)` denied. Another's allows it. A third never set
permissions, so the agent asks on every command and the developer
clicks "allow" out of habit. One Friday the agent deletes a
week of work. The postmortem finds three different configs and
no shared one.

Instructions in a markdown file advise. Permissions in a
settings file enforce. Teams that confuse the two get advice
where they needed a lock, and friction where they needed speed.
Team configuration separates guidance from enforcement and
commits the shared parts to the repo.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Advice is not a lock</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">CLAUDE.md says be careful. The settings file decides.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="169" font-size="14" text-anchor="middle" fill="#1B2838">CLAUDE.md: "be careful"</text>
<rect x="44" y="196" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="221" font-size="14" text-anchor="middle" fill="#1B2838">week of work deleted</text>
<text x="44" y="252" font-size="13" fill="#5C6B7A">Guidance did not stop the tool.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="169" font-size="14" text-anchor="middle" fill="#1B2838">deny: Bash(rm -rf:*)</text>
<rect x="420" y="196" width="256" height="40" rx="999" fill="#E7F1F8"/>
<text x="548" y="221" font-size="14" text-anchor="middle" fill="#1B2838">CLAUDE.md: still guidance</text>
<text x="420" y="252" font-size="13" fill="#5C6B7A">The rule stops the tool. The note advises.</text>
<defs><marker id="m-d71-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d71-1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">enforce, not advise</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Guidance influences behavior. Permissions decide it.</text>
</svg>
<figcaption>Shell 3. A markdown warning becomes an enforced deny rule. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lesson 7-2A owns the law this lesson applies: enforcement
lives in code before context, and prompts are not
authorization. Lesson 7-1A owns retries and reliability for
the MCP servers below.

| Foundation | What it gives this lesson |
|---|---|
| §7.2 enforcement | Guidance vs enforceable permissions |
| §7.1 systems | MCP servers are network calls with failure modes |

## 3. Mental model

Four settings scopes, highest priority last. Managed settings
from the organization win over everything. The shared project
file `.claude/settings.json`, committed to the repo, carries
team permissions, hooks, and plugins. The project-local file
`.claude/settings.local.json` carries personal overrides and
stays out of git. The user file `~/.claude/settings.json`
carries personal defaults across projects.

Inside the files, two kinds of entries. Guidance: CLAUDE.md
files and memory give the model standing instructions. They
shape behavior. They do not stop tools. Enforcement:
`permissions.allow`, `permissions.ask`, `permissions.deny`
rules name tools and decide without asking. A deny rule for
`Bash(rm -rf:*)` holds even if the model wants to run it.
Managed settings hold even if the user disagrees.

:::takeaway
Commit the shared file. Deny the dangerous tools. Advise in
CLAUDE.md. Never put a secret in either.
:::

<figure class="fig">
<svg viewBox="0 0 720 440" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="440" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Guidance shapes. Permissions decide</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Four scopes. Two entry kinds. One priority order.</text>
<rect x="24" y="96" width="672" height="120" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<rect x="40" y="112" width="144" height="40" rx="8" fill="#E6E2DA"/>
<text x="112" y="137" font-size="12" text-anchor="middle" fill="#1B2838">user: ~/.claude</text>
<rect x="200" y="112" width="144" height="40" rx="8" fill="#E7F1F8"/>
<text x="272" y="137" font-size="12" text-anchor="middle" fill="#1B2838">shared: .claude/</text>
<rect x="360" y="112" width="144" height="40" rx="8" fill="#F4E6D4"/>
<text x="432" y="137" font-size="12" text-anchor="middle" fill="#1B2838">local: .local.json</text>
<rect x="520" y="112" width="144" height="40" rx="8" fill="#F3D4D8"/>
<text x="592" y="137" font-size="12" text-anchor="middle" fill="#1B2838">managed: org wins</text>
<text x="44" y="188" font-size="13" fill="#5C6B7A">Priority rises left to right. Managed overrides all.</text>
<rect x="24" y="232" width="296" height="120" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="260" font-size="13" font-weight="500" fill="#5C6B7A">GUIDANCE (advises)</text>
<rect x="44" y="272" width="256" height="32" rx="999" fill="#E6E2DA"/>
<text x="172" y="293" font-size="12" text-anchor="middle" fill="#1B2838">CLAUDE.md standing notes</text>
<rect x="44" y="312" width="256" height="32" rx="999" fill="#E6E2DA"/>
<text x="172" y="333" font-size="12" text-anchor="middle" fill="#1B2838">reusable Skills</text>
<rect x="400" y="232" width="296" height="120" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="260" font-size="13" font-weight="500" fill="#5C6B7A">ENFORCEMENT (decides)</text>
<rect x="420" y="272" width="256" height="32" rx="8" fill="#E7F4EF"/>
<text x="548" y="293" font-size="12" text-anchor="middle" fill="#1B2838">allow / ask / deny rules</text>
<rect x="420" y="312" width="256" height="32" rx="8" fill="#E7F1F8"/>
<text x="548" y="333" font-size="12" text-anchor="middle" fill="#1B2838">hooks that block tools</text>
<text x="24" y="396" font-size="15" fill="#1B2838">The exam's trap puts a security control in CLAUDE.md. It belongs in permissions.</text>
</svg>
<figcaption>Shell 4. One config becomes four scopes with two entry kinds. Source: official docs, Oct 6 2026.</figcaption>
</figure>

## 4. Causal mechanism

A shared settings file makes the team identical. The deny
rules for destructive commands land on every clone with the
commit. Hooks run on every machine: a PreToolUse hook can
block a tool call before it runs, and a PostToolUse hook can
lint the file after an edit. Scoped subagents carry their own
tool lists, so a research subagent gets Read and Grep only
and cannot write. MCP servers are declared once in config,
so every teammate gets the same tools, and the tokens stay
out of chat.

Spend guardrails close the loop. Model selection per task
keeps cheap work on cheap models. A monthly spend cap with
an owner turns a surprise bill into a watched number. The
plan and admin requirements matter here: managed settings
and some guardrails need an organization plan and admin
rights. A control the team cannot deploy is not a control.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">One commit, eight identical agents</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">The shared file lands on every clone. Drift dies.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="80" height="56" rx="8" fill="#F3D4D8"/>
<text x="84" y="168" font-size="12" text-anchor="middle" fill="#1B2838">dev 1</text>
<text x="84" y="186" font-size="12" text-anchor="middle" fill="#1B2838">deny</text>
<rect x="132" y="144" width="80" height="56" rx="8" fill="#F6E7A8"/>
<text x="172" y="168" font-size="12" text-anchor="middle" fill="#1B2838">dev 2</text>
<text x="172" y="186" font-size="12" text-anchor="middle" fill="#1B2838">allow</text>
<rect x="220" y="144" width="80" height="56" rx="8" fill="#E6E2DA"/>
<text x="260" y="168" font-size="12" text-anchor="middle" fill="#1B2838">dev 3</text>
<text x="260" y="186" font-size="12" text-anchor="middle" fill="#1B2838">none</text>
<rect x="44" y="216" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="241" font-size="13" text-anchor="middle" fill="#1B2838">3 configs, 1 deletion</text>
<text x="44" y="276" font-size="13" fill="#5C6B7A">Drift across 8 developers.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="169" font-size="13" text-anchor="middle" fill="#1B2838">shared .claude/settings.json</text>
<rect x="420" y="196" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="548" y="221" font-size="13" text-anchor="middle" fill="#1B2838">8 clones, 1 config</text>
<rect x="420" y="252" width="256" height="40" rx="8" fill="#D9E8D3"/>
<text x="548" y="277" font-size="13" text-anchor="middle" fill="#1B2838">personal overrides in .local.json</text>
<defs><marker id="m-d71-4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d71-4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">commit the shared file</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Committed config is team config. Uncommitted config is a rumor.</text>
</svg>
<figcaption>Shell 3. Three drifting configs become one committed config. Source: original toy.</figcaption>
</figure>

## 5. Minimal worked example

Toy: eight-developer team, shared repo. Committed
`.claude/settings.json`:

```
{
  "permissions": {
    "allow": ["Bash(npm test:*)", "Bash(git status:*)", "Read", "Grep"],
    "ask": ["Bash(git push:*)"],
    "deny": ["Bash(rm -rf:*)", "Bash(sudo:*)", "Read(.env)", "Read(**/*.key)"]
  },
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit|Write",
      "hooks": [{"type": "command", "command": "./scripts/lint.sh"}]
    }]
  }
}
```

CLAUDE.md holds guidance: "run tests before marking a task
done." A scoped subagent for research carries `tools: Read,
Grep` only. MCP server config declares the shared doc-search
server once. The org deploys managed settings that deny
`WebFetch` to non-allowlisted domains. No user file overrides
it. Spend guardrail: default model for the team, monthly
spend reviewed by the team lead.

Spend arithmetic: before the shared config, 2 of 8
developers left the default model on for bulk refactors.
One month of agent-heavy work cost $4,800. After model
routing plus the guardrail, the same work costs $1,900.
Savings: $4,800 - $1,900 = $2,900 per month, $34,800 per
year. The numbers are a toy. The mechanism is real.

Mini question: "A team wants to stop agents from reading
secret files and to lint every edit. Which setup fits? A) A
CLAUDE.md note that says 'do not read secrets, run lint.' B)
Deny rules for secret paths, a PostToolUse hook that runs
lint, and the shared file committed to the repo. C) A bigger
model with better judgment."

### The 10-step best-answer method in action

STEP 1: Identify what the question asks: best architecture, first action, next action, root cause, control, metric, or optimization.
STEP 2: Identify lifecycle stage: discovery, design, implementation, preproduction, operation, or incident response.
STEP 3: Extract the objective.
STEP 4: Extract hard constraints.
STEP 5: Identify the system layer.
STEP 6: Eliminate technically infeasible options.
STEP 7: Eliminate options violating hard constraints.
STEP 8: Compare remaining options against the objective.
STEP 9: Check hidden dependencies and consequences.
STEP 10: Verify the complete answer or multi-select combination.

Do not assume the exam always wants more autonomy, a larger model, more tools, more logging, a human reviewer everywhere, a new framework, or a complete redesign. Sometimes the best answer is: clarify the requirement, remove an unnecessary capability, fix retrieval, add a deterministic validation gate, narrow permissions, or preserve an existing sufficient workflow. The scenario, not a slogan, determines the answer.

| Step | Action on this question |
|---|---|
| STEP 1 | Team control for secrets and lint |
| STEP 2 | Design: the config does not exist yet |
| STEP 3 | Enforce secret denial and lint on every edit |
| STEP 4 | Eight developers. Secrets in the repo. Edits constant |
| STEP 5 | Team configuration layer |
| STEP 6 | All three are feasible to write |
| STEP 7 | A violates enforcement: CLAUDE.md advises, it does not stop reads. C violates it too: judgment is not a lock |
| STEP 8 | B denies in code, lints via hook, commits the file |
| STEP 9 | B needs the secret-path globs right, or the deny misses |
| STEP 10 | B alone. Single select |

Verdict: B. The decisive law is guidance versus enforcement.
CLAUDE.md cannot deny a read. A deny rule can.

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| Settings scopes | Official docs, Oct 6 2026 | V2-D7.1 shared vs personal vs managed |
| allow / ask / deny | `permissions` in settings.json | V2-D7.1 enforceable permissions |
| PreToolUse / PostToolUse hooks | `hooks` in settings.json | V2-D7.1 deterministic automation |
| MCP server config | `.claude.json`, project config | V2-D7.1 shared tool config |
| Scoped subagents | `.claude/agents/*.md`, `tools` field | V2-D7.1 least-privilege agents |
| Skills | `.claude/skills/`, SKILL.md | V2-D7.1 reusable governed assets |
| Managed settings | Org deployment | V2-D7.1 admin and plan requirements |

## 7. Current limitations

Denied rules can be bypassed by a clever command rewrite:
`Bash(rm -rf:*)` misses `rm -rf` split across flags. Hooks
run shell commands, so a malicious hook is a risk: the team
must review committed hooks like code. Managed settings
need an org plan and admin rights, which a small team may
lack. Permissions ask on the rest, and prompt fatigue makes
developers click allow blindly.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Prompt fatigue breaks the ask</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Forty asks a day. The developer stops reading.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="40" rx="8" fill="#F6E7A8"/>
<text x="172" y="169" font-size="14" text-anchor="middle" fill="#1B2838">ask on everything</text>
<rect x="44" y="196" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="221" font-size="14" text-anchor="middle" fill="#1B2838">blind allow, day 3</text>
<text x="44" y="252" font-size="13" fill="#5C6B7A">The ask becomes decoration.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="169" font-size="14" text-anchor="middle" fill="#1B2838">allow the safe, deny the bad</text>
<rect x="420" y="196" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="548" y="221" font-size="14" text-anchor="middle" fill="#1B2838">ask only on the gray</text>
<text x="420" y="252" font-size="13" fill="#5C6B7A">Few asks. Each one read.</text>
<defs><marker id="m-d71-7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d71-7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">shrink the gray</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Ask is a budget. Spend it where judgment matters.</text>
</svg>
<figcaption>Shell 3. Ask-on-everything becomes ask-on-the-gray. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| No shared config | Each developer alone | Solo project, no secrets |
| Guidance only | CLAUDE.md, no permissions | Trusted team, no destructive tools |
| Shared enforceable config (this lesson) | Committed settings, deny rules, hooks | Team, secrets, destructive tools |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Security control needed | Permissions or hooks, never CLAUDE.md alone |
| Team shares a repo | Commit `.claude/settings.json` |
| Personal exceptions | `.claude/settings.local.json`, not the shared file |
| Org policy must hold | Managed settings, needs plan and admin |
| Secrets in the repo | Deny read rules on the paths |

## 10. Valid-but-inferior option

Guidance only in CLAUDE.md. Valid: it is fast to write and
shapes behavior well for style and conventions. Inferior as
the control: a note cannot stop a tool call, and an injection
can override it.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| CLAUDE.md note | Fast, shapes style | No enforcement. Reads continue |

## 11. Counterfactual where the alternative wins

Solo side project. One developer. No secrets in the repo.
No destructive tools. Guidance wins: a CLAUDE.md note is
enough, and permission machinery protects nothing.

| Situation | Winner | Why |
|---|---|---|
| Solo, no secrets, no risk | CLAUDE.md only | Nothing to enforce |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. Four scopes: user, shared ______, project
   ______, ______ (wins).
2. Guidance: ______.md. Enforcement:
   ______ rules and hooks.
3. A deny rule beats a ______ note.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A 20-person team shares one repo with prod
credentials in a vault and staging keys in
.env files. Write the permission rules, the
hook, and the file each lives in. Then name
the one setting that needs an org plan.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| Settings scopes: user `~/.claude/settings.json`, shared `.claude/settings.json`, local `.claude/settings.local.json`, managed settings win | Current product behavior | Official docs, docs.claude.com/en/docs/claude-code/settings | Oct 6, 2026 |
| allow, ask, and deny permission rules, PreToolUse and PostToolUse hooks, CLAUDE.md as standing instructions not enforcement | Current product behavior | Official docs, Oct 6 2026 | Oct 6, 2026 |
| Managed settings need org deployment. Some guardrails need plan and admin | Current product behavior | Official docs, Oct 6 2026 | Oct 6, 2026 |
| V2-D7.1 tests team config, guidance vs enforcement, hooks, sandboxing, scoped subagents, Skills, guardrails | Official exam scope via secondary summaries | S03, S04, blueprint ledger V2-D7.1 | Sept 2026 |
| Toy arithmetic: $4,800 vs $1,900 per month, $34,800 per year saved | Original toy, computed above | This lesson | Oct 6, 2026 |
| Subagent frontmatter fields (`tools`, `model`) and skill SKILL.md format | Current product behavior via secondary sources | Secondary sources, Oct 6 2026 | Oct 6, 2026 |

:::takeaway
Advise in CLAUDE.md. Enforce in permissions. Commit the
shared file. The exam's D7.1 trap is a control living in
guidance. Move it to the rule.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Advice is not a lock | CLAUDE.md warning | Deny rule stops the tool | d71-f01 | SVG | Original |
| u02 | Enforcement law carries over | -- | Prerequisite table | d71-f02 | Table | §7.2, §7.1 |
| u03 | Guidance shapes, permissions decide | One config | Four scopes, two kinds | d71-f03 | SVG | Official docs |
| u04 | One commit, eight identical agents | 3 drifting configs | 1 committed config | d71-f04 | SVG | Original |
| u05 | 10-step method picks B | Three options | B enforces in code | d71-f05 | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | d71-f06 | Table | Official docs, S03, S04 |
| u07 | Prompt fatigue breaks the ask | Ask on everything | Ask only on the gray | d71-f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | d71-f08 | Table | Original |
| u09 | Constraints decide the config | -- | Constraint verdict table | d71-f09 | Table | Original |
| u10 | Guidance-only valid but inferior | -- | Validity vs inferiority table | d71-f10 | Table | Original |
| u11 | Solo project favors guidance | -- | Counterfactual table | d71-f11 | Table | Original |
| u12 | Four scopes from memory | Blank recall card | Filled from memory | d71-f12 | ASCII | Original |
| u13 | Transfer to 20-person team | Unseen question | Key in Stage 8 | d71-f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | d71-f14 | Table | Mixed |
