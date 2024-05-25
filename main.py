import time

from matplotlib import pyplot as plt

from GeneticSolver import GeneticSolver
from data_generator import load_dataset


if __name__ == "__main__":
    FILE_PATH = "dataset4.pkl"
    SEED = 123  # You need to evaluate your approach with various seed due to the non-deterministic behavior of the GA
    solver = GeneticSolver(SEED)
    dataset = load_dataset(FILE_PATH)

    x1 = dataset["x1"]
    x2 = dataset["x2"]
    y = dataset["y"]

   

    start_time = time.time()
    solver.solve(x1, x2, y)
    end_time = time.time()

    print("Objective Value:", solver.calculate_objective(x1, x2, y), sep="\t")
    print("Elapsed Time (ms):", end_time - start_time, sep="\t")
    print("a:", solver.a, sep="\t")
    print("b:", solver.b, sep="\t")
    print("c:", solver.c, sep="\t")

#Plottings:
#1) Initialization range change impacts to Genetic Algorithm:
    # file_paths = ["dataset1.pkl","dataset2.pkl","dataset3.pkl","dataset4.pkl","dataset5.pkl"]
    # objective_values = []
    # solver = GeneticSolver(SEED)

    # for file_path in file_paths:
    #     dataset = load_dataset(file_path)
    #     x1 = dataset["x1"]
    #     x2 = dataset["x2"]
    #     y = dataset["y"]

    #     start_time = time.time()
    #     solver.solve(x1, x2, y)
    #     end_time = time.time()

    #     print(f"Dataset from: {file_path}")
    #     obj_val = solver.calculate_objective(x1, x2, y)
    #     objective_values.append(obj_val)
    #     print("Objective Value:", obj_val, sep="\t")
    #     print("Elapsed Time (ms):", end_time - start_time, sep="\t")
    #     print("a:", solver.a, sep="\t")
    #     print("b:", solver.b, sep="\t")
    #     print("c:", solver.c, sep="\t")
    
    # plt.figure(figsize=(10,6))
    # plt.bar(range(len(objective_values)),objective_values, tick_label = [f"Datset {i+1}" for i in range(len(objective_values))])
    # plt.xlabel("Dataset")
    # plt.ylabel("Objective Value")
    # plt.title(" Objective values of 5 Datasets (range:(-5,5))")
    # plt.show()

# #2) Max iteration impacts to Genetic Algorithm:
#     FILE_PATH = "dataset2.pkl"
#     objective_values = []
#     elapsed_times = []
#     max_iters = [100,200,300,400,500]
#     for max_iter in max_iters:
#         dataset = load_dataset(FILE_PATH)
#         solver = GeneticSolver(max_iter, SEED)
#         x1 = dataset["x1"]
#         x2 = dataset["x2"]
#         y = dataset["y"]

#         start_time = time.time()
#         solver.solve(x1, x2, y)
#         end_time = time.time()

#         print(f"Max iterations: {max_iter}")
#         obj_val = solver.calculate_objective(x1, x2, y)
#         objective_values.append(obj_val)
#         print("Objective Value:", obj_val, sep="\t")
#         elapsed_time = end_time - start_time
#         elapsed_times.append(elapsed_time)
#         print("Elapsed Time (ms):",elapsed_time , sep="\t")
#         print("a:", solver.a, sep="\t")
#         print("b:", solver.b, sep="\t")
#         print("c:", solver.c, sep="\t")
    
#     plt.figure(figsize=(12,6))
#     plt.subplot(1,2,1)
#     plt.plot(max_iters,objective_values,marker="o")
#     plt.title("Objective Values vs Max Itertions")
#     plt.ylabel("Objective Values")
#     plt.xlabel("Max Iterations")
#     plt.subplot(1,2,2)
#     plt.plot(max_iters,elapsed_times,marker="o")
#     plt.title("Elapsed Time vs Max Itertions")
#     plt.ylabel("Objective Values")
#     plt.xlabel("Max Iterations")

