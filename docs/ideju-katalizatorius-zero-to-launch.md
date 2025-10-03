# Idėjų Katalizatorius – Zero-to-Launch Blueprint

## Executive Summary
1. Idėjų Katalizatorius taps computer-vision and LLM pipelines to turn screenshots and text snippets into organized PARA knowledge, actionable tasks, and searchable insights for Lithuanian knowledge workers first, then English-speaking pros.
2. The go-to-market thesis blends AI-first automation (OCR + topic tagging + smart actions) with human-in-the-loop review to earn trust in regulated EU markets.
3. We will ship a responsive Next.js web app backed by a NestJS API, PostgreSQL, and Prisma, packaged via Docker and deployed on Vercel/Fly with GitHub Actions CI.
4. Privacy-by-design—EU hosting, GDPR compliance workflows, consent/cookie controls, encrypted storage, and user-controlled retention—removes adoption friction.
5. Monetization starts with freemium capture and AI-limited tier, then expands into subscription bundles with usage-based AI credits and team collaboration add-ons.
6. Analytics, SEO (lt-LT + en), and local partnerships drive awareness; experiment cadences (activation, conversion, retention) power growth loops beyond launch.
7. A four-week execution roadmap sequences discovery, foundation, AI integration, UX polish, and go-live readiness, supported by AI coding assistants, tests, and documentation.
8. Risk management spans AI hallucinations, data residency, and competitive shifts, with mitigation owners and GDPR artifacts prepared from day zero.

## 1. Quick Discovery & Constraints
### Product Idea
A bilingual (lt-LT/en) AI workspace that ingests screenshots, text, voice memos, and URLs, applies OCR + LLM summarization + PARA categorization, and recommends next steps (tasks, project attachments, archival) so busy knowledge workers never lose an insight.

### Product Snapshot
| Problem | Primary Users | Core Value | North Star Metric | Constraints |
|---|---|---|---|---|
| Fragmented capture of inspirations and research across screenshots, tabs, and notebooks stalls follow-through. | Lithuanian/EU knowledge workers, consultants, students, and creators juggling info from multiple channels. | Unified capture-to-action flow with automated structure, suggested actions, and recall. | % of captured items converted into organized tasks/projects within 24h. | GDPR compliance, limited startup budget, need for LT localization, reliance on third-party AI APIs. |

### MoSCoW Feature List
- **Must-have:** Multi-source capture (upload, copy/paste, email-in), OCR + language detection, automatic tagging & PARA classification, actionable suggestions (task/project/archive), unified inbox dashboard, smart search, consent banner & privacy center, basic analytics.
- **Should-have:** Browser extension, voice memo transcription, Notion/Trello exports, calendar linking, usage analytics dashboard, lt-LT/en UI toggle, offline-ready PWA shell.
- **Could-have:** Shared team spaces, Slack/Teams bots, AI meeting summaries, template marketplace, custom knowledge graph visualizations.
- **Won’t-have (initially):** Full project management suite, social sharing feed, deep document editing, native mobile apps (beyond PWA wrapper).

### Business Context Assumptions
- **Business model:** Freemium with €8/mo Pro (higher OCR/AI quotas, integrations) and €18/mo Team tier (collaborative inbox, admin).
- **Budget tier:** Medium—can afford managed cloud (Vercel + Fly), OpenAI/Gemini usage, Plausible analytics, and essential tooling.
- **Timeline:** 8 weeks total target; current plan covers first 4-week MVP build + soft launch.
- **Risk tolerance:** Moderate—willing to ship beta with guardrails, but zero tolerance for GDPR breaches.
- **Data sources:** User-uploaded media, optional email forwarding, public API metadata (titles, favicons).
- **Authentication:** Passwordless email magic link + optional OAuth (Google/Microsoft) with mandatory MFA for admins.

## 2. Market & Competitive Research
### Competitive Landscape
| Product | Target Users | Pricing | Standout Features | Gaps / Opportunities | Pros | Cons |
|---|---|---|---|---|---|---|
| Notion | Teams needing all-in-one workspace | Free–$20/member/mo, AI agent on higher tiers | AI agent, enterprise search, meeting notes beta | Complex for quick capture; PARA not native | Rich ecosystem, docs + databases | Steep learning curve, AI extras locked to higher tiers |
| Readwise Reader | Power readers consolidating content | Free beta; paid via Readwise subscription | Unified inbox for web/RSS/PDF/YouTube, highlights sync | Task conversion limited; no PARA | Deep annotation features | Focused on reading, not tasking |
| Heptabase | Researchers & students | 7-day trial then paid | Visual whiteboards, mindmaps, offline access | No automated capture suggestions | Strong visual thinking tools | Learning curve, pricing premium |
| Tana | Knowledge workers needing AI-native graph | Free tier; paid for automation | Supertags, custom feeds, meeting agent | PARA-like flows but complex setup | AI automation, flexible structure | Onboarding complexity, early-stage |
| Taskade | Builders of AI workflows | Free–$200/mo+ | AI app builder, agents, automations | Less emphasis on ingesting visuals | Powerful automations, teams | Pricing jumps, overkill for solo |
| Evernote | General note takers | Free–$14.16/mo | AI search, Adobe integration, SSO | Legacy UI, limited innovation | Brand recognition, cross-device | Perceived stagnation, quotas |

