# -*- coding: utf-8 -*-
entrada = open("numeros2.txt", "r")
promedios = []
for linea in entrada:
    valores = linea.split()
    valores_float = [float(valor) for valor in valores]
    promedio = sum(valores_float)/len(valores_float)
    promedios.append(promedio)
entrada.close()

salida = open("promedios.txt", "w")
for promedio in promedios:
    linea = "{:.2f}\n".format(promedio)
    salida.write(linea)
salida.close()
