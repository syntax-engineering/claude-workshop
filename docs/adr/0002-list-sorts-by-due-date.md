# `list` sorts by due date instead of insertion order

`todo list` sorts tasks by Due Date ascending, with tasks that have no due date placed last (ties broken by id, matching the prior insertion order). We chose this over preserving plain insertion/id order so the most urgent tasks surface at the top by default, without requiring a separate `--sort` flag. The trade-off is that this changes default output order for every user, including those with no due dates set on any task.
