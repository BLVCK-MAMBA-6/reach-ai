# 🗺️ Reach AI — Hackathon Roadmap

> **Mission:** Build a private, always-on opportunity intelligence agent that discovers and verifies opportunities, evaluates them against a user's profile, researches the people and work behind them, and recommends the next best action.

**Hackathon:** Nebius × NVIDIA Global AI Hackathon  
**Track:** Personal AI  
**Submission deadline:** October 30, 2026 at 6:00 p.m. GMT+1  
**Build window:** October 3–30, 2026  
**Project status:** 🟡 Foundation in progress

---

## 📊 Progress snapshot

| Milestone | Status | Target |
| --- | --- | --- |
| Product definition and repository | 🟡 In progress | Oct 4 |
| Nemotron extraction proof | ⚪ Not started | Oct 6 |
| Autonomous discovery and verification | ⚪ Not started | Oct 12 |
| Personal scoring and memory | ⚪ Not started | Oct 17 |
| Relationship intelligence and actions | ⚪ Not started | Oct 22 |
| Complete deployed product | ⚪ Not started | Oct 26 |
| Evaluation and submission assets | ⚪ Not started | Oct 29 |
| Devpost submission | ⚪ Not started | Oct 30 |

Legend: ✅ Complete · 🟡 In progress · 🔴 Blocked · ⚪ Not started

---

## 🎯 Definition of the MVP

Reach AI is MVP-complete when a new user can:

- [ ] Upload a résumé or enter a structured profile
- [ ] Review and confirm the extracted profile
- [ ] Receive automatically generated opportunity watchlists
- [ ] Discover opportunities without pasting individual URLs
- [ ] Open an opportunity with an official source and verification timestamp
- [ ] See deterministic eligibility status
- [ ] See explainable fit and application-readiness scores
- [ ] See relevant people, labs or publications when available
- [ ] Receive a prioritized next-action plan
- [ ] Approve or reject a prepared external action
- [ ] Inspect and delete agent memories
- [ ] Use the product through a public working URL

### Explicitly outside the MVP

- Automatic application submission
- Automatic email sending
- Scraping sites that prohibit automated access
- A native mobile application
- Large-scale recommendation-model training
- Guaranteed acceptance-probability predictions
- Full multi-user team collaboration
- Every possible opportunity category and source

---

# Phase 0 — Foundation

**Target:** October 3–4  
**Outcome:** A clean public project foundation with confirmed access to required services.

## Product and repository

- [x] Select the Personal AI track
- [x] Define the core problem and audience
- [x] Lock the project name: **Reach AI**
- [x] Define the subtitle: **A private opportunity intelligence agent**
- [x] Create the `reach-ai` GitHub repository
- [x] Make the repository public
- [x] Add the MIT License
- [x] Create a rich project README
- [x] Upload the README and animated asset to GitHub
- [x] Add `.gitignore` for Python, Node.js, environment files and local databases
- [x] Add `CONTRIBUTING.md`
- [x] Add `SECURITY.md`
- [x] Add this `roadmap.md` to the repository

## Accounts and access

- [ ] Confirm Devpost registration
- [x] Submit the Nebius AI Builder Program application
- [ ] Receive Nebius AI Builder Program approval
- [ ] Obtain Nebius Token Factory credentials
- [ ] Confirm available Nemotron model identifiers
- [ ] Obtain Tavily API credentials
- [ ] Create a PostgreSQL development database
- [ ] Decide between Memori and Mem0 for the MVP
- [ ] Document all required environment variables in `.env.example`
- [ ] Confirm no credentials are committed to Git

## Phase exit check

- [ ] A fresh clone contains the README, license and roadmap
- [ ] The required accounts are active
- [ ] The project can make one authenticated Nebius request
- [ ] The project can make one authenticated Tavily request

---

# Phase 1 — Nemotron extraction proof

**Target:** October 5–6  
**Outcome:** A real opportunity posting becomes schema-valid, evidence-grounded JSON.

## Opportunity schema

