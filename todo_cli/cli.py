import argparse
from datetime import date

from todo_cli.models import Task
from todo_cli.storage import DEFAULT_STORE_PATH, load_tasks, next_id, save_tasks
from pathlib import Path


def add_task(
    description: str, path: Path = DEFAULT_STORE_PATH, *, due_date: date | None = None
) -> Task:
    tasks = load_tasks(path)
    task = Task(id=next_id(tasks), description=description, due_date=due_date)
    tasks.append(task)
    save_tasks(tasks, path)
    return task


def complete_task(task_id: int, path: Path = DEFAULT_STORE_PATH) -> Task | None:
    tasks = load_tasks(path)
    for task in tasks:
        if task.id == task_id:
            task.done = True
            save_tasks(tasks, path)
            return task
    return None


def delete_task(task_id: int, path: Path = DEFAULT_STORE_PATH) -> bool:
    tasks = load_tasks(path)
    remaining = [task for task in tasks if task.id != task_id]
    if len(remaining) == len(tasks):
        return False
    save_tasks(remaining, path)
    return True


def set_due_date(
    task_id: int, due_date: date | None, path: Path = DEFAULT_STORE_PATH
) -> Task | None:
    tasks = load_tasks(path)
    for task in tasks:
        if task.id == task_id:
            task.due_date = due_date
            save_tasks(tasks, path)
            return task
    return None


def sorted_by_due_date(tasks: list[Task]) -> list[Task]:
    return sorted(tasks, key=lambda task: (task.due_date is None, task.due_date or date.max, task.id))


def format_task(task: Task, *, today: date | None = None) -> str:
    marker = "x" if task.done else " "
    line = f"[{marker}] {task.id}: {task.description}"
    if task.due_date is not None:
        line += f" (due {task.due_date.isoformat()}"
        if not task.done and task.due_date < (today if today is not None else date.today()):
            line += ", OVERDUE"
        line += ")"
    return line


def parse_date(value: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            f"invalid date {value!r}, expected YYYY-MM-DD"
        ) from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="todo", description="A simple todo list CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Task description")
    add_parser.add_argument("--due", type=parse_date, default=None, help="Due date (YYYY-MM-DD)")

    subparsers.add_parser("list", help="List all tasks")

    complete_parser = subparsers.add_parser("complete", help="Mark a task complete")
    complete_parser.add_argument("id", type=int, help="Task id")

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task id")

    due_parser = subparsers.add_parser("due", help="Set or clear a task's due date")
    due_parser.add_argument("id", type=int, help="Task id")
    due_group = due_parser.add_mutually_exclusive_group(required=True)
    due_group.add_argument("date", type=parse_date, nargs="?", help="New due date (YYYY-MM-DD)")
    due_group.add_argument("--clear", action="store_true", help="Remove the due date")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "add":
        task = add_task(args.description, due_date=args.due)
        print(f"Added: {format_task(task)}")
    elif args.command == "list":
        tasks = sorted_by_due_date(load_tasks())
        if not tasks:
            print("No tasks yet.")
        for task in tasks:
            print(format_task(task))
    elif args.command == "complete":
        task = complete_task(args.id)
        if task is None:
            print(f"No task with id {args.id}")
            return 1
        print(f"Completed: {format_task(task)}")
    elif args.command == "delete":
        deleted = delete_task(args.id)
        if not deleted:
            print(f"No task with id {args.id}")
            return 1
        print(f"Deleted task {args.id}")
    elif args.command == "due":
        due_date = None if args.clear else args.date
        task = set_due_date(args.id, due_date)
        if task is None:
            print(f"No task with id {args.id}")
            return 1
        if args.clear:
            print(f"Cleared due date for task {args.id}")
        else:
            print(f"Set due date for task {args.id} to {task.due_date.isoformat()}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
