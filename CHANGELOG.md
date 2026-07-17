# Changelog — QS Lab MI Research Package

All notable changes to this package. The version in `VERSION` is the package version installed by the install prompt.

## 1.0.0 — 2026-07-16
Initial release.
- Added command `/qsl-spy-ben1` — creates the **SPY Buy and Hold Benchmark 1** strategy file.
- Added strategy **SPY-BEN1** (`strategies/SPY Buy and Hold Benchmark 1.md`) — 100% SPY buy-and-hold, $100,000, 2005–2026.
- Added the install prompt (`INSTALL.md`) — installs commands into `~/.claude/skills/` so they work in every Claude Code session.
- Package distributed as a hosted zip: `https://dev.quantstrategylab.com/qslab-kit.zip`.

## 1.0.1 — 2026-07-16
- Rewrote the install prompt so the request is legible: states who publishes the package and what is inside, and makes Claude show the version and command list **before** installing. Installing skills adds instructions to the student's Claude Code, so the inspection is a designed step, not something to suppress.
- Install now adds skills alongside existing ones and changes nothing else.

## 1.1.0 — 2026-07-17
- Strategy delivery redesigned as fixed two-file packages: `spy-ben1.py` (canonical code) + `spy-ben1.pdf` (description). No code is shown on course pages; Claude downloads the package byte-for-byte and verifies SHA-256 checksums against `manifest.json`. Claude never generates or retypes strategy code — every student gets the identical files.
- Replaced `strategies/SPY Buy and Hold Benchmark 1.md` with the `strategies/spy-ben1/` package.
- Student experience is plain language: copy-button prompts on the course page; no slash commands to learn. The install flow and `/qsl-spy-ben1` are deprecated (skill retained temporarily, to be removed).