- [ ] Define the Pydantic `OpportunityExtraction` model
- [ ] Include title, organization, type and official URL
- [ ] Represent deadline date, time and timezone separately
- [ ] Represent application status explicitly
- [ ] Represent hard and soft requirements separately
- [ ] Include funding and benefits
- [ ] Include required documents
- [ ] Include selection criteria
- [ ] Include source-evidence spans
- [ ] Include missing-information and conflict arrays
- [ ] Version the schema

## Extraction prompt

- [ ] Create the first Nemotron Nano extraction prompt
- [ ] Require JSON only
- [ ] Require `null` or `not_stated` for absent information
- [ ] Prohibit inferred requirements
- [ ] Require evidence for every critical field
- [ ] Preserve exact timezone wording
- [ ] Add retry/repair behavior for invalid JSON
- [ ] Log model name, prompt version, latency and token usage

## Test set

- [ ] Collect 10 representative opportunity postings
- [ ] Include one fellowship
- [ ] Include one grant
- [ ] Include one internship
- [ ] Include one research program
- [ ] Include one hackathon
- [ ] Include one missing-timezone case
- [ ] Include one conflicting-deadline case
- [ ] Include one expired posting
- [ ] Include one ambiguous-eligibility case
- [ ] Include one duplicate or reposted opportunity

## Evaluation

- [ ] Achieve 100% JSON-schema validity after repair
- [ ] Check title and organization accuracy
- [ ] Check deadline date, time and timezone accuracy
- [ ] Check requirement extraction accuracy
- [ ] Confirm unstated information is not invented
- [ ] Confirm evidence points to the supplied source
- [ ] Save extraction fixtures for regression testing

## Phase exit check

- [ ] `posting text → validated JSON` works from a repeatable command
- [ ] At least 8 of 10 test postings pass critical-field review
- [ ] Failures are visible and do not silently enter the canonical database

---

# Phase 2 — Core application and data layer

**Target:** October 7–9  
**Outcome:** Reach AI has a working API, database and minimal interface.

## Repository structure

- [ ] Create `apps/web` using Next.js and TypeScript
- [ ] Create `apps/api` using FastAPI and Python
- [ ] Create shared schema package
- [ ] Create versioned prompt directory
- [ ] Create evaluation fixtures directory
- [ ] Create worker directories
- [ ] Add formatting and linting configuration

## Database

- [ ] Enable pgvector
- [ ] Create `profiles` table
- [ ] Create `opportunities` table
- [ ] Create `requirements` table
- [ ] Create `sources` and `evidence` tables
- [ ] Create `entities` table
- [ ] Create `relationships` table
- [ ] Create `assessments` table
- [ ] Create `actions` table
- [ ] Create `memories` table
- [ ] Add timestamps and provenance fields
- [ ] Add database migrations
- [ ] Add canonical-URL and duplicate constraints

## API foundation

- [ ] Add health endpoint
- [ ] Add structured error responses
- [ ] Add configuration validation
- [ ] Add database session management
- [ ] Add request and tool-call logging
- [ ] Add secret redaction to logs
- [ ] Add basic authentication/session strategy

## Minimal interface

- [ ] Create landing/onboarding screen
- [ ] Create dashboard shell
- [ ] Create opportunity-card component
- [ ] Create opportunity-detail screen
- [ ] Create loading, empty and error states

## Phase exit check

- [ ] Web and API run locally
- [ ] Database migrations run from a clean database
- [ ] A validated extraction can be stored and displayed

---

# Phase 3 — Autonomous discovery and verification

**Target:** October 10–12  
**Outcome:** Reach AI finds opportunities without requiring the user to paste URLs.

## Watchlist generation

- [ ] Convert confirmed profile goals into saved search themes
- [ ] Generate multiple narrow search queries per theme
- [ ] Store watchlists and search history
- [ ] Allow users to pause or edit watchlists
- [ ] Add location and funding constraints
- [ ] Add minimum preparation-time constraint
- [ ] Add a small serendipity percentage for adjacent opportunities

## Tavily discovery

