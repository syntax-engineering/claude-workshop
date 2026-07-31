# Due dates are date-only, not date-time

Tasks can have an optional Due Date, but it carries no time-of-day component (`date`, not `datetime`). We chose this over full date-time due dates to keep the CLI input format simple (`YYYY-MM-DD`) and to avoid timezone handling entirely, since a CLI todo list doesn't need hour-level precision on deadlines. If time-of-day due dates are needed later, this will require a migration of stored tasks and the `--due` input format.
