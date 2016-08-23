# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 08:27:45 2016

@author: karol
"""

import random as r

MAX_NUM = 1000
MAX_INT = 10
secreto = r.randint(1, MAX_NUM)


print(u'¡Bienvenido al Número Secreto!')
print(u'Adivina un número entre 1 y {}. Tienes {} intentos.'
      .format(MAX_NUM, MAX_INT))

encontrado = False
no_intentos = 0

while not encontrado and no_intentos < MAX_INT:
    no_intentos += 1
    num = input('Tu intento número {}: '.format(no_intentos))

    if num == secreto:
        encontrado = True
    elif num > secreto:
        print(u'El número secreto es menor')
    else:
        print(u'El número secreto es mayor')

if encontrado:
    print(u'¡Felicitaciones!')
else:
    print(u'Lo siento. ¡Intenta otra vez!')
