# ED Roster: build-and-learn plan

Oct 3, 2026 · @Alex

## How this plan works

You rebuild the ED Roster from an empty repo in two passes, about 6–8 hours a week. **Pass 1 (weeks 0–12)** builds a working roster app with the learning scaffolding below. **Pass 2 (weeks 13–20)** adds the feature specs near the end of this doc: leave, EFT, rotations, stats, swaps and the rest. The specs name a week in pass 1 where their foundations go, so you don't build something you'll have to rip out, but the full features come in pass 2. Each week Claude Code is given a little more autonomy, and it gets that autonomy only after you have done the underlying thing yourself. The finished app (`ed-roster.zip`) is your answer key, not your starting point.

This beats the three obvious alternatives:

- **Reading the finished code** gives you recognition, not recall. You'll nod along and still be unable to debug it.
- **Building from scratch without AI** teaches foundations but not how developers work now, and it's slow enough that most people stall around week 4.
- **Asking Claude to build it all** gets you an app you can't judge, extend or fix. That's the failure mode this plan is designed against.

### Graduated autonomy

| Level | Weeks | Who writes the code | Your job | You've earned the next level when |
| --- | --- | --- | --- | --- |
| 1. Tutor | 0–2 | You | Type it, run it, break it. Claude explains and answers. | You can explain every line of the walking skeleton and fix a red CI build alone |
| 2. Pair | 3–6 | Claude, in small steps | Approve the plan, read every diff before accepting, ask why | You catch at least one wrong or over-built Claude change per week |
| 3. Delegate | 7–10 | Claude, a whole feature at a time | Write the spec and the tests that define done; review the pull request | Your specs produce working features on the first or second attempt |
| 4. Orchestrate | 11–12 | Several Claude sessions in parallel, plus AI review in CI | Act as tech lead: split work, set guardrails, decide what merges | — |

*(Interactive timeline in the Claude doc: what you build each week, Claude Code's role, and the gates between Tutor → Pair → Delegate → Orchestrate. The week sections below carry the same content.)*

Each gate is a skill you demonstrate, not a date on the calendar: stay at a level until you can do it.

### Each week has the same six steps

1. **Learn** (≈1 h). The week's concepts. Ask Claude to explain them using your own repo, not generic examples.
2. **Build by hand** (≈2 h). The smallest version of the week's feature, typed by you.
3. **Build with Claude** (≈2 h). Extend it to the full feature at the week's autonomy level.
4. **Break it** (≈30 min). A debugging drill. Have Claude plant a bug in a branch without telling you where, then find it from the symptoms.
5. **Ship** (≈1 h). Pull request, green CI, merge, deploy. Add three lines to `LEARNINGS.md`: what you learned, what surprised you, what you'd ask Claude to do differently.
6. **Compare** (≈30 min). Ask Claude to compare your version with the matching part of the answer key and explain the trade-offs. Neither version is automatically right.

Split a week over two sittings, with the hand-build on the first day. Trying to do all six steps in one evening is the most common reason plans like this stall.

Every week ends with a checkpoint: three questions you should be able to answer without Claude. If you can't, repeat the hand-build step before moving on.

## Rules for working with Claude Code

Four habits carry the whole plan: plan before code, give Claude a check it can run, keep sessions clean, and review every diff as if a junior wrote it.

### The earn-the-right-to-delegate test

Hand Claude a task only when you can do all three of these. If any is missing, work that task one level lower (Tutor or Pair).

1. **Specify it.** You can write what done looks like as acceptance criteria or a failing test.
2. **Judge it.** You'd recognise a wrong or over-built answer.
3. **Debug it.** If it breaks at 2 a.m., you could find the cause without Claude.

### Tutor-mode CLAUDE.md (week 0)

`CLAUDE.md` in the repo root is read at the start of every session. Keep it short: Anthropic's guidance is that a bloated file gets ignored. Start with this and loosen it as you move up the levels.

```markdown
# Working style (learning project)
- Before editing, explain the plan and the why; wait for my OK.
- Keep each change small: one concern, under ~200 lines.
- After each change, explain the diff and name one concept I should understand.
- Never run git push, change .github/ or deploy/ files, or add a dependency without asking.
- Tests: pytest. Run them after every change and show me the output.
- Fictional data only. Never generate real names, emails or Monash Health identifiers.
- This is a learning project: when I ask how something works, teach; don't just do it.
- Stay in plan or manual permission mode unless I say otherwise.
```

### The session loop

1. **Explore, then plan.** Press `Shift+Tab` until the status bar shows plan mode. Claude reads files and proposes a plan without changing anything. `Ctrl+G` opens the plan in your editor so you can change it before approving.
2. **Give Claude a check it can run.** "Write the test first, run it, then make it pass" or "take a screenshot and compare it with the design". Without a check, you are the only test.
3. **Ask for evidence, not assurance.** The test output, the command and what it returned, or the screenshot. Never accept "this should work".
4. **Correct early.** `Esc` stops Claude mid-step. `Esc Esc` or `/rewind` restores earlier code and conversation. After two failed corrections, `/clear` and start again with a better prompt. A clean session beats a long, muddled one.
5. **One task per session.** `/clear` between unrelated tasks; the context window is the scarcest resource.

### Review checklist: when to push back

Read every diff for these before accepting it. Each is a common way AI-written code goes wrong.

- **Scope creep.** Files changed that weren't in the plan, or "while I was here" refactors.
- **New dependencies** you didn't ask for. Each one is code you now maintain and patch.
- **Tests bent to pass.** Weakened assertions, skipped tests, or mocks of the very thing under test.
- **Swallowed errors.** A bare `except: pass`, or a quiet default value that hides a failure.
- **Security slips.** SQL built from strings, a new route with no permission check, secrets in code, CSRF or TLS checks switched off.
- **Reinvention.** Writing a helper that already exists elsewhere in the repo.
- **Over-engineering.** An abstraction with one user, or configuration for things that never change.
- **Database traps.** A query inside a loop (the "N+1" problem), a model change with no migration, or a migration that can't be reversed.
- **Comments that narrate.** Comments should explain why, not restate what the code says.

When you spot one, don't just fix it. Ask Claude why it chose that and what the alternative was, then add a line to `CLAUDE.md` if it's a pattern. That's how the file earns its keep.

## Week 0: setup (about 4 hours)

By the end you have an empty repo on GitHub, every tool installed, and Claude Code set up in Tutor mode.

**Install on your Mac**

```bash
# package manager, then the core tools
brew install git gh uv ripgrep
gh auth login
# Claude Code (Anthropic's recommended native installer)
curl -fsSL https://claude.ai/install.sh | bash
claude --version
```

Also install VS Code with the Python and Ruff extensions, and OrbStack or Docker Desktop for containers. `uv` replaces `pip` and `venv`: it creates the project's virtual environment and locks exact package versions in one tool.

**Create the repo**

```bash
mkdir -p ~/projects/ed-roster-learn && cd ~/projects/ed-roster-learn
uv init --python 3.12          # also runs git init
printf ".env\n*.db\n.claude/worktrees/\n" >> .gitignore
git add . && git commit -m "Start ED Roster learning project"
gh repo create ed-roster-learn --public --source=. --push
```

Make it **public**. On GitHub's free plan, branch protection (forcing every change through a pull request) only works on public repos; private repos need GitHub Pro or above. Public is safe here because the data is fictional. The real rule is that no secret ever goes into git, public or not.

**Set up Claude Code**

1. Run `claude` in the repo and sign in.
2. Create `CLAUDE.md` with the Tutor-mode text from the rules section above, and commit it.
3. Check that `.gitignore` lists `.venv`, `.env` and `*.db` before anything else is committed. Once a secret is in git history, deleting the file doesn't remove it.
4. Unzip the answer key (`ed-roster.zip`) into a **separate** folder outside this repo. You'll open it in the weekly compare step, never before you've attempted the week.
5. Create `LEARNINGS.md` with one heading per week.

**Exercise: a guided tour of the answer key (Tutor mode).** In the answer-key folder, ask Claude in plan mode: "Give me a map of this codebase: what each folder does, how a request flows from the browser to the database and back, and which three files I should understand first." Draw the request flow yourself on paper, then compare it with Claude's answer.

**Checkpoint**

- What's the difference between git (the tool) and GitHub (the hosting service)?
- Why does `.env` never go into git, even in a private repo?
- What does `CLAUDE.md` change about how Claude behaves, and what can't it guarantee? (Hooks are what guarantee things; you'll meet them in week 11.)