- [ ] Implement `search_opportunities`
- [ ] Store discovery source and timestamp
- [ ] Find the likely official page
- [ ] Reject obviously expired results
- [ ] Extract source content for Nemotron
- [ ] Respect source and rate limitations
- [ ] Add backoff and degraded-source handling

## Verification

- [ ] Implement `find_official_source`
- [ ] Implement `verify_opportunity`
- [ ] Compare aggregator and official-page deadlines
- [ ] Preserve timezone and application-cycle context
- [ ] Assign source-confidence levels
- [ ] Flag conflicts rather than silently resolving them
- [ ] Record `last_verified_at`
- [ ] Store structured snapshots for future change detection

## Deduplication

- [ ] Normalize canonical URLs
- [ ] Match organization and normalized title
- [ ] Detect reposts from aggregators
- [ ] Distinguish a new annual cycle from a duplicate
- [ ] Provide a manual merge/review state for uncertainty

## Scheduled jobs

- [ ] Create daily discovery job
- [ ] Create reverification job
- [ ] Set safe per-run query and model budgets
- [ ] Log run status and partial failures
- [ ] Prevent one failed source from failing the full scan

## Phase exit check

- [ ] A confirmed profile produces its own watchlists
- [ ] A scheduled/manual scan discovers real opportunities
- [ ] At least one conflict or missing fact is surfaced correctly
- [ ] Duplicate records do not clutter the feed

---

# Phase 4 — Personal profile, eligibility and scoring

**Target:** October 13–17  
**Outcome:** Each opportunity receives a trustworthy, explainable personal assessment.

## Profile creation

- [ ] Support résumé upload
- [ ] Extract structured education, skills, projects and experience
- [ ] Ask users to confirm extracted information
- [ ] Collect citizenship/residency only when relevant and voluntarily provided
- [ ] Collect preferred opportunity types
- [ ] Collect funding and location preferences
- [ ] Collect current goals and time constraints
- [ ] Version confirmed profiles

## Eligibility firewall

- [ ] Convert hard requirements into machine-evaluable rules
- [ ] Implement age checks
- [ ] Implement citizenship/residency checks
- [ ] Implement education-level checks
- [ ] Implement location checks
- [ ] Implement application-open checks
- [ ] Return `needs_confirmation` when evidence is insufficient
- [ ] Prevent fit score from overriding ineligibility
- [ ] Display failed and unresolved requirements clearly

## Fit scoring

- [ ] Define weighted scoring rubric
- [ ] Score career/research alignment
- [ ] Score skills alignment
- [ ] Score experience evidence
- [ ] Score strategic value
- [ ] Score explicit user preferences
- [ ] Attach supporting profile and opportunity evidence
- [ ] Show confidence and unknowns

## Readiness scoring

- [ ] Detect required documents
- [ ] Check available profile/application assets
- [ ] Assess portfolio evidence
- [ ] Assess recommendation readiness
- [ ] Calculate practical preparation time
- [ ] Estimate application effort
- [ ] Calculate deadline risk
- [ ] Generate evidence-gap recommendations

## Phase exit check

- [ ] Eligibility is deterministic and auditable
- [ ] Fit and readiness are separate
- [ ] Every displayed reason links to profile or source evidence
- [ ] The interface never presents an unsupported acceptance probability

---

# Phase 5 — Agent memory and personalization

**Target:** October 16–18  
**Outcome:** Reach AI improves across sessions without turning inferred memories into unquestioned facts.

## Memory integration

- [ ] Select Memori or Mem0
- [ ] Connect memory to the selected agent runtime
- [ ] Keep PostgreSQL as the canonical system of record
- [ ] Define memory types
- [ ] Capture explicit preferences
- [ ] Capture inferred preferences separately
- [ ] Capture dismissal reasons
- [ ] Capture application outcomes
- [ ] Add confidence and provenance
- [ ] Add timestamps and expiration/decay
- [ ] Add sensitivity labels

## Memory Center

- [ ] Show what Reach AI remembers
- [ ] Show whether each memory was stated or inferred
- [ ] Show supporting evidence
- [ ] Allow confirm, correct and delete
- [ ] Allow users to prevent a memory from being used in outreach
- [ ] Add “forget this interaction” control

