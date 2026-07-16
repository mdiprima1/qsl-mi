# Step 0 — Install the QSL commands

The student has just installed the Claude desktop app (Pro subscription) and has never used QSL before. The course's first hands-on step shows this prompt with a copy button. The student opens **Claude Code** (in the desktop app) and pastes it.

## The install prompt (student copies this)

> Install my QSL research lab commands. Please do the following:
>
> 1. Download the file https://dev.quantstrategylab.com/qslab-kit.zip to a temporary folder.
> 2. Unzip it.
> 3. Create the folder `~/.claude/skills/` if it does not already exist.
> 4. Copy every folder inside the unzipped `.claude/skills/` into `~/.claude/skills/`. These are my QSL course commands, and I want them available in every Claude Code session.
> 5. List the QSL commands that are now installed.
> 6. Tell me to open a new Claude Code session and run `/qsl-spy-ben1` to create my first strategy.

## What happens
- Claude Code downloads and unpacks the kit and copies the skills into the student's personal skills folder (`~/.claude/skills/`), so the commands work in **every** session, not just one folder.
- Claude Code will ask permission to run the download and copy steps — the student approves once.
- After install, the student starts a **new** session (skills load at session start) and the QSL commands are available.

## Notes
- The kit is distributed as a hosted zip (same pattern as the existing lab-kit). Updating the kit later just replaces the zip; students re-run the install prompt to get new commands.
- The student must be in **Claude Code** (the coding mode of the desktop app), not the plain chat, because the install needs file and shell access.
