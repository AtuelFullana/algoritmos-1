"""Lógica del juego Unruly"""

from typing import List, Tuple, Any

Grilla = Any

VACIO = " "
NEGRO = "1"
BLANCO = "0"

def crear_grilla(desc: List[str]) -> Grilla:
    """Crea una grilla a partir de la descripción del estado inicial.

    La descripción es una lista de cadenas, cada cadena representa una
    fila y cada caracter una celda. Se puede asumir que la cantidad de las
    filas y columnas son múltiplo de dos. **No** se puede asumir que la
    cantidad de filas y columnas son las mismas.
    Los caracteres pueden ser los siguientes:

    Caracter  Contenido de la celda
    --------  ---------------------
         ' '  Vacío
         '1'  Casillero ocupado por un 1
         '0'  Casillero ocupado por un 0

    Ejemplo:

    >>> crear_grilla([
        '  1 1 ',
        '  1   ',
        ' 1  1 ',
        '  1  0',
    ])
    """
    grilla = desc
    grilla = []
    for i in range(len(desc)):
        fila = list(desc[i])
        grilla.append(fila)
    return grilla

def dimensiones(grilla: Grilla) -> Tuple[int, int]:
    """Devuelve la cantidad de columnas y la cantidad de filas de la grilla
    respectivamente (ancho, alto)"""
    columnas = len(grilla[0])
    filas = len(grilla)
    tupla_dimensiones = (columnas,filas)
    return tupla_dimensiones

def posicion_es_vacia(grilla: Grilla, col: int, fil: int) -> bool:
    """Devuelve un booleano indicando si la posición de la grilla dada por las
    coordenadas `col` y `fil` está vacía"""
    return (grilla[fil][col] == VACIO)

def posicion_hay_uno(grilla: Grilla, col: int, fil: int) -> bool:
    """Devuelve un booleano indicando si la posición de la grilla dada por las
    coordenadas `col` y `fil` está el valor 1"""
    return (grilla[fil][col] == NEGRO)

def posicion_hay_cero(grilla: Grilla, col: int, fil: int) -> bool:
    """Devuelve un booleano indicando si la posición de la grilla dada por las
    coordenadas `col` y `fil` está el valor 0"""
    return (grilla[fil][col] == BLANCO)

def cambiar_a_uno(grilla: Grilla, col: int, fil: int):
    """Modifica la grilla, colocando el valor 1 en la posición de la grilla
    dada por las coordenadas `col` y `fil`"""
    grilla[fil][col] = NEGRO
    return grilla

def cambiar_a_cero(grilla: Grilla, col: int, fil: int):
    """Modifica la grilla, colocando el valor 0 en la posición de la grilla
    dada por las coordenadas `col` y `fil`"""
    grilla[fil][col] = BLANCO
    return grilla

def cambiar_a_vacio(grilla: Grilla, col: int, fil: int):
    """Modifica la grilla, eliminando el valor de la posición de la grilla
    dada por las coordenadas `col` y `fil`"""
    grilla[fil][col] = VACIO
    return grilla

def misma_cant_cero_uno(fila: List[str]) -> bool:
    """Devuelve un booleano indicando si la grilla tiene la misma cantidad de
    cero y unos."""
    ceros = 0
    unos = 0
    for col in range(len(fila)):
        if fila[col] == BLANCO:
            ceros += 1
        if fila[col] == NEGRO:
            unos += 1
    return ceros == unos

def filas_de_columnas(grilla: Grilla) -> List[str]:
    """Crea una grilla nueva, a partir de la ingresada por parametro, en la cual una
    donde las columnas pasan a ser filas y las filas pasan a ser columnas."""
    lista_vacia = []
    for col in range(len(grilla[0])):
        columnas = []
        for fil in range(len(grilla)):
            columnas.append(grilla[fil][col])
        lista_vacia.append(columnas)
    return lista_vacia

def tres_casilleros_consecutivos(fila: List[str]) -> bool:
    """Devuelve un booleano indicando si hay tres casilleros consecutivos iguales."""
    ceros = 0
    unos = 0
    pasos = 0
    for elemento in fila:
        pasos += 1
        if elemento == BLANCO:
            unos = 0
            ceros += 1
        elif elemento == NEGRO:
            ceros = 0
            unos += 1
        if ceros == 3 or  unos == 3:
            return True
        if len(fila) < pasos:
            return False

def secuencia_es_valida(secuencia, fila: int):
    """Devuelve un booleano indicando si la fila de la secuencia denotada por el
    índice `fil` es considerada válida.
    
    Una fila válida cuando se cumplen todas estas condiciones:
        - La fila no tiene vacíos
        - La fila tiene la misma cantidad de unos y ceros
        - La fila no contiene tres casilleros consecutivos del mismo valor"""
    if fila > len(secuencia[0]):
        return False
    elif not misma_cant_cero_uno(secuencia[fila]) or tres_casilleros_consecutivos(secuencia[fila]):
        return False
    else:
        for i in range(len(secuencia[fila])):
            #Itera elemento por elemento de la secuencia
            if posicion_es_vacia(secuencia, i, fila):
                return False
    return True

def fila_es_valida(grilla: Grilla, fil: int) -> bool:
    """Devuelve un booleano indicando si la fila de la grilla denotada por el
    índice `fil` es considerada válida.

    Una fila válida cuando se cumplen todas estas condiciones:
        - La fila no tiene vacíos
        - La fila tiene la misma cantidad de unos y ceros
        - La fila no contiene tres casilleros consecutivos del mismo valor
    """
    return (secuencia_es_valida(grilla, fil))

def columna_es_valida(grilla: Grilla, col: int) -> bool:
    """Devuelve un booleano indicando si la columna de la grilla denotada por
    el índice `col` es considerada válida.

    Una columna válida cuando se cumplen todas estas condiciones:
        - La columna no tiene vacíos
        - La columna tiene la misma cantidad de unos y ceros
        - La columna no contiene tres casilleros consecutivos del mismo valor
    """
    return (secuencia_es_valida(filas_de_columnas(grilla),col))

def grilla_terminada(grilla: Grilla) -> bool:
    """Devuelve un booleano indicando si la grilla se encuentra terminada.

    Una grilla se considera terminada si todas sus filas y columnas son
    válidas."""
    for fil in range(len(grilla)):
        if not fila_es_valida(grilla, fil):
            return False
    for col in range(len(grilla[0])):
        if not columna_es_valida(filas_de_columnas(grilla), fil):
            return False
    return True