## Learning safeguards

- [ ] Distinguish “not interested” from “not enough time”
- [ ] Prevent one dismissal from becoming a permanent preference
- [ ] Ensure confirmed profile data outranks inferred memory
- [ ] Test retrieval for conflicting memories
- [ ] Test expired-memory behavior

## Phase exit check

- [ ] Preferences persist across sessions
- [ ] Users can inspect and delete memories
- [ ] Inferred memory cannot overwrite confirmed facts

---

# Phase 6 — Relationship intelligence

**Target:** October 18–20  
**Outcome:** Reach AI connects opportunities to the people and work that make them strategically meaningful.

## Entity enrichment

- [ ] Implement `research_entities`
- [ ] Identify relevant program staff, researchers and labs
- [ ] Find recent public work and publications
- [ ] Store facts with source and timestamp
- [ ] Distinguish verified facts from model inference
- [ ] Build opportunity-to-entity relationships
- [ ] Avoid sensitive or private-person data

## Relevance reasoning

- [ ] Compare publications with user projects and goals
- [ ] Explain why an entity is relevant
- [ ] Add confidence level
- [ ] Reject weak or coincidental connections
- [ ] Show source links in the interface

## Outreach justification

- [ ] Answer “Why this person?”
- [ ] Answer “Why now?”
- [ ] Identify the specific shared relevance
- [ ] Define a reasonable request
- [ ] Check whether the answer is already public
- [ ] Suppress outreach when no legitimate reason exists

## Phase exit check

- [ ] At least one opportunity displays a sourced entity graph
- [ ] Relevant publications are connected to actual profile evidence
- [ ] Outreach is recommended only when justified

---

# Phase 7 — Strategy and approval-gated action

**Target:** October 20–22  
**Outcome:** Reach AI turns intelligence into useful next steps without taking control away from the user.

## Strategy brief

- [ ] Rank opportunities by fit, readiness, urgency and effort
- [ ] Account for the user's available application time
- [ ] Reuse overlapping application assets
- [ ] Recommend apply, prepare, monitor or skip
- [ ] Generate a daily/weekly brief with Nemotron Ultra
- [ ] Explain why each recommendation was made

## Application plan

- [ ] Generate requirement checklist
- [ ] Work backward from official deadline
- [ ] Add practical deadlines for recommendations and documents
- [ ] Add submission buffer
- [ ] Identify the next smallest useful action

## Gmail and Calendar

- [ ] Configure Google OAuth
- [ ] Request only required scopes
- [ ] Read relevant messages only when authorized
- [ ] Prepare Gmail drafts without send permission
- [ ] Propose Calendar events
- [ ] Require approval before creating an event
- [ ] Store approval and execution receipts

## Action policy

- [ ] Classify actions by risk level
- [ ] Allow public research automatically
- [ ] Require confirmation for profile changes
- [ ] Require explicit approval for external writes
- [ ] Prevent email sending in the MVP
- [ ] Display tool failures honestly

## Phase exit check

- [ ] Reach AI creates a useful opportunity strategy
- [ ] It prepares at least one grounded email draft
- [ ] It proposes at least one calendar action
- [ ] Nothing external happens without the required approval

---

# Phase 8 — Product polish and deployment

**Target:** October 23–26  
**Outcome:** A coherent public product, not merely a collection of technical endpoints.

## Experience

- [ ] Complete onboarding flow
- [ ] Complete opportunity feed
- [ ] Complete opportunity-detail page
- [ ] Add eligibility, fit and readiness visualization
- [ ] Add evidence drawer
- [ ] Add people and publication section
- [ ] Add action approval queue
- [ ] Add Memory Center
- [ ] Add settings and data controls
- [ ] Add clear empty, loading and failure states
- [ ] Check mobile responsiveness
- [ ] Check keyboard accessibility
- [ ] Check color contrast

## Deployment

- [ ] Deploy web application
- [ ] Deploy FastAPI backend
- [ ] Deploy PostgreSQL database
- [ ] Configure secure production secrets
- [ ] Deploy scheduled jobs
- [ ] Add health monitoring
- [ ] Add safe model and search budgets
- [ ] Test production OAuth redirects
- [ ] Test using a clean browser session

