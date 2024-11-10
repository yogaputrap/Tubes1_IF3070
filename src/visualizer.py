import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from diagonalMagicCube import DiagonalMagicCube

class Visualizer:
    def __init__(self, cube):
        self.cube = cube

    def plot_cube(self, title="Magic Cube State"):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_title(title)
        
        # Set axis limits
        ax.set_xlim([0, self.cube.size])
        ax.set_ylim([0, self.cube.size])
        ax.set_zlim([0, self.cube.size])

        # Define color mapping for y values
        color_map = {
            0: 'red',    # For y = 0
            1: 'green',  # For y = 1
            2: 'blue',   # For y = 2
            3: 'orange', # For y = 3
            4: 'purple'  # For y = 4
        }

        # Plot each number in the cube with a color based on the y coordinate
        for x in range(self.cube.size):
            for y in range(self.cube.size):
                for z in range(self.cube.size):
                    number = self.cube.cube[x][y][z]
                    color = color_map.get(y, 'black')  # Default to 'black' if y is out of range
                    ax.text(x + 0.5, y + 0.5, z + 0.5, str(number), color=color,
                            ha='center', va='center', fontsize=8)

        # Customize axis labels
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Z-axis')
        plt.show()
