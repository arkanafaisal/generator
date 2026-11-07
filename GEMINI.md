# Self-Correcting Rules Engine

This file contains a growing ruleset that improves over time. At session start, read the entire "Learned Rules" section before doing anything.

## How it works

- I for Command, L for Agent
1. When the user corrects you or you make a mistake, immediately append a new rule to the "Learned Rules" section at the bottom of this file.
2. Rules are numbered sequentially and written as clear, imperative instructions.
3. Format: `N. [CATEGORY] Never/Always do X because Y.`
4. Categories: `[STYLE]`, `[CODE]`, `[ARCH]`, `[TOOL]`, `[PROCESS]`, `[DATA]`, `[UX]`, `[OTHER]`
5. Before starting any task, scan all rules below for relevant constraints.
6. If two rules conflict, the higher-numbered (newer) rule wins.
7. Never delete rules. If a rule becomes obsolete, append a new rule that supersedes it.

## When to add a rule

- User explicitly corrects your output ("no, do it this way")
- User rejects a file, approach, or pattern
- You hit a bug caused by a wrong assumption about this codebase
- User states a preference ("always use X", "never do Y")

## Learned Rules

1. [PROCESS] Never record one-time architectural setup steps or specific tech-stack details in Learned Rules; always limit rules to enduring coding styles, workflow practices, and developer preferences (superseding rules 2 and 3) because technical architecture must be inferred directly from the active codebase.

2. [ARCH] Always preserve the exact modular directory structure (such as utils/) and keep ported files line-for-line aligned with original code because minimizing comparison/diff discrepancies and facilitating direct side-by-side verification is essential.

3. [PROCESS] Never write changes on a commands that starts with "btw".

4. [PROCESS] Always document each Git commit in changelog.md with its short commit ID, structural context, and key code diff explanations (what was removed/changed/added and why) immediately upon committing because commit messages alone lack diff context.

5. [PROCESS] Always stage and commit changelog.md documentation together in the same atomic commit as the corresponding code changes (superseding rule 13's separate post-commit step) and never separate changelog updates into their own standalone commit because feature changes and their documentation must remain unified per feature.

6. [PROCESS] Never perform post-commit re-checking or separate commits just to update short commit IDs in changelog.md; always record the commit as [Unreleased] or update previous commit IDs lazily in subsequent feature commits (superseding rules 13 and 15 regarding immediate commit ID resolution) because checking git status and amending or updating commit IDs in the same turn wastes valuable development time.

7. [PROCESS] Never create or maintain README.md files unless explicitly requested because project documentation is already tracked in changelog.md and maintaining redundant documentation adds unnecessary overhead.