## Resilience

- [ ] Tavily failure does not crash the dashboard
- [ ] Model timeout produces a retryable state
- [ ] Invalid extraction cannot enter canonical records
- [ ] Scheduled jobs are idempotent
- [ ] Partial results are labelled correctly
- [ ] Sensitive values are redacted from logs

## Phase exit check

- [ ] Public demo URL works
- [ ] A new user can complete the full MVP journey
- [ ] The interface clearly demonstrates Personal AI memory and control

---

# Phase 9 — Evaluation and judge readiness

**Target:** October 27–28  
**Outcome:** Evidence that Reach AI works reliably, uses sponsor technology meaningfully and solves the stated problem.

## Automated and manual evaluation

- [ ] Run extraction evaluation suite
- [ ] Run eligibility-rule tests
- [ ] Run deadline and timezone tests
- [ ] Run duplicate-detection tests
- [ ] Run memory-precedence tests
- [ ] Run approval-policy tests
- [ ] Record average latency
- [ ] Record average model/search cost
- [ ] Document known limitations

## Target metrics

- [ ] 100% schema-valid stored opportunity records
- [ ] 100% hard eligibility checks traceable to a rule and evidence
- [ ] 100% displayed deadlines include source and verification timestamp
- [ ] 0 external actions without required approval
- [ ] 0 real secrets committed to the repository
- [ ] At least 10 representative evaluation cases

## Judge-facing proof

- [ ] Document where Nemotron Nano is used
- [ ] Document where Nemotron Super is used
- [ ] Document where Nemotron Ultra is used
- [ ] Document Token Factory integration
- [ ] Document Nebius Serverless Jobs integration
- [ ] Document NemoClaw/OpenShell or explain the final secure-runtime choice
- [ ] Document Tavily search and verification use
- [ ] Show evidence provenance and audit receipts
- [ ] Prepare specific impact story for students and early-career applicants

## Phase exit check

- [ ] The happy-path demo is repeatable
- [ ] At least one failure case is demonstrated honestly
- [ ] Every sponsor integration performs a real product function

---

# Phase 10 — Submission

**Target:** October 29–30  
**Outcome:** A complete Devpost submission delivered before the deadline.

## Repository

- [ ] Confirm repository is public
- [ ] Confirm MIT license is visible at repository root
- [ ] Confirm README setup instructions work from a fresh clone
- [ ] Add architecture diagram
- [ ] Add final screenshots and product GIF
- [ ] Add deployed-demo link
- [ ] Add demo-video link
- [ ] Add test/evaluation summary
- [ ] Remove dead links and placeholders
- [ ] Check repository for secrets

## Demo video — maximum three minutes

- [ ] Write final video script
- [ ] Show the user problem immediately
- [ ] Show profile onboarding
- [ ] Show autonomous opportunity discovery
- [ ] Show an official-source conflict being caught
- [ ] Show eligibility, fit and readiness
- [ ] Show relevant person/publication connection
- [ ] Show approval-gated action
- [ ] Show memory controls and audit evidence
- [ ] Show Nebius/NVIDIA usage clearly
- [ ] Record clean voiceover
- [ ] Add captions
- [ ] Upload publicly to YouTube
- [ ] Verify playback without authentication

## Devpost entry

- [ ] Select Personal AI track
- [ ] Add project description
- [ ] Explain the real audience and problem
- [ ] Explain how Reach AI works
- [ ] Add working-demo URL
- [ ] Add public repository URL
- [ ] Add public video URL
- [ ] Explain Nemotron usage
- [ ] Explain Token Factory and Nebius usage
- [ ] Explain Tavily usage
- [ ] Add feedback on sponsor tools
- [ ] Disclose any pre-existing components and hackathon-period updates
- [ ] Review official rules once more
- [ ] Submit before October 30 at 6:00 p.m. GMT+1
- [ ] Reopen the submission and confirm every link works

---

## 🧱 Critical path

