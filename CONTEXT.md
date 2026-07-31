# todo-cli

A small command-line todo list app, used as a low-stakes place to practice a
build workflow.

## Language

**Due date**:
The date by which a task is expected to be completed. Optional per task;
stored as a date with no time component (`YYYY-MM-DD`).
_Avoid_: Deadline, due time

**Overdue**:
A task whose due date is strictly before today and which is not yet done.
Completing a task always clears its overdue status, regardless of when it
was completed.
_Avoid_: Late, past due
