import random
import math

class SimulatedAnnealing:
    def __init__(self, cube):
        self.cube = cube

    def anneal(self, initial_temperature=1000, cooling_rate=0.95, max_iterations=1000, record=None):
        temperature = initial_temperature
        current_score = self.cube.objective_function()

        stuck_counter = 0  # Counter for 'stuck' frequency
        stuck_threshold = 50  # Number of iterations before considering the algorithm stuck
        stuck_frequency = 0  # Track how often we get stuck

        e_values = []  # To track the values of e^(deltaE/T)
        stuck_frequencies = []  # To track stuck frequencies

        for iteration in range(max_iterations):
            if temperature < 1e-3:  # Avoid temperatures too close to zero
                break

            if record is not None:
                record.append(current_score)

            pos1 = self.random_position()
            pos2 = self.random_position()
            self.cube.swap_numbers(pos1, pos2)
            neighbor_score = self.cube.objective_function()

            delta_e = neighbor_score - current_score

            # Calculate the probability of accepting the worse solution
            try:
                # Safeguard for very large exponent values
                acceptance_probability = math.exp(-delta_e / temperature)
                e_values.append(acceptance_probability)  # Store e^(deltaE/T)
            except OverflowError:
                print(f"Overflow encountered in calculation at iteration {iteration}.")
                break

            if delta_e < 0 or random.random() < acceptance_probability:
                current_score = neighbor_score
                stuck_counter = 0  # Reset stuck counter if improvement happens
            else:
                stuck_counter += 1

            # Check if stuck in local optimum
            if stuck_counter > stuck_threshold:
                stuck_frequency += 1
                stuck_counter = 0  # Reset the stuck counter

            stuck_frequencies.append(stuck_frequency)
            temperature *= cooling_rate

        return e_values, stuck_frequencies

    def random_position(self):
        """Generates a random position in the cube for swapping."""
        return (
            random.randint(0, self.cube.size - 1),
            random.randint(0, self.cube.size - 1),
            random.randint(0, self.cube.size - 1)
        )
    