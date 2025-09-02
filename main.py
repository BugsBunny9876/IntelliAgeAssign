from PSO import pso
from GenAlg import ga
from ACO import aco
from PenEval import evaluate_fitness
import matplotlib.pyplot as plt

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
            position, fitness = aco(tasks, employees)
            print("Assignment:", position)
            print("Fitness Score:", fitness)

        elif choice == "4":
            print("Exiting test harness.")
            break

        else:
            print("Invalid option. Try again.")

def run_and_plot_algorithms(tasks, employees, num_runs=5):
    ga_histories, pso_histories, aco_histories = [], [], []
    ga_final_fitness, pso_final_fitness, aco_final_fitness = [], [], []

    for run in range(num_runs):
        print(f"\nRun {run + 1}:")
        _, ga_fitness, ga_history = ga(tasks, employees)
        ga_histories.append(ga_history)
        ga_final_fitness.append(ga_fitness)
        print(f"GA Final Fitness = {ga_fitness}")

        _, pso_fitness, pso_history = pso(tasks, employees)
        pso_histories.append(pso_history)
        pso_final_fitness.append(pso_fitness)
        print(f"PSO Final Fitness = {pso_fitness}")

        _, aco_fitness, aco_history = aco(tasks, employees)
        aco_histories.append(aco_history)
        aco_final_fitness.append(aco_fitness)
        print(f"ACO Final Fitness = {aco_fitness}")

    # Plotting GA
    plt.figure(figsize=(12, 8))
    max_ga_len = max(len(h) for h in ga_histories)
    generations_ga = range(max_ga_len)
    for i, history in enumerate(ga_histories):
        plt.plot(range(len(history)), history, label=f'GA Run {i+1}', alpha=0.3, color='blue')
    avg_ga = [sum(h[i] for h in ga_histories if i < len(h)) / sum(1 for h in ga_histories if i < len(h)) for i in range(max_ga_len)]
    plt.plot(generations_ga, avg_ga, label='GA Average', color='blue', linewidth=2)
    plt.xlabel('Generations')
    plt.ylabel('Objective Function Value (Total Penalty)')
    plt.title('Convergence of Genetic Algorithm (GA)')
    plt.legend()
    plt.grid(True)
    plt.savefig('ga_convergence.png')
    plt.close()

    # Plotting PSO
    plt.figure(figsize=(12, 8))
    max_pso_len = max(len(h) for h in pso_histories)
    generations_pso = range(max_pso_len)
    for i, history in enumerate(pso_histories):
        plt.plot(range(len(history)), history, label=f'PSO Run {i+1}', alpha=0.3, color='green')
    avg_pso = [sum(h[i] for h in pso_histories if i < len(h)) / sum(1 for h in pso_histories if i < len(h)) for i in range(max_pso_len)]
    plt.plot(generations_pso, avg_pso, label='PSO Average', color='green', linewidth=2)
    plt.xlabel('Iterations')
    plt.ylabel('Objective Function Value (Total Penalty)')
    plt.title('Convergence of Particle Swarm Optimization (PSO)')
    plt.legend()
    plt.grid(True)
    plt.savefig('pso_convergence.png')
    plt.close()

    # Plotting ACO
    plt.figure(figsize=(12, 8))
    max_aco_len = max(len(h) for h in aco_histories)
    generations_aco = range(max_aco_len)
    for i, history in enumerate(aco_histories):
        plt.plot(range(len(history)), history, label=f'ACO Run {i+1}', alpha=0.3, color='red')
    avg_aco = [sum(h[i] for h in aco_histories if i < len(h)) / sum(1 for h in aco_histories if i < len(h)) for i in range(max_aco_len)]
    plt.plot(generations_aco, avg_aco, label='ACO Average', color='red', linewidth=2)
    plt.xlabel('Iterations')
    plt.ylabel('Objective Function Value (Total Penalty)')
    plt.title('Convergence of Ant Colony Optimization (ACO)')
    plt.legend()
    plt.grid(True)
    plt.savefig('aco_convergence.png')
    plt.close()

    return ga_final_fitness, pso_final_fitness, aco_final_fitness

if __name__ == "__main__":
    ga_fitness, pso_fitness, aco_fitness = run_and_plot_algorithms(tasks, employees, num_runs=5)
    menu()