## Weeks 1–2: the delivery pipeline (Tutor mode)

By the end of week 2, a one-page app is live on HTTPS, and every change reaches it through a pull request with tests run automatically. Everything later goes through this pipeline, so deployment stops being scary.

### Week 1: walking skeleton and the pull-request workflow

**Deliverable:** a FastAPI app with a `/healthz` endpoint and one HTML page, one test, a linter, and CI that runs on every pull request, merged into `main` through a PR.

**Concepts:** the HTTP request and response; what a web framework does (routing) versus the server that runs it (uvicorn); virtual environments and lockfiles; git commits, branches, merging; pull requests; continuous integration (CI).

**Exercises**

1. **Learn.** Run `curl -v http://localhost:8000/healthz` and ask Claude to explain every line of the output.
2. **Build by hand.**
   - `uv add fastapi uvicorn`, then write `app/main.py` with `/healthz` returning JSON and `/` returning a page that says "ED Roster".
   - `uv add --dev pytest ruff httpx`, then write one test with FastAPI's `TestClient`.
3. **Git drill.** Work on a branch, make three small commits, push, and open a PR with `gh pr create`. Then create a merge conflict on purpose (two branches editing the same line) and resolve it yourself.
4. **CI by hand.** Write `.github/workflows/ci.yml` yourself: check out the code, install uv, `uv sync`, `uv run ruff check`, `uv run pytest`. Make it fail on purpose, then fix it.
5. **Protect `main`.** Require a pull request and a passing CI check before anything merges.
6. **With Claude (Tutor).** Ask it to review your workflow file, explain anything you copied without understanding, and suggest one improvement (dependency caching is a good one). You make the change.

**Break it:** have Claude plant a broken import on a branch without telling you where. Find it from the CI log alone.

**Checkpoint**

- What does uvicorn do that FastAPI doesn't?
- Why trust CI's clean machine over your laptop?
- What's in `uv.lock`, and why commit it?

**Answer key:** `app/main.py` (the health check), `tests/conftest.py`.

### Week 2: containers and the first HTTPS deploy

**Deliverable:** the skeleton live at `https://roster.<your-domain>`, plus a `DEPLOY.md` runbook you wrote while doing it.

**Concepts:** images versus containers; layers and build caching; configuration through environment variables (the "12-factor" principle); ports and container networks; DNS records; TLS certificates and reverse proxies; SSH keys, firewalls and running as a non-root user.

**Exercises**

1. **Learn.** In plan mode, have Claude walk you through the answer key's `Dockerfile` and `docker-compose.yml` line by line. Don't copy them.
2. **Build by hand.** Write a `Dockerfile` for your skeleton, then a `docker-compose.yml`. Read one setting (the app name) from `.env` so you see configuration flow in.
3. **Server by hand.** Follow the hosting steps from our earlier conversation, typing every command yourself: a Sydney droplet, a non-root user, the firewall, Docker, a deploy key, Caddy, DNS. The smallest droplet that fits for now is 1 vCPU / 2 GB at US$12/month (about A$17.25). Resize to 2 vCPU / 4 GB in week 8, when the solver arrives.
4. **Write `DEPLOY.md` as you go.** Every command, in order, with one line on why.
5. **With Claude (Tutor).** Ask it to review `DEPLOY.md` for missing steps and security gaps, and to explain any command you ran but didn't fully understand.

**Break it:** stop the app container and see what Caddy returns (it should be a 502 error). Then read `docker compose logs` to see why.

**Checkpoint**

- Why does the app listen only on `127.0.0.1`, and what bypasses the `ufw` firewall?
- What happens to the app when the server reboots, and which setting decides that?
- Where does Caddy keep its certificates, and what happens if that storage is deleted?

**Answer key:** `Dockerfile`, `docker-compose.yml`, `deploy/`.

## Weeks 3–5: data, interface and security (Pair mode)

From week 3, Claude writes most of the code in small steps and you read every diff before accepting it. You still hand-build the first instance of each pattern, then Claude follows your pattern for the rest. Update `CLAUDE.md`: keep "plan first, wait for my OK", but drop "explain every diff" for routine changes.

### Week 3: data model and migrations

**Deliverable:** PostgreSQL in Docker Compose; models for periods, roles with their own shift times, streams, the team template, and staff with dated EFT; Alembic migrations; a seed script with fictional data; one read-only admin page listing them.

**Concepts:** relational modelling (keys, one-to-many, many-to-many through a join table); constraints (unique, foreign key, cascade); what an ORM does, compared with the SQL you already write; sessions and transactions; migrations as version control for the schema.

**Exercises**

1. **Learn.** Draw the data model on paper from the requirements first. Then ask Claude to critique it. Who's right about staff holding several roles?
2. **Build by hand.** The `Period` model and your first migration with `alembic revision --autogenerate`. Read the generated file, apply it, roll it back, re-apply it.
3. **Pair.** Claude adds the other models one at a time. Review each migration before it runs.
4. **See the SQL.** Turn on SQLAlchemy's `echo=True`. Find the extra query per row on your listing page (the N+1 problem) and fix it with `joinedload`.

**Break it:** on a throwaway copy, write a migration that renames a column by dropping and re-adding it. Watch the data vanish, then do it properly.

**Checkpoint**

- Why do staff and roles need a separate join table?
- What does autogenerate miss? (Renames and data changes are two.)
- Why store a night shift as start time plus duration rather than start and end times?

**Answer key:** `app/models.py`. It has no Alembic: here you're improving on it.

### Week 4: server-rendered pages and your design system

**Deliverable:** admin pages for periods, roles with their shift times, and streams, plus the team-template grid editor. Styled only with your design tokens, and usable on a phone.

**Concepts:** server-rendered HTML versus a single-page JavaScript app; Jinja templates and inheritance; forms and the post-redirect-get pattern; validation messages; HTMX partial page updates; CSS custom properties and the two-layer token model; accessibility basics (labels, focus, contrast).

**Exercises**

1. **Learn and decide.** Ask Claude for the trade-offs of server-rendered pages with HTMX versus React for this app. Record your decision in `docs/decisions/0001-ui.md`. That's an architecture decision record (ADR), a habit worth keeping.
2. **Build by hand.** The base layout, the period list, and a create form with validation.
3. **Pair.** "Follow the pattern in the periods page to build roles and streams." Check it really did follow it.
4. **Design to code.** Export `tokens.css` from your Design System artifact and write `app.css` using semantic tokens only. Ask Claude to check the contrast of every text pair.
5. **HTMX.** Make one cell of the team template save without reloading the page.

**Break it:** submit `25:00` as a start time, and a day shift that ends before it starts. You should see a clear message, never a crash page.

**Checkpoint**

- Why redirect after a successful form submission?
- Which token layer do components use, and why?
- What does an HTMX request send and receive, compared with a single-page app?

**Answer key:** `app/templates/`, `app/static/app.css`, the coverage editor in `app/routers/admin.py`.

### Week 5: authentication, permissions and security

**Deliverable:** sign in and out; two user types, admin and staff; hashed passwords; CSRF protection on every form; security headers; Dependabot and secret scanning switched on.

**Concepts:** authentication (who you are) versus authorisation (what you may do); why password hashes are deliberately slow; sessions and signed cookies; cross-site request forgery (CSRF); cross-site scripting and template auto-escaping; SQL injection; the OWASP Top 10 list of common web risks; threat modelling.

**Exercises**

1. **Threat model with Claude.** Who could misuse a roster app, and how? A staff member reading colleagues' leave notes? A forged request that publishes the roster? Write five threats and their mitigations in `SECURITY.md`.
2. **Build by hand.** Password hashing, the sign-in form, and a `require_admin` check.
3. **Pair.** Claude adds CSRF protection and security headers. You write the tests first, proving a staff user gets a 403 error on every admin page.
4. **Your first subagent.** "Use a subagent to review the auth changes for security issues." It reviews in a fresh context, so it isn't marking its own work.

