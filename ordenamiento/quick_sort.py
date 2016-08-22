# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 10:17:55 2016

@author: karol
"""


def quicksort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p)
        quicksort(A, p+1, hi)
        
    


def partition(A, lo, hi):
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


def quick_sort(A):
    quicksort(A, 0, len(A)-1)

    

if __name__ == "__main__":
    import random as r
    import copy as c
    import time as t
    maximo = 10
    cantidad = 10
    lista = [r.randint(0, maximo) for i in xrange(cantidad)]
    original = c.copy(lista)
    print("Original: ", original)

    start = t.time()
    A= quick_sort(lista)
    end = t.time()

    print("Ordenada: ", A)
    print("Tiempo: ", (end - start))
