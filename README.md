<div align="center">

# 🌍 Reach AI

### A private opportunity intelligence agent

<p>
  <strong>Discover what is possible. Understand your fit. Take the next step.</strong>
</p>

![Reach AI progress](docs/assets/reach-ai-progress.gif)

<p>
  <img alt="Hackathon" src="https://img.shields.io/badge/Nebius%20×%20NVIDIA-Global%20AI%20Hackathon-76B900?style=for-the-badge&logo=nvidia&logoColor=white">
  <img alt="Track" src="https://img.shields.io/badge/Track-Personal%20AI-6C63FF?style=for-the-badge">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge">
  <img alt="Status" src="https://img.shields.io/badge/Status-Building%20in%20Public-F59E0B?style=for-the-badge">
</p>

<p>
  <a href="#-the-problem">Problem</a> •
  <a href="#-what-reach-ai-does">Solution</a> •
  <a href="#-how-it-works">How it works</a> •
  <a href="#%EF%B8%8F-architecture">Architecture</a> •
  <a href="#-quick-start">Quick start</a> •
  <a href="#%EF%B8%8F-roadmap">Roadmap</a>
</p>

</div>

---

## ✨ The vision

Talent is everywhere. Access to the right opportunity is not.

Fellowships, grants, internships, research programs, hackathons and open-source programs are scattered across thousands of websites, newsletters, university pages and social posts. Finding a listing is only the beginning. Applicants still have to determine whether it is legitimate, whether they are eligible, whether it is worth their time, who is behind it and what they should do next.

**Reach AI turns that fragmented search into a private, always-on opportunity strategy.**

It does not simply return more links. It discovers opportunities automatically, verifies critical details against official sources, connects programs to the people and work behind them, evaluates them against the user's private profile and recommends a grounded next action.

> The goal is not to apply everywhere. The goal is to move confidently toward the opportunities that can genuinely change your trajectory.

---

## 💡 The problem

Opportunity discovery is noisy and unequal:

- Promising programs are distributed across disconnected sources.
- Aggregator pages can contain outdated deadlines or incomplete requirements.
- A person may look like a strong match but fail one hard eligibility condition.
- Generic recommendation engines rarely explain *why* something fits.
- Applicants do not know which lab, researcher, publication or program contact matters.
- Deadlines hide earlier practical deadlines for references, transcripts and work samples.
- Existing tools make people manage lists instead of helping them make decisions.

The result is missed deadlines, wasted applications and talented people never seeing the paths available to them.

---

## 🚀 What Reach AI does

Reach AI creates a continuous loop from **discovery to decision to action**.

### 🔭 Discovers

- Builds autonomous watchlists from the user's goals and constraints
- Searches for fellowships, grants, internships, research programs, hackathons and other programs
- Monitors selected organizations, labs, researchers and topics
- Reads opportunity emails and newsletters when the user chooses to connect them

### ✅ Verifies

- Locates the official source
- Cross-checks deadlines, requirements and application status
- Preserves timezone information
- Flags conflicting or missing details instead of guessing
- Detects expired listings, duplicates and new annual cycles

### 🧭 Evaluates

- Applies deterministic rules to hard eligibility requirements
- Calculates explainable strategic-fit and application-readiness scores
- Identifies evidence from the user's résumé, projects and experience
- Surfaces missing documents, skills and portfolio evidence
- Estimates deadline risk and application effort

### 🕸️ Connects

- Researches relevant people, labs and organizations
- Finds recent publications and projects related to the opportunity
- Builds sourced relationships between opportunities and entities
- Explains why a person or publication is relevant before suggesting outreach

### ⚡ Acts—with permission

- Generates application checklists and preparation timelines
- Drafts grounded outreach using verified context
- Prepares Gmail drafts
- Proposes Calendar events
- Records an execution receipt for every approved action

**Reach AI researches autonomously. External actions remain approval-gated.**

---

## 🎬 Demo

> 🚧 The working demo is being built for the Nebius × NVIDIA Global AI Hackathon.

