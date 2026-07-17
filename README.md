# QS Lab MI Research Package

**Version 1.3.0** — the research lab for the QSL course *Modern Investing for Everyone*.

You do not write code. You paste prompts into Claude Code, and Claude does the work — creating strategies, running analysis, and building reports.

## Install
See **[INSTALL.md](INSTALL.md)** for the install prompt. It installs the QSL commands into `~/.claude/skills/`, so they work in every Claude Code session.

Requirements: the Claude desktop app with a Pro subscription, using **Claude Code** (the coding mode — it needs file and shell access to install).

## Commands
See **[COMMANDS.md](COMMANDS.md)**. Currently one:

| Command | What it does |
|---|---|
| `/qsl-spy-ben1` | Creates the **SPY Buy and Hold Benchmark 1** strategy file |

## Contents
| Path | What it is |
|---|---|
| `.claude/skills/` | The commands installed into the student's Claude Code |
| `strategies/` | The canonical strategy files (QuantConnect code) |
| `VERSION` | The package version |
| `CHANGELOG.md` | Version history |
| `INSTALL.md` | The install prompt (step 0 of the course) |

## Updating
Re-run the install prompt. It downloads the current package and replaces the installed commands.
