from typing import List, Tuple, Any

import gamelib

ANCHO_VENTANA = 300
ALTO_VENTANA = 360

Grilla = Any

def juego_crear() -> Grilla:
    """Inicializar el estado del juego"""
    grilla = []
    for f in range(0,10):
        lista_vacia = []
        for c in range(0,12):
            lista_vacia.append(" ")
        grilla.append(lista_vacia)
    return grilla

def turno(grilla: Grilla) -> bool:
    """Recibe por parametro el juego, y si hay menos cantidad O que de X en el tablero,
    devuelve True, caso contrario devuelve False"""
    contador_de_X = 0
    contador_de_O = 0
    for f in range(len(grilla)):
        for c in range(len(grilla[0])):
            if grilla[f][c] == "X":
                contador_de_X += 1
            if grilla[f][c] == "O":
                contador_de_O += 1
    if contador_de_O <= contador_de_X:
        return False
    else:
        return True

def pixeles_a_tabla(pixeles_en_x: int,pixeles_en_y: int) -> int:
    """Recibe el numero de pixeles y devuelve la coordenadas en el tablero"""
    ancho_celda = int(((pixeles_en_x/ANCHO_VENTANA)*10))
    alto_celda = int(((pixeles_en_y/ALTO_VENTANA)*12))
    tupla = (ancho_celda,alto_celda)
    return tupla

def tabla_a_pixeles(ancho_celda: int, alto_celda: int) -> Tuple[int]:
    """Recibe la posicion de la tabla y la convierte a pixeles"""
    pixeles_en_x = int(((ancho_celda*ANCHO_VENTANA)/10))
    pixeles_en_y = int(((alto_celda*ALTO_VENTANA)/12))
    tupla_de_pixeles = (pixeles_en_x,pixeles_en_y)
    return tupla_de_pixeles

def juego_actualizar(grilla: Grilla, x: int, y: int) -> Grilla:
    """Actualizar el estado del juego

    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """
    coordenadas_x,coordenadas_y = pixeles_a_tabla(x,y)
    if coordenadas_y == 11 or coordenadas_y == 0:
        return grilla
    elif grilla[coordenadas_x][coordenadas_y] == "O" or grilla[coordenadas_x][coordenadas_y] == "X":
        return grilla
    else:
        if turno(grilla) == False:
            grilla[coordenadas_x][coordenadas_y] = "O"
            return grilla
        elif turno(grilla) == True:
            grilla[coordenadas_x][coordenadas_y] = "X"
            return grilla

def juego_mostrar(grilla: Grilla):
    """Actualizar la ventana"""
    gamelib.draw_text('5 en línea', 150, 15)
    gamelib.draw_line(0,330,300,330)

    #Muestra el tablero
    for y in range(30,330,30):
        for x in range(0,301,30):
            gamelib.draw_line(x,y,x+30,y)
            gamelib.draw_line(x,y,x,y+30)

    #Muestra el turno
    if turno(grilla) == True:
        gamelib.draw_text('Turno: X', 150, 345)
    if turno(grilla) == False:
        gamelib.draw_text('Turno: O', 150, 345)

    #Muestra los casilleros elegidos
    for c in range(len(grilla)):
        for f in range(len(grilla[0])):
            x,y = tabla_a_pixeles(c,f)
            if grilla[c][f] == "O":
                gamelib.draw_text('O', x+15, y+15, fill='red' , size = "23")
            elif grilla[c][f] == "X":
                gamelib.draw_text('X', x+15, y+15, fill='lightblue' , size = "23")

def main():
    juego = juego_crear()

    # Ajustar el tamaño de la ventana
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:
        gamelib.draw_begin()
        juego_mostrar(juego)
        gamelib.draw_end()

        # Terminamos de dibujar la ventana, ahora procesamos los eventos (si el
        # usuario presionó una tecla o un botón del mouse, etc).

        # Esperamos hasta que ocurra un evento
        ev = gamelib.wait()

        if not ev:
            # El usuario cerró la ventana.
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y # averiguamos la posición donde se hizo click
            juego = juego_actualizar(juego, x, y)

gamelib.init(main)