import json
from pathlib import Path

from todo_cli.models import Task

DEFAULT_STORE_PATH = Path("todos.json")


def load_tasks(path: Path = DEFAULT_STORE_PATH) -> list[Task]:
    if not path.exists():
        return []
    raw = json.loads(path.read_text())
    return [Task.from_dict(item) for item in raw]


def save_tasks(tasks: list[Task], path: Path = DEFAULT_STORE_PATH) -> None:
    path.write_text(json.dumps([task.to_dict() for task in tasks], indent=2))


def next_id(tasks: list[Task]) -> int:
    return max((task.id for task in tasks), default=0) + 1
