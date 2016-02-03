# coding: utf-8
from __future__ import division
import random

from sudoku import Sudoku


class GeneticAlgorithm:

    def __init__(self, puzzle, population_size):
        self.puzzle = puzzle
        self.population_size = population_size
        pass

    def generate_individual(self):
        individual = []
        individual_size = len(self.puzzle.emptyIndexes)
        for i in range(len(self.puzzle.emptyIndexes)):
            choice = random.choice(range(individual_size))
            individual.append(choice)
            individual_size -= 1
        return individual

    def generate_population(self):
        population = []
        for i in range(self.population_size):
            population.append(self.generate_individual())
        return population