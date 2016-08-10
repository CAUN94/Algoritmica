# -*- coding: utf-8 -*-
productos = set()
cantidades = dict()
costos = dict()

entrada = open("transacciones.txt", "r")
for linea in entrada:
    (producto, cantidad, precio_unitario) = linea.split()
    if producto in productos:
        cantidades[producto] += float(cantidad)
        costos[producto] += float(cantidad) * float(precio_unitario)
    else:
        productos.add(producto)
        cantidades[producto] = float(cantidad)
        costos[producto] = float(cantidad) * float(precio_unitario)
entrada.close()

salida = open("agregados.txt", "w")
for producto in productos:
    linea = "{:<16}{:5.1f}{:8.2f}\n"\
        .format(producto, cantidades[producto], costos[producto])
    salida.write(linea)
salida.close()
