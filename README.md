<p align="center">
  <img src="docs/assets/hero.svg" width="100%" alt="Expunge-OPS: Autonomous customer data erasure orchestration across PostgreSQL and Object Storage with LangGraph AI agents, sandbox rehearsal, human approval gate, and cryptographic SHA-256 proof.">
</p>

<p align="center">
  <a href="https://github.com/Yug-dev0/Expunge-OPS/actions/workflows/ci.yml"><img alt="CI Status" src="https://github.com/Yug-dev0/Expunge-OPS/actions/workflows/ci.yml/badge.svg"></a>
  <a href="https://github.com/Yug-dev0"><img alt="Author & Maker" src="https://img.shields.io/badge/Author%20%26%20Maker-Yug-00f2fe?logo=github&logoColor=white&labelColor=0d1117"></a>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-38bdf8?labelColor=0d1117"></a>
  <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-5.6-3178c6?logo=typescript&logoColor=white&labelColor=0d1117">
  <img alt="React" src="https://img.shields.io/badge/React-18-61dafb?logo=react&logoColor=0c1024&labelColor=0d1117">
  <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-16-4169e1?logo=postgresql&logoColor=white&labelColor=0d1117">
  <img alt="MinIO" src="https://img.shields.io/badge/MinIO-S3%20SigV4-c72e49?logo=minio&logoColor=white&labelColor=0d1117">
  <img alt="LangGraph" src="https://img.shields.io/badge/agents-LangGraph.js-10b981?logo=langchain&logoColor=white&labelColor=0d1117">
  <img alt="OpenAI gpt-5.5" src="https://img.shields.io/badge/OpenAI-gpt--5.5-f59e0b?logo=openai&logoColor=white&labelColor=0d1117">
  <img alt="Claude Supported" src="https://img.shields.io/badge/Claude-Opus--5.5-d97706?logo=anthropic&logoColor=white&labelColor=0d1117">
  <img alt="Voice commands" src="https://img.shields.io/badge/voice-Web%20Speech%20API-8b5cf6?labelColor=0d1117">
  <img alt="Tests" src="https://img.shields.io/badge/tests-194%20passed-10b981?logo=vitest&logoColor=white&labelColor=0d1117">
</p>

<h2 align="center">Expunge-OPS</h2>
<h3 align="center">Delete a customer from every system, and prove it.</h3>

<p align="center">
  <b>Expunge-OPS</b> is an autonomous enterprise privacy orchestration engine for GDPR, CCPA, and statutory "Right to Erasure" compliance. A team of LangGraph AI agents investigates customer footprints across PostgreSQL databases and S3 object storage, simulates actions in an isolated zero-harm sandbox, creates verified checksummed backups, halts for an operator to cryptographically approve <i>one canonical SHA-256 plan hash</i>, executes through guarded parameterization, and continuously rescans until zero personal data remains.
</p>

<p align="center">
  <a href="#-quick-start"><b>Quick Start</b></a> ·
  <a href="#-the-core-philosophy"><b>Why Expunge-OPS</b></a> ·
  <a href="#-lifecycle-of-an-erasure-request"><b>How It Works</b></a> ·
  <a href="#-multi-agent-swarm"><b>The Agents</b></a> ·
  <a href="#-the-5-immutable-safety-gates"><b>Safety Model</b></a> ·
  <a href="#-demo-customers--scenarios"><b>Demo Personas</b></a> ·
  <a href="#-console-tour"><b>Console Tour</b></a> ·
  <a href="#-architecture"><b>Architecture</b></a> ·
  <a href="#-http-rest-api--mcp-catalog"><b>API & MCP</b></a> ·
  <a href="#-author--maker"><b>Author</b></a>
</p>

<br>

<p align="center">
  <img src="docs/assets/showcase-3d.webp" width="100%" alt="Three console screens layered in 3D: the overview and a deletion plan in the onyx theme, and a certificate of erasure for CUST-1042 in the cream theme.">
</p>

---

## 💡 The Core Philosophy

In production applications, a **"Right to Erasure"** (GDPR Art. 17 / CCPA § 1798.105) request is never just `DELETE FROM users WHERE id = $1`.

In modern architectures, customer records are fragmented across dozens of relational tables, microservice schemas, and cloud object storage buckets. Some rows are legally mandated to be retained (tax legislation, anti-money laundering, active dispute holds), some records are shared across workspaces or foreign-key hierarchies, and post-deletion verification is almost universally absent.

