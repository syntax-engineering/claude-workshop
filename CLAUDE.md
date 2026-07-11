# todo-cli

A small command-line todo list app. Plain Python, no framework — the point
of this repo is to be a low-stakes place to practice a build workflow, not
to showcase architecture.

## Conventions

- **Type hints are required** on every function's parameters and return
  value. Untyped code should be flagged in review.
- **`todo_cli/storage.py` and `todo_cli/models.py` must stay side-effect-free
  with respect to stdout** — no `print()` calls in those modules. All
  user-facing output belongs in `todo_cli/cli.py`.
- **Use `pathlib.Path`** for file paths, never `os.path`.
- **Functions over mutation** — prefer functions that take data in and
  return new data out (see `storage.py`'s `load_tasks`/`save_tasks`) over
  functions that mutate shared/global state.
- **Every new CLI subcommand needs a test** in `tests/test_cli.py`.

## Testing

- Tests use `pytest`. Run the full suite with `pytest` from the repo root.
- Anything touching the filesystem must use the `tmp_path` fixture — never
  read or write the real `todos.json` in a test.
- Tests should exercise the public functions in `todo_cli/cli.py` and
  `todo_cli/storage.py`, not reach into private state.

## Agent skills

### Issue tracker

Issues and specs live as local markdown files under `.scratch/`. See
`docs/agents/issue-tracker.md`.

### Domain docs

Single-context — `CONTEXT.md` + `docs/adr/` at the repo root, created
lazily. See `docs/agents/domain.md`.
