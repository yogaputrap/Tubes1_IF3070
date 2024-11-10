import random

class DiagonalMagicCube:
    def __init__(self, size=5):
        self.size = size
        self.cube = self.generate_initial_cube()
        self.magic_number = self.calculate_magic_number()

    def generate_initial_cube(self):
        numbers = list(range(1, self.size**3 + 1))
        random.shuffle(numbers)
        cube = [[[None for _ in range(self.size)] for _ in range(self.size)] for _ in range(self.size)]
        index = 0
        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    cube[x][y][z] = numbers[index]
                    index += 1
        return cube

    def calculate_magic_number(self):
        n = self.size
        return sum(range(1, n**3 + 1)) // (n * (n + 1) // 2)

    def swap_numbers(self, pos1, pos2):
        x1, y1, z1 = pos1
        x2, y2, z2 = pos2
        self.cube[x1][y1][z1], self.cube[x2][y2][z2] = self.cube[x2][y2][z2], self.cube[x1][y1][z1]

    def objective_function(self):
        deviation = 0
        target_sum = self.magic_number

        # Check row sums
        for x in range(self.size):
            for y in range(self.size):
                row_sum = sum(self.cube[x][y][z] for z in range(self.size))
                deviation += abs(row_sum - target_sum)

        # Check column sums
        for x in range(self.size):
            for z in range(self.size):
                col_sum = sum(self.cube[x][y][z] for y in range(self.size))
                deviation += abs(col_sum - target_sum)

        # Check pillar sums
        for y in range(self.size):
            for z in range(self.size):
                pillar_sum = sum(self.cube[x][y][z] for x in range(self.size))
                deviation += abs(pillar_sum - target_sum)

        # Check diagonals in each plane
        for i in range(self.size):
            diag1 = sum(self.cube[i][j][j] for j in range(self.size))
            diag2 = sum(self.cube[i][j][self.size - j - 1] for j in range(self.size))
            deviation += abs(diag1 - target_sum)
            deviation += abs(diag2 - target_sum)

            diag3 = sum(self.cube[j][i][j] for j in range(self.size))
            diag4 = sum(self.cube[self.size - j - 1][i][j] for j in range(self.size))
            deviation += abs(diag3 - target_sum)
            deviation += abs(diag4 - target_sum)

            diag5 = sum(self.cube[j][j][i] for j in range(self.size))
            diag6 = sum(self.cube[j][self.size - j - 1][i] for j in range(self.size))
            deviation += abs(diag5 - target_sum)
            deviation += abs(diag6 - target_sum)

        # Check main space diagonals of the cube
        main_diag1 = sum(self.cube[i][i][i] for i in range(self.size))
        main_diag2 = sum(self.cube[i][i][self.size - i - 1] for i in range(self.size))
        main_diag3 = sum(self.cube[i][self.size - i - 1][i] for i in range(self.size))
        main_diag4 = sum(self.cube[self.size - i - 1][i][i] for i in range(self.size))
        deviation += abs(main_diag1 - target_sum)
        deviation += abs(main_diag2 - target_sum)
        deviation += abs(main_diag3 - target_sum)
        deviation += abs(main_diag4 - target_sum)

        return deviation
    