#     plt.show()

    # #3) Population Size impacts to Genetic Algorithm:
    # FILE_PATH = "dataset1.pkl"
    # objective_values = []
    # elapsed_times = []
    # pop_sizes = [100,200,300,400,500]
    # for pop_size in pop_sizes:
    #     dataset = load_dataset(FILE_PATH)
    #     solver = GeneticSolver(pop_size, SEED)
    #     x1 = dataset["x1"]
    #     x2 = dataset["x2"]
    #     y = dataset["y"]

    #     start_time = time.time()
    #     solver.solve(x1, x2, y)
    #     end_time = time.time()

    #     print(f"Population size: {pop_size}")
    #     obj_val = solver.calculate_objective(x1, x2, y)
    #     objective_values.append(obj_val)
    #     print("Objective Value:", obj_val, sep="\t")
    #     elapsed_time = end_time - start_time
    #     elapsed_times.append(elapsed_time)
    #     print("Elapsed Time (ms):",elapsed_time , sep="\t")
    #     print("a:", solver.a, sep="\t")
    #     print("b:", solver.b, sep="\t")
    #     print("c:", solver.c, sep="\t")
    
    # plt.figure(figsize=(12,6))
    # plt.subplot(1,2,1)
    # plt.plot(pop_sizes,objective_values,marker="o")
    # plt.title("Objective Values vs Population Size")
    # plt.ylabel("Objective Values")
    # plt.xlabel("Population Size")
    # plt.subplot(1,2,2)
    # plt.plot(pop_sizes,elapsed_times,marker="o")
    # plt.title("Elapsed Time vs Population Size")
    # plt.ylabel("Objective Values")
    # plt.xlabel("Population Size")

    # plt.show()

    # #4) Elitism rate impacts to Genetic Algorithm:
    # FILE_PATH = "dataset3.pkl"
    # objective_values = []
    # elapsed_times = []
    # elitism_rates = [0.05, 0.1 , 0.15, 0.20, 0.25]
    # for elitism_rate in elitism_rates:
    #     dataset = load_dataset(FILE_PATH)
    #     solver = GeneticSolver(elitism_rate, SEED)
    #     x1 = dataset["x1"]
    #     x2 = dataset["x2"]
    #     y = dataset["y"]

    #     start_time = time.time()
    #     solver.solve(x1, x2, y)
    #     end_time = time.time()

    #     print(f"Elitism Rates: {elitism_rate}")
    #     obj_val = solver.calculate_objective(x1, x2, y)
    #     objective_values.append(obj_val)
    #     print("Objective Value:", obj_val, sep="\t")
    #     elapsed_time = end_time - start_time
    #     elapsed_times.append(elapsed_time)
    #     print("Elapsed Time (ms):",elapsed_time , sep="\t")
    #     print("a:", solver.a, sep="\t")
    #     print("b:", solver.b, sep="\t")
    #     print("c:", solver.c, sep="\t")
    
    # plt.figure(figsize=(12,6))
    # plt.subplot(1,2,1)
    # plt.plot(elitism_rates,objective_values,marker="o")
    # plt.title("Objective Values vs Elitism Rate")
    # plt.ylabel("Objective Values")
    # plt.xlabel("Elitism Rate")
    # plt.subplot(1,2,2)
    # plt.plot(elitism_rates,elapsed_times,marker="o")
    # plt.title("Elapsed Time vs Population Size")
    # plt.ylabel("Objective Values")
    # plt.xlabel("Elitism Rate")
    # plt.show()

    # #4) Mutation rate impacts to Genetic Algorithm:
    # FILE_PATH = "dataset3.pkl"
    # objective_values = []
    # elapsed_times = []
    # mutation_rates = [0.2,0.25 ,0.3,0.35, 0.4 ,0.45, 0.5,0.55, 0.6,0.65, 0.7,0.75, 0.8,0.85, 0.9,0.95]
    # for mutation_rate in mutation_rates:
    #     dataset = load_dataset(FILE_PATH)
    #     solver = GeneticSolver(mutation_rate, SEED)
    #     x1 = dataset["x1"]
    #     x2 = dataset["x2"]
    #     y = dataset["y"]

    #     start_time = time.time()
    #     solver.solve(x1, x2, y)
    #     end_time = time.time()

    #     print(f"Mutaation Rates: {mutation_rate}")
    #     obj_val = solver.calculate_objective(x1, x2, y)
    #     objective_values.append(obj_val)
    #     print("Objective Value:", obj_val, sep="\t")
    #     elapsed_time = end_time - start_time
    #     elapsed_times.append(elapsed_time)
    #     print("Elapsed Time (ms):",elapsed_time , sep="\t")
    #     print("a:", solver.a, sep="\t")
    #     print("b:", solver.b, sep="\t")
    #     print("c:", solver.c, sep="\t")
    
    # plt.figure(figsize=(12,6))
    # plt.subplot(1,2,1)
    # plt.plot(mutation_rates,objective_values,marker="o")
    # plt.title("Objective Values vs Mutation Rate")
    # plt.ylabel("Objective Values")
    # plt.xlabel("Population Size")
    # plt.subplot(1,2,2)
    # plt.plot(mutation_rates,elapsed_times,marker="o")
    # plt.title("Elapsed Time vs Mutation Rate")
    # plt.ylabel("Objective Values")
    # plt.xlabel("Population Size")
    # plt.show()

    # #6) Random Seed impacts to Genetic Algorithm:
    # FILE_PATH = "dataset1.pkl"
    # objective_values = []
    # elapsed_times = []
    # seeds = [ 0, 1, 5 ,10,20,30,40,50,60,70,80,90,100,123]
    # for seed in seeds:
    #     dataset = load_dataset(FILE_PATH)
    #     solver = GeneticSolver(seed)
    #     x1 = dataset["x1"]
    #     x2 = dataset["x2"]
    #     y = dataset["y"]

    #     start_time = time.time()
    #     solver.solve(x1, x2, y)
    #     end_time = time.time()

    #     print(f"Seeds: {seed}")
    #     obj_val = solver.calculate_objective(x1, x2, y)
    #     objective_values.append(obj_val)
    #     print("Objective Value:", obj_val, sep="\t")
    #     elapsed_time = end_time - start_time
    #     elapsed_times.append(elapsed_time)
    #     print("Elapsed Time (ms):",elapsed_time , sep="\t")
    #     print("a:", solver.a, sep="\t")
    #     print("b:", solver.b, sep="\t")
    #     print("c:", solver.c, sep="\t")
    
    # plt.figure(figsize=(12,6))
    # plt.subplot(1,2,1)
    # plt.plot(seeds,objective_values,marker="o")
    # plt.title("Objective Values vs Seed")
    # plt.ylabel("Objective Values")
    # plt.xlabel("Seed")
    # plt.subplot(1,2,2)
    # plt.plot(seeds,elapsed_times,marker="o")
    # plt.title("Elapsed Time vs Seed")
    # plt.ylabel("Objective Values")
    # plt.xlabel("Seed")
    # plt.show()





