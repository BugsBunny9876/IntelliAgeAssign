def evaluate_fitness(position, task_data, employee_data,
                     alpha=0.2, beta=0.2, delta=0.2, gamma=0.2, sigma=0.2):
    # Track penalties
    overload_penalty = 0
    skill_mismatch_penalty = 0
    difficulty_violation_penalty = 0
    deadline_violation_penalty = 0
    unique_assignment_penalty = 0

    # Task assignment check
    task_counts = [0] * len(task_data)
    employee_workload = [0] * len(employee_data)
    employee_tasks = [[] for _ in range(len(employee_data))]

    for task_idx, emp_idx in enumerate(position):
        task_counts[task_idx] += 1
        task = task_data[task_idx]
        emp = employee_data[emp_idx]

        employee_workload[emp_idx] += task["time"]
        employee_tasks[emp_idx].append((task_idx, task))

        # Skill match
        if task["skill"] not in emp["skills"]:
            skill_mismatch_penalty += 1

        # Difficulty check
        if emp["level"] < task["difficulty"]:
            difficulty_violation_penalty += 1

    # Unique assignment penalty
    for count in task_counts:
        if count != 1:
            unique_assignment_penalty += abs(1 - count)  # Penalize if not assigned exactly once

    # Overload check
    for emp_idx, total_hours in enumerate(employee_workload):
        if total_hours > employee_data[emp_idx]["hours"]:
            overload_penalty += total_hours - employee_data[emp_idx]["hours"]

    # Deadline violation
    for emp_idx, tasks in enumerate(employee_tasks):
        sorted_tasks = sorted(tasks, key=lambda t: t[1]["time"])  # sort by task time
        finish_time = 0
        for task_idx, task in sorted_tasks:
            finish_time += task["time"]
            if finish_time > task["deadline"]:
                deadline_violation_penalty += finish_time - task["deadline"]

    # Compute total fitness as weighted sum of penalties
    fitness = (alpha * overload_penalty +
               beta * skill_mismatch_penalty +
               delta * difficulty_violation_penalty +
               gamma * deadline_violation_penalty +
               sigma * unique_assignment_penalty)

    return fitness
