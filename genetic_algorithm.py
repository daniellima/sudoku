# coding: utf-8
from __future__ import division
import random

from sudoku import Sudoku
from utils import get_initial_sudoku


class GeneticAlgorithm:

    def __init__(self, puzzle, population_size):
        self.puzzle = puzzle
        self.missing = self.puzzle.missing_numbers()
        self.population_size = population_size
        pass

    def generate_individual_indexed_list(self):
        individual_indexed_list = []
        individual_size = len(self.missing)
        for i in range(len(self.missing)):
            choice = random.choice(range(individual_size))
            individual_indexed_list.append(choice)
            individual_size -= 1
        return individual_indexed_list

    def generate_population(self):
        population = []
        for i in range(self.population_size):
            population.append(self.generate_individual_indexed_list())
        return population

    def get_individual_from_indexed_list(self, individual_indexed_list):
        missing_numbers = list(self.missing)
        individual = []
        for i in individual_indexed_list:
            individual.append(missing_numbers[i])
            missing_numbers[i:i+1] = []
        return individual

    def fitness_function(self, individual_indexed_list):
        new_sudoku = get_initial_sudoku()
        individual = self.get_individual_from_indexed_list(individual_indexed_list)
        new_sudoku.fill_missing(individual)
        return 216 - new_sudoku.evaluate()

    def mutation_function(self, individual_indexed_list):
        numbers_to_mutate = random.sample(individual_indexed_list,2)
        
        number1 = numbers_to_mutate[0];
        number2 = numbers_to_mutate[1];

        numbers_to_mutate[0] = number2
        numbers_to_mutate[1] = number1

        return numbers_to_mutate