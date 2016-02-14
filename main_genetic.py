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
from utils import get_initial_sudoku, timing, avg_times, reset_times


@timing
def single_test(steps, population_size, crossover_chance, mutation_chance, evaluate_number):
    sudoku = get_initial_sudoku()

    ga = GeneticAlgorithm(sudoku)

    solver = GeneticSolver(
        sudoku,
        steps = steps,
        population_size = population_size,
        crossover_chance = crossover_chance,
        mutation_chance = mutation_chance
        )

    population = solver.solve()

    population.sort(key=lambda ind: ga.fitness_function(ind))

    ind = ga.get_individual_from_indexed_list(population[-1:][0])

    sudoku.fill_missing(ind)

    print(sudoku)
    evaluation = sudoku.evaluate()
    print(evaluation)
    evaluate_number = evaluate_number + sudoku.evaluate()

    um, dois, tres, quatro, cinco, seis, sete, oito, nove = 0,0,0,0,0,0,0,0,0
    for i in sudoku.puzzle:
     if i == 1:
         um += 1
     elif i == 2:
         dois += 1
     elif i == 3:
         tres += 1
     elif i == 4:
         quatro += 1
     elif i == 5:
         cinco += 1
     elif i == 6:
         seis += 1
     elif i == 7:
         sete += 1
     elif i == 8:
         oito += 1
     elif i == 9:
         nove += 1

    print('\nUm', um)
    print('Dois', dois)
    print('Tres', tres)
    print('Quatro', quatro)
    print('Cinco', cinco)
    print('Seis', seis)
    print('Sete', sete)
    print('Oito', oito)
    print('Nove', nove)
    return evaluate_number


def run_tests(steps, population_size, crossover_chance=0.8, mutation_chance=0.01):
    tests = 100
    evaluate_number = 0
    for i in range(tests):
        evaluate_number = single_test(steps, population_size, crossover_chance, mutation_chance, evaluate_number)
        print("teste: %d/%d" % (i, tests-1))
    print("MEDIA:", evaluate_number/tests)
    return evaluate_number/tests


if __name__ == '__main__':
    run_tests(steps=2, population_size=2)

    print("media de tempo: %0.3f ms" % avg_times())
