import random
import csv
import copy
from PenEval import evaluate_fitness




# PSO function aligned with pseudocode
def pso(task_data, employee_data, num_particles=30, max_iterations=500):
    # Parameters
    n = len(task_data)  # Number of dimensions (tasks)
    N = num_particles  # Number of particles
    T_max = max_iterations  # Maximum iterations
    w = 0.5  # Inertia weight
    c1 = 1.5  # Cognitive coefficient
    c2 = 1.5  # Social coefficient
    x_min = 0  # Minimum employee index
    x_max = len(employee_data) - 1  # Maximum employee index

    # Step 1: Initialization
    x = []  # Particle positions: x[i][d]
    v = []  # Particle velocities: v[i][d]
    pBest = []  # Personal best positions
    fitness_pBest = []  # Personal best fitness values

    for i in range(N):
        position = [random.randint(x_min, x_max) for _ in range(n)]
        velocity = [random.uniform(-4, 4) for _ in range(n)]  # Velocity range as per Eight Queens
        x.append(position)
        v.append(velocity)
        pBest.append(position[:])
        fitness_pBest.append(evaluate_fitness(position, task_data, employee_data))

    # Initialize global best
    k = min(range(N), key=lambda i: fitness_pBest[i])
    gBest = pBest[k][:]
    fitness_gBest = fitness_pBest[k]

    # Log fitness for CSV
    fitness_log = []

    # Step 2: Main optimization loop
    for t in range(T_max):
        for i in range(N):
            for d in range(n):
                r1 = random.random()
                r2 = random.random()
                # Velocity update
                v[i][d] = w * v[i][d] + c1 * r1 * (pBest[i][d] - x[i][d]) + c2 * r2 * (gBest[d] - x[i][d])
                # Position update
                x[i][d] = round(x[i][d] + v[i][d])
                # Boundary handling
                x[i][d] = x[i][d] % (x_max + 1)
                if x[i][d] < x_min:
                    x[i][d] += (x_max + 1)

            # Evaluate fitness
            fitness_current = evaluate_fitness(x[i], task_data, employee_data)

            # Update personal best
            if fitness_current < fitness_pBest[i]:
                pBest[i] = x[i][:]
                fitness_pBest[i] = fitness_current

        # Update global best
        for i in range(N):
            if fitness_pBest[i] < fitness_gBest:
                gBest = pBest[i][:]
                fitness_gBest = fitness_pBest[i]

        # Log fitness
        fitness_log.append((t + 1, fitness_gBest))

    # Write to CSV
    with open('pso_fitness.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Iteration', 'Fitness'])
        for iteration, fitness in fitness_log:
            writer.writerow([iteration, fitness])

    return gBest, fitness_gBest, fitness_log