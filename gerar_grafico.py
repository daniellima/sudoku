# -*- coding: utf-8 -*-
import sys
from matplotlib import pyplot as plt
import numpy as np


def gerar_grafico(nome):
    fig = plt.figure()
    steps = [50, 100, 200, 500, 1000]
    errors = [68.05, 67.32, 66.21, 63.15, 60.43]

    Y = errors
    X = steps
    width = .35
    ind = np.arange(len(Y))
    plt.bar(ind, Y)
    plt.xticks(ind + width / 2, X)

    plt.savefig("%s.png" % nome)
    plt.close(fig)
if __name__ == '__main__':
    if len(sys.argv) == 2:
        nome = sys.argv[1]
    else:
        nome = 'media_erros_passos'

    gerar_grafico(nome)
