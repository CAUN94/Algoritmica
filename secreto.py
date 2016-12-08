# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 08:27:45 2016

@author: karol
"""

import random as r

MAX_NUM = 1000000
MAX_INT = 100000
secreto = r.randint(1, MAX_NUM)

number=MAX_NUM/2 #Numero que se elige al preguntar

def solver(number,state,intento): #metodo que decide el siguiente numero

    numero= 1+round(500/2**(intento)) #numero a restar o sumar al numero actual
    if state == "menor": 
        
        number=number-numero

     
    elif state == "mayor":
         number=number+numero  
    
    return number


print(u'¡Bienvenido al Número Secreto!')
print(u'Adivina un número entre 1 y {}. Tienes {} intentos.'
      .format(MAX_NUM, MAX_INT))

encontrado = False
no_intentos = 0

while not encontrado and no_intentos < MAX_INT:
    no_intentos += 1
    print ("Responde: {}".format(number))
    print ("Turno:{}".format(no_intentos))
    num = number

    if num == secreto:
        encontrado = True
    elif num > secreto:
        print(u'El número secreto es menor')
        number=solver(number,"menor",no_intentos)
    else:
        print(u'El número secreto es mayor')
        number=solver(number,"mayor",no_intentos)
        
        

if encontrado:
    print(u'¡Felicitaciones!')
else:
    print(u'Lo siento. ¡Intenta otra vez!')
