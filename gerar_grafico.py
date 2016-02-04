# -*- coding: utf-8 -*-
import sys
from matplotlib import pyplot as plt
import numpy as np

from main_genetic import run_tests, avg_times, reset_times


def caso1():
    "erros por passos, com populacao = 6"
    X = [50, 100, 200, 500, 1000, 10000]
    Y = []
    # Y = [68.05, 67.32, 66.21, 63.15, 60.43, 47.77]
    for x in X:
        y = run_tests(steps=x, population_size=6)
        Y.append(y)

    gerar_grafico(
        name="media_erros_passos_pop6",
        label="erro",
        title="erros por passos, com populacao = 6",
        X=X,
        Y=Y
    )


def caso2():
    "erros por populacao, com passos = 100"
    X = [10, 20, 30, 40, 50, 60, 70]
    Y = []
    # Y = [63.73, 61.11, 58.04, 57.03, 55.08, 55.14, 55]
    for x in X:
        y = run_tests(steps=100, population_size=x, crossover_chance=0.8)
        Y.append(y)

    gerar_grafico(
        name="media_erros_pop_passos100",
        label="erro",
        title="erros por populacao, com passos = 100",
        X=X,
        Y=Y
    )
    reset_times()


def caso3():
    "erros por crossover, com populacao = 40, passos = 100"
    X = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    Y = []
    for x in X:
        y = run_tests(steps=100, population_size=40, crossover_chance=x)
        Y.append(y)

    gerar_grafico(
        name="avg_erro_cross_pop40_passos100",
        label="erro",
        title="erros por crossover, com populacao = 40, passos = 100",
        X=X,
        Y=Y
    )
    reset_times()


def caso4():
    "erros por mutacao, com populacao = 40, passos = 100"
    X = [0.1, 0.2, 0.3, 0.4, 0.5]
    Y = []
    # Y = [55.13, 56.16, 56.41, 57.36, 57.79]
    for x in X:
        y = run_tests(steps=100, population_size=40, mutacao=x)
        Y.append(y)

    gerar_grafico(
        name="avg_erro_mut_pop40_passos100",
        label="erro",
        title="erros por mutacao, com populacao = 40, passos = 100",
        X=X,
        Y=Y
    )
    reset_times()


def gerar_grafico(name, label, title, X, Y):
    fig = plt.figure()
    width = .35
    ind = np.arange(len(Y))
    plt.bar(ind, Y, label=label)

    plt.xticks(ind + width / 2, X)

    plt.title(title)
    # Now add the legend with some customizations.
    legend = plt.legend(loc='best', shadow=True)
    frame = legend.get_frame()
    frame.set_facecolor('0.90')

    # Set the fontsize
    for label in legend.get_texts():
        label.set_fontsize('large')

    for label in legend.get_lines():
        label.set_linewidth(1.5)  # the legend line width

    plt.savefig("%s.png" % name)
    plt.close(fig)

if __name__ == '__main__':
    caso1()
    caso2()
    caso3()
    caso4()
