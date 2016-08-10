# -*- coding: utf-8 -*-
ventas = []

entrada = open("agregados.txt", "r")
for linea in entrada:
    (producto, cantidad, valor) = linea.split()
    ventas.append({
        "producto": producto, "cantidad": float(cantidad),
        "valor": float(valor)
    })
entrada.close()

ventas_por_cantidad = sorted(
    ventas, key=(lambda x: x["cantidad"]), reverse=True
)

salida = open("agregados_por_cantidad.txt", "w")
for venta in ventas_por_cantidad:
    linea = "{:<16}{:5.1f}{:8.2f}\n"\
        .format(venta["producto"], venta["cantidad"], venta["valor"])
    salida.write(linea)
salida.close()

ventas_por_valor = sorted(ventas, key=(lambda x: x["valor"]), reverse=True)

salida = open("agregados_por_valor.txt", "w")
for venta in ventas_por_valor:
    linea = "{:<16}{:5.1f}{:8.2f}\n"\
        .format(venta["producto"], venta["cantidad"], venta["valor"])
    salida.write(linea)
salida.close()
