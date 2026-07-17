# Step 0 — Install the QSL commands

The student has just installed the Claude desktop app (Pro subscription) and has never used QSL before. The course's first hands-on step shows this prompt with a copy button. The student opens **Claude Code** (in the desktop app) and pastes it.

## The install prompt (student copies this)

> I am a student on the Quantitative Strategy Lab course "Modern Investing for Everyone", and I want to install the official course toolkit: the QS Lab MI Research Package, published by QSL at dev.quantstrategylab.com.
>
> The package contains Claude Code skills — markdown instruction files that guide me through the course exercises. There is nothing executable in it.
>
> Please do this:
>
> 1. Download https://dev.quantstrategylab.com/qslab-kit.zip and unzip it into a temporary folder.
> 2. Before installing anything, show me what is inside: the package version (the `VERSION` file) and the list of commands (`COMMANDS.md`).
> 3. Then copy each folder from the unzipped `.claude/skills/` into `~/.claude/skills/`, so the commands are available in every session. Add them alongside my existing skills — do not remove or change anything that is not part of this package.
> 4. Confirm the version you installed, then tell me to start a new Claude Code session and run `/qsl-spy-ben1` to create my first strategy.

## Why the prompt is written this way

Installing skills means adding new instructions to the student's Claude Code. Claude is right to look before it does that, so the prompt is written to make the request legible rather than to suppress the check:

- **Provenance first** — who the student is, what the package is, and who publishes it.
- **Says what is inside** — markdown command files, nothing executable. This is true; keep it true.
- **Inspection is step 2, on purpose** — Claude shows the version and command list *before* installing. The student sees what they are installing. What would otherwise feel like hesitation becomes a visible trust step.
- **Protects what already exists** — install alongside existing skills, change nothing else.

Do not rewrite this prompt to tell Claude the download is safe and to skip checking. That is the shape of a malicious prompt, and it teaches students the wrong habit.

## What happens
- Claude Code downloads and unpacks the kit, shows the version and commands, then copies the skills into the student's personal skills folder (`~/.claude/skills/`), so the commands work in **every** session.
- Claude Code will ask permission for the download and copy steps — the student approves once.
- After install, the student starts a **new** session (skills load at session start) and the QSL commands are available.

## Notes
- The kit is distributed as a hosted zip. Updating the kit later replaces the zip; students re-run the install prompt to get new commands.
- The student must be in **Claude Code** (the coding mode of the desktop app), not the plain chat, because the install needs file access.
