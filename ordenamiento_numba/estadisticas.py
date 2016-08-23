# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 10:17:55 2016

@author: karol
"""

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from quick_sort import quick_sort

algos = ["Bubble", "Insertion", "Selection", "Quick"]
colores = ['r', 'g', 'b', 'y']

if __name__ == "__main__":
    import random as r
    import copy as c
    import time as t
    import matplotlib.pyplot as plt
    MAXIMO = 1000
    TAMANIO = 1000
    CANTIDAD = 500
    tiempos = [[] for i in xrange(4)]
    funciones = [bubble_sort, insertion_sort, selection_sort, quick_sort]

    for no_experimento in xrange(CANTIDAD):
        original = [r.randint(0, MAXIMO) for i in xrange(TAMANIO)]
        for i in xrange(4):
            lista = c.copy(original)
            start = t.time()
            funciones[i](lista)
            end = t.time()
            tiempos[i].append(end - start)
    plt.ioff()
    plt.figure("Histogramas cumulativos")
    plt.suptitle(u'Distribuciones de tiempos de ejecución')
    for i in xrange(4):
        plt.hist(tiempos[i], cumulative=True, normed=True,
                 histtype='step', color=colores[i], label=algos[i])
    plt.legend(loc='lower center', shadow=True, fontsize='large')

    plt.figure("Boxplots")
    plt.suptitle(u'Distribuciones de tiempos de ejecución')
    plt.boxplot(tiempos, labels=algos)

    plt.ion()
    plt.show()
    plt.ginput()
