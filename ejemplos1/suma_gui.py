# -*- coding: utf-8 -*-
from easygui import enterbox, ynbox

suma = 0.0
mas_numeros = True
while (mas_numeros):
    numero = enterbox(msg='Ingresa un numero', title='Numero')
    suma += float(numero)
    mensaje = "La suma de los numeros ingresados es {}. "\
        "Quieres sumar mas numeros?".format(suma)
    mas_numeros = ynbox(msg=mensaje, title="Continuar?", choices=('Si', 'No'))
