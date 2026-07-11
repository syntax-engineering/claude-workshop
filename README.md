# todo-cli

A small command-line todo list, used as the starter project for the
"building a feature with skills" workshop.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Verify it works

```bash
pytest
todo add "Buy milk"
todo list
```

If `pytest` passes and `todo list` shows your task, you're ready for the
workshop — no further setup needed.

## Usage

```bash
todo add "<description>"   # add a new task
todo list                  # list all tasks
todo complete <id>          # mark a task done
todo delete <id>            # remove a task
```

Tasks are stored in `todos.json` in the current directory.

## Working with Claude Code

This repo has a curated set of Claude Code skills installed under
`.claude/skills/`. See `CLAUDE.md` for the conventions Claude should follow
when writing code here.