*Citations:* Competitive claims summarized from vendor materials.【F:references/competitor-excerpts.md†L3-L24】

### Insights
1. AI-native workspaces emphasize automation but often demand heavy configuration—leaving room for an opinionated PARA-first default.
2. Few incumbents treat screenshots + OCR as first-class; this is a differentiator for Lithuanian professionals relying on visuals.
3. Pricing clusters around $10–$20/mo, so a €8 solo plan with targeted LT localization can undercut while sustaining margins.

### Differentiation Bets
1. **LT-first experience:** Native lt-LT copy, templates, and calendar holidays to win local mindshare before expanding to en.【F:references/competitor-excerpts.md†L3-L24】
2. **Capture-to-action automation:** Inline “next best action” suggestions triggered immediately after OCR reduces drop-off versus generic note apps.
3. **Compliance transparency:** Built-in privacy center, data residency in EU, and visible GDPR tooling as trust signal lacking in some competitors.

## 3. Product Requirements Document (PRD)
### Overview
Idėjų Katalizatorius is a web-based capture and organization platform transforming scattered inspiration into structured, actionable knowledge for Lithuanian and EU professionals.

### Goals & Non-Goals
- **Goals:** Rapid capture; automated structuring; actionable workflows; high recall search; GDPR compliance-by-default.
- **Non-Goals:** Full-scale project management, social sharing networks, replacing CRM/PM suites.

### Personas
1. **Rasa – Strategy Consultant (LT, 34):** Collects screenshots from webinars, needs quick conversion into client deliverables.
2. **Dainius – Product Manager (LT, 29):** Juggles research articles and meeting notes, wants PARA organization and task sync.
3. **Emily – Remote Student (EN, 22):** Studies across languages, needs OCR + translation + reminders.

### Jobs To Be Done
- When I capture a screenshot with an insight, I need it classified and summarized so I can act on it later without manual tagging.
- When I review my inbox of ideas, I want clear suggestions (task, project, archive) so nothing stalls.
- When I search past research, I expect OCR + tags + AI summaries to surface the right item fast.

### Use Cases
1. **Capture & classify:** Upload screenshot → auto OCR → recommended tags/areas.
2. **Action suggestion:** Choose “Create task” to push into task list with attachments.
3. **Knowledge retrieval:** Use search filters (tag, PARA, text) to find prior items.
4. **Consent management:** Accept or adjust cookie/analytics preferences.

### Success Metrics
- **North Star:** 60% of captured items converted to action or categorized within 24 hours.
- **KPIs:** (1) First capture-to-action under 10 minutes median; (2) Weekly active users / sign-ups ≥ 40% after 4 weeks; (3) Search success rate ≥ 70%; (4) GDPR data subject request turnaround < 5 days; (5) NPS ≥ +20 among LT users.

### Assumptions
- Users are willing to upload sensitive notes if GDPR assurances are clear.
- AI APIs (OpenAI GPT-4.1, Google Gemini 1.5) stay affordable within budget.
- PARA resonates locally due to GTD popularity.

### Risks
- AI hallucination misclassifying critical info.
- OCR accuracy drop for handwritten Lithuanian text.
- Vendor lock-in or API rate limits.
- Adoption barrier from new behavior (uploading screenshots).

### Open Questions
- Should offline desktop capture app be prioritized for LT market?
- Which AI provider offers best LT-language OCR accuracy within budget?
- Do we need integration with Lithuanian calendar/task tools (e.g., Bitrix24)?

### Core User Stories & Acceptance Criteria
1. **As a consultant, I can upload a screenshot and see AI metadata.**
   - *Given* I am authenticated, *when* I drop a screenshot into the capture widget, *then* the system stores the file, extracts OCR text, suggests tags, and surfaces PARA category within 5 seconds.
2. **As a user, I can convert captured insight into a task.**
   - *Given* AI metadata is displayed, *when* I click “Create task,” *then* a task is created with original file, summary, due date suggestion, and appears in Today list.
3. **As a user, I can manage consent preferences.**
   - *Given* I visit the site for the first time, *when* the cookie banner appears, *then* I can accept all, reject non-essential, or customize categories, and my choice is logged with timestamp.

## 4. UX & Design System
### Sitemap
- Home
  - Landing (marketing)
  - Pricing
  - Blog
  - Legal (Privacy, Terms, DPA)
- App (authenticated)
  - Inbox
    - Capture modal
    - Bulk actions
  - Tasks
  - Projects
  - Search
  - Insights (analytics)
  - Settings
    - Profile & localization
    - Integrations
    - Privacy center (consents, exports)

### Key User Flows
1. **Capture Flow:** Login → Inbox → “Add capture” → Upload/ paste → AI processing (loading state) → Tag/area suggestions → Choose action (task/project/archive) → Confirmation toast.
2. **Task Review Flow:** Inbox → Filter by PARA → Select item → Review AI summary → Accept suggested due date → Task created → Task board updated.
3. **Search Flow:** Header search → Enter keyword or tag → Results list (with OCR snippet highlight) → Open detail → Jump to related items.
4. **Consent Flow:** Landing page → Cookie banner → Choose preference → Banner collapses → Privacy center records + accessible from footer.