> [!IMPORTANT]
> **Expunge-OPS treats data erasure like a zero-downtime, audited infrastructure migration.**
> Agents can investigate and prepare plans using strictly read-only tools. Only a named human operator can authorize an execution. Every action is bound to a single-use SHA-256 hash.

### Key Architectural Pillars

| Pillar | How Expunge-OPS Enforces It |
|---|---|
| **🤖 Read-Only AI Discovery** | LangGraph agents survey systems using strictly read-only MCP catalog tools. No agent has a delete tool in its schema, and the API gateway blocks destructive requests from agent contexts. |
| **📜 Versioned Retention Policy** | Every table and S3 bucket is governed by an explicit [statutory retention policy](packages/policy-engine/src/retention-policy.ts). Data is either `DELETE`, `REDACT`, or `RETAIN` with the exact legal basis recorded. |
| **🧪 Zero-Harm Sandbox Rehearsal** | Before any data changes, the deletion plan executes against an isolated simulation. On PostgreSQL, this runs in an active transaction that is **always rolled back**, verifying every foreign key constraint and cascade without persisting changes. |
| **📦 Verified Checksummed Backup** | Affected records are snapshotted prior to execution. Every row and object is immediately re-read and validated with SHA-256 checksums before the approval gate unlocks. |
| **🛡️ Cryptographic Human Gate** | An operator must type the exact customer ID (e.g., `CUST-1042`) to approve one canonical SHA-256 plan hash. Approvals are single-use, non-transferable, and time-boxed (default 15 minutes). |
| **🔍 Verifiable Rescan & Proof** | Following execution, every connector runs a live deep rescan. Zero residual personal data triggers a cryptographically sealed Certificate of Erasure. Any leftover data trips a hard failure and offers one-click rollback. |
| **🔏 Tamper-Evident Audit Chain** | Every event from discovery to certificate issuance is appended to a cryptographic SHA-256 hash chain, verifiable in real time via the API or console. |

---

## ⚡ Quick Start

### Prerequisites
- **Node.js**: `v20.12.0` or newer
- **Package Manager**: `npm` (v10+)
- **Docker & Docker Compose**: Optional (required only for PostgreSQL 16 & MinIO local infrastructure mode)

---

### Option A: Instant In-Memory Simulation (Zero Setup)

Expunge-OPS runs out of the box with zero external dependencies using its built-in in-memory stateful dataset:

```bash
# Clone the repository
git clone https://github.com/Yug-dev0/Expunge-OPS.git
cd Expunge-OPS

# Install monorepo dependencies
npm install

# Start both the API (port 3001) and Web Console (port 5173) concurrently
npm run dev
```

