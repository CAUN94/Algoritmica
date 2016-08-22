# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 19:17:55 2016

@author: Cristóbal
"""

import random      
import time as t

nr_arrays=100       #nr de arrays a generar
cant_numbers=1000   #cantidad de numeros en los arrays
maximo=100          #el maximo numero que alcanza cada array
array_arrays=[]     #array vacio

def random_list(x): #metodo que crear los arrays
    array=[]
    for i in range(x):
        array.append(random.randrange(1,maximo+1,1))
    
    return array
    
def bubble_sort(A): #bubble sort
    seguir = True
    largo = len(A)
    while (seguir):
        seguir = False
        for i in xrange(largo - 1):
            if (A[i] > A[i+1]):
                A[i], A[i+1] = A[i+1], A[i]
                seguir = True
                
    return A
    

def insertion_sort(A):#insertion sort
    largo = len(A)
    for posicion in xrange(1, largo):
        posAct = posicion
        while posAct > 0 and A[posAct - 1] > A[posAct]:
            A[posAct - 1], A[posAct] = A[posAct], A[posAct - 1]
            posAct -= 1
    
    return A


def quicksort(A, lo, hi):#quick sort
    if lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p)
        quicksort(A, p+1, hi)


def partition(A, lo, hi):#partition
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


def quick_sort(A):#quick sort
    quicksort(A, 0, len(A)-1)
    
    return A
    


def selection_sort(A):#selection sort
    largo = len(A)
    for posicion in xrange(largo):
        posMin = posicion
        for posComp in xrange(posicion+1, largo):
            if (A[posComp] < A[posMin]):
                posMin = posComp
        if (posMin != posicion):
            A[posMin], A[posicion] = A[posicion], A[posMin]
    
    return A

#  ciclo que crea nr_arrays arreglos con cant_numbers cantidad de numeros,
#  cada arreglo se almacena en array_arrays
            
for i in range(nr_arrays):
    array = random_list(cant_numbers)
    array_arrays.append(array)
  

bubble_time=[] # arreglo donde se almacena los tiempos de bubble sort
selection_time=[]# arreglo donde se almacena los tiempos de selection sort
quick_time=[]   # arreglo donde se almacena los tiempos de quick sort
insertion_time=[]# arreglo donde se almacena los tiempos de insertion sort

# ciclo donse se recorre todos los arreglos 
for j in range(nr_arrays):

    
    lista = array_arrays[j]   #arreglo actual 
    print("Array Nr:",j+1)    #print del arreglo actual
    
    print("");
    
    start = t.time()
    A= bubble_sort(lista)
    end = t.time()
    print("Tiempo Bubble Sort: ",end-start )

    
    time=end-start
    bubble_time.append(time)    
    
    print("Tiempo Insertion Sort: ",end-start )
    
    time=end-start
    insertion_time.append(time)      
    
    start = t.time()
    A= selection_sort(lista)
    end = t.time()
    print("Tiempo Selection Sort: ",end-start )
    
    time=end-start
    selection_time.append(time)      
    
    start = t.time()
    A= quick_sort(lista)
    end = t.time()
    print("Tiempo Quick Sort: ",end-start )
    
    time=end-start
    quick_time.append(time)      
    
    minimo = min(lista)
    print("Minimo Valor ",minimo)
    maximo = max (lista)
    print("Maximo Valor",maximo)
    promedio= sum(lista)/len(lista)
    print ("Promedio: ",promedio)
    
    print("")
    
    
    
    print("----------------------------------------------------")

print("")
print("Estadisticas de todos los algoritmos")
print("----------------------------------------------------")

print("Estadisticas Bubble Sort")
promedio = sum(bubble_time)/len(bubble_time)
print("Promedio: ",promedio)
minimo = min(bubble_time)
print("Minimo: ",minimo)
maximo = max(bubble_time)
print("Maximo: ",maximo)

print("----------------------------------------------------")

print("Estadisticas Insertion Sort")
promedio = sum(insertion_time)/len(insertion_time)
print("Promedio: ",promedio)
minimo = min(insertion_time)
print("Minimo: ",minimo)
maximo = max(insertion_time)
print("Maximo: ",maximo)

print("----------------------------------------------------")



print("Estadisticas Selection Sort")
promedio = sum(selection_time)/len(selection_time)
print("Promedio: ",promedio)
minimo = min(selection_time)
print("Minimo: ",minimo)
maximo = max(selection_time)
print("Maximo: ",maximo)

print("----------------------------------------------------")

print("Estadisticas Quick Sort")
promedio = sum(quick_time)/len(quick_time)
print("Promedio: ",promedio)
minimo = min(quick_time)
print("Minimo: ",minimo)
maximo = max(quick_time)
print("Maximo: ",maximo)

print("----------------------------------------------------")
print("----------------------------------------------------")
print("Hecho por Cristobal Ugarte")



