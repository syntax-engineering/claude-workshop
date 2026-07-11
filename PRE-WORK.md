# Pre-work: Building a Feature With Skills

You'll need about 15 minutes to do this before the session. Please do it
ahead of time — we won't have time to debug local setup issues live.

## 1. Confirm Claude Code access

You should already have a Claude Code seat on our Team plan. Confirm you can
run:

```bash
claude --version
```

If that fails, see [Claude Code's install docs](https://docs.claude.com/en/docs/claude-code)
or ask in `#<workshop-channel>` before the session.

## 2. Clone the starter repo

```bash
git clone <starter-repo-url> todo-cli
cd todo-cli
```

## 3. Set up and verify the app runs

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
todo add "Buy milk"
todo list
```

You're ready if `pytest` passes and `todo list` prints back "Buy milk".

## If local setup doesn't work

Two fallback options — pick whichever is easier for you, no need to debug
further on your own machine:

- **GitHub Codespaces** — open the repo on GitHub and use "Code → Create
  codespace on main". The devcontainer installs everything (Python, deps,
  Claude Code) automatically.
- **Claude Code on the web** — go to [claude.ai/code](https://claude.ai/code),
  connect your GitHub account if you haven't already, and open the starter
  repo from there. No local install needed at all.

## Optional, for engineers

If you want to explore beyond what we cover in the session, you can install
the full [mattpocock/skills](https://github.com/mattpocock/skills) suite —
we're only using a curated subset (already included in the starter repo)
for the workshop itself, so this is just for people who want to keep
exploring afterward.

## What to expect

We'll build a small feature on this todo app together, live, using a
handful of Claude Code skills that walk through interviewing out the
requirements, writing a spec, and implementing test-first. No prior
experience with any of this is assumed — bring the todo app running and
we'll do the rest together.
