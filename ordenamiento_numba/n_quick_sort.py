# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 10:17:55 2016

@author: karol
"""
from numba import jit


@jit(nopython=True, cache=True)
def n_quicksort(A, lo, hi):
    if lo < hi:
        p = n_partition(A, lo, hi)
        n_quicksort(A, lo, p)
        n_quicksort(A, p+1, hi)


@jit(nopython=True, cache=True)
def n_partition(A, lo, hi):
    pivot = A[lo]
    i = lo - 1
    j = hi + 1
    while (True):
        i += 1
        while A[i] < pivot:
            i += 1
        j -= 1
        while A[j] > pivot:
            j -= 1
        if i >= j:
            return j
        A[i], A[j] = A[j], A[i]


@jit(nopython=True, cache=True)
def n_quick_sort(A):
    n_quicksort(A, 0, len(A)-1)

if __name__ == "__main__":
    import random as r
    import copy as c
    import time as t
    maximo = 1000
    cantidad = 1000
    lista = [r.randint(0, maximo) for i in xrange(cantidad)]
    original = c.copy(lista)
    print("Original: ", original)

    start = t.time()
    n_quick_sort(lista)
    end = t.time()

    print("Ordenada: ", lista)
    print("Tiempo: ", (end - start))
