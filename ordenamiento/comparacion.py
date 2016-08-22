# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 10:17:55 2016

@author: karol
"""

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from quick_sort import quick_sort

algos = ["Bubble sort", "Insertion sort", "Selection sort", "Quick sort"]

if __name__ == "__main__":
    import random as r
    import copy as c
    import time as t
    maximo = 1000
    cantidad = 1000
    funciones = [bubble_sort, insertion_sort, selection_sort, quick_sort]
    original = [r.randint(0, maximo) for i in xrange(cantidad)]

    for i in xrange(4):
        lista = c.copy(original)
        start = t.time()
        funciones[i](lista)
        end = t.time()
        print(algos[i])
        print("Tiempo: {:.4f}".format(end - start))
