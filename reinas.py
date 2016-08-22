# -*- coding: utf-8 -*-
import math as m
import matplotlib.pyplot as plt

N = 4
reinas = []
opciones = ['Limpiar', 'Agregar reina', 'Eliminar reina']
columnas = [chr(i) for i in range(ord('A'), ord('A')+N)]
filas = [str(i) for i in range(1, N+1)]
colores = ['black', 'white', 'grey', 'green', 'red']


def maneja_reinas(reinas, acc, fil, col):
    conflicto = False
    victoria = False

    if fil in filas and col in columnas:
        reina = (filas.index(fil), columnas.index(col))
    elif fil in range(N) and col in range(N):
        reina = (fil, col)

    if acc == 'Limpiar':
        reinas = []
    elif acc == 'Agregar reina':
        if reina not in reinas:
            reinas.append(reina)
        else:
            reinas.remove(reina)
    else:
        if reina in reinas:
            reinas.remove(reina)
        else:
            reinas.append(reina)

    # iniciar el tablero como libre
    tablero = [[1 for i in xrange(N)] for i in xrange(N)]

    # marcar los campos amenazados
    for x, y in reinas:
        for i in range(N):
            if i != y:
                tablero[x][i] = 2
            if i != x:
                tablero[i][y] = 2
        for i in range(-min(x, y), min(N-x, N-y)):
            if i != 0:
                tablero[x+i][y+i] = 2
        for i in range(max(-x, y-N+1), min(N-x, y+1)):
            if i != 0:
                tablero[x+i][y-i] = 2

    # marcar cada reina e informar si es amenazada
    for x, y in reinas:
        if (tablero[x][y] == 2):
            # print 'Reina en ({},{}) es amenazada por otra reina'.format(x, y)
            conflicto = True
            tablero[x][y] = 4
        else:
            tablero[x][y] = 3

    # verificar la condicion de exito
    if not conflicto and len(reinas) == N:
        tablero = [[3 for i in xrange(N)] for i in xrange(N)]
        victoria = True
    return victoria, tablero


def muestra_reinas(tablero, ax):
    ax.matshow(tablero, origin='lower', extent=(0, N, 0, N),
               vmin=1, vmax=4, picker=1)
    ax.xaxis.set_ticks(range(0, N), minor=False)
    ax.xaxis.set_ticks([0.5+i for i in xrange(0, N)], minor=True)
    ax.xaxis.set_ticklabels(columnas, minor=True)
    ax.xaxis.set_ticklabels([], minor=False)
    ax.xaxis.tick_bottom()
    ax.yaxis.set_ticks(range(0, N), minor=False)
    ax.yaxis.set_ticks([0.5+i for i in xrange(0, N)], minor=True)
    ax.yaxis.set_ticklabels(filas, minor=True)
    ax.yaxis.set_ticklabels([], minor=False)
    plt.grid(color='y', linestyle='-', linewidth=1)
    plt.draw()


def onclose(event):
    global fin
    fig.canvas.stop_event_loop()
    plt.close()
    fin = True


if __name__ == "__main__":
    plt.ioff()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    fig.canvas.mpl_connect('close_event', onclose)

    (f, c) = ('', '')
    fin, tab = maneja_reinas(reinas, 'Limpiar', f, c)
    muestra_reinas(tab, ax)

    fin = False
    while not fin:
        res = plt.ginput()
        if len(res) == 1:
            (f, c) = (int(m.floor(res[0][1])), int(m.floor(res[0][0])))
            if f in range(N) and c in range(N):
                fin, tab = maneja_reinas(reinas, 'Agregar reina', f, c)
                muestra_reinas(tab, ax)
