from datetime import date

from todo_cli.models import Task


def test_to_dict_round_trip():
    task = Task(id=1, description="Buy milk")
    assert Task.from_dict(task.to_dict()) == task


def test_default_done_is_false():
    task = Task(id=1, description="Buy milk")
    assert task.done is False


def test_default_due_date_is_none():
    task = Task(id=1, description="Buy milk")
    assert task.due_date is None


def test_to_dict_round_trip_with_due_date():
    task = Task(id=1, description="Buy milk", due_date=date(2026, 8, 15))
    assert Task.from_dict(task.to_dict()) == task
    assert task.to_dict()["due_date"] == "2026-08-15"