<!-- Replace this path with the final recorded product GIF. -->
<!-- ![Reach AI product demo](docs/assets/reach-ai-demo.gif) -->

The final demo will show Reach AI:

1. Learning a user profile from a résumé and confirmed preferences
2. Creating its own opportunity-monitoring plan
3. Discovering opportunities without requiring pasted URLs
4. Catching a conflicting or outdated deadline
5. Separating eligibility, fit and readiness
6. Connecting an opportunity to a relevant person and recent publication
7. Preparing an application plan and grounded outreach draft
8. Requesting approval before creating any external action

**Live demo:** Coming soon  
**Demo video:** Coming soon

---

## 🔄 How it works

```mermaid
flowchart TD
    P["Private profile and goals"] --> W["Autonomous watchlists"]
    W --> D["Continuous discovery"]
    D --> V["Verify and deduplicate"]
    V --> I["Eligibility, fit and readiness"]
    I --> R["People and research intelligence"]
    R --> A["Approval-gated action"]
    A --> F["Outcome feedback and memory"]
    F --> W
```

### A result should answer five questions

| Question | Reach AI response |
| --- | --- |
| Can I apply? | Deterministic eligibility result with unresolved conditions |
| Is it worth applying? | Explainable fit, readiness, effort and deadline risk |
| Why does it match me? | Evidence connected to the user's confirmed profile |
| Who and what should I know? | Relevant people, labs, organizations and publications |
| What should I do next? | Prioritized, approval-controlled action plan |

---

## 🧠 Intelligence model

Reach AI keeps three concepts separate:

### Eligibility

A rule-based result for hard requirements such as citizenship, residency, education, age, location and application status.

Possible states:

- `eligible`
- `likely_eligible`
- `needs_confirmation`
- `ineligible`

### Strategic fit

An explainable score based on:

- Career or research alignment
- Skills alignment
- Experience evidence
- Strategic value
- Explicit user preferences

### Application readiness

A separate score based on:

- Required documents
- Portfolio evidence
- Recommendation readiness
- Available preparation time
- Profile completeness

This prevents a high-fit opportunity from being mistaken for an easy or immediately ready application.

---

## 🏗️ Architecture

```mermaid
flowchart TD
    UI["Next.js interface"] --> API["FastAPI backend"]
    API --> AG["Personal agent runtime"]
    AG --> MR["Nemotron model router"]
    AG --> TL["Reach AI tools"]

    TL --> TV["Tavily web intelligence"]
    TL --> GC["Gmail and Calendar"]
    TL --> DB["Postgres and pgvector"]
    TL --> MM["Agent memory"]
    TL --> OS["OpenShell sandbox"]

    JOB["Nebius Serverless Jobs"] --> AG
    MR --> TF["Nebius Token Factory"]
```

### Technology stack

| Layer | Technology | Purpose |
| --- | --- | --- |
| Interface | Next.js + TypeScript | Onboarding, dashboard, approvals and memory controls |
| Application API | FastAPI + Python | Business rules, scoring, authorization and agent tools |
| Agent runtime | Hermes Agent with NemoClaw/OpenShell | Planning, tool use and secured execution |
| Models | NVIDIA Nemotron on Nebius Token Factory | Extraction, reasoning, research and briefs |
| System of record | PostgreSQL | Profiles, opportunities, requirements, evidence and actions |
| Semantic retrieval | pgvector | Profile-to-opportunity and evidence retrieval |
| Agent memory | Memori or Mem0 | Preferences, feedback and longitudinal personalization |
| Background work | Nebius Serverless Jobs | Discovery, reverification and change detection |
| Web intelligence | Tavily Search and Extract | Current discovery and official-source verification |
| Integrations | Gmail and Google Calendar | Read-only context, drafts and proposed events |

### Model routing

| Workload | Default route |
| --- | --- |
| Structured extraction and triage | Nemotron Nano |
| Classification and deduplication | Nemotron Nano |
| Hard eligibility rules | Deterministic Python |
| Profile comparison and source conflicts | Nemotron Super |
| People and publication research | Nemotron Super + Tavily |
| High-value strategy briefs | Nemotron Ultra |