**Break it:** turn off the CSRF check on a branch. Build a page on another local port that silently submits "publish roster", and watch it succeed. Restore the check and watch it fail.

**Checkpoint**

- Why is a fast hash bad for passwords?
- What does a `SameSite=Lax` cookie protect against, and what not?
- Where should a permission check live so a new page can't forget it?

**Answer key:** `app/auth.py`, `app/routers/auth.py`, the permission tests in `tests/test_web.py`.

## Weeks 6–9: the rostering engine (Pair to Delegate)

This is the heart of the app and where you move to Delegate mode: you write the spec and the tests, and Claude builds a whole feature to pass them. Weeks 8 and 9 are the hardest; budget 8–10 hours for each.

### Week 6: staff, preferences, and your first spec

**Deliverable:** staff management (roles, streams, start and end dates, and dated EFT entered by admins); staff-entered preferences with the admin review queue; leave requests and approval; rotations with a bulk CSV import you preview before saving. In pass 1, build only the data model for EFT, leave and rotations plus the basic preference form; the review queue, approval workflows and bulk import are pass 2.

**Concepts:** modelling flexible rules as data rather than code; validating input at the edge of the system; test fixtures and factories; parametrised tests; file uploads.

**Exercises**

1. **Design first.** Sketch one data structure that can express "no Monday lates", "not Thursdays" and "never Fridays (second job)". Then compare it with the answer key's `Preference` model.
2. **Build by hand.** The `matches(date, shift)` function. Write ten parametrised test cases before the code.
3. **Pair.** Claude builds the staff pages and the preference form.
4. **Your first spec.** Write a one-page `SPEC.md` for CSV import (columns, error messages, what happens to duplicates) before Claude writes any code. Then have Claude implement it. This is the bridge into Delegate mode.

**Break it:** import a CSV saved from Excel (it adds an invisible byte-order mark), one with an unknown role, and one with a duplicate email.

**Checkpoint**

- Why store preferences as data instead of `if` statements?
- What's the difference between a fixture and a factory?
- Where should validation live, and why there?

**Answer key:** the `Preference` model, `apply_pref_form` in `app/routers/me.py`, the import in `app/routers/admin.py`.

### Week 7: the rule checker, test first

**Deliverable:** an independent rule checker for rest between shifts, consecutive days and nights, days off after nights, maximum shifts and maximum hours per rolling week, maximum shift length, the period mix (such as 50:50 or 40:40:20), EFT-based hours, weekend load and coverage gaps. It's a set of pure functions with a thorough test suite, plus a Check page and a simple form to enter shifts by hand so you have rosters to check.

**Concepts:** pure functions and keeping domain logic out of the web framework; test-driven development (red, green, refactor); edge cases; property-based testing with Hypothesis.

**Exercises**

1. **Write the rules in English** with a table of examples for each (a pass and a fail).
2. **Delegate for the first time.** You write the failing tests from that table. Claude implements until they pass. Tell it not to change the tests, then check the diff to confirm it didn't.
3. **A property test.** For example, "the checker gives the same result whatever order the shifts arrive in". Hypothesis then generates hundreds of cases you'd never think of.
4. **A daylight-saving decision.** Victoria's clocks change in April and October, so a 23:00–08:30 night on change night is an hour longer or shorter. Decide how the app counts it and record the decision in an ADR. (The answer key ignores it, which is itself a decision.)

**Break it:** have Claude plant an off-by-one error in the consecutive-days rule. If your tests don't catch it, they're too weak; add the test that would have. Deliberately breaking code to test your tests is called mutation testing.

**Checkpoint**

- Why must the checker be independent of the solver that builds rosters?
- What does a property test find that example tests miss?
- How does your app count hours on the night the clocks change?

**Answer key:** `app/solver/checker.py`, `tests/test_solver.py`.

### Week 8: the solver, part 1 (hard rules)

**Deliverable:** auto-roster for two weeks that fills the team template while keeping every hard rule, with your checker confirming zero breaches. Resize the droplet to 2 vCPU / 4 GB this week.

**Concepts:** why rostering explodes combinatorially (49 doctors × 91 days × about 20 positions); greedy algorithms versus constraint programming; a CP-SAT model's parts (yes/no decision variables, constraints, an objective); feasible versus optimal; slack variables.

**Exercises**

1. **A toy by hand.** Four doctors, seven days, two shifts and three rules, in OR-Tools in one script. Ask Claude to write out your model as maths so you can see the structure.
2. **Greedy first, by hand.** Write a 30-line "fill each slot with the first free person" roster. Find a case where it gets stuck but CP-SAT succeeds. That's the reason the solver exists.
3. **Delegate.** Spec the hard constraints. Claude builds the solver module. Acceptance test: its output passes your checker with zero errors on the demo data.
4. **Make it impossible.** Remove staff until it fails with INFEASIBLE. Then add "unfilled" slack variables so it returns a roster with visible gaps instead of nothing.

**Break it:** shifts in the week before the window must count toward rest rules. Remove that and see whether your checker notices.

**Checkpoint**

- What is one decision variable in your model, in plain words?
- Why are slack variables better than failing?
- How can a solver be correct and still useless?

**Answer key:** `app/solver/context.py`, the first half of `app/solver/engine.py`.

### Week 9: the solver, part 2 (fairness, preferences, performance)

**Deliverable:** 13-week rosters with soft rules solved in the five-step priority order (EFT-based hours, period mix, fair shares pro-rated by EFT, then preferences); a pre-flight capacity check; solving in the background with a progress page; and a benchmark script that tracks unfilled positions, rule breaches, fairness spread and run time.

**Concepts:** objective functions where weights make trade-offs explicit; two-phase optimisation (fill first, then balance); convex penalties so a shortfall is shared rather than dumped on one person; benchmark-driven development; background jobs. Weights are rostering policy, so they belong in settings where admins can see them, not buried in code.

**Exercises**

1. **Predict, then test.** Before changing anything, predict what happens if the hours weight is 10× the preference weight. Run it. Were you right?
2. **Benchmark first, by hand.** `bench.py` prints its metrics as JSON on fixed data with a fixed random seed.
3. **Delegate against a number.** "Reduce the largest hours deviation without increasing unfilled positions. Run `bench.py` after each change." Claude can now iterate on its own, because it has a check it can run. You can also set the benchmark as a `/goal` condition so Claude keeps working until it's met.
4. **The pre-flight check.** Recreate the template with 3 consultant day shifts for every 2 evenings, and confirm the check predicts the conflict with a hard 50:50 rule before any solve.

**Break it:** start two solves at once. What happens, and what should?

**Checkpoint**

- Why solve in two phases?
- Why is "fair" a modelling choice, not a fact?
- What happens to a running solve if the server restarts?

**Answer key:** the objective section of `app/solver/engine.py`, `app/solver/preflight.py`, `app/jobs.py`.

## Weeks 10–12: shipping like a modern team (Delegate to Orchestrate)

The last three weeks turn a working app into a run service, then use it to practise how AI-native teams work: you act as tech lead over several Claude sessions, with automated checks as the guardrails.

### Week 10: views, manual override and publishing

**Deliverable:** the week grid, the by-person matrix, a mobile "my shifts" page, a cell editor with ranked candidates and rule flags, locking, publishing, an A4 landscape printout, a calendar (iCal) feed, sick leave on the fly, flags on unmet preferences, and a stats page per person.

**Concepts:** designing for different users (admin versus staff); HTMX partial swaps and events; print stylesheets; locking and audit logs for accountability; the iCal format; checking interfaces with screenshots.

**Exercises**

1. **Design before code.** Mock the week view in Claude Design using your design system. The mock becomes part of the spec.
2. **Delegate with a visual check.** Spec each view with acceptance criteria. Ask Claude to take Playwright screenshots at 1440 px and 390 px wide and compare them with the mock, listing the differences and fixing them.
3. **Build by hand.** The print stylesheet. Iterate until one week fits on one A4 landscape page; there's no shortcut to developing the eye for this.
4. **Writer and reviewer.** One Claude session builds the cell editor; a second, fresh session reviews it against the spec. Fresh context isn't biased toward code it just wrote.

