import time
import matplotlib.pyplot as plt
from diagonalMagicCube import DiagonalMagicCube
from hillClimbing import HillClimbing
from simulatedAnnealing import SimulatedAnnealing
from geneticAlgorithm import GeneticAlgorithm
from visualizer import Visualizer

def run_experiment(algorithm_class, name, runs=3, population_size=None, generations=None):
    results = []
    
    for i in range(runs):
        print(f"Running {name}, Trial {i+1}...")

        # Initialize the cube and algorithm
        magic_cube = DiagonalMagicCube()
        initial_state = [row[:] for row in magic_cube.cube]
        
        # Visualize initial state of the cube
        visualizer = Visualizer(magic_cube)
        visualizer.plot_cube(title=f"{name} - Initial State (Trial {i+1})")
        
        # Create the algorithm instance
        if name == "Genetic Algorithm":
            algorithm = algorithm_class(magic_cube)
            if population_size is not None and generations is not None:
                result = algorithm.run(population_size=population_size, generations=generations, record=None)
        else:
            algorithm = algorithm_class(magic_cube)
        
        # Track time and objective function values
        start_time = time.time()
        objective_values = []
        
        # Run the algorithm with iteration tracking
        if name == "Hill Climbing":
            iteration_count = algorithm.steepest_ascent(record=objective_values)
        elif name == "Simulated Annealing":
            e_values, stuck_frequencies = algorithm.anneal(record=objective_values)
        elif name == "Genetic Algorithm":
            algorithm.run(record=objective_values)
        
        end_time = time.time()
        
        # Store final state and results
        final_state = [row[:] for row in magic_cube.cube]
        final_objective_value = magic_cube.objective_function()
        duration = end_time - start_time
        
        # Visualize final state of the cube
        visualizer.plot_cube(title=f"{name} - Final State (Trial {i+1})")
        
        results.append({
            "initial_state": initial_state,
            "final_state": final_state,
            "objective_values": objective_values,
            "final_objective_value": final_objective_value,
            "duration": duration,
            "iterations": iteration_count if name == "Hill Climbing" else None,  # Catat iterasi untuk Hill Climbing
            "e_values": e_values if name == "Simulated Annealing" else None,
            "stuck_frequencies": stuck_frequencies if name == "Simulated Annealing" else None
        })
        
        print(f"Final Objective: {final_objective_value}, Duration: {duration:.2f} seconds")
        if name == "Hill Climbing":
            print(f"Total Iterations: {iteration_count}")

    # Plotting objective function progression for each run
    for i, result in enumerate(results):
        plt.plot(result["objective_values"], label=f"Trial {i+1}")
    
    plt.title(f"{name} - Objective Function Over Iterations")
    plt.xlabel("Iterations")
    plt.ylabel("Objective Function Value")
    plt.legend()
    plt.show()

    # Plot e^(delta E / T) for Simulated Annealing
    if name == "Simulated Annealing":
        for i, result in enumerate(results):
            plt.plot(result["e_values"], label=f"Trial {i+1}")

        plt.title(f"{name} - e^(delta E / T) Over Iterations")
        plt.xlabel("Iterations")
        plt.ylabel("e^(delta E / T)")
        plt.legend()
        plt.show()

        # Plot stuck frequencies for Simulated Annealing
        for i, result in enumerate(results):
            plt.plot(result["stuck_frequencies"], label=f"Trial {i+1}")

        plt.title(f"{name} - Frequency of 'Stuck' States Over Iterations")
        plt.xlabel("Iterations")
        plt.ylabel("Stuck Frequency")
        plt.legend()
        plt.show()

    return results

def run_genetic_algorithm_experiment():
    # Run experiments for Genetic Algorithm with different populations and generations
    population_sizes = [50, 100, 200]
    generations_options = [50, 100, 200]

    # Experiment 1: Fixed population, varied generations
    fixed_population = 100
    for generations in generations_options:
        print(f"Running Genetic Algorithm with Population Size {fixed_population} and Generations {generations}")
        genetic_results = run_experiment(GeneticAlgorithm, "Genetic Algorithm", population_size=fixed_population, generations=generations)
        print(f"Experiment with Population Size {fixed_population} and Generations {generations} completed.")

    # Experiment 2: Fixed generations, varied population sizes
    fixed_generations = 100
    for population_size in population_sizes:
        print(f"Running Genetic Algorithm with Population Size {population_size} and Generations {fixed_generations}")
        genetic_results = run_experiment(GeneticAlgorithm, "Genetic Algorithm", population_size=population_size, generations=fixed_generations)
        print(f"Experiment with Population Size {population_size} and Generations {fixed_generations} completed.")

def main():
    # Run experiments for each algorithm
    hill_climbing_results = run_experiment(HillClimbing, "Hill Climbing")
    simulated_annealing_results = run_experiment(SimulatedAnnealing, "Simulated Annealing")
    genetic_algorithm_results = run_genetic_algorithm_experiment()

    print("Experiment completed. Results recorded and plotted.")

if __name__ == "__main__":
    main()
    