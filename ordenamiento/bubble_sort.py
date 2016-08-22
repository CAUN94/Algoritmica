# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 10:17:55 2016

@author: karol
"""


def bubble_sort(A):
    seguir = True
    largo = len(A)
    while (seguir):
        seguir = False
        for i in xrange(largo - 1):
            if (A[i] > A[i+1]):
                A[i], A[i+1] = A[i+1], A[i]
                seguir = True


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
    bubble_sort(lista)
    end = t.time()

    print("Ordenada: ", lista)
    print("Tiempo: ", (end - start))
