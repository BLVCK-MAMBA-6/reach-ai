# Reach AI: Project Plan

> Working name. Find/replace if it changes. Names already ruled out: OpportunityOS (taken), Voyager, Explora, Exposure, Open Reach (Openreach collision).

**Event:** Nebius x NVIDIA Global AI Hackathon (Devpost)
**Track:** Personal AI
**Deadline:** Oct 30, 2026, 6:00pm GMT+1. **Target submit: Oct 29.**

**One-liner:** A private AI agent that finds opportunities you fit, verifies the critical facts against official sources, researches the people and work behind them, explains your fit, and prepares your next action. Nothing is sent without your approval.

**Positioning rule:** never call it a tracker or an aggregator. Lead with *verified, private, relationship-aware, approval-controlled*.

---

## 1. Hard requirements (do not miss)

- [ ] Runs on **Nebius Token Factory** or AI Cloud
- [ ] Uses at least one **NVIDIA open source model** (Nemotron)
- [ ] Personal AI brief: always-on, private, persistent memory, reusable skills, tools of your choice, tasks across daily workflows
- [ ] Working demo URL (public)
- [ ] Demo video: public YouTube, **3 minutes or less**
- [ ] Public repo with **open source license visible at the top** (MIT)
- [ ] README with setup and run instructions
- [ ] README highlights: how Nemotron is used, where Token Factory helped, other Nebius tools used
- [ ] Written feedback on Nebius Token Factory / AI Cloud and NVIDIA tools (also eligible for Most Valuable Feedback, $100)
- [ ] Choose track: Personal AI
- [ ] If attending an IRL Builders & Brews event, pick the city at submission (City Winner Award)
- [ ] Read the full Official Rules once (especially anything about reusing existing work)

**Extra prize angle:** Best Use of Tavily ($3,000). Tavily is core to verification and discovery, so document it clearly.

---

## 2. Setup checklist (Oct 3-4)

- [ ] Finish Devpost registration; sign up for the **Nebius Builder Program** first (credits for Token Factory and Tavily)
- [ ] Token Factory account + API key
- [ ] Tavily API key
- [ ] NVIDIA developer account / build.nvidia.com key
- [ ] Public GitHub repo with MIT license committed first
- [ ] Google Cloud project: Gmail + Calendar APIs, OAuth consent screen, add yourself as test user
- [ ] YouTube channel ready for a public upload
- [ ] Keep a running `FEEDBACK.md` of friction and praise for Nebius/NVIDIA tools
- [ ] Check the hackathon Updates/Discussions tabs for schedule or maintenance notices

**Go/no-go test:** posting text -> Nemotron (Nano) on Token Factory -> schema-valid, evidence-grounded JSON. Run it on 10 real postings. Everything else depends on this.

---

## 3. MVP scope

**Build:**
1. Profile from a résumé plus a short questionnaire (user-confirmed)
2. Seeded discovery: 3-5 profile-derived Tavily queries, one scheduled scan
3. Official-source finding and deadline verification
4. Deterministic eligibility check
5. Explainable fit score and deadline risk
6. One person/lab and one recent publication linked to an opportunity
7. Evidence-grounded action plan and outreach draft
8. Approval-gated actions (Gmail draft, proposed calendar event)
9. Daily brief
10. Audit view: sources, timestamps, corrections, action receipts
11. Memory screen: view, edit, delete what the agent remembers

**Cut line (drop in this order if behind):** NemoClaw/OpenShell wrapper -> Telegram -> real Calendar write -> self-scoring beyond logging -> readiness score -> pgvector.
**Never cut:** verification, deterministic eligibility, the brief, approvals, audit log.

---

## 4. Stack

