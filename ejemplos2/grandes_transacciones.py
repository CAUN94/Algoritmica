# -*- coding: utf-8 -*-
transacciones = []

entrada = open("transacciones.txt", "r")
for linea in entrada:
    (producto, cantidad, valor) = linea.split()
    transacciones.append({
        "producto": producto, "cantidad": float(cantidad),
        "precio": float(valor)
    })
entrada.close()

grandes_transacciones = [
    transaccion for transaccion in transacciones
    if transaccion["cantidad"]*transaccion["precio"] > 5
]

salida = open("grandes_transacciones.txt", "w")
for venta in grandes_transacciones:
    linea = "{:<16}{:5.1f}{:8.2f}\n"\
        .format(venta["producto"], venta["cantidad"], venta["precio"])
    salida.write(linea)
salida.close()
