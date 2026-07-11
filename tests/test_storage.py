from pathlib import Path

from todo_cli.models import Task
from todo_cli.storage import load_tasks, next_id, save_tasks


def test_load_tasks_missing_file_returns_empty(tmp_path: Path):
    assert load_tasks(tmp_path / "missing.json") == []


def test_save_and_load_round_trip(tmp_path: Path):
    path = tmp_path / "todos.json"
    tasks = [Task(id=1, description="Buy milk")]
    save_tasks(tasks, path)
    assert load_tasks(path) == tasks


def test_next_id_empty_list():
    assert next_id([]) == 1


def test_next_id_increments_from_max():
    tasks = [Task(id=1, description="a"), Task(id=5, description="b")]
    assert next_id(tasks) == 6
