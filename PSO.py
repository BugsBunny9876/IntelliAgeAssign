from PenEval import evaluate_fitness
import random

def pso(task_data, employee_data, num_particles=30, max_iterations=500):
    # Initialize particles
    particles = []
    for _ in range(num_particles):
        position = [random.choice(range(len(employee_data))) for _ in range(len(task_data))]  # One employee per task
        velocity = [random.uniform(-1, 1) for _ in range(len(task_data))]  # Real-valued velocity vector
        particles.append({
            "position": position,
            "velocity": velocity,
            "pbest_position": position[:],
            "pbest_fitness": evaluate_fitness(position, task_data, employee_data)
        })

    # Initialize global best
    gbest_position = min(particles, key=lambda p: p["pbest_fitness"])["pbest_position"][:]
    gbest_fitness = evaluate_fitness(gbest_position, task_data, employee_data)

    # PSO Parameters
    w = 0.5   # inertia
    c1 = 1.5  # cognitive
    c2 = 1.5  # social

    for iteration in range(max_iterations):
        for p in particles:
            new_velocity = []
            new_position = []

            for i in range(len(p["position"])):
                r1, r2 = random.random(), random.random()
                inertia = w * p["velocity"][i]
                cognitive = c1 * r1 * (p["pbest_position"][i] - p["position"][i])
                social = c2 * r2 * (gbest_position[i] - p["position"][i])

                # Velocity update
                v_new = inertia + cognitive + social
                new_velocity.append(v_new)

                # Position update: round and clip to valid employee indices
                pos_new = int(round(p["position"][i] + v_new)) % len(employee_data)
                new_position.append(pos_new)

            p["velocity"] = new_velocity
            p["position"] = new_position

            # Fitness evaluation
            fitness = evaluate_fitness(new_position, task_data, employee_data)

            # Update personal best
            if fitness < p["pbest_fitness"]:
                p["pbest_position"] = new_position[:]
                p["pbest_fitness"] = fitness

            # Update global best
            if fitness < gbest_fitness:
                gbest_position = new_position[:]
                gbest_fitness = fitness

        print(f"Iteration {iteration}: Best Fitness = {gbest_fitness}")
        if gbest_fitness == 0:
            break  # Perfect solution found

    return gbest_position, gbest_fitness
