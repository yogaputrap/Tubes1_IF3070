import random

class HillClimbing:
    def __init__(self, cube):
        self.cube = cube

    def steepest_ascent(self, max_iterations=1000, record=None):
        iteration_count = 0  # Menambahkan penghitung iterasi
        
        for iteration in range(max_iterations):
            iteration_count += 1  # Meningkatkan jumlah iterasi
            current_score = self.cube.objective_function()
            if record is not None:
                record.append(current_score)

            best_neighbor = None
            best_score = current_score

            # Generate and evaluate neighbors by swapping numbers
            for _ in range(100):  # Limit the number of neighbors considered
                pos1 = self.random_position()
                pos2 = self.random_position()
                self.cube.swap_numbers(pos1, pos2)
                neighbor_score = self.cube.objective_function()

                if neighbor_score < best_score:
                    best_neighbor = (pos1, pos2)
                    best_score = neighbor_score
                self.cube.swap_numbers(pos1, pos2)  # Swap back

            if best_neighbor:
                pos1, pos2 = best_neighbor
                self.cube.swap_numbers(pos1, pos2)
            else:
                break  # Stop if no improvement

        return iteration_count  # Mengembalikan jumlah iterasi

    def random_position(self):
        """Generates a random position in the cube for swapping."""
        return (
            random.randint(0, self.cube.size - 1),
            random.randint(0, self.cube.size - 1),
            random.randint(0, self.cube.size - 1)
        )
