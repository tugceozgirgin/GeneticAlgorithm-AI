import copy
import numpy as np
import random
from random import Random


class GeneticSolver:
    """
        This class employs your genetic algorithm implementations.
    """
    seed: int    #: Specified Random Seed. You need to set specified random seed
    a: float     #: **a** parameter in the linear function
    b: float     #: **b** parameter in the linear function
    c: float     #: **c** parameter in the linear function
    rnd: Random  #: Example random object. You can use it

    def __init__(self, seed: int):
        """
            Construction of the class.

            :param seed: Specified Random Seed
        """
        self.seed = seed
        self.rnd = random.Random(seed)
        random.seed(seed)
        np.random.seed(seed)

        #Variables 
        self.population_size = 100
        self.max_iter = 100
        self.elitism_rate = 0.05
        self.tournament_size = 3
        self.mutation_rate = 0.7


    def solve(self, x1: np.ndarray, x2: np.ndarray, y: np.ndarray):
        """
            This method runs your genetic algorithm for the given dataset

            **Note**: You need specify the parameters (a,b,c) at the end of the solve method

            :param x1: First independent features from the dataset as a NumPy array
            :param x2: Second independent features from the dataset as a NumPy array
            :param y: Target dependent values from the dataset as a NumPy array
        """

        #Initiate Population
        my_population = self.initiate_population()
        
        for iter in range(self.max_iter):
            mean_squared_errors = [self.fitness_score( x1,x2,y,sample) for sample in my_population]
            next_generation = []

            #Elitism: copy best ones  directly to the next generation 
            sorted_my_population = sorted(my_population, key=lambda sample:self.fitness_score(x1,x2,y,sample))
            elite_group_size = len(my_population)* self.elitism_rate
            elite_generation = sorted_my_population[:int(elite_group_size)]
            next_generation = elite_generation

            #Tournament Selection
            rest_of_the_population =  sorted_my_population[int(elite_group_size):]
            selected_population = self.tournament_selection(rest_of_the_population,x1,x2,y)

            #Cross-over
            child_generation = []
            while len(selected_population)!= 0:
                
                if len(selected_population) > 1:
                  parent1,parent2 = self.rnd.sample(selected_population,2)
                  child1,child2 = self.single_point_crossover(parent1,parent2)
                 
                  child_generation.append(child1)
                  child_generation.append(child2)
                
                  selected_population.remove(parent1)
                  selected_population.remove(parent2)

                else: # if there is no pair left
                  last_parent = selected_population.pop()
                  child_generation.append(last_parent)
            
            #Mutation
            mutated_childs = []
            for child in child_generation:
                mutated_child = self.random_resetting_mutation(child)
                mutated_childs.append(mutated_child)

            next_generation.extend(mutated_childs)
            my_population = next_generation

        best_solution = min(my_population, key=lambda sample:self.fitness_score(x1,x2,y,sample))

        self.a = best_solution.get('a')
        self.b = best_solution.get('b')
        self.c = best_solution.get('c')


    
    def random_resetting_mutation(self,child):
        mutated_child = copy.deepcopy(child)
        if random.random() < self.mutation_rate:
            mutated_gene = self.rnd.choice([1,2,3])
            if mutated_gene == 1:
                mutated_child['a'] = self.rnd.uniform(-5,5)
            elif mutated_gene == 2:
                mutated_child['b'] = self.rnd.uniform(-5,5)
            elif mutated_gene == 3:
                mutated_child['c'] = self.rnd.uniform(-5,5)
        return mutated_child

    
    def single_point_crossover(self, parent1, parent2):
        crossover_border = self.rnd.choice([1,2])
        if crossover_border == 1: # swap b and c s
            return({'a': parent1['a'], 'b': parent2['b'], 'c':parent2['c']},
                   {'a': parent2['a'], 'b': parent1['b'], 'c':parent1['c']})
        elif crossover_border == 2: # swap  c s
            return({'a': parent1['a'], 'b': parent1['b'], 'c':parent2['c']},
                   {'a': parent2['a'], 'b': parent2['b'], 'c':parent1['c']})
        else:
             return parent1, parent2 


    def tournament_selection(self,selection_population,x1,x2,y):
        selecteds = []
        for index in range(len(selection_population)):
            k_random_samples = self.rnd.sample(selection_population, self.tournament_size)
            selected = min(k_random_samples, key=lambda sample: self.fitness_score(x1,x2,y,sample))
            selecteds.append(selected)
        return selecteds


    def fitness_score(self,x1,x2,y,sample):
        cumulative_mse = 0
        for index in range(len(y)):
           y_pred = sample['a']* x1[index]  + sample['b']*x2[index] +sample['c']
           mse = (y_pred -y[index])**2
           cumulative_mse+=mse
        return (cumulative_mse/len(y))
    

    def initiate_population(self):
        population = []
        for index in range(self.population_size):
            sample = {
                'a': self.rnd.uniform(-1,1),
                'b': self.rnd.uniform(-1,1),
                'c': self.rnd.uniform(-1,1)
            }
            population.append(sample)
        
        return population
    

    def calculate_objective(self, x1: np.ndarray, x2: np.ndarray, y: np.ndarray):
        """
            This method calculates objective function value (i.e., mean squared error)
        :param x1: First independent features from the dataset as a NumPy array
        :param x2: Second independent features from the dataset as a NumPy array
        :param y: Target dependent values from the dataset as a NumPy array
        :return: Prediction error
        """
        return np.mean(np.power(x1 * self.a + x2 * self.b + self.c - y, 2.))

        