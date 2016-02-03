# coding: utf-8

# Trabalho Sudoku
# Alunos: Annanda Sousa, Daniel Lima e Tayssa Vandelli

# Ideia do código
"""
Heurística escolhida:
Minimizar a quantidade de erros de números dispostos no tabuleiro.

"""

from genetic_solver import GeneticSolver
from genetic_algorithm import GeneticAlgorithm
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

ga = GeneticAlgorithm(sudoku)

solver = GeneticSolver(
    sudoku,
    steps = 500,
    population_size = 4,
    crossover_chance = 0.8,
    mutation_chance = 0.01
    )

population = solver.solve()

population.sort(key=lambda ind: ga.fitness_function(ind))

ind = ga.get_individual_from_indexed_list(population[-1:][0])

sudoku.fill_missing(ind)

print(sudoku)
print(sudoku.evaluate())