**Break it:** as a staff member, try to see unpublished dates by editing the URL and through the calendar feed. Your tests must prove both are blocked.

**Checkpoint**

- Why lock manual changes automatically?
- How do you prove each kind of user sees only the right dates?
- Who needs the audit log, and when?

**Answer key:** `app/routers/roster.py`, `app/templates/roster/`, `app/templates/partials/cell_editor.html`, the print section of `app/static/app.css`.

### Week 11: production readiness

**Deliverable:** continuous deployment (merging to `main` deploys to a staging copy; a git tag deploys to production); structured logs; an uptime alert; nightly backups with a tested restore; Claude reviewing every pull request in CI; hooks that enforce formatting.

**Concepts:** continuous integration versus continuous deployment; separate environments and their configuration; versioned container images in a registry; secrets in GitHub Actions; observability (logs, health checks, alerts); recovery targets: how much data you can lose (RPO) and how long you can be down (RTO); advisory rules (`CLAUDE.md`) versus guaranteed ones (hooks).

**Exercises**

1. **Build by hand.** The deploy workflow: build the image, push it to GitHub's container registry, deploy to staging over SSH. You write the YAML.
2. **Restore drill.** Restore last night's backup into staging and time it. That time is your real RTO.
3. **Hooks.** A `PostToolUse` hook that runs `ruff format` after every file Claude edits, and a `PreToolUse` hook that blocks edits to `.env` and to migrations already applied. Hooks live in `.claude/settings.json`; run `/hooks` to see what's configured.
4. **AI code review in CI.** Run `/install-github-app` in Claude Code and choose the review workflow. On your next three pull requests, compare its comments with your own review: where it's right, where it's noisy, where it's wrong.
5. **Headless Claude.** On each release tag, `claude -p` writes release notes from the merged pull requests.

**Break it (game day):** stop the database container in staging mid-solve. Follow your runbook, then write a short blameless postmortem: what happened, how you noticed, what you'll change.

**Checkpoint**

- What's the difference between CI and CD?
- What are your RPO and RTO, as numbers?
- Why is a hook more reliable than a rule in `CLAUDE.md`?

**Answer key:** only `deploy/` covers this. Staging, CD and AI review go beyond the answer key.

### Week 12: capstone, shift-swap requests

**Deliverable:** a feature the answer key doesn't have. A doctor offers a shift, a colleague accepts, the checker validates the swap, an admin approves, and the audit log and notifications follow. Delivered through spec, parallel agents, AI and human review, and CD.

**Concepts:** spec-driven development; splitting work into parallel streams; git worktrees; integration risk and contract tests; the human as the accountable tech lead.

**Exercises**

1. **Spec by interview.** Ask Claude: "I want to build shift-swap requests. Interview me in detail using the AskUserQuestion tool about implementation, UI, edge cases and trade-offs, then write a complete spec to SPEC.md." Then start a fresh session to build from it.
2. **Split the work into three streams:** data model and migration; swap validation (reusing the checker); interface and notifications. Agree the interfaces between them in the spec first.
3. **Run them in parallel.** `claude --worktree swap-model`, `claude --worktree swap-rules` and `claude --worktree swap-ui` in three terminals. Each gets its own checkout and branch, so they can't collide.
4. **Make a skill.** Turn your shipping routine (spec check, tests, implement, screenshots, pull request) into `.claude/skills/ship-feature/SKILL.md`, invoked as `/ship-feature`.
5. **Be the tech lead.** Decide the merge order, resolve the integration conflicts, tag the release.
6. **Retrospective.** How long would this have taken working the week 4 way? Where did parallel agents cost more than they saved? Update `CLAUDE.md` to reflect your new level.

**Checkpoint**

- For each stream, could you have specified it, judged it and debugged it?
- What's one thing you'd never delegate, and why?
- What in your process would you change for the next feature?

## Pass 2, weeks 13–20: the full feature set (Delegate to Orchestrate)

Pass 2 builds the three feature specs that follow, in dependency order, at the autonomy you earned in pass 1. Each week keeps the six-step rhythm, with one change: the hand-build step becomes writing the spec and the acceptance tests yourself, and Claude builds to them.

| Week | Build | From spec | Depends on |
| --- | --- | --- | --- |
| 13 | Leave types, request-and-approve workflow, privacy rules; sick leave on the fly | Rules, leave, onboarding | Pass 1 preferences and roster views |
| 14 | Preference importance levels, the admin review queue, make-it-a-requirement, per-rotation budget | Two user types, EFT | Week 13 workflow (reuse it) |
| 15 | Dated EFT, full-time hours per role, pro-rated targets and tolerances in the checker and solver | Two user types, EFT | Pass 1 checker and solver |
| 16 | Rotations, bulk import with dry-run preview, roll-over, long leave as an employment break | Rules, leave, onboarding | Week 15 EFT |
| 17 | Period mix and weekend-load rules, pre-flight checks, the five-step priority solve with slack; fairness ledger between runs; minimum-changes re-rostering mode | Both | Week 15 |
| 18 | Fatigue sequencing rules, supervision rules, request cut-off and publish-ahead settings | Review section | Week 17 |
| 19 | Unmet-preference flags, per-person stats page, calendar day types and named templates | Rules, leave, onboarding | Weeks 14 and 17 |
| 20 | Shift swaps with eligibility and re-check; open-shift board; config export and import for any team | All three | Everything above |

By week 20 you have an app that a department could trial on fictional data, and that MH IT could assess.

## Feature spec: configurable for any team

Each team runs its own copy of the app, which starts blank. The team defines its own roles and gives each role its own times for each shift; nothing ED-specific is built in. This is a spec for you to build, folded into the weeks listed at the end.

### Decisions

- **One copy per team.** One install serves one team, with its own database and settings. No multi-team data model.
- **Shift times belong to roles.** Shifts are named periods (Day, Late, Night). Each role works a period at its own times, and a role with no times for a period never works it.

Example (fictional):

| Role | Day | Late | Night |
| --- | --- | --- | --- |
| Consultant | 08:00–18:00 | 14:00–24:00 | — |
| Registrar | 07:30–17:30 | 14:30–24:00 | 22:00–08:30 |
| Intern | 08:00–16:30 | 14:30–23:00 | — |

### Why this shape

There are two ways to model role-specific times:

- **Option A, role-tagged shift types.** Make "Registrar Night 22:00" its own shift type, restricted to registrars. It's a smaller change, but the roster grows a separate band per role, and rules like "50:50 day/evening" have to group shift types by hand.
- **Option B, periods plus per-role times (chosen).** The roster, team template and rules talk about periods; the hours come from the role. One "Night" band shows everyone on nights, and rules stay simple.

Option B is a bigger refactor and the better long-term model.

### Data model changes

| Entity | Fields | Notes |
| --- | --- | --- |
| `Period` (replaces `ShiftType`) | name, category (day / evening / night), colour, sort order | What the template, views and rules refer to |
| `RoleShift` (new) | role, period, start time, duration, active | One row per role per period; no row means the role doesn't work that period |
| `CoverageRequirement` | period instead of shift type | Stream, role, day class, minimum and maximum unchanged |
| `Assignment` | period and role, **plus a copy of the start time and duration** | The copy keeps a published roster unchanged if a role's times are edited later |

### Minimum staffing: role groups

The team template already lets an admin set, per shift × stream × weekday/weekend, how many of each role are required. It can say "1 consultant" but not "1 registrar *or* HMO". Role groups close that gap.

- **`RoleGroup`**: a name and a set of roles, defined by admins. Examples: "Senior decision-maker" = Consultant or In charge; "Middle grade" = Registrar or HMO; "Any doctor" = every role.
- **A template row names either a role or a role group.** The minimum is met by anyone holding any role in the group. The grid editor shows groups as extra columns after the roles.
- **Everything else stays as it is.** Coverage checks, the solver's fill step, gap flags and the manual-override candidate list all treat a group row as "one position, several eligible roles". Someone who holds two roles (In charge and Consultant) still fills only one position per shift.
- **Resolution order in the solver:** fill single-role rows first, then group rows with whoever is left. This stops the only consultant on duty being used for a "middle grade" slot while a registrar sits idle.
- **Rule reuse.** A role group is the same object a supervision rule needs ("Intern requires a *Senior decision-maker* on the same stream and period"), so build groups once in week 3 and reuse them in week 18.

