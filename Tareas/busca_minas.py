# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 17:55:41 2016

@author: Cristobal Ugarte y Paulina Montesinos
"""

from random import randrange

def contar_minas(cord_x,cord_y):
    suma=0
    for x in range (cord_x-1,cord_x+2):
        for y in range(cord_y-1,cord_y+2):
            if x>=0 and x<=length-1  and y>=0  and y<=length-1:
                if matriz_no_visible[x][y]=="M":
                    suma = suma+1
    return suma
    

def show_matriz(matriz):
    for array in matriz:
        for value in array:
            print value,"  ",
        print "\n"

length = input ("Ingresa el largo del tablero: ")
cant = input ("Ingresa la cantidad de minas en el juego: ")


matriz_no_visible = []
for x in range (length):
    array=[]
    for y in range (length):
        array.append(0)
    matriz_no_visible.append(array)
    
matriz_visible = []
for x in range (length):
    array=[]
    for y in range (length):
        array.append('#')
    matriz_visible.append(array)
    
minas=0

while minas!=cant:
    x_random=randrange(0,length)
    y_random=randrange(0,length)
    if matriz_no_visible[x_random][y_random]!="M":
        matriz_no_visible[x_random][y_random]="M"
        minas=minas+1




for x in range (length):
    for y in range (length):
        mina=contar_minas(x,y)
        if matriz_no_visible[x][y]!= "M":
            matriz_no_visible[x][y]=mina

encontradas=0
while encontradas!=cant:
    show_matriz(matriz_visible)
    print("\n")
    alternativa=input("Escribe 0 si quieres indicar donde esta una Mina o 1 si quieres seleccionar una coordenada: ")
    if alternativa == 0:
        res_y= input("Elige una coordenada x del tablero: ")-1
        res_x= input("Elige una coordenada y del tablero: ")-1
        
        if matriz_no_visible[res_x][res_y]== "M":
            encontradas=encontradas+1

        matriz_visible[res_x][res_y]= "@"
        
    elif alternativa == 1:
        res_y= input("Elige una coordenada x del tablero: ")-1
        res_x= input("Elige una coordenada y del tablero: ")-1
        
        if matriz_no_visible[res_x][res_y]== 0 :  
            for x in range (res_x-1,res_x+2):
                for y in range(res_y-1,res_y+2):
                    if x>=0 and x<=length-1  and y>=0  and y<=length-1:
                        matriz_visible[x][y]=matriz_no_visible[x][y]

        elif matriz_no_visible[res_x][res_y]!="M":
            matriz_visible[res_x][res_y]=matriz_no_visible[res_x][res_y]

        elif matriz_no_visible[res_x][res_y]=="M":
            matriz_visible[res_x][res_y]=matriz_no_visible[res_x][res_y]
            print("Perdiste\n")
            show_matriz(matriz_no_visible)
            print ("\n")
            break
        
            
        
print("\n Ganaste")
show_matriz(matriz_no_visible)
        
        
    