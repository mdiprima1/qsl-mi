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