| Layer | Choice |
|---|---|
| Models | Nemotron on Token Factory: Nano (extract/classify), Super (compare/research/drafts), Ultra (weekly strategy, top few opportunities only) |
| Backend / tools | FastAPI |
| Database + memory | PostgreSQL (canonical records) plus a `memory` table with confidence, timestamp, expiry, edit/delete |
| Web research | Tavily (search, extract, official-source verification) |
| Paper/author facts | OpenAlex or arXiv API |
| Scheduled work | Nebius Serverless Jobs |
| Frontend | Next.js, installable as a PWA |
| Your data | Gmail + Calendar via OAuth (read + draft only; **no send scope**) |
| Agent shell (stretch) | NemoClaw + OpenShell with Hermes **or** OpenClaw (not both), egress allowlist |

**Risks to resolve early**
- Can NemoClaw route inference to Token Factory (custom compatible endpoint)? Test Oct 4-5. NemoClaw is alpha software.
- If the agent shell fights you for more than half a day, drop it. FastAPI is the real product.
- Check Ultra latency and cost; cache its outputs.

---

## 5. Architecture

```
You (PWA dashboard / optional Telegram)
        |
        v
[ Optional: OpenShell sandbox (NemoClaw) -> Hermes agent ]
        |  tool calls (authed HTTPS)
        v
[ FastAPI: tools + business logic + audit log ]
   |            |              |
   v            v              v
Token Factory   Postgres       External (allowlisted)
(Nemotron)      records +      Tavily, OpenAlex/arXiv,
                memory         Gmail, Calendar
        ^
        |
Nebius Serverless Jobs: scan -> verify -> assess -> brief
```

---

## 6. Model routing

| Task | Execution |
|---|---|
| Extract structured posting data | Nano |
| Classify, deduplicate | Nano |
| Hard eligibility rules | Deterministic Python |
| Compare profile with requirements | Super |
| Research people and publications | Super + Tavily / OpenAlex |
| Resolve conflicting sources | Super |
| Weekly strategy brief | Ultra (top few only) |
| Outreach drafts | Super (Ultra for high-value) |
| Calendar/checklist records | Deterministic code |

---

## 7. Data model (Postgres)

- **profile:** education, skills, experience, projects, interests, goals, citizenship/residency, locations, preferences, `confirmed_at`
- **opportunity:** title, org, type, official_url, deadline_at, deadline_timezone, status, funding, location, source_confidence, last_verified_at
- **requirement:** opportunity_id, category, text, rule_operator, expected_value, hard_requirement, evidence_id
- **entity:** type (person | lab | org | publication), name, url, facts, last_verified_at
- **relationship:** source_entity, type, target_entity, evidence_id, confidence
- **evidence:** source_url, snippet, retrieved_at, label (`fact` | `inference` | `recommendation`)
- **assessment:** opportunity_id, profile_version, eligibility_status, fit_score, deadline_risk, evidence_gaps, explanation
- **action:** type, status, risk_level, approval_required, payload, approved_at, executed_at, receipt
- **memory:** content, source_interaction, confidence, sensitivity, created_at, expires_at
- **prediction (log only):** claim, predicted_at, outcome, resolved_at

**Precedence:** user-confirmed profile > officially verified facts > explicit recent feedback > inferred memory.

---

## 8. Scoring

**Eligibility (code, never LLM):**
```python
if failed_hard_requirements:   status = "ineligible"
elif unresolved_hard_requirements: status = "needs_confirmation"
else:                          status = "eligible"
```

**Fit (model scores soft parts only, with evidence for each):**
| Component | Weight |
|---|---:|
| Research/career alignment | 30 |
| Skills alignment | 25 |
| Experience evidence | 20 |
| Strategic value | 15 |
| User preferences | 10 |

Show: `Eligible - 87% fit - Medium deadline risk`, with confidence and the evidence behind each component. Label every claim as fact, inference, or recommendation.

---

## 9. Agent tools (small and testable)

`search_opportunities`, `extract_opportunity`, `find_official_source`, `verify_opportunity`, `deduplicate_opportunity`, `evaluate_eligibility`, `calculate_fit`, `research_entities`, `find_recent_publications`, `generate_action_plan`, `create_email_draft`, `propose_calendar_event`, `record_feedback`, `store_memory`, `retrieve_memories`

