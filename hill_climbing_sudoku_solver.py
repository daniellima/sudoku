# coding: utf-8
from __future__ import division


class HillClimbingSudokuSolver:

    def __init__(self, sudoku, steps):
        self.sudoku = sudoku
        self.steps = steps

    def solve(self):
        missing = self.sudoku.missing_numbers()
        self.sudoku.random_fill_missing(missing)

        swaps = self.sudoku.get_possible_swaps()

        for _ in range(self.steps):
            print("Step " + str(_))
            best_swap = None
            best_evaluation = self.sudoku.evaluate()

            for swap in swaps:
                # don't swap numbers that are equals
                if self.sudoku.puzzle[swap[0]] == self.sudoku.puzzle[swap[1]]:
                    continue
                self.sudoku.swap(swap[0], swap[1])
                current_evaluation = self.sudoku.evaluate()
                if current_evaluation == 0:
                    return self.sudoku # we found the solution \o
                if current_evaluation < best_evaluation:
                    best_evaluation = current_evaluation
                    best_swap = swap
                self.sudoku.swap(swap[1], swap[0])

            if best_swap == None: # atingimos um maximo local
                # tem que ver melhor o que fazer aqui. Fiz a estratégia de mudanças aleatorias
                import random

                print("Triste.")
                #print(self.sudoku)
                print("Número de erros:",self.sudoku.evaluate())
                # muitas mudanças aleatorias para evitar que ele caia nesse maximo local novamente
                number_random_swaps = 10
                for i in range(number_random_swaps):
                    self.sudoku.swap(random.choice(self.sudoku.emptyIndexes), random.choice(self.sudoku.emptyIndexes))
                continue

            self.sudoku.swap(best_swap[0], best_swap[1])

        return self.sudoku
