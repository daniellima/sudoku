# coding: utf-8
from __future__ import division

# Trabalho Sudoku
# Alunos: Annanda Sousa, Daniel Lima e Tayssa Vandelli

# Ideia do código
"""
Heurística escolhida:
Minimizar a quantidade de erros de números dispostos no tabuleiro.

"""

from hill_climbing_sudoku_solver import HillClimbingSudokuSolver
from sudoku import Sudoku

_ = Sudoku.EMPTY
sudoku = Sudoku([
    _, _, _,   7, _, _,   _, _, _,
    1, _, _,   _, _, _,   _, _, _,
    _, _, _,   4, 3, _,   2, _, _,

    _, _, _,   _, _, _,   _, _, 6,
    _, _, _,   5, _, 9,   _, _, _,
    _, _, _,   _, _, _,   4, 1, 8,

    _, _, _,   _, 8, 1,   _, _, _,
    _, _, 2,   _, _, _,   _, 5, _,
    _, 4, _,   _, _, _,   3, _, _
])

solver = HillClimbingSudokuSolver(sudoku, steps=5000)
solved = solver.solve()
print(solved)
print("Número de erros:", sudoku.evaluate())

# missing = sudoku.missing_numbers()
# sudoku.fill_missing(missing)
# print(sudoku)

# print sudoku
# print sudoku.evaluate()
# sudoku.swap(0, 18)
# print sudoku
# print sudoku.evaluate()

#print len(sudoku.emptyIndexes) == 81 - 17 # 64
#print len(sudoku.get_possible_swaps()) == 2016 # somatorio de 63 até 1
