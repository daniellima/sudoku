# coding: utf-8

class Sudoku:
    SIZE = 3
    EMPTY = 0

    def __init__(self, puzzle):
        self.WIDTH = self.SIZE * self.SIZE
        #  "list" creates a copy of a list
        self.puzzle = list(puzzle)

    def get(self, line, column):
        return self.puzzle[line * self.WIDTH + column]

    def set(self, line, column, value):
        self.puzzle[line * self.WIDTH + column] = value

    def missing_numbers(self):
        # create a list with every possible number.
        # Ex: nine ones, nine twos, etc...
        all = []
        for n in range(self.WIDTH):
            i = [n+1] * self.WIDTH
            all.extend(i)

        for line in range(self.WIDTH):
            for column in range(self.WIDTH):
                if not self.get(line, column) == Sudoku.EMPTY:
                    all.remove(self.get(line, column))
        return all

    def random_fill_missing(self, missing):
        for line in range(self.WIDTH):
            for column in range(self.WIDTH):
                if self.get(line, column) == Sudoku.EMPTY:
                    self.set(line, column, missing.pop(0))

    def evaluate(self):
        pass

    def copy(self):
        return Sudoku(self.puzzle)

    def __str__(self):
        text = ""
        for line in range(self.WIDTH): # goes from 0 to self.WIDTH-1
            for column in range(self.WIDTH):
                el = self.get(line, column)
                if el == 0: el = '.'
                text += str(el) + " "
                if column % self.SIZE == self.SIZE - 1:
                    text += ' '
                if column == self.WIDTH-1:
                    text += '\n'
                if line % self.SIZE == self.SIZE - 1 and column == self.WIDTH-1:
                    text += "\n"

        return text