- **Web Console**: [http://localhost:5173](http://localhost:5173)
- **Operator Console**: [http://localhost:5173/console](http://localhost:5173/console)
- **API Health Check**: [http://localhost:3001/health](http://localhost:3001/health)

> [!TIP]
> In in-memory mode, discovery and deletion operations are fully functional: erasing a customer updates the active dataset, and post-erasure rescans prove 0 residual records. You can restore the original 8-customer demo dataset at any time by clicking **"Reset demo data"** in the sidebar.

---

### Option B: Full Production Docker Stack (PostgreSQL 16 + MinIO S3)

To rehearse against a real database with foreign-key rollback transactions and real S3 object storage with SigV4 signing:

```bash
# 1. Spin up PostgreSQL 16 and MinIO in the background
docker compose up -d

# 2. Seed the relational schema and buckets with the 8-customer fixture
npm run seed:local

# 3. Launch Expunge-OPS connected to the local Docker infrastructure
CONNECTOR_MODE=local npm run dev
```

In local connector mode:
- **PostgreSQL**: Runs with 13 tables, strict foreign keys, and audit triggers. The sandbox executes real SQL transactions with `ROLLBACK`.
- **MinIO S3**: Manages customer uploads across 3 buckets (`user-avatars`, `compliance-documents`, `audit-cold-storage`) using pure SigV4 signing (no bulky AWS SDKs).
- **Persistent Storage**: Add `ERASEROPS_PERSISTENCE=postgres` to persist all request states into the `eraseops_requests` PostgreSQL table.

---

### Option C: Enable AI Agents (OpenAI `gpt-5.5` or Anthropic Claude)

By default, Expunge-OPS runs on deterministic rule-based agent twins. To enable live reasoning:

```bash
# For OpenAI gpt-5.5 (Responses API, store: false)
echo 'OPENAI_API_KEY=sk-...' > .env
npm run dev

# Or for Anthropic Claude (claude-opus-5-5)
echo 'ANTHROPIC_API_KEY=sk-ant-...' > .env
npm run dev
```

When an API key is detected, the console badge displays **OpenAI · gpt-5.5** (or **Claude · claude-opus-5-5**). Without an API key, all workflows remain 100% operational via the deterministic twin engine.

---

### Option D: Run as an MCP Server (Cursor, Claude Desktop, Windsurf)

Expunge-OPS exposes its full discovery, dependency calculation, and rescan catalog as a Model Context Protocol (MCP) server over standard input/output:

```bash
npm run dev:mcp
```

Add this configuration to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "expunge-ops": {
      "command": "node",
      "args": ["/absolute/path/to/Expunge-OPS/apps/mcp-server/dist/index.js"]
    }
  }
}
```

---

## 🔄 Lifecycle of an Erasure Request

Every request flows through a strict 7-stage deterministic pipeline. No stage can be bypassed:

```mermaid
stateDiagram-v2
  direction LR
  [*] --> DISCOVERING: Customer ID / Voice Command
  DISCOVERING --> PLAN_READY: Footprint + Dependencies + Policy
  PLAN_READY --> SANDBOX_FAILED: Rehearsal finds FK/orphan harm
  PLAN_READY --> BACKING_UP: Rehearsal passes
  BACKING_UP --> AWAITING_HUMAN_APPROVAL: Backup verified & checksummed
  AWAITING_HUMAN_APPROVAL --> APPROVED: Operator types customer ID
  AWAITING_HUMAN_APPROVAL --> REJECTED: Operator rejects with reason
  APPROVED --> EXECUTING: Guarded execute (plan hash + token)
  EXECUTING --> VERIFYING_DELETION: Connectors run parameterized actions
  EXECUTING --> EXECUTION_FAILED: Transport or query error
  VERIFYING_DELETION --> COMPLETED: Active rescan finds 0 residual
  VERIFYING_DELETION --> VERIFICATION_FAILED: Personal data still detected
  EXECUTION_FAILED --> ROLLED_BACK: One-click restore from backup
  VERIFICATION_FAILED --> ROLLED_BACK: One-click restore from backup
  SANDBOX_FAILED --> [*]
  REJECTED --> [*]
  COMPLETED --> [*]
  ROLLED_BACK --> [*]
```

### Detailed Pipeline Breakdown

| # | Stage | Autonomous Agent Activity | Deterministic Protection & Evidence |
|:-:|---|---|---|
| **1** | **Discover** | Discovery Agent scans allowlisted connectors, maps foreign-key trees (e.g. `order_items` &rarr; `orders`), and catalogues S3 objects. | Emits an immutable footprint list containing exact resource IDs and counts. |
| **2** | **Classify** | Policy Engine maps each record to statutory rules (GDPR Art. 17, Art. 6(1)(c), Tax Code). | Assigns action (`DELETE`, `REDACT`, `RETAIN`) with recorded legal basis. Unclassified fields default to `RETAIN`. |
| **3** | **Rehearse** | Simulates the plan on an isolated environment. In PostgreSQL, executes inside a transaction that is always rolled back. | Fails immediately on foreign-key violations, shared organization ownership, or orphaned rows. |
| **4** | **Back Up** | Snapshots all rows and objects targeted for deletion or redaction. | Immediately reads back all backup records, computing and verifying SHA-256 hashes against the manifest. |
| **5** | **Approve** | The LangGraph execution pauses at a checkpoint (`interrupt()`). | Unlocks only when a named human operator types `CUST-xxxx` to approve the specific canonical plan hash. |
| **6** | **Execute** | Guarded route executes strictly the approved, parameterized operations. Connectors enforce rate limits per operator. | Compares planned counts against database affected-row counts. Mismatches trip safety alarms. |
| **7** | **Prove** | Every connector initiates an independent, active rescan across all tables and buckets. | 0 residual yields a tamper-evident Certificate of Erasure; any remaining data flags failure and enables rollback. |

---

## 🤖 Multi-Agent Swarm

Expunge-OPS features a [LangGraph.js](https://langchain-ai.github.io/langgraphjs/) state graph located in [`apps/api/src/agent/graph.ts`](apps/api/src/agent/graph.ts). Advanced LLMs drive the stages that require nuanced judgment, while all destructive or state-altering actions remain strictly deterministic and gated behind human approval.

```mermaid
flowchart TD
  UserPrompt(["Goal (Spoken or Typed)"]) --> IntakeAgent["Intake Agent<br/><i>Extracts intent & customer identifier</i>"]
  IntakeAgent --> DiscoveryAgent["Discovery Agent<br/><i>gpt-5.5 + read-only MCP catalog</i>"]
  DiscoveryAgent --> RiskEngine["Grounded Risk Engine<br/><i>Merges LLM analysis with hard database facts</i>"]
  RiskEngine -->|Erasure or Dry Run| PlannerAgent["Planner Agent<br/><i>Executes sandbox & verified backup</i>"]
  RiskEngine -->|Investigation Query| BriefingReporter["Reporter Agent<br/><i>Produces risk assessment briefing</i>"]
  PlannerAgent --> BriefingReporter
  BriefingReporter -->|Plan Ready| HumanCheckpoint{{"Human Checkpoint<br/><b>LangGraph interrupt()</b>"}}
  HumanCheckpoint -->|Operator types CUST-ID| GuardedExecutor["Guarded Executor<br/><i>Executes parameterized plan & triggers rescan</i>"]
  HumanCheckpoint -->|Operator denies| RejectionRecorder["Rejection Recorder<br/><i>Logs denial reason to audit chain</i>"]
  GuardedExecutor --> FinalReporter["Final Briefing<br/><i>Issues Certificate & Audit Proof</i>"]
  RejectionRecorder --> FinalReporter
```

### Grounded Agent Safety Guarantees

- **No Destructive Tools**: Agents interact solely with read-only MCP catalog tools (`discover_customer_postgres`, `calculate_dependencies`, `rescan_customer`). Destructive tools are neither defined in model schemas nor accepted at the MCP boundary.
- **Privacy-Preserving Context**: LLMs only see obfuscated metadata and masked names (`"Mira K."`), never unmasked emails, phone numbers, or credit card records.
- **Zero Model Retention (`store: false`)**: OpenAI calls explicitly set `store: false`. No prompt data or reasoning history is retained on OpenAI servers.
- **LangGraph Checkpoint Interruption**: When a deletion plan is prepared, the graph issues an `interrupt()`. Resuming requires passing the operator's verified identity and confirmation string.
- **Deterministic Rule Twins**: When `OPENAI_API_KEY` is not configured, or if the LLM encounters a network timeout or refusal, the graph immediately falls back to deterministic rule-based node twins. The system never crashes due to AI provider outages.

---

## 🛡️ The 5 Immutable Safety Gates

Expunge-OPS enforces a zero-trust execution perimeter. Bypassing any gate is architecturally prohibited:

```
[ Incoming Request ]
         │
         ▼
  ┌──────────────┐
  │ 1. Allowlists│ ──► Refuses unknown connectors, hosts, or production credentials
  └──────────────┘
         │
         ▼
  ┌──────────────┐
  │ 2. Agent Wall│ ──► Agents possess only read-only discovery tools; zero delete APIs
  └──────────────┘
         │
         ▼
  ┌──────────────┐
  │ 3. Rehearsal │ ──► PostgreSQL transaction rollback + verified read-back backup
  └──────────────┘
         │
         ▼
  ┌──────────────┐
  │ 4. Human Gate│ ──► Operator types CUST-ID; single-use canonical SHA-256 plan hash
  └──────────────┘
         │
         ▼
  ┌──────────────┐
  │ 5. Proof/Scan│ ──► Deep active rescan: 0 residual = Certificate; residual = Rollback
  └──────────────┘
```

1. **Connector & Environment Allowlists**: Connectors are restricted to configured schemas and buckets. `DEMO_MODE` must evaluate to `true`; requests targeting unallowlisted infrastructure are aborted before execution.
2. **Read-Only Model Boundary**: Agent execution contexts are strictly isolated. Destructive endpoints require an `x-operator-identity` header and a cryptographically valid approval token.
3. **Sandbox & Read-Back Backup**: Deletion cannot proceed without a successful rehearsal report. Backups are snapshotted and re-read from storage to verify SHA-256 hashes before approval is even made available.
4. **Canonical Single-Use Plan Hash**: Approvals are bound to `hash(canonical(plan))`. Modifying a single character of the plan invalidates the approval token. Approvals are strictly single-use and expire after `APPROVAL_TTL_MINUTES` (default 15 minutes).
5. **Mandatory Deep Rescan**: Claiming success without executing is impossible. Connectors perform a full independent query sweep post-execution; if any residual customer data is detected, the workflow fails and triggers rollback.

---

## 👥 Demo Customers & Scenarios

The synthetic dataset ([`infra/fixtures/demo-dataset.json`](infra/fixtures/demo-dataset.json)) contains 8 realistic customer personas across 13 PostgreSQL tables and 3 MinIO storage buckets. **No customer is hard-coded or special-cased in application code**; every behavior is derived from data relationships and policy definitions.

| Customer ID | Data Footprint & Scenario | Expected Workflow Outcome |
|---|---|---|
| `CUST-1042` | Profile, 2 addresses, orders, support tickets, analytics, 4 files in S3 | **Happy Path**: 9 records deleted, 3 redacted, 4 retained for statutory tax laws. 0 residual confirmed; Certificate issued. |
| `CUST-2088` | Two orders with payment records, three analytics events | **Rejection Path**: Ideal for testing operator rejection. Audit chain records the denial reason; zero data is altered. |
| `CUST-3175` | 12 analytics events, 5 support threads, 5 files across buckets | **Large Blast Radius**: Evaluates high-volume multi-table discovery. Demonstrates dry-run review before execution. |
| `CUST-4410` | Single login record and marketing profile | **Minimal Blast Radius**: PostgreSQL-only single-row deletion and immediate verification. |
| `CUST-7001` | S3 document stored in cold `ARCHIVE` storage class | **Backup Gate Blocker**: Archived objects cannot be immediately read back and checksummed; approval remains securely locked. |
| `CUST-9001` | Owner of shared workspace `ORG-501` with active co-members | **Sandbox Simulation Blocker**: Rehearsal detects that deleting the workspace would orphan records owned by `CUST-9002` and `CUST-9003`. Plan is blocked. |
| `CUST-9002` / `CUST-9003` | Non-owner members of workspace `ORG-501` | **Safe Erasure**: Only the individual's membership row is expunged; the shared workspace and co-members remain intact. |
| `CUST-5555` | Non-existent customer identifier | **Definitive 404**: Scans all allowlisted connectors and returns a detailed audit showing zero records found across all systems. |

---

## 🖥️ Console Tour

Expunge-OPS features a custom-built interface styled after high-security fiduciary printing (guilloche rosettes, gold-foil seals, dynamic redaction bars, and high-contrast typography).

<table>
  <tr>
    <td width="50%"><img src="docs/assets/screens/plan.webp" alt="Request workspace for CUST-1042 showing the deletion plan, color-coded by action, and the safety rail with type-to-confirm approval."><br><b>Plan & Safety Rail.</b> Real-time display of planned deletions, redactions, and retention holds with explicit statutory legal bases. Approval unlocks only when all safety checks are green.</td>
    <td width="50%"><img src="docs/assets/screens/certificate.webp" alt="Certificate of erasure with a guilloche rosette and a gold-foil Verified erased seal."><br><b>Certificate of Erasure.</b> Displays approver, plan hash, execution timestamp, zero-residual confirmation, and cryptographic audit hash. One-click export to print-ready PDF.</td>
  </tr>
  <tr>
    <td><img src="docs/assets/screens/graph-9001.webp" alt="Dependency graph for CUST-9001 showing the owned workspace referenced by two other customers' membership rows."><br><b>Dependency Graph.</b> Visualizing relational cascades. CUST-9001's workspace is flagged because other customers rely on it, blocking the sandbox.</td>
    <td><img src="docs/assets/screens/backup-7001.webp" alt="Backup tab for CUST-7001 explaining that an archived object blocked the backup."><br><b>Verified Backup Gate.</b> Shows row and object snapshots. For CUST-7001, an archived object cannot be read back, halting the pipeline before approval.</td>
  </tr>
  <tr>
    <td><img src="docs/assets/screens/sandbox.webp" alt="Sandbox tab listing the checks run against an isolated copy for each system."><br><b>Sandbox Simulation Report.</b> Complete breakdown of simulated changes, integrity checks, foreign key cascades, and isolation guarantees before touching real data.</td>
    <td><img src="docs/assets/screens/palette.webp" alt="Command bar with a dictated command and the system's plain-language reading of it."><br><b>Voice Command Bar (<kbd>⌘K</kbd>).</b> Speak or type natural language instructions. The assistant resolves names and dictates back its interpretation before opening a request.</td>
  </tr>
  <tr>
    <td><img src="docs/assets/screens/audit.webp" alt="Audit log with hash-chained events across all requests and a verified status banner."><br><b>Tamper-Evident Audit Log.</b> Append-only event log across all requests. Each event embeds the previous event's SHA-256 hash; any manual tampering breaks the verification chain.</td>
    <td><img src="docs/assets/screens/systems.webp" alt="Systems page showing live row counts per PostgreSQL table and object counts per MinIO bucket."><br><b>Systems Inventory.</b> Live connector telemetry across 13 tables and 3 S3 buckets. Watch table row counts drop and backup storage grow in real time.</td>
  </tr>
  <tr>
    <td><img src="docs/assets/screens/customers.webp" alt="Customers page with masked names, warm initial avatars, footprint bars and residual personal-data counts."><br><b>Customer Directory.</b> Masked customer identities with live footprint bars and real-time residual personal data counters.</td>
    <td><img src="docs/assets/screens/policies.webp" alt="Policies page with active limits, the five safety gates and the retention rules."><br><b>Retention Policies.</b> Live configuration display showing statutory retention rules, execution limits, rate-limit thresholds, and active safety gates.</td>
  </tr>
</table>

### Dual Design: Onyx & Vellum

The interface offers two meticulously crafted visual modes: **Onyx** (cyber obsidian dark mode) and **Vellum** (security paper cream with burnished gold accents). Both modes fully adhere to WCAG AA accessibility contrast standards.

<table>
  <tr>
    <td width="50%"><img src="docs/assets/screens/landing.webp" alt="Landing page in the onyx theme"><br><b>Onyx (Dark Mode).</b> Obsidian black with glowing cyan, emerald, and crimson status highlights.</td>
    <td width="50%"><img src="docs/assets/screens/landing-light.webp" alt="Landing page in the vellum theme"><br><b>Vellum (Light Mode).</b> High-grade cream security paper with burnished gold foil accents.</td>
  </tr>
</table>

<p align="center">
  <img src="docs/assets/mobile-3d.webp" width="85%" alt="Expunge-OPS responsive interface on mobile devices">
  <br><sub>Fully responsive layout optimized for desktop, tablet, and mobile displays.</sub>
</p>

---

## 🏗️ Architecture

```
                                  OPERATOR INTERFACES
                 ┌──────────────────────────────────────────────────┐
                 │  Web Console (React 18)   │   Voice Command Bar  │
                 │  MCP Stdio Client         │   REST API Clients   │
                 └─────────────────────────┬────────────────────────┘
                                           │
                                           ▼
                                 EXPUNGE-OPS API CORE
                 ┌──────────────────────────────────────────────────┐
                 │ • WorkflowService (State Machine & Guarded Path) │
                 │ • LangGraph Multi-Agent Swarm (OpenAI / Claude)  │
                 │ • Policy Engine (GDPR / Statutory Retention)     │
                 │ • Sandbox Rehearsal Engine (Simulation Checks)   │
                 │ • Backup Service (SHA-256 Verified Read-Back)    │
                 │ • Tamper-Evident SHA-256 Audit Chain Generator   │
                 └─────────────────────────┬────────────────────────┘
                                           │
                                           ▼
                                   CONNECTOR ADAPTERS
                 ┌──────────────────────────────────────────────────┐
                 │ • Mock In-Memory Connector (Zero-dependency)     │
                 │ • PostgreSQL Connector (Parameterized + Rollback)│
                 │ • MinIO S3 Connector (SigV4 Signed REST)         │
                 └──────────────────────────────────────────────────┘
```

### Monorepo Structure

```text
Expunge-OPS/
├── apps/
│   ├── api/             # Express API, WorkflowService, LangGraph agent swarm, guarded execution
│   ├── web/             # React 18, Vite, TailwindCSS, React Flow, Web Speech API console
│   └── mcp-server/      # Model Context Protocol server over stdio for external AI clients
├── packages/
│   ├── connectors/      # Schema registry, stateful mock dataset, PostgreSQL & MinIO adapters
│   ├── policy-engine/   # Retention policy rules, statutory holds, and execution preconditions
│   ├── sandbox/         # Plan simulation, foreign-key cascade checks, and isolation reports
│   ├── backup/          # Snapshot capture, SHA-256 manifest calculation, and read-back verification
│   ├── audit/           # Append-only SHA-256 cryptographic audit chain and tamper validation
│   ├── report/          # Certificate of Erasure generation and PDF export models
│   ├── workflow/        # Deterministic state machine and lifecycle transition guards
│   ├── execution/       # Guarded, rate-limited execution coordinator
│   ├── approval/        # Canonical plan hash generator and single-use approval tokens
│   ├── blast-radius/    # Cross-table footprint and dependency analyzer
│   ├── storage/         # Local and persistent workflow state adapters
│   └── shared/          # Core TypeScript interfaces, DTOs, and error hierarchies
├── infra/
│   ├── fixtures/        # Single-source synthetic demo dataset (8 personas, 76 rows, 14 objects)
│   └── postgres/        # PostgreSQL schemas, foreign key definitions, and audit trigger SQL
├── backend/             # Python reference implementation (FastAPI, SQLAlchemy, Python LangGraph)
└── docs/                # Architectural specifications, security policies, and asset files
```

---

## 📡 HTTP REST API & MCP Catalog

### REST API Endpoints

| Method | Endpoint | Description | Guard / Headers |
|---|---|---|---|
| `GET` | `/health` | Service health status, active connector mode, allowlisted systems | Public |
| `GET` | `/api/overview` | Platform telemetry, total records, residual count, audit chain status | Public |
| `GET` | `/api/customers` | Directory of customers with masked names, live footprints, and latest requests | Public |
| `GET` | `/api/systems` | Real-time connector inventory per table and S3 bucket | Public |
| `GET` | `/api/policies` | Active retention policies, safety gates, and rate-limiting thresholds | Public |
| `GET` | `/api/audit` | Full append-only audit event log with cryptographic chain verification | Public |
| `POST` | `/api/requests` | Open a new erasure request (`{customerId, reason, dryRun}`) | Public |
| `GET` | `/api/requests/:id` | Fetch workflow snapshot, current state, and safety gate indicators | Public |
| `POST` | `/api/requests/:id/approve` | Submit approval (`{confirmation: "CUST-xxxx"}`) | `x-operator-identity` |
| `POST` | `/api/requests/:id/reject` | Reject request with optional reason (`{reason}`) | `x-operator-identity` |
| `POST` | `/api/requests/:id/execute-guarded` | Execute approved plan (`{approvalId, planHash}`) | Rate-limited + `x-operator-identity` |
| `POST` | `/api/requests/:id/rollback` | Restore data from pre-erasure backup after execution failure | `x-operator-identity` |
| `GET` | `/api/requests/:id/verification` | Perform live rescan of all systems for customer records | Public |
| `GET` | `/api/requests/:id/report` | Retrieve Certificate of Erasure and residual proof | Public |
| `POST` | `/api/agent/runs` | Initiate LangGraph agent run (`{goal}`) via Server-Sent Events (SSE) | Public |
| `POST` | `/api/agent/runs/:id/resume` | Resume paused agent run at human checkpoint with decision | `x-operator-identity` |
| `POST` | `/api/demo/reset` | Restore demo dataset to pristine initial fixture state | Public |

### End-to-End Command Line Execution

```bash
# 1. Open an erasure request for CUST-4410
REQUEST=$(curl -s -X POST http://localhost:3001/api/requests \
  -H "Content-Type: application/json" \
  -H "x-operator-identity: yug" \
  -d '{"customerId":"CUST-4410","reason":"Right to erasure request","dryRun":false}')
REQUEST_ID=$(echo $REQUEST | jq -r .requestId)

# 2. Approve the plan by confirming the customer ID
APPROVAL=$(curl -s -X POST http://localhost:3001/api/requests/$REQUEST_ID/approve \
  -H "Content-Type: application/json" \
  -H "x-operator-identity: yug" \
  -d '{"confirmation":"CUST-4410"}')
APPROVAL_TOKEN=$(echo $APPROVAL | jq -r .approval.token)
PLAN_HASH=$(echo $APPROVAL | jq -r .plan.hash)

# 3. Execute through the guarded endpoint
curl -s -X POST http://localhost:3001/api/requests/$REQUEST_ID/execute-guarded \
  -H "Content-Type: application/json" \
  -H "x-operator-identity: yug" \
  -d "{\"approvalId\":\"$APPROVAL_TOKEN\",\"planHash\":\"$PLAN_HASH\"}" | jq '{state, verification}'
```

### Model Context Protocol (MCP) Tools

When running `npm run dev:mcp`, the following tools are exposed over JSON-RPC:

- `discover_customer_postgres`: Discovers all relational records belonging to a customer across allowlisted tables.
- `discover_customer_storage`: Scans S3 buckets for customer-associated objects.
- `calculate_dependencies`: Computes foreign-key trees and identifies co-dependent or shared organizational records.
- `simulate_rehearsal`: Runs non-destructive sandbox simulation against target connectors.
- `rescan_customer`: Deep rescans all connectors to detect any lingering residual personal data.

---

## ⚙️ Configuration (.env)

Expunge-OPS is configured through environment variables. Copy `.env.example` to `.env` to customize settings:

```bash
cp .env.example .env
```

| Variable | Default Value | Description |
|---|---|---|
| `API_PORT` | `3001` | HTTP port for the Express API |
| `CONNECTOR_MODE` | `mock` | Connector backend: `mock` (in-memory) or `local` (PostgreSQL + MinIO) |
| `ERASEOPS_PERSISTENCE` | `memory` | Request state storage: `memory` or `postgres` (`eraseops_requests` table) |
| `ALLOWLIST_SYSTEMS` | `postgres-primary,minio-storage` | Comma-separated list of permitted systems |
| `APPROVAL_TTL_MINUTES` | `15` | Expiration window for human approval tokens |
| `DESTRUCTIVE_RATE_LIMIT` | `3` | Maximum permitted execution invocations per window |
| `DESTRUCTIVE_RATE_WINDOW_SECONDS` | `60` | Duration of the rate-limiting sliding window |
| `OPENAI_API_KEY` | *(optional)* | OpenAI API key for `gpt-5.5` agent reasoning |
| `OPENAI_MODEL` | `gpt-5.5` | OpenAI model identifier (`gpt-5.5` or `gpt-5.4-mini`) |
| `ANTHROPIC_API_KEY` | *(optional)* | Anthropic API key for Claude agent reasoning |
| `ERASEOPS_MODEL` | `claude-opus-5-5` | Model identifier when using Anthropic Claude |
| `DATABASE_URL` | `postgresql://eraseops:eraseops@localhost:5432/eraseops` | PostgreSQL connection string (in `local` mode) |
| `MINIO_ENDPOINT` | `http://localhost:9000` | S3 MinIO endpoint (in `local` mode) |
| `MINIO_ACCESS_KEY` | `minioadmin` | MinIO access key |
| `MINIO_SECRET_KEY` | `minioadmin` | MinIO secret key |

---

## 🧪 Comprehensive Verification Suite

Expunge-OPS includes a rigorous automated test suite comprising 194+ passing unit, contract, and lifecycle tests, plus end-to-end integration tests:

```bash
# Run type checking, unit tests, and production build
npm run typecheck
npm test
npm run build

# Run integration tests against live PostgreSQL & MinIO (requires docker compose up -d)
npm run test:integration

# Run Python reference implementation tests
pip install -r backend/requirements.txt
pytest backend
```

### Verified Test Invariants
- **LangGraph Agent Workflow**: Scripted mock runs verifying tool calls, rejected destructive attempts, `interrupt()` handling, resumption, and rule-based twin fallbacks.
- **Cryptographic Plan Hashing**: Verification that single-bit changes in proposed actions produce different SHA-256 hashes and invalidate tokens.
- **Approval Expiry & Replay Prevention**: Tests guaranteeing that approvals cannot be replayed or utilized past expiration.
- **Foreign Key Sandbox Failures**: Verification that dependent records owned by other customers correctly block execution during rehearsal.
- **PostgreSQL Transaction Rollback**: Verification that rehearsals never alter production database state.
- **Backup Tamper Detection**: Tests ensuring corrupted or altered backups are rejected during read-back.
- **Zero-Residual Rescan Invariant**: Verification that mock connectors claiming deletion without executing are immediately caught and flagged by the rescan validator.
- **Tamper-Evident Hash Chain**: Unit tests confirming that modifying an audit event invalidates all downstream event hashes.

---

## 👨‍💻 Author & Maker

Expunge-OPS was created, architected, and built by **Yug** ([@Yug-dev0](https://github.com/Yug-dev0)).

- **GitHub**: [@Yug-dev0](https://github.com/Yug-dev0)
- **Repository**: [https://github.com/Yug-dev0/Expunge-OPS](https://github.com/Yug-dev0/Expunge-OPS)
- **Project License**: [MIT License](LICENSE)

---

<div align="center">

**Expunge-OPS** · *Autonomous Privacy Orchestration with Cryptographic Proof*

<sub>Built for security teams, privacy officers, and developers who refuse to compromise between automation and safety.</sub>

</div>