**Acceptance tests**

1. A row "1 Middle grade" is satisfied by a registrar, by an HMO, and flagged as a gap when neither is present.
2. A shift with "1 Consultant" and "1 Senior decision-maker" needs two different people; one consultant doesn't satisfy both.
3. The manual-override list for a group row shows every eligible role, each flagged for leave, rest and double-booking as now.
4. Deleting a role that belongs to a group is refused until it's removed from the group.
5. Round-tripping a config export recreates the groups and the template rows that use them.

### Behaviour changes

- **Team template editor:** only shows role × period cells that have times. Most teams share one set of times, so the role-times grid has an "apply to all roles" shortcut, and different times per role are the exception.
- **Solver:** only creates options where the role has times for that period. Hours and rest gaps come from each assignment's own times; the rest check pairs the actual times, not the period names.
- **Rule checker:** the same, reading the copied times on each assignment.
- **Views:** rows grouped by period. A role's times show in its row label, such as "Registrar 22:00–08:30".
- **Manual override:** offering a role a period it has no times for shows ⛔.
- **Editing a role's times:** changes unpublished assignments only. Before saving, show the admin how many future shifts will move.

### Starting blank, per team

- **No built-in setup.** The seed creates nothing team-specific. On first sign-in, an admin sees a setup checklist: team name and terms, periods, roles, the role-times grid, streams, template, rules, staff import.
- **Configurable terms.** What to call a stream (stream, pod, team, area), plus the app name, organisation and colours (through the brand token layer).
- **Starter configs.** `configs/ed.json`, `configs/hith.json` and `configs/ward.json` can be imported, and the current setup can be exported to JSON. Keep these files in git and review changes like code: that's "configuration as code".
- **Deployment.** Same container image for every team; a different `.env` and database per team. Caddy routes `ed.<domain>` and `hith.<domain>` to separate app containers.

### Migrating existing data

Write an Alembic data migration:

1. Each existing shift type becomes a period.
2. Each shift type × role pair in the team template becomes a `RoleShift` with that shift's times.
3. Each assignment gets its period and a copy of its times.

Run it on a copy of the database first, and write a downgrade.

### Acceptance tests (write these before the code)

1. A role with no Night times can't get a night: not in the template editor, not from the solver, and manual override shows ⛔.
2. A registrar working Night (22:00–08:30) can't start Day at 07:30 the next morning; the rest rule uses the registrar's own times.
3. Contracted-hours totals use each role's own shift lengths.
4. Changing Intern Late from 14:30–23:00 to 15:00–23:30 moves unpublished shifts only; published shifts keep their old times.
5. A fresh install has no roles or periods. Importing `configs/hith.json` produces a working roster in under 10 minutes.
6. Exporting a config and importing it into a blank copy gives an identical setup.

### Where it fits

| Week | Add |
| --- | --- |
| 3 (pass 1) | Model `Period` and `RoleShift` from the start, instead of shared shift types |
| 4 (pass 1) | The role-times grid editor with "apply to all roles"; the terms setting |
| 8–9 (pass 1) | Solver and checker use per-role times and rest pairs |
| 11 (pass 1) | Deploy a second copy ("HITH") on the same server through Caddy: same image, different config |
| 20 (pass 2) | Config export and import, starter configs, the first-run setup checklist |

## Feature spec: rules, leave, onboarding, stats and swaps

None of these eleven needs is fully met by the answer key. Minimum staffing comes closest, eight are partly there, and two are new: sick leave on the fly and shift swaps. Build leave and on-the-fly sick leave first: they are what keep a roster usable once real life happens.

| # | Need | In the answer key today | What to add | Week |
| --- | --- | --- | --- | --- |
| 1 | Day / evening / night ratios | 50:50 between two periods | A three-way mix rule, e.g. 40:40:20, per role | 17 |
| 2 | Weekday / weekend ratio | Fair share of weekends among peers | A per-person cap, e.g. at most 1 weekend in 3, or weekend shifts at most 30% | 17 |
| 3 | Public holidays | A holiday list and one global "treat as weekend" switch | A choice per day: weekend, weekday or a custom template; "special days" for local events | 19 |
| 4 | Leave with approval | Leave entered as a "not available" preference | Leave types and a request-and-approve workflow, separate from preferences | 13 |
| 5 | Preferences | Staff add avoid, prefer or request, by date, weekday or period | Importance levels, the admin review queue and a per-person budget (next section) | 14 |
| 6 | Minimum staffing | Template minimums for weekdays and weekends, plus a headcount rule per period | Role groups ("1 registrar or HMO"), in spec 1; date-specific overrides, e.g. winter surge | 3, 19 |
| 7 | Sick leave on the fly | — | "Mark sick" in a few taps, gaps flagged, replacements ranked | 13 |
| 8 | Bulk onboarding with rotations | CSV import of staff | Dated rotations with bulk import and a preview before saving | 16 |
| 9 | Unmet preferences highlighted | Listed in the check report | Flagged on the roster, a "preferences met" figure per person, shown on My shifts | 19 |
| 10 | Per-person stats | A table in the auto-roster report | A stats page for each person, for this rotation and year to date | 19 |
| 11 | Shift swaps | A basic version is the week 12 capstone | Offers shown only to eligible colleagues (flow below) | 20 |

### Ratio rules

- **Period mix.** Target percentages per period that sum to 100, a tolerance in shifts, and the roles it applies to. Hard or soft. It replaces the 50:50 rule: 50:50 becomes day 50, evening 50, night 0.
- **Weekend load.** Either a cap such as "at most 1 weekend in any 3" (a rolling window), or a maximum share of weekend and public-holiday shifts. Hard or soft.
- **Pre-flight check.** Test both against the team template before solving, as the 50:50 check does now. A 40:40:20 mix is impossible if the template has no nights for that role.

### Calendar: holidays and special days

- **`CalendarDay`**: date, name, kind (public holiday or special day), which staffing template applies, and whether it counts as a weekend for fairness.
- **Named templates.** Templates become named (Weekday, Weekend, plus custom ones like "Christmas reduced"), and each staffing requirement belongs to one.
- **Yearly import.** Import each year's holidays from a CSV or calendar file instead of typing them.

### Leave

- **Leave types, configured per team:** name, colour, whether it needs approval, and whether it counts toward contracted hours. Conference leave usually counts; annual leave usually lowers the target.
- **Workflow:**
  - A request is *pending*, then *approved* or *declined*. An approved request can later be *cancelled*.
  - The solver treats pending leave as a strong "prefer not", so a plan never depends on leave that may be declined. Approved leave is a hard block.
- **Approval queue.** Each request shows its impact: which shifts become hard to fill, and who else is off on those days.
- **Privacy.** Colleagues see only "On leave". The type and any note are visible to the person and to admins. Sick and parental leave are personal information, so keep notes optional and short.
- **Data:**
  - `LeaveType`
  - `LeaveRequest`: person, type, dates, optionally which periods, status, note, who decided and when

### Sick leave on the fly

1. An admin taps the person's name on the roster (or "Mark sick" on a day) and chooses the days: today, today and tomorrow, or custom.
2. The app records approved sick leave and takes the person off their shifts in that range. The removed shifts stay in the audit log.
3. The empty positions show as gaps, with the ranked replacement list already filtered to people who are eligible and free.
4. The whole thing takes at most three taps on a phone.

### Onboarding by rotation

- **`Rotation`**: a name and dates, e.g. "Term 1 2027".
- **`RotationMember`**: person, role, hours, streams and dates for that rotation. Someone can be a registrar in one rotation and a consultant in the next.
- **Bulk import per rotation, with a dry run first.**
  - The preview lists new people, changed roles, leavers and errors.
  - Nothing is saved until you confirm, and then everything saves in one transaction.
  - Logins are created in bulk, with temporary passwords or single sign-on.
