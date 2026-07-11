from dataclasses import asdict, dataclass


@dataclass
class Task:
    id: int
    description: str
    done: bool = False

    def to_dict(self) -> dict:
        return asdict(self)

    @staticmethod
    def from_dict(data: dict) -> "Task":
        return Task(
            id=data["id"],
            description=data["description"],
            done=data.get("done", False),
        )
