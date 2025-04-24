from PSO import pso
from GenAlg import ga
from ACO import aco

# Task data: ID, Time, Difficulty, Deadline, Skill
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

# Employee data: ID, Available hours, Skill level, Skills
employees = [
    {"id": "E1", "hours": 10, "level": 4, "skills": ["A", "C"]},
    {"id": "E2", "hours": 12, "level": 6, "skills": ["A", "B", "C"]},
    {"id": "E3", "hours": 8, "level": 3, "skills": ["A"]},
    {"id": "E4", "hours": 15, "level": 7, "skills": ["B", "C"]},
    {"id": "E5", "hours": 9, "level": 5, "skills": ["A", "C"]},
]

def menu():
    while True:
        print("\n--- Task Assignment Optimiser ---")
        print("1. Run PSO")
        print("2. Run GA")
        print("3. Run ACO")
        print("4. Exit")
        choice = input("Choose an algorithm to run: ")

        if choice == "1":
            print("\n[PSO Placeholder] Running PSO...")
            position, fitness = pso(tasks, employees)
            print("Assignment:", position)
            print("Fitness Score:", fitness)

        elif choice == "2":
            print("\n[GA Placeholder] Running Genetic Algorithm...")
            position, fitness = ga(tasks, employees)
            print("Assignment:", position)
            print("Fitness Score:", fitness)

        elif choice == "3":
            print("\n[ACO Placeholder] Running Ant Colony Optimisation...")
            #position, fitness = aco(task_data, employee_data)
            print("Assignment:", position)
            print("Fitness Score:", fitness)

        elif choice == "4":
            print("Exiting test harness.")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()
