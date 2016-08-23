# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 10:17:55 2016

@author: karol
"""
from numba import jit


@jit(nopython=True, cache=True)
def n_selection_sort(A):
    largo = len(A)
    for posicion in xrange(largo):
        posMin = posicion
        for posComp in xrange(posicion+1, largo):
            if (A[posComp] < A[posMin]):
                posMin = posComp
        if (posMin != posicion):
            A[posMin], A[posicion] = A[posicion], A[posMin]


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
    n_selection_sort(lista)
    end = t.time()

    print("Ordenada: ", lista)
    print("Tiempo: ", (end - start))
