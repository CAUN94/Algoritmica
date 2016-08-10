# -*- coding: utf-8 -*-
import sys

productos = set()
cantidades = dict()
costos = dict()

try:
    try:
        entrada = open("transacciones.txt", "r")
    except IOError:
        raise ValueError("No se pudo abrir el archivo para leer")

    try:
        for linea in entrada:
            campos = linea.split()
            if campos[0] in productos:
                cantidades[campos[0]] += float(campos[1])
                costos[campos[0]] += float(campos[1]) * float(campos[2])
            else:
                productos.add(campos[0])
                cantidades[campos[0]] = float(campos[1])
                costos[campos[0]] = float(campos[1]) * float(campos[2])
    except IndexError:
        raise ValueError(
            "Una linea del archivo de entrada no tiene numero de elementos"
            " adecuado (3)"
        )
    except ValueError:
        raise ValueError("Uno de los valores no es un numero")
    finally:
        entrada.close()

    try:
        salida = open("agregados.txt", "w")
        for producto in productos:
            linea = "{:<16}{:5.1f}{:8.2f}\n"\
                .format(producto, cantidades[producto], costos[producto])
            salida.write(linea)
        salida.close()
    except IOError:
        raise ValueError("No se pudo escribir el archivo de resultados")

except ValueError as e:
    print(e.message)
