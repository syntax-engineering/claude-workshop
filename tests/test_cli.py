from datetime import date
from pathlib import Path

from todo_cli.cli import (
    add_task,
    complete_task,
    delete_task,
    format_task,
    set_due_date,
    sorted_by_due_date,
)
from todo_cli.models import Task
from todo_cli.storage import load_tasks


def test_add_task_persists(tmp_path: Path):
    path = tmp_path / "todos.json"
    task = add_task("Buy milk", path)
    assert load_tasks(path) == [task]


def test_add_task_with_due_date_persists(tmp_path: Path):
    path = tmp_path / "todos.json"
    task = add_task("Buy milk", path, due_date=date(2026, 8, 15))
    assert task.due_date == date(2026, 8, 15)
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


def test_format_task_shows_due_date():
    task = Task(id=1, description="Buy milk", due_date=date(2026, 8, 15))
    assert format_task(task, today=date(2026, 8, 1)) == "[ ] 1: Buy milk (due 2026-08-15)"


def test_format_task_flags_overdue_when_not_done():
    task = Task(id=1, description="Buy milk", due_date=date(2026, 8, 1))
    assert format_task(task, today=date(2026, 8, 15)) == "[ ] 1: Buy milk (due 2026-08-01, OVERDUE)"


def test_format_task_does_not_flag_overdue_when_done():
    task = Task(id=1, description="Buy milk", done=True, due_date=date(2026, 8, 1))
    assert format_task(task, today=date(2026, 8, 15)) == "[x] 1: Buy milk (due 2026-08-01)"


def test_set_due_date_updates_task(tmp_path: Path):
    path = tmp_path / "todos.json"
    task = add_task("Buy milk", path)
    updated = set_due_date(task.id, date(2026, 8, 15), path)
    assert updated is not None
    assert updated.due_date == date(2026, 8, 15)
    assert load_tasks(path) == [updated]


def test_set_due_date_can_clear(tmp_path: Path):
    path = tmp_path / "todos.json"
    task = add_task("Buy milk", path, due_date=date(2026, 8, 15))
    cleared = set_due_date(task.id, None, path)
    assert cleared is not None
    assert cleared.due_date is None


def test_set_due_date_missing_task_returns_none(tmp_path: Path):
    path = tmp_path / "todos.json"
    add_task("Buy milk", path)
    assert set_due_date(999, date(2026, 8, 15), path) is None


def test_sorted_by_due_date_orders_earliest_first():
    later = Task(id=1, description="later", due_date=date(2026, 8, 20))
    earlier = Task(id=2, description="earlier", due_date=date(2026, 8, 10))
    no_due = Task(id=3, description="no due")
    assert sorted_by_due_date([later, earlier, no_due]) == [earlier, later, no_due]


def test_sorted_by_due_date_ties_break_by_id():
    second = Task(id=2, description="b", due_date=date(2026, 8, 10))
    first = Task(id=1, description="a", due_date=date(2026, 8, 10))
    assert sorted_by_due_date([second, first]) == [first, second]
