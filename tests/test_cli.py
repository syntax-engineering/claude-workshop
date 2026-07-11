from pathlib import Path

from todo_cli.cli import add_task, complete_task, delete_task, format_task
from todo_cli.models import Task
from todo_cli.storage import load_tasks


def test_add_task_persists(tmp_path: Path):
    path = tmp_path / "todos.json"
    task = add_task("Buy milk", path)
    assert load_tasks(path) == [task]


def test_complete_task_marks_done(tmp_path: Path):
    path = tmp_path / "todos.json"
    task = add_task("Buy milk", path)
    completed = complete_task(task.id, path)
    assert completed is not None
    assert completed.done is True


def test_complete_missing_task_returns_none(tmp_path: Path):
    path = tmp_path / "todos.json"
    add_task("Buy milk", path)
    assert complete_task(999, path) is None


def test_delete_task_removes_it(tmp_path: Path):
    path = tmp_path / "todos.json"
    task = add_task("Buy milk", path)
    assert delete_task(task.id, path) is True
    assert load_tasks(path) == []


def test_delete_missing_task_returns_false(tmp_path: Path):
    path = tmp_path / "todos.json"
    add_task("Buy milk", path)
    assert delete_task(999, path) is False


def test_format_task_shows_marker():
    assert format_task(Task(id=1, description="Buy milk")) == "[ ] 1: Buy milk"
    assert format_task(Task(id=2, description="Walk dog", done=True)) == "[x] 2: Walk dog"
