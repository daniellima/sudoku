# coding: utf-8
from __future__ import division
import random

from sudoku import Sudoku

class GeneticAlgorithm:

    def __init__(self, puzzle):
        self.puzzle = puzzle
        pass

    def generate_index_list(self):
        individuo = []
        indexed_list_size = len(self.puzzle.emptyIndexes)
        for i in range(len(self.puzzle.emptyIndexes)):
            choice = random.choice(range(indexed_list_size))
            individuo.append(choice)
            indexed_list_size -= 1
        return individuo
