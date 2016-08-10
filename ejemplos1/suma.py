# -*- coding: utf-8 -*-
entrada = open("numeros1.txt", "r")
suma = 0.0
for linea in entrada:
    valor = float(linea)
    suma += valor
entrada.close()

salida = open("suma.txt", "w")
linea = "{:.2f}\n".format(suma)
salida.write(linea)
salida.close()
