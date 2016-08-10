# -*- coding: utf-8 -*-
productos = {"bread", "tomatoes", "milk", "coffee", "bread"}
precios_lista = {
    "bread": 1.39, "tomatoes": 0.26, "milk": 1.45,
    "coffee": 2.99, "bread": 1.39
}
transacciones = [
    {"producto": "bread", "cantidad": 1, "precio": 1.39},
    {"producto": "tomatoes", "cantidad": 6, "precio": 0.26},
    {"producto": "milk", "cantidad": 3, "precio": 1.45},
    {"producto": "coffee", "cantidad": 3, "precio": 2.49},
    {"producto": "tomatoes", "cantidad": 4, "precio": 0.26},
    {"producto": "bread", "cantidad": 5, "precio": 1.39}
]

venta_maxima = 0
venta_producto = ""
venta_precio = 0
venta_cantidad = 0
venta_minima = 100000000;


for transaccion in transacciones:
    valor = transaccion["cantidad"] * transaccion["precio"]
    if valor < venta_minima:
        venta_minima = valor
        venta_producto = transaccion["producto"]
        venta_precio = transaccion["precio"]
        venta_cantidad = transaccion["cantidad"]
        venta_descuento = 100 - 100*venta_precio/precios_lista[venta_producto]

print("El valor mas bajo de una transaccion fue {} {}.".format(venta_minima))
print(
    "Se realizo para el producto {}, por cantidad {}, a precio {}."
    .format(venta_producto, venta_cantidad, venta_precio)
)
print("Se aplico un descuento de {:.0f}%.".format(venta_descuento))
