from todo_cli.models import Task


def test_to_dict_round_trip():
    task = Task(id=1, description="Buy milk")
    assert Task.from_dict(task.to_dict()) == task


def test_default_done_is_false():
    task = Task(id=1, description="Buy milk")
    assert task.done is False
