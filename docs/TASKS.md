# Build plan

Work through one phase at a time. Each phase ends with a check-in before the next starts.

## Phase 1 — Scaffold ✅
- [x] Project structure (`src/triage/`, `tests/`, `docs/`, `examples/`)
- [x] Config from env / `.env` (`config.py`), `.env.example`, `.gitignore`
- [x] Tracker-neutral `Issue` model and `IssueTracker` interface
- [x] CLI skeleton: `triage fetch | run | report`
- [x] README, this task list, smoke test
- [x] Public GitHub repo `juliavasan/bug-triage-agent`, first push

## Phase 2 — Fetch
- [ ] `GitHubTracker` implementing `IssueTracker` (REST API, read-only, `GITHUB_TOKEN`)
- [ ] Pull ~500 most recent issues (open + closed), skip pull requests, handle pagination
- [ ] Capture duplicate hints (`duplicate` label, "Duplicate of #N" in comments / closing reason) for evals
- [ ] Cache to `data/issues.json`; reruns read the cache unless `--refresh`
- [ ] Tests with a recorded API fixture (no network)

## Phase 3 — Duplicates
- [ ] Deterministic pass: exact / near-exact title matches
- [ ] Embeddings (`text-embedding-3-small`) cached to `data/embeddings.parquet` by content hash
- [ ] Hybrid search: cosine similarity + BM25, combined score
- [ ] Rerank top candidates (LLM judge on the shortlist only), with reason + confidence
- [ ] Cluster into duplicate groups; `triage run` prints top clusters

## Phase 4 — Routing + severity
- [ ] Derive owning areas from the repo's existing labels (mapping file, reviewable by a human)
- [ ] Deterministic routing when labels already decide the area
- [ ] LLM picks area + severity otherwise, with reason + confidence
- [ ] Severity factors in user impact and duplicate-cluster size
- [ ] Cache LLM results by input hash

## Phase 5 — Summaries + trends
- [ ] 3-line summary per bug: repro steps, affected devices/platforms, likely cause
- [ ] Week-over-week counts by area and keyword; flag significant increases
- [ ] Write everything to `output/suggestions.json`

## Phase 6 — Report
- [ ] Self-contained HTML report (no external assets)
- [ ] Top section: "What a TPM should act on this week"
- [ ] Duplicate clusters, routing table, severity, summaries, trend chart
- [ ] Readable by a non-engineer in 2 minutes

## Phase 7 — Evals
- [ ] Ground truth from issues labeled / closed as duplicates, and existing area labels
- [ ] Duplicate precision / recall; routing accuracy
- [ ] `triage eval` prints a scorecard

## Phase 8 — Polish
- [ ] README with Mermaid architecture diagram
- [ ] Sample report under `examples/`
- [ ] "How this would run inside a real engineering org" section
- [ ] Optional: Postgres + pgvector backend behind the same vector-store interface
