# coding: utf-8

from genetic_algorithm import GeneticAlgorithm

class GeneticSolver:

    def __init__(self, sudoku, steps, population_size, crossover_chance, mutation_chance):
        self.sudoku = sudoku
        self.steps = steps
        self.population_size = population_size
        self.crossover_chance = crossover_chance
        self.mutation_chance = mutation_chance

    def solve(self):
        ga = GeneticAlgorithm(self.sudoku)
        population = ga.generate_population(self.population_size);

        pop = population
        for _ in range(self.steps):
            pop = ga.select(pop)
            ga.crossover(pop, self.crossover_chance)
            for i in range(len(pop)):
                pop[i] = ga.mutation(pop[i], self.mutation_chance)

        return pop
