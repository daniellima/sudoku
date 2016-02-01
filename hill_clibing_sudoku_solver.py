# coding: utf-8

class HillClibingSudokuSolver:

    def __init__(self, sudoku, steps):
        self.sudoku = sudoku
        self.steps = steps

    def solve(self):
        missing = self.sudoku.missing_numbers()

        copy = self.sudoku.copy()

        copy.random_fill_missing(missing)

        return copy.evaluate()

        return copy

        return self.sudoku
