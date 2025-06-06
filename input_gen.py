import numpy as np
import csv
from ACO import aco
from PenEval import evaluate_fitness

# Task data
tasks = [
    {"id": "T1", "time": 4, "difficulty": 3, "deadline": 8, "skill": "A"},
    {"id": "T2", "time": 6, "difficulty": 5, "deadline": 12, "skill": "B"},
    {"id": "T3", "time": 2, "difficulty": 2, "deadline": 6, "skill": "A"},
    {"id": "T4", "time": 5, "difficulty": 4, "deadline": 10, "skill": "C"},
    {"id": "T5", "time": 3, "difficulty": 1, "deadline": 7, "skill": "A"},
    {"id": "T6", "time": 8, "difficulty": 6, "deadline": 15, "skill": "B"},
    {"id": "T7", "time": 4, "difficulty": 3, "deadline": 9, "skill": "C"},
    {"id": "T8", "time": 7, "difficulty": 5, "deadline": 14, "skill": "B"},
    {"id": "T9", "time": 2, "difficulty": 2, "deadline": 5, "skill": "A"},
    {"id": "T10", "time": 6, "difficulty": 4, "deadline": 11, "skill": "C"},
]

# Employee data
employees = [
    {"id": "E1", "hours": 10, "level": 4, "skills": ["A", "C"]},
    {"id": "E2", "hours": 12, "level": 6, "skills": ["A", "B", "C"]},
    {"id": "E3", "hours": 8, "level": 3, "skills": ["A"]},
    {"id": "E4", "hours": 15, "level": 7, "skills": ["B", "C"]},
    {"id": "E5", "hours": 9, "level": 5, "skills": ["A", "C"]},
]

# Encoding helpers
def one_hot_skill(skill):
    return [int(skill == 'A'), int(skill == 'B'), int(skill == 'C')]

def one_hot_skill_set(skills):
    return [int('A' in skills), int('B' in skills), int('C' in skills)]

def construct_pair_vector(task, employee):
    return [
        task['time'], task['difficulty'], task['deadline'],
        *one_hot_skill(task['skill']),
        employee['hours'], employee['level'],
        *one_hot_skill_set(employee['skills'])
    ]

def construct_input_vector(position, tasks, employees):
    input_vec = []
    for task_idx, emp_idx in enumerate(position):
        input_vec += construct_pair_vector(tasks[task_idx], employees[emp_idx])
    return input_vec

# Dataset generation
X_data = []
y_data = []
seen = set()

while len(X_data) < 100:
    position, fitness, _ = aco(tasks, employees)
    key = tuple(position)
    if key in seen:
        continue
    seen.add(key)

    x_vec = construct_input_vector(position, tasks, employees)
    X_data.append(x_vec)
    y_data.append(fitness)

# Save to CSV using only built-in libraries
with open("mapping_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([f"F{i}" for i in range(110)] + ["Penalty"])
    for x, y in zip(X_data, y_data):
        writer.writerow(x + [y])

print("Saved 100 mappings to mapping_data.csv")
