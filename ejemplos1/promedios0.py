# -*- coding: utf-8 -*-
numeros2 = [
    [5.5, 3.4, 3.9, 4.8],
    [6, 5.7, 5.1],
    [2.3, 3.7, 4.8, 5.4],
    [3.9, 4.2, 4, 4.8, 4.4]
]
promedios = []
for notas in numeros2:
    promedio = sum(notas)/len(notas)
    promedios.append(promedio)
print(promedios)