- **Roll over.** "Copy last rotation" carries continuing staff forward. Leavers end automatically at the rotation's end date.

### Unmet preferences and per-person stats

- **On the roster.** A flag on any shift that goes against a preference. Hovering shows why, for example "no one else could fill Silver In-charge".
- **Preferences met %:** honoured preferences divided by those that applied, per person. Show the spread across the team so the same people aren't always the ones missing out. An optional soft rule can spread unmet preferences evenly.
- **Stats page per person:**
  - hours against target
  - period mix against target
  - weekends and public holidays, nights, the longest run of days
  - leave taken by type, preferences met, swaps made
  - all shown for this rotation and year to date, with the team median beside each figure
- **Who sees what.** Staff see their own stats; admins see everyone's.

### Shift swaps

- **Two modes.** The person offering picks a shift and either gives it away or offers it in exchange for one of the other person's shifts.
- **Eligibility.** The offer appears only to colleagues who meet all of these:
  - have the right role and times for that period
  - are not on approved or pending leave that day
  - are not already working that day
  - would still meet every hard rule after the swap (rest, consecutive days, weekly cap, hours ceiling), as would the person offering
- **Re-check on acceptance.** The swap is checked again when someone accepts, because the roster may have changed since the offer.
- **Approval.** An admin approves, or a setting auto-approves swaps that break no soft rules. Offers expire a set number of hours before the shift. Every step is audited.

*(Interactive diagram in the Claude doc: shift swap flow — eligibility filter → offer → re-check on acceptance → admin approval. Text version: a swap request is offered only to people who are not on leave and not already working that shift; eligibility is re-checked when someone accepts, because the roster may have changed; the admin approves before the assignment moves.)*

The filter runs twice: once to decide who sees the offer, and again on acceptance, because someone may have picked up a shift or leave in between.

### Acceptance tests

1. A 40:40:20 rule for registrars leaves every registrar within ±2 shifts of each target over 13 weeks.
2. A hard "1 weekend in 3" rule: nobody works two weekends in any three in a row.
3. Christmas Day on a custom "Christmas reduced" template is staffed to that template and counts as a weekend for fairness.
4. Pending leave is avoided where possible; approved leave is never rostered; declined leave changes nothing.
5. Marking someone sick today removes their late shift within three taps, and the replacement list excludes anyone working today, on leave, or who would break the rest rule.
6. A Term 1 import preview shows new, changed, leaving and invalid rows, and nothing is saved until confirmed.
7. A Saturday night swap offer isn't shown to someone on leave that day, someone starting a day shift at 07:30 on Sunday, or an intern with no night times.
8. A colleague viewing the roster sees "On leave", never the leave type.

### Scope, honestly

This is most of pass 2 (weeks 13–20). Build in this order: leave and sick-on-the-fly, ratio rules, rotation onboarding, unmet preferences and stats, swaps (already the capstone), then the calendar templates.

## Feature spec: two user types, EFT, and how the auto-roster decides

There are two kinds of user: admins, who run the roster, and staff, who manage their own availability. Every share of work is pro-rated by each person's EFT (their fraction of full-time). The auto-roster then works through a fixed order of priorities, so a staff member's genuine requirement can never lose to a nice-to-have.

### Two user types

|  | Admin | Staff |
| --- | --- | --- |
| Business rules, team template, periods, roles | Edit | — |
| Leave | Approve or decline | Request; see own status |
| Preferences | Review: accept, change priority, make a requirement, or decline | Enter own, with importance and an optional reason; see the admin's decision |
| EFT | Enter it, with the date it starts | View own only |
| Auto-roster, manual override, publishing | Yes | — |
| Roster | All dates, including drafts | Published dates only |
| Stats | Everyone | Own |
| Logins, making someone an admin | Yes | — |

This replaces the answer key's three access levels (staff, manager, admin) with two. Any admin can make another person an admin; keep at least two admins so the team is never locked out.

Only admins enter EFT; staff can see their own. It's a contract term, and it changes everyone else's share of nights and weekends. Preferences are the opposite: staff enter them, and admins decide how much each one counts.

### Preferences: staff enter, admins prioritise

- **Staff enter every preference themselves.** For each one they give dates, weekdays or periods, how important it is (*would like*, *important*, *essential*), and an optional reason. These map to low, medium and high priority. A staff member can't make anything binding.
- **Admins review each one in a queue** and choose one action:
  - **Accept** at the importance the person gave.
  - **Change priority** up or down (low, medium, high), for example raising a carer's request or lowering a routine "no Mondays".
  - **Make it a requirement:** hard, never broken by the auto-roster. Examples: "not available Fridays (second job)", "no nights (approved medical restriction)", "works Monday to Wednesday only".
  - **Decline,** with a short reason the person sees.
- **Before review,** a preference counts at the importance the person chose, capped at *high*. Nothing becomes hard until an admin makes it a requirement.
- **Queue order:** items marked *essential* first, then by start date, so time-sensitive ones aren't missed.
- **Staff see the outcome** on their availability page: accepted at what priority, made a requirement, or declined and why.
- **Keep the priority levels honest.** If everyone marks everything *essential*, the levels mean nothing. Give each person a budget per rotation, for example three *high* preferences. The admin can override the budget when a case needs it. This is the "preference points" approach many rostering systems use.
- **Part-time is EFT, not a preference.** Working 0.6 is set through EFT, which drives every target below. A working pattern such as "Monday to Wednesday" is a preference the admin makes a requirement.

### EFT and pro-rating

- **Settings per role:** full-time hours per week (e.g. consultant 40, registrar 38).
- **Per person:** an EFT value that's **dated**. "0.6 from 1 Dec" changes the targets from that date only. This ties into rotation membership in the previous spec section.
- **Expected hours** for a period = EFT × full-time hours × weeks, minus leave that doesn't count toward hours. The stats page shows the expected number of shifts beside the hours.

Which rules scale with EFT, and which don't:

| Rule | Scales with EFT? | How |
| --- | --- | --- |
| Contracted hours target | Yes | EFT × full-time hours |
| Fair share of weekends, nights, public holidays | Yes | Team total × (person's EFT ÷ sum of everyone's EFT) |
| Period mix (e.g. 40:40:20) | Yes, automatically | It's a percentage of each person's own shifts |
| Ratio tolerances | Yes | Set as a percentage, not shifts: ±1 shift is 4% for a full-timer but 10% at 0.4 EFT |
| Shifts per week, as a contract limit | Optional, per rule | e.g. at most EFT × 5 rounded up, plus 1 |
| Rest between shifts, consecutive days and nights, days off after nights | **Never** | These are safety limits, the same for everyone |

### How the auto-roster decides

**Horizon.** Admins set how far ahead to generate (default 13 weeks) and how far ahead the roster is published (e.g. 6 weeks). "Generate the next period" starts the day after the last published date.

**Priorities, strictly in order.** Each step is optimised while holding the steps before it:

1. **Never broken:** hard business rules, approved leave, approved requirements, employment dates.
2. **Fill the template:** minimum staffing on every shift. Any gap is reported, never hidden.
3. **Contracted hours:** each person's EFT-based target, within tolerance.
4. **Business soft rules:** ratios, fair shares, whole weekends, by weight.
5. **Preferences**, by strength, spreading any that can't be met evenly across the team.

**A note on strict order.** Taken literally, a tiny improvement at step 4 outweighs any number of preferences at step 5. Allow a small configurable slack, e.g. "accept up to 5% worse on step 4 if it meets more preferences". The report should then say what was traded.

**Report.** Group the run report by those five steps: what's broken (should be nothing), gaps, hours against EFT, business-rule shortfalls, unmet preferences.

### Acceptance tests

