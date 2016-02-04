# -*- coding: utf-8 -*-
import sys
from matplotlib import pyplot as plt
import numpy as np


def gerar_grafico(name, label, title):
    fig = plt.figure()
    steps = [50, 100, 200, 500, 1000]
    errors = [68.05, 67.32, 66.21, 63.15, 60.43]

    Y = errors
    X = steps
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
    if len(sys.argv) == 4:
        _, name, label, title = sys.argv
    else:
        name = 'media_erros_passos'
        label = 'variavel'
        title = 'titulo'

    gerar_grafico(name, label, title)
