# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 10:17:55 2016

@author: karol
"""
from numba import jit


@jit
def bubble_sort(A):
    """
    bubble_sort ordena de forma creciente los elementos del arreglo A entregado
    como argumento. Se modifica directamente el arreglo entregado.
    """
    seguir = True
    largo = len(A)
    while seguir:
        seguir = False
        for i in xrange(largo - 1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                seguir = True

if __name__ == "__main__":
    import random as r
    import copy as c
    import time as t

    MAXIMO = 1000
    CANTIDAD = 1000
    lista = [r.randint(0, MAXIMO) for i in xrange(CANTIDAD)]
    # lista = np.random.random_integers(0, MAXIMO, CANTIDAD)
    print(type(lista))

#    n_bubble_sort = autojit(bubble_sort)
#    original = c.copy(lista)
#    print(type(original))
#    print("Original: ", original)

    start = t.time()
    bubble_sort(lista)
    # lista.sort()
    end = t.time()

    print("Ordenada: ", lista)
    print("Tiempo: ", (end - start))