1. A 0.5 EFT registrar's expected hours and expected weekend shifts are half a 1.0 EFT registrar's, within tolerance.
2. EFT changing from 1.0 to 0.6 on 1 Dec lowers targets from that date only; hours before it are unchanged.
3. A 0.4 EFT consultant on a 40:40:20 rule stays within the percentage tolerance, not ±1 shift.
4. Rest and consecutive-day limits are identical for every EFT.
5. A preference the admin makes a requirement ("never Fridays") is never broken, even when that leaves a Friday gap; the gap is reported.
6. An *essential* preference not yet reviewed is honoured where possible, never treated as hard, and listed separately when not met.
7. Raising a preference's priority changes the next auto-roster run; declining it removes it from the solve, and the staff member sees the reason.
8. A staff member can't exceed their high-priority budget for a rotation unless an admin overrides it.
9. A staff login can't see drafts, other people's leave types or stats, or any admin page, and can't change anyone's EFT, including their own. An admin can't remove the last admin.
10. With 5% slack allowed, preferences met rise, and the report states the business-rule cost.

### Where it fits

| Week | Add |
| --- | --- |
| 3 (pass 1) | Dated EFT and full-time hours per role in the data model, so nothing has to be migrated later |
| 5 (pass 1) | Two user types and the permission tests in test 9 |
| 14 (pass 2) | The preference review queue (accept, change priority, make a requirement, decline) and the per-rotation budget, reusing the leave workflow from week 13 |
| 15 (pass 2) | EFT-scaled targets and percentage tolerances in the checker and solver |
| 17 (pass 2) | The five-step solve with configurable slack; the report grouped by step |

## Review: your requirements, checked, and ideas from other rostering tools

All 24 of your requirements are now covered in the plan or the specs. The review found eight inconsistencies, all now fixed, plus six gaps that need a decision from you. Comparing with other rostering tools and Victorian rostering guidance suggests four additions worth making before real use.

### Your requirements, traced

| # | Your requirement | Where it's covered | Status |
| --- | --- | --- | --- |
| 1 | Configurable shift types and times | Spec 1 (periods and role times); weeks 3–4 | Covered |
| 2 | Streams with 1–5 people, varying by shift | Team template; week 4 | Covered |
| 3 | Configurable role names | Weeks 3–4; spec 1 | Covered |
| 4 | Preference patterns (no Thursdays, no Monday lates) and unavailable dates | Spec 3 preferences; week 6 | Covered |
| 5 | Business rules such as 50:50 day/evening for consultants | Spec 2 ratio rules; weeks 7, 9 | Covered |
| 6 | Minimum staffing by day/evening and weekday/weekend | Team template and headcount rule; spec 2 | Covered |
| 7 | Auto-roster for the next 3 months, configurable | Spec 3 horizon; weeks 8–9 | Covered |
| 8 | Manual override | Week 10 | Covered |
| 9 | Web login | Week 5 | Covered |
| 10 | Monash Health theme | Your design system artifact; brand tokens in spec 1 | Covered, for learning only |
| 11 | Staff see own shifts; admin prints the week | Week 10 | Covered |
| 12 | Roles and their shifts configurable by any team | Spec 1 | Covered |
| 13 | Day/evening/night and weekday/weekend ratios | Spec 2 ratio rules | Covered |
| 14 | Public holidays as weekends; mark any day | Spec 2 calendar | Covered |
| 15 | Leave with approval: conference, annual, parental, sick | Spec 2 leave | Covered; long leave is a gap (below) |
| 16 | Sick leave on the fly | Spec 2 | Covered |
| 17 | Bulk onboarding with rotations | Spec 2 | Covered |
| 18 | Unmet preferences highlighted | Spec 2 | Covered |
| 19 | Per-person stats | Spec 2 | Covered |
| 20 | Swaps never offered to people on leave or already working | Spec 2 swap flow | Covered |
| 21 | Two user types | Spec 3 | Covered; weeks 5 and 10 fixed |
| 22 | Business rules before preferences; some preferences are requirements | Spec 3 priority order | Covered |
| 23 | EFT pro-rating, with EFT entered by admins | Spec 3 | Covered; fixed in this review |
| 24 | Staff enter preferences; admins accept, prioritise or make them requirements | Spec 3 | Covered |

### Fixed in this review

- **Weeks 3–10 described the original design**: shared shift types, three access levels, leave stored as a preference, 50:50 only. They now match the specs.
- **"Manager" appeared in the specs and the swap diagram.** It now reads "admin" throughout.
- **EFT is admin-only.** Staff can no longer request changes, and acceptance test 9 checks they can't edit it.
- **Week 0 pushed to GitHub before any commit,** which fails. A commit step is added, and the `.gitignore` lines now come before the first commit.
- **The second spec overstated what's already built.** It now says none of the eleven is fully met, eight are partly there and two are new.
- **Two importance scales didn't line up.** *Would like*, *important* and *essential* now map to low, medium and high priority.
- **Per-role times would have forced every team to enter times for each role.** An "apply to all roles" shortcut keeps shared times the default.
- **The plan's length was understated.** The intro now says the specs add three to four weeks.

### Gaps that need a decision

