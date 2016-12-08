# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt


from matplotlib.colors import ListedColormap


N = 10
reinas = []
opciones = ['Limpiar', 'Agregar reina', 'Eliminar reina']
columnas = [chr(i) for i in range(ord('A'), ord('A')+N)]
filas = [str(i) for i in range(1, N+1)]
colores = ['Ivory', 'Wheat', 'Gold', 'FireBrick']
solver = []
inicio = []

print ("")

def maneja_reinas(reinas, acc, fil, col):
    conflicto = False
    victoria = False

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
            conflicto = True
            tablero[x][y] = 4
        else:
            tablero[x][y] = 3

    # verificar la condicion de exito
    if not conflicto and len(reinas) == N:
        victoria = True
   
    return victoria, tablero


def prepara_imagen(tablero, ax):
    img = ax.matshow(tablero, extent=(0, N, 0, N), origin='lower',
                     vmin=1, vmax=4, interpolation='none', aspect=1,
                     cmap=ListedColormap(colores, 'indexed'))

    ax.xaxis.tick_bottom()

    ax.xaxis.set_ticks(range(0, N), minor=False)
    ax.xaxis.set_ticklabels([], minor=False)
    ax.xaxis.set_ticks([0.5+i for i in xrange(0, N)], minor=True)
    ax.xaxis.set_ticklabels(columnas, minor=True)

    ax.yaxis.set_ticks(range(0, N), minor=False)
    ax.yaxis.set_ticklabels([], minor=False)
    ax.yaxis.set_ticks([0.5+i for i in xrange(0, N)], minor=True)
    ax.yaxis.set_ticklabels(filas, minor=True)

    ax.tick_params(axis='both', which='both', length=0)
    ax.grid(color='Gold', linestyle='-', linewidth=1)
    for spine in ax.spines.values():
        spine.set_edgecolor('Gold')
        spine.set_linewidth(3)

    return img


def onclose(event):
    global fin
    fig.canvas.stop_event_loop()
    plt.close()
    fin = True
    

def solver(N):
    
   

        
        for i in range(N):
            for j in range(N):
                vic, tab = maneja_reinas(reinas, 'Agregar reina', i, j)
                img_reinas.set_data(tab)
                plt.draw()
                if vic:
                    fig.text(
                        0.5, 0.5, 'Felicitaciones!', color='orange', size='xx-large',
                        family='humor sans', ha='center', va='center', alpha=0.5,
                        bbox=dict(facecolor='ivory', edgecolor='orange', boxstyle='round')
                    )
                    plt.draw()
                    plt.ginput()  
                   
                if  tab[i][j]==4:
               
                    if i in range(N) and j in range(N):
                        vic, tab = maneja_reinas(reinas, 'Agregar reina', i, j)
                        

      


                
            
        
                

        
    
    


if __name__ == "__main__":
    plt.ioff()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    fig.canvas.mpl_connect('close_event', onclose)

    (f, c) = ('', '')
    fin, tab = maneja_reinas(reinas, 'Limpiar', f, c)
    img_reinas = prepara_imagen(tab, ax)
    plt.draw()

    fin = False
    vic = False
   
    while not fin and not vic:
        
        
        solver(N)


 