The most capable model is reserved for the few decisions that need it. Routine scanning remains fast and credit-efficient.

---

## 🔐 Privacy and control

Reach AI is designed for the **Personal AI** track, so privacy is part of the product—not a footer.

- PostgreSQL remains the authoritative source for verified facts.
- Agent memory stores preferences and interaction patterns, not unchecked truth.
- Every inferred memory includes confidence, provenance and a timestamp.
- Users can inspect, correct and delete remembered information.
- Sensitive profile fields are excluded from outreach by default.
- Gmail sending permission is not required for the MVP.
- Calendar changes require explicit approval.
- Every external action produces an audit receipt.

### Trust precedence

```text
User-confirmed profile
    > officially verified facts
    > explicit recent feedback
    > inferred agent memory
```

### Action policy

| Action | Policy |
| --- | --- |
| Search public sources | Automatic |
| Extract and classify an opportunity | Automatic |
| Save a discovered opportunity | Automatic |
| Prepare a checklist | Automatic |
| Create an email draft | Prepare, then notify |
| Send an email | Explicit approval |
| Create a calendar event | Explicit approval |
| Change a confirmed profile fact | Confirmation required |

---

## 🧩 Core data model

```mermaid
erDiagram
    PROFILE ||--o{ ASSESSMENT : receives
    OPPORTUNITY ||--o{ ASSESSMENT : evaluated_as
    OPPORTUNITY ||--o{ REQUIREMENT : contains
    OPPORTUNITY ||--o{ EVIDENCE : supported_by
    OPPORTUNITY }o--o{ ENTITY : connected_to
    PROFILE ||--o{ MEMORY : personalizes
    ASSESSMENT ||--o{ ACTION : recommends
```

Core objects:

- **Profile:** confirmed skills, goals, projects, constraints and preferences
- **Opportunity:** canonical program record and verified application state
- **Requirement:** structured hard or soft condition with supporting evidence
- **Entity:** person, lab, organization or publication
- **Relationship:** sourced connection between two entities
- **Assessment:** eligibility, fit, readiness, risk and explanation
- **Memory:** stated or inferred preference with provenance and expiration
- **Action:** approval state, payload and execution receipt

---

## 🛠️ Repository structure

```text
reach-ai/
├── apps/
│   ├── web/                 # Next.js interface
│   └── api/                 # FastAPI application
├── packages/
│   ├── schemas/             # Shared opportunity and profile schemas
│   ├── scoring/             # Eligibility, fit and readiness logic
│   └── prompts/             # Versioned extraction and reasoning prompts
├── workers/
│   ├── discovery/           # Scheduled opportunity scans
│   ├── verification/        # Reverification and change detection
│   └── enrichment/          # People, labs and publication research
├── evals/
│   ├── fixtures/            # Representative opportunity postings
│   └── tests/               # Extraction and decision-quality evaluations
├── docs/
│   └── assets/              # Images, diagrams and demo GIFs
├── infra/                   # Deployment and job configuration
├── .env.example
├── LICENSE
└── README.md
```

---

## ⚡ Quick start

### Prerequisites

- Python 3.11+
- Node.js 22+
- PostgreSQL with pgvector
- Nebius Token Factory credentials
- Tavily API credentials
- Optional Google OAuth credentials

### 1. Clone the repository

```bash
git clone https://github.com/BLVCK-MAMBA-6/reach-ai.git
cd reach-ai
```

### 2. Configure environment variables

```bash
cp .env.example .env
```

```dotenv
NEBIUS_API_KEY=
NEBIUS_BASE_URL=
NEMOTRON_NANO_MODEL=
NEMOTRON_SUPER_MODEL=
NEMOTRON_ULTRA_MODEL=

TAVILY_API_KEY=
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/reach_ai

GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
GOOGLE_REDIRECT_URI=
```

Never commit real credentials.

### 3. Start the API

