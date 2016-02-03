# coding: utf-8

from genetic_algorithm import GeneticAlgorithm

class GeneticSolver:

    def __init__(self, sudoku, steps, population_size):
        self.sudoku = sudoku
        self.steps = steps
        self.population_size = population_size

    def solve(self):
        ga = GeneticAlgorithm(self.sudoku, self.population_size)
        population = ga.generate_population();

        pop = population
        for _ in range(self.steps):
            pop = ga.select(pop)
            ga.crossover(pop)
            for i in range(len(pop)):
                pop[i] = ga.mutation(pop[i])

        return pop
