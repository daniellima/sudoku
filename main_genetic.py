# coding: utf-8
from __future__ import division

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

ga = GeneticAlgorithm(sudoku, 4)

ind = ga.generate_individual_indexed_list()

print('Essa é a lista dos numeros faltando', sudoku.missing_numbers())

print("Esse é a lista de individuo:", ind)
individual = ga.get_individual_from_indexed_list(ind)

print("Essa é o individuo real", individual)

fitness_value = ga.fitness_function(ind)
print('fitnes value', fitness_value)

pop = ga.generate_population()
print('population', pop)
ga.crossover(pop)
print('population', pop)

# um, dois, tres, quatro, cinco, seis, sete, oito, nove = 0,0,0,0,0,0,0,0,0
# for i in individual:
#     if i == 1:
#         um += 1
#     elif i == 2:
#         dois += 1
#     elif i == 3:
#         tres += 1
#     elif i == 4:
#         quatro += 1
#     elif i == 5:
#         cinco += 1
#     elif i == 6:
#         seis += 1
#     elif i == 7:
#         sete += 1
#     elif i == 8:
#         oito += 1
#     elif i == 9:
#         nove += 1
#
# print('Um', um)
# print('Dois', dois)
# print('Tres', tres)
# print('Quatro', quatro)
# print('Cinco', cinco)
# print('Seis', seis)
# print('Sete', sete)
# print('Oito', oito)
# print('Nove', nove)
