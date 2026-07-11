import argparse

from todo_cli.models import Task
from todo_cli.storage import DEFAULT_STORE_PATH, load_tasks, next_id, save_tasks
from pathlib import Path


def add_task(description: str, path: Path = DEFAULT_STORE_PATH) -> Task:
    tasks = load_tasks(path)
    task = Task(id=next_id(tasks), description=description)
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


def format_task(task: Task) -> str:
    marker = "x" if task.done else " "
    return f"[{marker}] {task.id}: {task.description}"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="todo", description="A simple todo list CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Task description")

    subparsers.add_parser("list", help="List all tasks")

    complete_parser = subparsers.add_parser("complete", help="Mark a task complete")
    complete_parser.add_argument("id", type=int, help="Task id")

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task id")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "add":
        task = add_task(args.description)
        print(f"Added: {format_task(task)}")
    elif args.command == "list":
        tasks = load_tasks()
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

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