- **Rule values from your agreements.** Rest, maximum hours and night limits must match your enterprise agreements and local fatigue policy. The [Victorian rostering toolkit](https://www.safercare.vic.gov.au/sites/default/files/2025-07/Victorian_rostering_toolkit.pdf) gives concrete numbers, but it's written for nurses and midwives, and doctors' agreements differ. Keep every value configurable, and have medical workforce sign off the defaults.
- **Long leave.** Months of parental leave should pause targets and fair shares automatically, rather than appearing as hundreds of leave days in the stats. Model it as a break in employment.
- **Leave balances.** The spec tracks leave taken, not entitlement; balances live in payroll. Decide whether to show an imported balance or leave it out.
- **Sick self-reporting.** Should staff report themselves sick in the app (approved automatically, admins alerted), or only admins?
- **Supervision.** For example: an intern is never rostered without a registrar or consultant on the same shift, and only credentialed consultants can be in charge. Role times cover part of this; it needs its own rule type.
- **Rostered versus worked hours.** Unrostered overtime is a fatigue and pay issue the roster can't see. Leave it out of version 1, but plan a timesheet export.

### Second review: further improvements

A second pass over the whole doc, checking it as a plan you'll actually follow rather than as a list of features.

**Structural fixes made**

- **The 12 weeks were overloaded.** The specs were folded into weeks 6, 9 and 10 as if they fitted, and the intro said the specs "add three to four weeks" while the week-by-week plan still ended at 12. The plan is now two passes: weeks 0–12 build a working app, weeks 13–20 build the three specs in dependency order. Each spec's "Where it fits" table now says which parts are pass 1 foundations and which wait for pass 2.
- **`CLAUDE.md` gained three lines:** no real names or Monash Health identifiers, teach when asked how something works, and stay in plan or manual permission mode. Auto mode is now Claude Code's default and would skip exactly the moments the early weeks need.
- **A sitting-size warning** was added to the weekly rhythm: split each week over two sittings.

**Rule gaps found this pass**

- **No maximum hours per week.** Rest and consecutive-day rules exist, but nothing caps total hours in a rolling 7 days. Add it as a hard rule in week 7; take the number from your agreement and the fatigue policy. With 10-hour shifts, five in a week is already 50 hours.
- **Maximum shift length and overrun.** The app assumes rostered end times. Add a configurable maximum shift length, and leave the room for a later "actual finish" field so unrostered overtime can be measured.
- **Leave cancellation.** The state machine has pending, approved, declined and cancelled, but cancelling approved leave after a roster is published should re-open those days as available and notify the admin, not silently restore shifts.
- **Daylight saving.** Week 7 asks you to decide how a night shift is counted on the change night. The decision also affects rest-gap maths and the iCal feed. Store assignment times in UTC with the local date, and compute durations from real instants, not wall-clock arithmetic.

**Design improvements**

- **Audit who changed EFT.** Since admins control EFT and it drives everyone's targets, every EFT change should be audited with the old value, new value, effective date and who made it. Add it to the acceptance tests.
- **Preference budget by EFT?** A 0.5 EFT person has half the shifts, so three high-priority preferences carry twice the weight. Either scale the budget by EFT or state deliberately that you don't. Pick one and write it down.
- **Supervision is a template rule, not a people rule.** The simplest reliable form: a stream–period template row can require that another role is also present in the same stream ("Intern requires Registrar or Consultant on Silver, same period"). That's a coverage constraint the solver already understands.
- **Soft-lock before publication.** Add two dates per roster run: a request cut-off (no new preferences for that period) and a publish date. Between them, admins review the draft. After publication, changes go through swaps, leave or admin override only.
- **Re-rostering mode is worth bringing forward.** Once sick leave on the fly exists (week 13), a full re-solve that moves dozens of published shifts will be unusable. The minimum-changes solve mode in week 20 should move to week 17 alongside the solver work. The pass 2 table is updated.

**Learning-plan improvements**

- **Week 3 is the right time to introduce `pyright`** (a type checker). Typed models catch a whole class of bugs before tests run, and Claude writes better code when types constrain it. One line in CI, lifelong habit.
- **Add a "demo day" at weeks 6, 12 and 20:** show the app to one colleague on fictional data and write down what they tried first and what confused them. Real feedback beats another feature.
- **Keep this doc in the repo.** Export it to `docs/PLAN.md` and update it with each pull request that changes scope. A plan that only exists outside the repo drifts, which is exactly what this review found.

**Still your call** (unchanged from the first review): rule values from your agreements, long leave as an employment break, leave balances, sick self-reporting, and rostered versus worked hours.

### Ideas from other rostering tools

Based on what each vendor publishes; I haven't used these products.

| # | Idea | Seen in | Why it matters | Recommendation |
| --- | --- | --- | --- | --- |
| 1 | Fairness memory across rosters | Lightning Bolt ("workload and fairness analysis") | The spec resets fairness every 13 weeks, so each run is fair but the year may not be: the same people keep getting Christmas | **Add before real use**: carry a fairness ledger between runs (week 9) |
| 2 | Fatigue-aware sequencing | Victorian rostering toolkit: forward rotation (day, late, night), no nights just before leave, at most 3 nights in a row | Current rules limit counts, not order | **Add before real use**: rules for forward rotation, no late-then-early, no nights before leave, no isolated single shifts (week 7) |
| 3 | Request deadlines and lock windows | Victorian toolkit: soft and hard lock periods, publishing 28 days ahead | Late preferences shouldn't destabilise a published roster | **Add before real use**: a request cut-off before each run and a publish-ahead setting (week 9) |
| 4 | Supervision and skill-mix rules | HosPortal ("Set Supervision Requirements"), RosterLab (skill mix) | Safety: juniors are never unsupervised | **Add before real use**: a supervision rule type (week 7) |
| 5 | Re-rostering with minimal disruption | RosterLab ("Re-rostering") | After sick leave, a fresh solve can move many people's shifts | **Next**: a minimum-changes mode that fills gaps by moving as few published shifts as possible (week 10) |
| 6 | Open-shift board | RosterLab ("Open Shifts"), HosPortal ("Swaps & shifts Market"), Victorian toolkit (supplementary roster) | Volunteers fill gaps before admins start phoning | **Next**: unfilled shifts shown to eligible staff, first to accept wins (week 12) |
| 7 | Notifications | HosPortal (email, SMS, alerts), RosterLab (mobile) | Staff miss changes otherwise | **Next**: email for publishing, approvals, swaps and new gaps; push notifications later (week 11) |
| 8 | Plain-language explanations | RosterLab ("AI Roster Assistant") | "Why am I on Christmas?" is the most common roster complaint | **Later**: answer each person from the solver report using the Claude API, a natural tie-in with your AI work |
| 9 | Self-rostering round | RosterLab (self-scheduling) | Consultants often pick first, then the solver fills the rest | **Later** |
| 10 | Timesheets and payroll export | HosPortal (timesheet adjust and export) | Pay and overtime | **Later**: CSV export only |
| 11 | Night-duty preference types | Victorian toolkit: permanent nights, blocks or ad hoc | Some people prefer blocks of nights | **Next**: add as preference options (week 6) |

Sources: [Lightning Bolt summary](https://intuitionlabs.ai/software/emergency-department-operations/ed-physician-scheduling/lightning-bolt) · [RosterLab healthcare](https://rosterlab.com/industries/healthcare) · [HosPortal](https://www.hosportal.com/) · [Victorian rostering toolkit, Safer Care Victoria, June 2025](https://www.safercare.vic.gov.au/sites/default/files/2025-07/Victorian_rostering_toolkit.pdf)

## Speed-up map: after you know the foundations

Once you understand a foundation, Claude Code turns days of typing into a spec, a check, and a review. The work doesn't vanish; the bottleneck moves from writing code to specifying what you want and verifying what you got. The right-hand column is what stays yours however capable the tools get.

| Foundation | Learned in | How Claude Code speeds it up | What you still own |
| --- | --- | --- | --- |
| Project setup | Weeks 0–1 | `/init` drafts `CLAUDE.md`; one prompt scaffolds an app, tests and CI in your conventions | The conventions themselves; branch protection |
| CI and CD pipelines | Weeks 1, 11 | Writes workflow YAML; `@claude` on a pull request fixes a red build from its log | What must pass before a release; secrets and permissions |
| Containers and servers | Week 2 | Writes Dockerfiles and compose files; diagnoses failures from logs | What's exposed to the internet; backups and restores |
| Data model and migrations | Week 3 | Drafts models and migrations from your diagram | The model's shape; reading every migration before it runs |
| Pages and design | Weeks 4, 10 | Builds pages from a Claude Design mock and checks them by screenshot | User-experience decisions, accessibility, print |
| Security | Week 5 | A security-review subagent and AI review on every pull request | The threat model; final approval; permission design |
| Business rules | Weeks 6–7 | Implements rules from your test tables; generates property tests | The rules themselves (workforce policy) and the tests |
| Optimisation | Weeks 8–9 | Iterates against `bench.py` until a `/goal` is met | Weights are policy; deciding what's good enough |
| Large mechanical changes | Week 12 | `/batch` splits a refactor across parallel subagents in worktrees | Choosing the change; reviewing the result |
| Docs and release notes | Week 11 | `claude -p` in CI writes them from merged pull requests | Accuracy and what users need to know |

A useful rule for any new task: if you could write the acceptance test in under ten minutes, delegate it. If you can't, the task isn't understood yet, and that's work for you, not Claude.

## Costs, and what to learn next

Pass 1 costs roughly A$65–90 in hosting, and pass 2 about A$35 a month more, plus your existing Claude subscription and a domain. Prices were checked on 3 October 2026 at US$1 = A$1.438. Australian customers are probably charged 10% GST on top (not verified).

| Item | When | Cost per month |
| --- | --- | --- |
| [DigitalOcean droplet](https://www.digitalocean.com/pricing/droplets), 1 vCPU / 2 GB | Weeks 2–7 | US$12 ≈ A$17.25 |
| Same droplet resized to 2 vCPU / 4 GB | Week 8 onward | US$24 ≈ A$34.50 |
| Weekly droplet backups (20% of the droplet's price) | Optional | US$2.40–4.80 ≈ A$3.45–6.90 |
| GitHub, public repo, with Actions | Throughout | Free ([standard runners on public repos](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions)) |
| Domain name | From week 2 | About A$15–25 a year (not verified) |

Run staging in week 11 as a second Compose project on the same droplet to avoid paying for a second server. Destroy the droplet when you finish if you don't want to keep the app running.

**After week 12**, pick by interest:

- **Single sign-on with Microsoft Entra ID**, the piece that makes it usable inside a hospital.
- **Typed Python** (pyright or mypy) to catch a whole class of errors before tests run.
- **Multi-tenancy with Postgres row-level security**, if you ever want one install to serve several departments.
- **An accessibility audit** against WCAG 2.2 AA (the web accessibility standard), with real screen-reader testing.
- **The same app in React**, to feel the server-rendered versus single-page trade-off from the inside.

**Sources:** [Claude Code best practices](https://code.claude.com/docs/en/best-practices.md) · [Hooks](https://code.claude.com/docs/en/hooks-guide.md) · [Skills](https://code.claude.com/docs/en/skills.md) · [Worktrees](https://code.claude.com/docs/en/worktrees.md) · [GitHub Actions for Claude Code](https://code.claude.com/docs/en/github-actions.md) · [Claude Code setup](https://code.claude.com/docs/en/setup.md) · [GitHub protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) · [Xe AUD/USD rate](https://www.xe.com/en-us/currencyconverter/convert/?Amount=1&From=AUD&To=USD)
