# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 10:17:55 2016

@author: karol
"""

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from quick_sort import quick_sort

algos = ['Bubble', 'Insertion', 'Selection', 'Quick']
colores = ['r', 'g', 'b', 'y']

if __name__ == "__main__":
    import random as r
    import copy as c
    import time as t
    import matplotlib.pyplot as plt
    TAMANIO = 1000
    MAXIMO = 1000
    tiempos = [[] for i in xrange(4)]
    tamanios = range(1, MAXIMO)
    funciones = [bubble_sort, insertion_sort, selection_sort, quick_sort]

    for tamanio in tamanios:
        original = [r.randint(0, MAXIMO) for i in xrange(TAMANIO)]
        for i in xrange(4):
            lista = c.copy(original)
            start = t.time()
            funciones[i](lista)
            end = t.time()
            tiempos[i].append(end - start)

    plt.ioff()
    plt.xkcd()
    for i in xrange(4):
        plt.plot(tamanios, tiempos[i], linestyle='-',
                 color=colores[i], aa=True, label=algos[i])
    plt.title('Tiempos de ejecucion')
    plt.legend(loc='upper left', shadow=True, fontsize='large')
    plt.ion()
    plt.show()
    plt.ginput()
    plt.rcdefaults()