### Low-Fi Wireframes (Textual)
- **Inbox:** Two-column layout; left: list of captures with tags/areas chips; right: detail card with screenshot preview, OCR text, AI summary, CTA buttons (Task / Project / Archive) plus metadata chips.
- **Task Board:** Kanban with Today / This Week / Later; cards show title, source capture thumbnail, due date, status toggle.
- **Search:** Top search bar with filters (Type, Tags, Area, Date). Results as cards with snippet highlight; left facet panel for tags/areas.
- **Privacy Center:** Modal with toggles for Essential, Analytics (Plausible), AI improvements; export/delete request buttons.

### Design System
- **Spacing scale:** 4, 8, 12, 16, 24, 32, 48 px.
- **Typography:** Inter (Headings: 700 weights; Body: 400/500). Sizes: Display 32px, H1 28px, H2 24px, H3 20px, Body 16px, Caption 14px.
- **Color Tokens:**
  - Primary: Baltic Blue `#1E3A8A` (AA compliant on white).
  - Secondary: Amber `#F59E0B` for highlights.
  - Neutral: Slate `#0F172A` text, `#64748B` secondary, `#F8FAFC` backgrounds.
  - Success: Emerald `#10B981`; Danger: Rose `#F43F5E`; Warning: `#F97316`.
- **Components:**
  - Button (variants: Primary, Secondary, Ghost; props: `intent`, `size`, `icon`, `loading`).
  - Card (`title`, `meta`, `actions`).
  - Tag chip (`label`, `color`, `icon`, `dismissible`).
  - Modal (`title`, `isOpen`, `onClose`, `size`).
  - Data list (`items`, `onSelect`).
  - Tooltip (`content`, `placement`).
