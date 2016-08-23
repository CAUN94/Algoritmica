# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 10:17:55 2016

@author: karol
"""

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from quick_sort import quick_sort

from n_bubble_sort import n_bubble_sort
from n_insertion_sort import n_insertion_sort
from n_selection_sort import n_selection_sort
from n_quick_sort import n_quick_sort

import numpy as np

algos = [
    "Bubble sort", "Insertion sort", "Selection sort", "Quick sort",
    "N. Bubble sort", "N. Insertion sort", "N. Selection sort",
    "N. Quick sort", "NumPy sort"
]


def numpy_sort(A):
    A = np.array(A)
    A.sort()


if __name__ == "__main__":
    import random as r
    import copy as c
    import time as t
    maximo = 1000
    cantidad = 10000
    funciones = [
        bubble_sort, insertion_sort, selection_sort, quick_sort,
        n_bubble_sort, n_insertion_sort, n_selection_sort, n_quick_sort,
        numpy_sort
    ]
    original = [r.randint(0, maximo) for i in xrange(cantidad)]
    # original = np.random.randint(0, maximo, cantidad)
    for i in xrange(9):
        lista = c.copy(original)
        start = t.time()
        funciones[i](lista)
        end = t.time()
        print(algos[i])
        print("Tiempo: {:.4f}".format(end - start))