```bash
cd apps/api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Start the web application

```bash
cd apps/web
npm install
npm run dev
```

Open `http://localhost:3000`.

> Setup commands will be updated as the implementation stabilizes.

---

## 🧪 Evaluation

Reach AI is tested against realistic failure cases:

- Conflicting deadlines
- Missing timezones
- Closed or expired applications
- Citizenship and residency exclusions
- Ambiguous education requirements
- Duplicate aggregator listings
- New cycles of recurring opportunities
- Missing official sources
- Weak person-to-opportunity connections
- Unsupported outreach claims

Key measurements:

| Metric | Why it matters |
| --- | --- |
| JSON-schema validity | Downstream tools require predictable output |
| Field extraction accuracy | Prevents corrupted opportunity records |
| Deadline accuracy | Avoids costly missed applications |
| Eligibility accuracy | Prevents wasted effort |
| Evidence coverage | Makes recommendations auditable |
| Duplicate-detection accuracy | Keeps the opportunity feed clean |
| Tool latency and model cost | Keeps continuous monitoring sustainable |

---

## 🗺️ Roadmap

### Phase 1 — Foundation

- [x] Define the product and Personal AI track
- [x] Design the core architecture
- [x] Create the public repository
- [ ] Validate Nemotron structured extraction
- [ ] Add schema validation and evidence spans

### Phase 2 — Discovery

- [ ] Generate profile-based watchlists
- [ ] Add scheduled Tavily discovery
- [ ] Find and verify official sources
- [ ] Deduplicate opportunity records
- [ ] Detect deadline and requirement changes

### Phase 3 — Personal intelligence

- [ ] Extract and confirm user profiles
- [ ] Implement the eligibility firewall
- [ ] Implement explainable fit scoring
- [ ] Implement application-readiness scoring
- [ ] Add editable agent memory

### Phase 4 — Relationships and action

- [ ] Connect opportunities to people, labs and publications
- [ ] Add evidence-gap analysis
- [ ] Generate weekly opportunity strategy
- [ ] Prepare grounded outreach drafts
- [ ] Add approval-gated Calendar actions

### Phase 5 — Ship

- [ ] Deploy the public demo
- [ ] Complete evaluation suite
- [ ] Record the three-minute video
- [ ] Publish setup documentation
- [ ] Submit to Devpost

---

## 🏆 Hackathon alignment

Reach AI is being built for the **Personal AI Track** of the Nebius × NVIDIA Global AI Hackathon.

### NVIDIA

- Nemotron Nano for extraction and high-volume triage
- Nemotron Super for routine reasoning and enrichment
- Nemotron Ultra for high-value strategy generation
- NemoClaw/OpenShell for secure personal-agent execution

### Nebius

- Token Factory for Nemotron inference
- Serverless Jobs for scheduled discovery and reverification

### Tavily

- Search and extraction for autonomous discovery
- Official-source verification
- People, lab and publication research
- Current-information grounding

---

## 🌱 Why this matters

Reach AI is for the student who never heard about the fellowship, the researcher who discovered the grant too late, the early-career builder who could not tell whether they qualified and the talented applicant whose network did not expose them to the right room.

Progress often begins with one opening:

- one program that funds the next degree,
- one lab that recognizes the research,
- one mentor who replies,
- one internship that creates a career,
- one application submitted before the deadline.

**Reach AI exists to help people see that opening—and take the next step with confidence.** 🌅

---

## 🤝 Contributing

Reach AI is currently under active hackathon development. Issues, evaluation cases and thoughtful pull requests are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Add or update tests.
4. Open a pull request explaining the problem and the change.

Please do not commit private résumés, emails, API keys or personally identifiable test data.

---

## 📜 License

Released under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

Built with open models and infrastructure from NVIDIA and Nebius, web intelligence from Tavily, and the belief that access to life-changing opportunities should not depend on already knowing where to look.

<div align="center">

### 🌍 Reach AI

**Find what is within reach—and what could be.**

⭐ Star the repository to follow the journey.

</div>
