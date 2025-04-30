import random
import copy
from PenEval import evaluate_fitness

def aco(task_data, employee_data, num_ants=20, evaporation_rate=0.3, Q=100, max_iterations=200):
    num_tasks = len(task_data)
    num_employees = len(employee_data)

    # Initialise pheromone matrix with 1.0
    pheromones = [[1.0 for _ in range(num_employees)] for _ in range(num_tasks)]

    best_solution = None
    best_fitness = float('inf')

    fitnessHistory = []

    for iteration in range(max_iterations):
        all_solutions = []

        for ant in range(num_ants):
            solution = []
            for task_idx in range(num_tasks):
                pheromone_row = pheromones[task_idx]
                total_pheromone = sum(pheromone_row)
                probabilities = [p / total_pheromone for p in pheromone_row]
                chosen_employee = random.choices(range(num_employees), weights=probabilities, k=1)[0]
                solution.append(chosen_employee)

            fitness = evaluate_fitness(solution, task_data, employee_data)
            all_solutions.append((solution, fitness))

            if fitness < best_fitness:
                best_fitness = fitness
                best_solution = solution

        # Evaporation
        for i in range(num_tasks):
            for j in range(num_employees):
                pheromones[i][j] *= (1 - evaporation_rate)

        # Deposit
        for solution, fitness in all_solutions:
            for task_idx, emp_idx in enumerate(solution):
                pheromones[task_idx][emp_idx] += Q / (fitness + 1)  # add 1 to avoid division by 0

        fitnessHistory.append(best_fitness)
        print(f"Iteration {iteration + 1}, Best Fitness: {best_fitness}")
        if best_fitness == 0:
            break  # early stop if perfect solution found

    return best_solution, best_fitness, fitnessHistory
