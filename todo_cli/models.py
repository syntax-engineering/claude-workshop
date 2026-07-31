from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    id: int
    description: str
    done: bool = False
    due_date: date | None = None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "description": self.description,
            "done": self.done,
            "due_date": self.due_date.isoformat() if self.due_date is not None else None,
        }

    @staticmethod
    def from_dict(data: dict) -> "Task":
        due_date_raw = data.get("due_date")
        return Task(
            id=data["id"],
            description=data["description"],
            done=data.get("done", False),
            due_date=date.fromisoformat(due_date_raw) if due_date_raw is not None else None,
        )
