# Pre-work: Building a Feature With Skills

You'll need about 15 minutes to do this before the session. Please do it
ahead of time — we won't have time to debug local setup issues live.

Pick **one** of the three setups below — whichever fits how you like to
work. All three end up in the same place: the `todo-cli` starter repo open
and ready to go. If you get stuck on any of them, ask in
`#claude-discussion` before the session.

## Option A: Claude Code on the web (recommended if you don't code day-to-day)

No install required — this runs entirely in your browser.

1. Go to [claude.ai/code](https://claude.ai/code) and sign in with your Team
   account.
2. Connect your GitHub account if you haven't already.
3. Open the starter repo (`https://github.com/syntax-engineering/claude-workshop`) from there.
4. Once it's open, just ask Claude in the chat: "Set up this project and run
   the tests." It'll create the virtual environment, install dependencies,
   and run `pytest` for you.
5. Confirm it works by asking Claude to run `todo add "Buy milk"` and
   `todo list` — you're ready if it prints back "Buy milk".

## Option B: Claude Code for Desktop

A native app for Mac or Windows — still no terminal commands to type
yourself.

1. Download the [desktop app](https://claude.ai/download) and sign in with
   your Team account.
2. Choose "Clone Repository" and point it at the starter repo URL
   (`https://github.com/syntax-engineering/claude-workshop`).
3. Once it's open, ask Claude in the chat: "Set up this project and run the
   tests." It'll create the virtual environment, install dependencies, and
   run `pytest` for you.
4. Confirm it works by asking Claude to run `todo add "Buy milk"` and
   `todo list` — you're ready if it prints back "Buy milk".

## Option C: Claude Code CLI (if you're comfortable in a terminal)

1. Install Claude Code, if you don't already have it:

   **macOS:**

   ```bash
   curl -fsSL https://claude.ai/install.sh | bash
   ```

   Or, if you use Homebrew:

   ```bash
   brew install --cask claude-code@latest
   ```

   **Windows (PowerShell):**

   ```powershell
   irm https://claude.ai/install.ps1 | iex
   ```

   Then confirm it's installed:

   ```bash
   claude --version
   ```

   If that fails, see [Claude Code's install docs](https://docs.claude.com/en/docs/claude-code).

2. Clone the starter repo:

   ```bash
   git clone https://github.com/syntax-engineering/claude-workshop todo-cli
   cd todo-cli
   ```

3. Set up and verify the app runs:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -e ".[dev]"
   pytest
   todo add "Buy milk"
   todo list
   ```

   You're ready if `pytest` passes and `todo list` prints back "Buy milk".

## If none of these work

- **GitHub Codespaces** — open the repo on GitHub and use "Code → Create
  codespace on main". The devcontainer installs everything (Python, deps,
  Claude Code) automatically.

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