Every tool returns:
```json
{ "success": true, "data": {}, "evidence_ids": [], "warnings": [], "error": null }
```

---

## 10. Approval policy

| Action | Policy |
|---|---|
| Search public sources | Automatic |
| Extract and classify a posting | Automatic |
| Store a discovered opportunity | Automatic |
| Read connected email | Within configured scope only |
| Create a checklist | Automatic |
| Prepare an email draft | Automatic, notify user |
| Send an email | **Not built** (no send scope) |
| Create a calendar event | Explicit approval |
| Change confirmed profile facts | Confirmation required |
| Delete user data | Explicit user action |

---

## 11. Schedule

| Dates | Focus | Milestone |
|---|---|---|
| Oct 3-5 | Setup, Nemotron JSON test, repo, schemas, FastAPI + Next.js skeletons | Posting -> valid opportunity JSON |
| Oct 6-12 | Tavily discovery, official-source verification, dedup, evidence records, scheduled scan | Profile -> verified opportunity list |
| Oct 13-17 | Profile extraction, eligibility rules, fit scoring, memory table + review UI | Opportunity -> explainable assessment |
| Oct 18-22 | People/lab/paper linkage, outreach drafts, action plans, approvals + receipts | Assessment -> controlled action |
| Oct 23-26 | Dashboard, daily brief, detail + audit pages, deploy (frontend, API, jobs) | Complete working product |
| Oct 27-28 | Evaluation set, fixes, demo recording | Measured results + video |
| Oct 29 | README, architecture diagram, feedback write-up, submit | **Submitted** |
| Oct 30 | Buffer only | |

**Calendar conflicts:** the Amazon hackathon closes Oct 23, in the middle of the Oct 18-22 block. Decide early which one gets the best hours. If time is short, protect verification, the brief, and approvals.

---

## 12. Evaluation set (Oct 27-28)

Test cases: wrong aggregator deadline, missing timezone, ineligible citizenship, ambiguous education requirement, duplicate postings, expired opportunity, conflicting official pages, weak research alignment, relevant person with no good outreach reason, changed deadline.

Measure: JSON validity, field accuracy, deadline accuracy, eligibility accuracy, dedup accuracy, evidence coverage, average cost, average time. Report real numbers in the README.

---

## 13. Demo script (3:00 max)

| Time | Beat |
|---|---|
| 0:00-0:25 | Problem: opportunities are everywhere, trust and fit are not |
| 0:25-0:50 | Upload résumé -> confirmed profile and monitoring plan |
| 0:50-1:20 | Run scan -> opportunities found, duplicates and ineligible items rejected |
| 1:20-1:50 | **The "AI caught something" moment:** aggregator deadline vs official deadline; show eligibility and fit |
| 1:50-2:20 | Relevant lab, person, recent paper, tied to the user's work |
| 2:20-2:45 | Action plan + outreach draft; approve one action, reject another |
| 2:45-3:00 | Audit trail, editable memory, "nothing sent without approval" |

Use real data or clearly labeled sample data. If the wrong-deadline case is staged, say so in the video.

---

## 14. Definition of done

A new user can: upload a résumé; get a watchlist; see discovered opportunities without pasting URLs; see at least one officially verified opportunity; understand eligibility and fit; view the people/research behind it; generate an evidence-grounded plan; approve or reject an external action; inspect and delete what the agent remembers; use it from a public URL.

---

## 15. Final submission checklist

- [ ] Deployed demo works from a fresh account
- [ ] Public GitHub repo, MIT license visible at top
- [ ] README: setup steps, architecture diagram, Nemotron/Token Factory/Nebius/Tavily usage
- [ ] Demo video uploaded as public YouTube, 3 minutes or less
- [ ] Feedback on Nebius and NVIDIA tools written
- [ ] Track selected (Personal AI); city selected if applicable
- [ ] All links tested while logged out
- [ ] Submitted by Oct 29
