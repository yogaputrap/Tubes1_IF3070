from diagonalMagicCube import DiagonalMagicCube
import random

class GeneticAlgorithm:
    def __init__(self, cube):
        self.cube = cube

    def run(self, population_size=50, generations=100, record=None):
        # Initialize population with DiagonalMagicCube objects
        population = [DiagonalMagicCube(self.cube.size) for _ in range(population_size)]

        # Initialize variables for tracking
        max_objective_values = []
        avg_objective_values = []
        initial_state = [row[:] for row in self.cube.cube]  # Track the initial state

        for generation in range(generations):
            population.sort(key=lambda cube: self.evaluate(cube))
            next_generation = population[:population_size // 2]  # Select top half

            # Record the maximum and average objective function values for the generation
            max_objective_values.append(self.evaluate(population[0]))
            avg_objective_values.append(sum(self.evaluate(cube) for cube in population) / population_size)

            # Record the objective function value at the start of this generation
            if record is not None:
                record.append(self.evaluate(population[0]))

            # Crossover and mutation to create new population
            while len(next_generation) < population_size:
                parent1 = random.choice(population)
                parent2 = random.choice(population)
                child = self.crossover(parent1, parent2)
                self.mutate(child)
                next_generation.append(child)

            population = next_generation

        # Final state and objective function
        final_state = [row[:] for row in self.cube.cube]
        final_objective_value = self.evaluate(population[0])

        return {
            "initial_state": initial_state,
            "final_state": final_state,
            "final_objective_value": final_objective_value,
            "max_objective_values": max_objective_values,
            "avg_objective_values": avg_objective_values,
            "population_size": population_size,
            "generations": generations
        }

    def evaluate(self, cube):
        # Evaluate the fitness of a cube by its objective function
        return cube.objective_function()

    def crossover(self, parent1, parent2):
        """Perform a crossover between two parents to produce a child."""
        child = DiagonalMagicCube(self.cube.size)

        # Randomly determine a split index for each dimension (x, y, z)
        x_split = random.randint(0, self.cube.size - 1)
        y_split = random.randint(0, self.cube.size - 1)
        z_split = random.randint(0, self.cube.size - 1)

        # Copy parts of parent1 and parent2 into the child cube
        for x in range(self.cube.size):
            for y in range(self.cube.size):
                for z in range(self.cube.size):
                    if x < x_split and y < y_split and z < z_split:
                        child.cube[x][y][z] = parent1.cube[x][y][z]
                    else:
                        child.cube[x][y][z] = parent2.cube[x][y][z]

        return child

    def mutate(self, cube, mutation_rate=0.01):
        """Perform a mutation on the cube by swapping two random numbers."""
        if random.random() < mutation_rate:
            pos1 = self.random_position()
            pos2 = self.random_position()
            cube.swap_numbers(pos1, pos2)

    def random_position(self):
        """Generates a random position in the cube for swapping."""
        return (
            random.randint(0, self.cube.size - 1),
            random.randint(0, self.cube.size - 1),
            random.randint(0, self.cube.size - 1)
        )
    