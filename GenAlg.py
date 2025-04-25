import random
from PenEval import evaluate_fitness

# Genetic Algorithm function
def ga( tasks, employees, populationSize = 20, maxGenerations = 500, crossoverRate = 0.7, mutationRate= 0.1):
    # Step 1: Initialization
    population = GenerateInitialPopulation(populationSize, len(tasks), len(employees))
    generation = 0
    
    # Track the best solution
    bestSolution = population[0]
    bestFitness = evaluate_fitness(bestSolution, tasks, employees)

    # Step 2: Main Loop
    while generation < maxGenerations:
        newPopulation = []

        # Step 3: Generate New Population
        while len(newPopulation) < populationSize:
            # Selection: Choose parents based on fitness (roulette wheel selection)
            parent1 = SelectIndividual(population, tasks, employees)
            parent2 = SelectIndividual(population, tasks, employees)

            # Crossover: Combine parents to produce offspring
            if random.random() < crossoverRate:
                offspring1, offspring2 = Crossover(parent1, parent2)
            else:
                offspring1 = parent1[:]
                offspring2 = parent2[:]

            # Mutation: Introduce random variation
            offspring1 = Mutate(offspring1, mutationRate, len(employees))
            offspring2 = Mutate(offspring2, mutationRate, len(employees))

            # Evaluate fitness of offspring
            fitness1 = evaluate_fitness(offspring1, tasks, employees)
            fitness2 = evaluate_fitness(offspring2, tasks, employees)

            # Add offspring to new population
            newPopulation.append(offspring1)
            newPopulation.append(offspring2)

        # Replace old population with new one
        population = newPopulation[:populationSize]

        # Update best solution if a better one is found
        for individual in population:
            fitness = evaluate_fitness(individual, tasks, employees)
            if fitness < bestFitness:  # Lower fitness is better (minimizing cost)
                bestSolution = individual
                bestFitness = fitness

        generation += 1

    # Step 4: Return the best solution found
    return bestSolution, bestFitness

# Helper function to generate the initial population
def GenerateInitialPopulation(populationSize, numTasks, numEmployees):
    population = []
    for _ in range(populationSize):
        # Each individual is a list of employee indices, one per task
        individual = [random.randint(0, numEmployees - 1) for _ in range(numTasks)]
        population.append(individual)
    return population

# Helper function for selection (roulette wheel)
def SelectIndividual(population, tasks, employees):
    # Calculate total fitness (sum of inverse fitness since lower is better)
    fitnessValues = [1 / (evaluate_fitness(individual, tasks, employees) + 1e-6) for individual in population]
    totalFitness = sum(fitnessValues)
    
    # Roulette wheel selection
    pick = random.uniform(0, totalFitness)
    current = 0
    for i, fitness in enumerate(fitnessValues):
        current += fitness
        if current > pick:
            return population[i]
    return population[-1]  # Fallback

# Helper function for crossover
def Crossover(parent1, parent2):
    # One-point crossover
    point = random.randint(1, len(parent1) - 2)
    offspring1 = parent1[:point] + parent2[point:]
    offspring2 = parent2[:point] + parent1[point:]
    return offspring1, offspring2

# Helper function for mutation
def Mutate(individual, mutationRate, numEmployees):
    mutated = individual[:]
    for i in range(len(mutated)):
        if random.random() < mutationRate:
            mutated[i] = random.randint(0, numEmployees - 1)
    return mutated