These items determine whether the project can succeed. Work on them before visual extras.

1. [ ] Nebius authentication and first Nemotron response
2. [ ] Schema-valid opportunity extraction
3. [ ] Official-source discovery and verification
4. [ ] Deterministic eligibility engine
5. [ ] Explainable fit/readiness assessment
6. [ ] Complete profile → discovery → assessment → action loop
7. [ ] Public deployment
8. [ ] Repeatable three-minute demo
9. [ ] Valid Devpost submission

---

## 🌟 Stretch goals

Only begin these after the complete MVP works.

- [ ] Browser extension for one-click capture
- [ ] Email newsletter forwarding address
- [ ] Opportunity portfolio optimizer based on available weekly hours
- [ ] Historical application-outcome calibration
- [ ] Change alerts for funding and requirements
- [ ] Multiple résumé/profile variants
- [ ] Recommendation-letter workflow
- [ ] Exportable application package
- [ ] Voice brief
- [ ] Multi-language opportunity summaries
- [ ] Collaborative mentor/advisor view

---

## ⚠️ Risk register

| Risk | Early warning | Mitigation | Status |
| --- | --- | --- | --- |
| Nemotron does not return reliable JSON | Invalid or invented fields in initial tests | Pydantic validation, constrained prompt, repair pass and rejection state | ⚪ |
| Too many services slow development | Integration work exceeds core-feature work | Keep FastAPI as the stable core; add integrations one at a time | ⚪ |
| Autonomous search becomes expensive | High query/model use per scan | Query budgets, deduplication and tiered model routing | ⚪ |
| Aggregators provide wrong facts | Official and secondary pages disagree | Official-source precedence and visible conflict state | ⚪ |
| Memory creates false preferences | One action changes future ranking too strongly | Confidence, expiry, provenance and user confirmation | ⚪ |
| OAuth review blocks production | Google integration cannot be approved in time | Demo with test users; retain manual download/draft fallback | ⚪ |
| Serverless integration is delayed | Jobs cannot be deployed reliably | Keep a manual scan trigger and local scheduled-worker fallback | ⚪ |
| Scope grows beyond deadline | Core loop remains incomplete after Oct 20 | Freeze new features; complete critical path only | ⚪ |
| Live demo fails | External service outage or rate limit | Seed a verified demo account and record fallback footage | ⚪ |
| Name conflict creates distraction | More branding work replaces product work | Keep Reach AI through submission; revisit afterward | ✅ |

---

## 📅 Daily stand-up template

Copy this block into an issue or project note each day:

```markdown
### Date: YYYY-MM-DD

**Yesterday**
- [ ]

**Today**
- [ ]

**Blocked by**
- None

**Proof completed**
- Test, screenshot, commit or deployed URL:

**Next critical-path item**
- [ ]
```

---

## ✅ Release checklist

### Product

- [ ] Full MVP journey works
- [ ] No obvious broken UI states
- [ ] Important claims show evidence
- [ ] Eligibility cannot be overridden by a fit score
- [ ] User approval controls work
- [ ] Memory is inspectable and deletable

### Engineering

- [ ] Tests pass
- [ ] Migrations run cleanly
- [ ] Logs redact secrets and personal data
- [ ] Jobs are idempotent
- [ ] Production environment variables are configured
- [ ] Error monitoring is enabled

### Submission

- [ ] Demo URL works publicly
- [ ] Repository is public
- [ ] License is visible
- [ ] README is current
- [ ] Video is public and under three minutes
- [ ] Devpost description matches the shipped product
- [ ] Sponsor integrations are clearly demonstrated

---

## 🌅 Progress principle

> A smaller system that completes the entire journey is more valuable than a larger system made of disconnected features.

When choosing what to build next, prioritize:

1. **Does it complete the user loop?**
2. **Can it be demonstrated clearly?**
3. **Does it make the recommendation more trustworthy?**
4. **Does it strengthen the Personal AI story?**
5. **Can it be finished and tested before submission?**

Every checked box is evidence that Reach AI is moving from an idea toward a system that can help someone discover their next chapter. 🚀
