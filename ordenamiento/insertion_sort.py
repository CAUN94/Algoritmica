# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 10:17:55 2016

@author: karol
"""


def insertion_sort(A):
    largo = len(A)
    for posicion in xrange(1, largo):
        posAct = posicion
        while posAct > 0 and A[posAct - 1] > A[posAct]:
            A[posAct - 1], A[posAct] = A[posAct], A[posAct - 1]
            posAct -= 1

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
    insertion_sort(lista)
    end = t.time()

    print("Ordenada: ", lista)
    print("Tiempo: ", (end - start))