- **Accessibility:** Minimum contrast ratio 4.5:1 for text; focus states with 2px outline (#1E3A8A @ 40% opacity) + offset.

## 5. Technical Architecture
### High-Level Diagram (Text Description)
- **Frontend:** Next.js 14 (App Router) with TypeScript, React Query, Zustand for state, running on Vercel Edge. Integrates Plausible, Segment, and Sentry browser SDK.
- **Backend:** NestJS API on Node 20, deployed to Fly.io with Docker. Modules: Auth, Capture, AI Processing, Tasks, Search, Consent. Handles REST/GraphQL (REST primary) with WebSocket for processing updates.
- **AI Services:** OpenAI (GPT-4.1 mini for summarization), Google Gemini 1.5 Flash for LT/EN text + metadata, Azure Computer Vision for OCR fallback.
- **Database:** PostgreSQL 15 (managed by Neon or Supabase EU region) with Prisma ORM.
- **Storage:** S3-compatible (Wasabi EU-Central) for media; Cloudflare R2 optional for CDN.
- **Cache/Queue:** Redis (Upstash EU) for job queue & caching AI responses.
- **Auth:** Clerk or custom passwordless via Magic Links + OAuth + MFA. JWT tokens w/ short TTL.
- **Observability:** Sentry for traces, Logtail for structured logs, Grafana Cloud for metrics.
- **CI/CD:** GitHub Actions (lint/test/build), preview deploys (Vercel preview), backend staging deploy to Fly.

### Data Model (Entities & Relations)
Entities: `User`, `Workspace`, `Capture`, `CaptureFile`, `CaptureMetadata`, `Task`, `Project`, `Tag`, `Area`, `ActionLog`, `ConsentLog`, `Integration`, `Webhook`, `UsageQuota`, `AIJob`.

```mermaid
erDiagram
    Workspace ||--o{ User : members
    Workspace ||--o{ Capture : contains
    Workspace ||--o{ Project : includes
    Workspace ||--o{ Area : organizes
    Workspace ||--o{ Tag : defines
    Capture ||--|{ CaptureFile : has
    Capture ||--o{ CaptureMetadata : enriched_with
    Capture ||--o{ Task : converts_to
    Capture ||--o{ ActionLog : tracked_by
    Project ||--o{ Task : groups
    User ||--o{ Task : owns
    User ||--o{ ConsentLog : records
    Workspace ||--o{ Integration : configures
    Workspace ||--o{ UsageQuota : monitors
    AIJob ||--|| Capture : processes
```

### Key Attributes
- **User:** id, email, locale, role, mfa_enabled.
- **Workspace:** id, name, plan, region, default_locale.
- **Capture:** id, workspace_id, user_id, source_type (upload, email, clipper), status, para_area_id, summary, created_at.
- **CaptureFile:** id, capture_id, url, mime_type, checksum.
- **CaptureMetadata:** id, capture_id, ocr_text, detected_language, tags[], sentiment, confidence_scores.
- **Task:** id, capture_id, project_id, title, due_date, status, priority.
- **ConsentLog:** id, user_id, workspace_id, categories (jsonb), ip, user_agent, timestamp.
- **UsageQuota:** id, workspace_id, period_start, period_end, captures_used, ai_tokens_used.
- **AIJob:** id, capture_id, provider, status, started_at, completed_at, error.

### API Spec (REST)
- `POST /v1/auth/magic-link` — Body `{ email }` → 202 accepted; triggers magic link email. No auth.
- `POST /v1/captures` — Multipart with file or text; Auth: Bearer. Response `{ captureId, status }`.
- `GET /v1/captures/{id}` — Returns capture with metadata `{ id, files[], metadata, suggestions[] }`.
- `POST /v1/captures/{id}/actions` — Body `{ actionType: "task"|"project"|"archive", payload }` → returns created resource id.
- `GET /v1/search` — Query params `q`, `tags[]`, `area`, `type`. Returns paginated results.
- `GET /v1/tasks` — Filter by status/due_date.
- `POST /v1/privacy/consent` — Body `{ categories, version }` for logging preferences.
- `POST /v1/privacy/export` — Initiates export job.
- `DELETE /v1/privacy/data` — Right to erasure request.
- `GET /v1/usage/quota` — Returns current usage vs. plan limits.

**Response Schema Example:**
```json
{
  "id": "cap_123",
  "summary": "AI summarized text...",
  "paraArea": "Projects",
  "tags": ["#leadership", "#citata"],
  "files": [{"url": "https://cdn.../file.png", "mimeType": "image/png"}],
  "ocrText": "Lithuanian OCR...",
  "suggestions": [
    {"type": "task", "title": "Peržiūrėti strategijos skaidrę", "dueDate": "2025-03-06"},
    {"type": "project", "projectId": "proj_7"},
    {"type": "archive"}
  ]
}
```

### Non-Functional Requirements
- **Performance:** 95th percentile capture processing < 5s; search results < 2s.
- **Availability:** 99.5% monthly uptime; RPO 1h, RTO 4h.
- **Security:** Data encrypted at rest (AES-256) and transit (TLS 1.3). Regular dependency scanning, audit logs.
- **Rate limits:** 60 capture requests/min per workspace; 10 export requests/day.
- **Privacy-by-design:** Data minimization, configurable retention (default 365 days), consent logging, EU data residency, DPIA completed pre-launch.

## 6. AI Coding Strategy
- **Tooling:**
  - OpenAI GPT-4.1 for code generation, docstrings, summarization (commercial license, ensure usage logs pseudonymized).
  - GitHub Copilot in IDE for boilerplate, backed by enterprise policy.
  - Cursor or Replit Agents for rapid prototyping UI components.
  - Google AI Studio (Gemini 1.5 Flash) for LT language support and test data generation.
- **Prompt Playbooks:**
  - **Codegen:** “You are a NestJS expert. Generate a controller for capture creation with DTO validation (lt/en localization).”
  - **Refactor:** Provide diff with acceptance criteria, request improved separation of concerns.
  - **Tests:** Ask AI to write Vitest/Jest suites covering success + failure states.
  - **Docs:** Summaries of module responsibilities and API docs.
  - **Commit messages:** Conventional commits, include scope and summary.
- **Guardrails:**
  - Mandatory PR review (2-eye) for AI-authored code.
  - Run ESLint, Prettier, TypeScript strict mode, Jest/Vitest, Cypress e2e before merge.
  - Sensitive code (auth, billing) reviewed manually.
  - Maintain prompt library in repo to standardize usage.

## 7. Implementation Plan
### Work Breakdown Structure
- **Epic A: Foundations**
  - A1: Set up monorepo (Next.js frontend, NestJS backend).
  - A2: Configure design system scaffolding, theming.
  - A3: Establish Prisma schema, migrations, seed.
- **Epic B: Capture Pipeline**
  - B1: File upload API + storage integration.
  - B2: OCR service integration + fallback.
  - B3: LLM metadata generation + PARA classification.
  - B4: Suggestions engine (task/project/archive logic).
- **Epic C: Application UX**
  - C1: Inbox UI with real-time updates.
  - C2: Task board & detail view.
  - C3: Search interface with filters.
  - C4: Consent banner + privacy center.
- **Epic D: Compliance & Analytics**
  - D1: GDPR data map, consent logging.
  - D2: Cookie banner (lt/en), Plausible integration.
  - D3: Privacy policy & terms drafting.
- **Epic E: DevOps & Launch**
  - E1: GitHub Actions pipeline.
  - E2: Vercel/Fly deployments + staging.
  - E3: Monitoring & alerting setup.
  - E4: Beta onboarding + feedback loop.

### Estimates (Story Points / Days)
- Epic A: 5 SP each (15 total).
- Epic B: 6+8+8+5 = 27 SP.
- Epic C: 8+5+6+4 = 23 SP.
- Epic D: 3+2+4 = 9 SP.
- Epic E: 4+3+3+2 = 12 SP.
Total ≈ 86 SP (~4 weeks for 2 engineers).

### RACI Matrix
| Function | Product Discovery | Architecture | Frontend | Backend | AI/ML | QA | Compliance | Marketing |
|---|---|---|---|---|---|---|---|---|
| Product/Growth Lead (you) | A | C | C | C | C | R | A | A |
| Solution Architect (you) | C | A/R | R | R | R | C | C | C |
| AI Engineer (contractor) | C | C | C | C | A/R | C | C | C |
| QA Specialist (part-time) | I | I | C | C | C | A/R | I | C |
| Legal Advisor | I | I | I | I | I | I | A/R | I |
| Marketing Lead (you) | A | I | C | I | I | I | C | A/R |
(A=Accountable, R=Responsible, C=Consulted, I=Informed)

### 4-Week Timeline (ASCII Gantt)
```
Week:      |1|2|3|4|
Foundations|██████          |
Capture    |  ████████      |
UX         |    ████████    |
Compliance |      ████      |
DevOps     |  ███  ████     |
Beta Prep  |        ████    |
```

### Definition of Ready
- User story with clear acceptance criteria (Given/When/Then).
- Dependencies identified; designs or wireframes attached.
- Test data or API contracts available.
- Non-functional requirements noted.

### Definition of Done
- Code merged with tests (unit/integration) passing.
- Accessibility checks (axe) with no critical issues.
- Documentation updated (README + storybook entry).
- Monitoring/alerts configured if applicable.
- Feature flagged and demoed to stakeholders.

## 8. Development Environment & CI/CD
- **Bootstrap:** `./scripts/setup.sh` to install Node 20, pnpm, dependencies, pre-commit hooks, and generate `.env.local` templates.
- **Environments:** `.env.development`, `.env.staging`, `.env.production` with secrets stored in Doppler or 1Password.
- **Secrets Management:** Use Doppler for runtime injection; no plaintext in repo. GitHub Actions pulls from encrypted secrets.
- **CI Pipeline:**
  - `pnpm lint` (ESLint + Prettier).
  - `pnpm test` (Jest/Vitest, coverage ≥ 80%).
  - `pnpm typecheck` (tsc --noEmit).
  - `pnpm build` (Next.js + NestJS).
  - Cypress e2e smoke on PR (parallelized via GitHub Actions matrix).
  - Upload coverage to Codecov.
  - Vercel preview deploy (frontend) and Fly staging deploy (backend) per PR.
- **CD Pipeline:**
  - Merge to main triggers staging deployment (Vercel + Fly).
  - Manual promotion to production after QA sign-off.
  - Feature flags via LaunchDarkly-lite (Stateless JSON) to roll out gradually.
  - Rollback: Use `flyctl releases` revert + Vercel instant rollback; maintain DB rollback via Prisma migrations history.

## 9. Deployment Guide
- **Hosting Choices:**
  - Frontend on Vercel (Hobby → Pro €20/mo) for fast edge rendering.
  - Backend on Fly.io Machines (shared-cpu-1x, 1GB RAM ≈ $10/mo) in FRA (EU).
  - PostgreSQL via Neon (Scalable serverless) EU-West ~€25/mo.
  - Object storage via Wasabi EU-Central €6/mo (1TB tier).
- **Setup Steps:**
  1. Provision Vercel project, connect GitHub repo, set environment vars.
  2. Deploy backend via Fly: `fly launch`, configure secrets, scale to 2 instances for HA.
  3. Create Neon database, configure branches for staging/prod, connect via Prisma.
  4. Configure Plausible (EU) domain, embed script respecting consent.
  5. Set up DNS (Cloudflare) with CNAME for app + API subdomains.
- **Scaling Plan:** Auto-scale Fly to 2x CPU when CPU >70% for 5 min; Vercel auto-scaling edges.
- **Health Checks:** HTTP `/healthz` returning DB + Redis status; Fly auto restarts on failure; UptimeRobot monitors every 1 min.
- **Backups:** Neon point-in-time up to 7 days; daily logical backups to Wasabi; Wasabi versioning on.
- **Restore Drill:** Quarterly simulate DB restore to staging; verify recovery under 1h.

## 10. QA & Security
- **Test Plan:**
  - Unit: Jest/Vitest for services (AI pipeline mocks), coverage 80%+.
  - Integration: Supertest hitting Nest controllers with Prisma test DB.
  - E2E: Cypress covering capture-to-task, search, consent flows.
  - Accessibility: axe-core automation + manual screen reader check (NVDA/VoiceOver).
  - Performance: Lighthouse ≥ 85 mobile, 90 desktop; WebPageTest for TTFB < 1s EU.
  - Cross-browser: Latest Chrome, Safari, Firefox; Android Chrome + iOS Safari via BrowserStack.
  - Mobile responsiveness: breakpoints 360, 768, 1024, 1440.
- **Security Checklist (mapped to OWASP Top 10):**
  - A01 Broken Access Control → RBAC, unit tests on guards.
  - A02 Cryptographic Failures → Force HTTPS, rotate keys quarterly.
  - A03 Injection → Use Prisma parameterization, validate DTOs.
  - A04 Insecure Design → Threat modeling sessions per epic.
  - A05 Security Misconfig → Infrastructure as code, least privilege IAM.
  - A07 Identification & Auth Failures → MFA for admins, short-lived tokens.
  - A08 Software & Data Integrity → Dependabot, signed releases.
  - A09 Security Logging → Centralize logs, alert on auth anomalies.
  - A10 SSRF → Validate outbound webhooks, allowlist domains.
  - Add: DDoS protection with Cloudflare, rate limiting.

## 11. Analytics & Observability
- **Metrics:** Activation (first capture, first conversion), retention (WAU/MAU), conversion (free→Pro), feature adoption (search usage, tasks created), churn (downgrades, inactivity).
- **Instrumentation:**
  - Plausible (self-hosted EU) for privacy analytics; fallback PostHog for product analytics.
  - Event Taxonomy: `capture_created`, `capture_converted`, `search_performed`, `task_completed`, `consent_updated`, `plan_upgraded`.
  - Dashboards: Activation funnel, retention cohort, usage heatmap, AI cost per workspace.
- **Logging/Tracing:** Sentry (frontend/back), OpenTelemetry traces to Grafana; log correlation IDs per request.
- **Alerting:** PagerDuty or Opsgenie; thresholds: API error rate >2% (5-min), AI job backlog >50 pending, OCR latency >6s.
- **On-call Playbook:** Runbook with triage steps, rollback commands, communication templates.

## 12. SEO & ASO Plan
- **Technical Checklist:**
  - Next.js i18n routing with `/lt` default, `/en` secondary and `hreflang` tags.
  - XML sitemap via Next API; robots.txt allowing marketing pages.
  - Meta tags: `og`, `twitter`, structured data (Product schema with pricing, FAQ).
  - Core Web Vitals targets: LCP < 2.5s, CLS < 0.1, INP < 200ms.
  - Lazy-load heavy assets, prefetch localization bundles.
- **Content Plan (90 days):**
  - Pillar pages: “PARA metodika lietuviams,” “AI idėjų tvarkymas,” “GDPR-compliant AI workspace.”
  - Cluster topics (lt-LT/en) each week: AI productivity, PARA templates, LT success stories, compliance guides.
  - Editorial calendar: 2 blog posts/week (1 LT, 1 EN), 1 case study/month, monthly webinar recap.
- **Link Acquisition & PR:**
  - Partner with LT productivity influencers, LinkedIn thought leaders.
  - Guest posts on EU tech blogs, collaborate with co-working hubs.
  - Submit to Product Hunt, BetaList, Lithuanian startup directories.
- **90-Day Timeline:**
  - Weeks 1-2: Launch landing pages, sitemap, initial blog posts.
  - Weeks 3-6: Publish PARA pillar + 6 supporting posts, begin backlink outreach.
  - Weeks 7-10: Case study + webinar, push PR in LT media.
  - Weeks 11-13: Optimize based on Search Console, run localized ads.
- **Weekly Cadence:** Monday content planning, Wednesday publish LT article, Thursday publish EN article, Friday analytics review.
- **PWA ASO:** Add manifest, service worker, 512px icons; optimize install prompt copy.

## 13. Monetization & Pricing
- **Model:** Freemium → Subscription tiers with usage-based AI credit add-ons.
- **Price Ladder:**
  - Free: 100 captures/mo, limited AI summaries, single workspace.
  - Pro (€8/mo): 1,000 captures, advanced AI (multi-step suggestions), integrations, custom PARA areas.
  - Team (€18/user/mo): Shared inbox, admin console, SSO, audit logs, priority support.
  - Add-on: AI Boost packs (€5 per +500 captures) usage-based.
- **Trials/Discounts:** 14-day Pro trial, student 30% discount, referral 1 free month.
- **Payment Stack:** Stripe Billing (EU data residency), VAT ID collection, automatic invoices, SEPA direct debit.
- **Pricing Page Wireframe (Text):**
  - Hero: “Pasirink planą” with toggle (monthly/annual) and currency switch (EUR default).
  - Cards per tier with capture limits, AI features, integrations table, CTA buttons.
  - FAQ accordion, compliance badges (GDPR, EU hosting).
- **Event Tracking:** `pricing_view`, `plan_select`, `checkout_start`, `checkout_complete`, `downgrade_initiated`, `coupon_applied`.

## 14. Post-Launch Growth
- **Activation Checklist:** Welcome email (lt/en), in-app tour, first capture prompt, AI suggestion demo, set PARA defaults, invite to community.
- **Lifecycle Flows:**
  - Day 0 email with video tutorial; Day 3 tips; Day 7 “convert ideas to tasks” nudge; Day 14 plan upsell.
  - SMS (optional) for Pro trial ending.
- **Referral Loop:** Provide unique link granting both referrer and friend +100 AI captures.
- **Churn Reasons:** Capture through exit survey; auto-schedule win-back email after 30 days with new feature highlight.
- **Experiment Backlog (ICE):**
  1. Guided PARA setup wizard (Impact 8, Confidence 6, Effort 3 → ICE 56).
  2. AI summary in email digest (7,7,4 → 49).
  3. Browser extension beta waitlist (6,6,5 → 36).
  4. Lithuanian webinar series (5,7,4 → 35).
  5. Task sync with Notion API (6,5,6 → 30).
- **90-Day Growth Roadmap:** Month 1 activation focus; Month 2 conversion (pricing tests); Month 3 retention (workspace analytics, community).

## 15. Risk Register & Compliance
- **Top Risks:**
  1. AI misclassification (P=Medium, I=High) → Human override UI, confidence thresholds.
  2. Data breach (P=Low, I=Critical) → Encryption, pen tests, incident response plan.
  3. Vendor outage (P=Medium, I=Medium) → Multi-provider AI fallback, queue replay.
  4. OCR accuracy for Lithuanian (P=High, I=Medium) → Evaluate providers, allow manual correction.
  5. Budget overrun from AI costs (P=Medium, I=Medium) → Usage quotas, monitor spend dashboard.
  6. Regulatory change (P=Low, I=High) → Track EU AI Act updates, legal counsel check-ins.
  7. Low adoption (P=Medium, I=High) → Beta feedback loops, adjust onboarding.
  8. Talent bandwidth (P=High, I=Medium) → AI-assisted coding, prioritize backlog.
  9. Integration delays (P=Medium, I=Low) → Feature flags, stubbed connectors.
  10. Negative PR (P=Low, I=Medium) → Transparent privacy policy, quick response process.
- **GDPR Artifacts:** Data Processing Agreement template, Article 30 data inventory, consent logs stored per workspace, user self-service export/delete, DPIA doc, retention policy (default 12 months, configurable), subprocessor list.

## Additional Deliverables
### Tech Stack Matrix
| Layer | Option | Pros | Cons | Est. Monthly Cost |
|---|---|---|---|---|
| Frontend | Next.js 14 on Vercel | Edge rendering, built-in i18n, preview deploys | Vendor lock-in | €20 |
| Backend | NestJS on Fly.io | Modular, TypeScript DI, EU regions | Requires ops for scaling | €25 |
| DB | Neon Postgres | Serverless autoscaling, branching | Newer service | €25 |
| Storage | Wasabi S3 | Low cost, EU | Requires CDN setup | €6 |
| Cache/Queue | Upstash Redis | Serverless, EU, pay-per-use | Limited custom config | €10 |
| AI | OpenAI GPT-4.1 mini | High quality, multi-language | Cost per token | €50 (est) |
| AI (alt) | Google Gemini 1.5 Flash | Strong LT support | Rate limits | €30 |
| Analytics | Plausible self-host | GDPR-friendly, LT data center | Limited advanced funnels | €12 |
| Monitoring | Sentry | Deep tracing | Paid for volume | €20 |

### Environment Variables Catalog
| Name | Purpose | Scope |
|---|---|---|
| `DATABASE_URL` | Prisma connection string | Backend all envs |
| `SHADOW_DATABASE_URL` | Prisma migrations | Dev/CI |
| `REDIS_URL` | Queue/cache connection | Backend |
| `STORAGE_BUCKET` | S3 bucket name | Backend |
| `STORAGE_REGION` | S3 region | Backend |
| `OPENAI_API_KEY` | LLM access | Backend |
| `GEMINI_API_KEY` | Alt LLM access | Backend |
| `AZURE_OCR_KEY` | OCR fallback | Backend |
| `JWT_SECRET` | Auth signing | Backend |
| `MAGIC_LINK_SECRET` | Email token signing | Backend |
| `NEXT_PUBLIC_PLAUSIBLE_DOMAIN` | Analytics config | Frontend |
| `PLAUSIBLE_API_KEY` | Stats ingestion | Backend/Analytics |
| `SENTRY_DSN` | Error reporting | Frontend/Backend |
| `STRIPE_SECRET_KEY` | Billing API | Backend |
| `STRIPE_WEBHOOK_SECRET` | Verify webhooks | Backend |
| `EMAIL_FROM` | Transactional email | Backend |
| `RESEND_API_KEY` | Email provider | Backend |

### Sample `.env.example`
```bash
# Database
DATABASE_URL="postgresql://user:pass@host:5432/ideju_katalizatorius"
SHADOW_DATABASE_URL="postgresql://user:pass@host:5432/ideju_katalizatorius_shadow"

# Cache & Storage
REDIS_URL="rediss://:password@eu1.upstash.io:6379"
STORAGE_BUCKET="ideju-captures"
STORAGE_REGION="eu-central-1"

# AI Providers
OPENAI_API_KEY="sk-..."
GEMINI_API_KEY="ai-..."
AZURE_OCR_KEY="..."

# Auth & Security
JWT_SECRET="replace-me"
MAGIC_LINK_SECRET="replace-me"

# Observability
SENTRY_DSN="https://public@sentry.io/project"
NEXT_PUBLIC_PLAUSIBLE_DOMAIN="analytics.idejukatalizatorius.lt"
PLAUSIBLE_API_KEY="plausible-..."

# Billing & Email
STRIPE_SECRET_KEY="sk_live_..."
STRIPE_WEBHOOK_SECRET="whsec_..."
EMAIL_FROM="noreply@idejukatalizatorius.lt"
RESEND_API_KEY="re_..."
```

### Example Database Migration (Prisma)
```sql
-- 20250305_init_capture_pipeline
CREATE TABLE "Workspace" (
  "id" UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  "name" TEXT NOT NULL,
  "plan" TEXT NOT NULL DEFAULT 'free',
  "default_locale" TEXT NOT NULL DEFAULT 'lt-LT',
  "created_at" TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE "Capture" (
  "id" UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  "workspace_id" UUID NOT NULL REFERENCES "Workspace"("id") ON DELETE CASCADE,
  "user_id" UUID NOT NULL,
  "source_type" TEXT NOT NULL,
  "status" TEXT NOT NULL DEFAULT 'processing',
  "para_area" TEXT,
  "summary" TEXT,
  "created_at" TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE "CaptureMetadata" (
  "id" UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  "capture_id" UUID NOT NULL REFERENCES "Capture"("id") ON DELETE CASCADE,
  "ocr_text" TEXT,
  "detected_language" TEXT,
  "tags" TEXT[],
  "confidence" NUMERIC(5,2)
);

CREATE INDEX "idx_capture_workspace_created" ON "Capture" ("workspace_id", "created_at");
```

### Example API Route + Controller + Test Skeletons
```ts
// apps/api/src/capture/capture.controller.ts
import { Controller, Post, UseGuards, UploadedFile, UseInterceptors } from '@nestjs/common';
import { FileInterceptor } from '@nestjs/platform-express';
import { AuthGuard } from '../auth/auth.guard';
import { CaptureService } from './capture.service';

@Controller('v1/captures')
@UseGuards(AuthGuard)
export class CaptureController {
  constructor(private readonly captureService: CaptureService) {}

  @Post()
  @UseInterceptors(FileInterceptor('file'))
  async create(@UploadedFile() file: Express.Multer.File) {
    return this.captureService.createFromUpload({ file });
  }
}
```

```ts
// apps/api/src/capture/capture.service.ts
import { Injectable } from '@nestjs/common';

@Injectable()
export class CaptureService {
  async createFromUpload({ file }: { file: Express.Multer.File }) {
    // TODO: persist file, enqueue AI job
    return { captureId: 'cap_temp', status: 'processing' };
  }
}
```

```ts
// apps/api/src/capture/capture.controller.spec.ts
import { Test, TestingModule } from '@nestjs/testing';
import * as request from 'supertest';
import { INestApplication } from '@nestjs/common';
import { CaptureModule } from './capture.module';

describe('CaptureController (e2e)', () => {
  let app: INestApplication;

  beforeAll(async () => {
    const moduleFixture: TestingModule = await Test.createTestingModule({
      imports: [CaptureModule],
    }).compile();

    app = moduleFixture.createNestApplication();
    await app.init();
  });

  it('creates capture from upload', () => {
    return request(app.getHttpServer())
      .post('/v1/captures')
      .set('Authorization', 'Bearer test-token')
      .attach('file', Buffer.from('fake'), 'test.png')
      .expect(201)
      .expect(res => {
        expect(res.body.status).toBe('processing');
      });
  });
});
```

### Backlog (Epics → Stories)
- **Epic A:** Foundations
  - Story A1: As a developer, scaffold Next.js + NestJS monorepo (Given repository, When running setup script, Then both apps start).
  - Story A2: As a designer, set up design tokens in Tailwind/Styled System (Given tokens, When building components, Then theme switch works).
- **Epic B:** Capture Pipeline
  - Story B1: As a user, upload screenshot (Given auth, When uploading, Then capture status shows processing).
  - Story B2: As AI system, perform OCR (Given capture queued, When OCR service runs, Then text stored with >90% accuracy for typed text).
  - Story B3: As user, see suggestions (Given metadata ready, When viewing capture, Then suggestions list displayed).
- **Epic C:** UX
  - Story C1: As user, view inbox list (Given captures exist, When visiting inbox, Then list sorted by newest with status chips).
  - Story C2: As user, create task (Given suggestion, When selecting task, Then task board updates within 2s).
  - Story C3: As user, filter search (Given tags, When filtering, Then results reduce accordingly).
- **Epic D:** Compliance
  - Story D1: As visitor, manage cookies (Given banner, When customizing, Then preferences saved per GDPR).
  - Story D2: As admin, export data (Given request, When clicking export, Then email with download link within 24h).
- **Epic E:** DevOps
  - Story E1: As engineer, see CI pass (Given PR, When pipeline runs, Then lint/test/typecheck succeed).
  - Story E2: As operator, deploy staging (Given main branch, When release triggered, Then staging updated automatically).

### Day-1 to Day-30 Execution Checklist
- **Day 1-3:** Confirm assumptions, finalize PRD & design system, set up repo & CI skeleton.
- **Day 4-7:** Implement auth + capture upload stub, configure storage, start OCR integration POC.
- **Day 8-10:** Build inbox UI skeleton, wire loading states, finalize PARA taxonomy defaults.
- **Day 11-14:** Integrate OCR + LLM summarization, set up Redis queue, record latency metrics.
- **Day 15-18:** Implement task board, search filters, localization (lt/en toggle).
- **Day 19-21:** Add consent banner, privacy center, Plausible integration, finalize legal drafts.
- **Day 22-24:** Harden analytics, instrumentation, Stripe checkout, finalize pricing copy.
- **Day 25-27:** Load testing, security review, fix bugs, prepare onboarding emails.
- **Day 28-30:** Soft launch to beta cohort, monitor metrics, schedule feedback interviews, plan iteration backlog.

### References
See curated source table for external validation of competitor positioning and pricing.【F:references/web-sources.md†L1-L8】【F:references/competitor-excerpts.md†L3-L24】

