import random

import niveles
import unruly

from typing import List, Tuple, Any

Grilla = Any

def grillas_con_guiones_bajo(grilla:Grilla):
    """Modifica la grilla, colocando el valor '_' en las posiciones de la 
    grilla donde hay ' '."""
    grilla_a_modificar = unruly.crear_grilla(grilla)
    for fil in range(len(grilla)):
        for col in range(len(grilla[0])):
            if unruly.posicion_es_vacia(grilla, col, fil):
                grilla_a_modificar[fil][col] = "_"
    return grilla_a_modificar

def imprimir_grilla(grilla: Grilla):
    """Recibe una grilla por parametro. Es la grilla que se le muestra al usuario, agrega el 
    numero de filas para que el usuario se guie."""
    grilla_a_imprimir = grillas_con_guiones_bajo(grilla)
    juego = "---oh hi---"
    print(juego)
    print(" ",end="")

    # Imprime el numero de columna
    for numero_columna in range(len(grilla_a_imprimir[0])):
        print(" | ",end="")
        print(numero_columna,end="")
    # Cuando termina de hace un salto de linea
    print("")

    for col in range(len(grilla_a_imprimir[0])):
        for fil in range(len(grilla_a_imprimir)):
            # Muestra el numero de fila
            if fil == 0:
                print(col,end="")
                print(" | ",end="")
                # Muestra la primera columna de la grilla
                print(" ".join(grilla_a_imprimir[col][fil]),"  ",end="")

            else:
                # Muestra el resto de la grilla
                print(" ".join(grilla_a_imprimir[col][fil]),"  ",end="")
        # Cuando termina la fila hace un salto de linea
        print("")

def cambiar_valores(grilla: Grilla, columna: int, fila: int, valor: str):
    """Recibe por parametro una grilla y dependiendo el valor, la modifica
    y la devuelve."""
    if valor == "1":
        grilla_nueva = unruly.cambiar_a_uno(grilla, columna, fila)
    elif valor == "0":
        grilla_nueva = unruly.cambiar_a_cero(grilla, columna, fila)
    elif valor == " ":
        grilla_nueva = unruly.cambiar_a_vacio(grilla, columna, fila)
    return grilla_nueva

def chequeos_de_datos(lista: list, primer_numero: int, segundo_numero: int) -> bool:
    """Recibe por parametro una lista y dos numeros y chequea que tenga 3 elementos,
    que el primer y segundo elemento sean numeros positivos y que no sean mayores al 
    primer_numero y al segundo_numero respectivamente."""
    if len(lista) == 3:
        if not lista[0].isdigit() or not lista[1].isdigit():
            return False
        else: 
            if (int(lista[0]) >= 0 and int(lista[0]) < primer_numero) and (int(lista[1]) >= 0 and int(lista[1]) < segundo_numero):
                return True
    return False

def main():
    nivel = random.choice(niveles.NIVELES)
    grilla = unruly.crear_grilla(nivel)

    filas,columnas = unruly.dimensiones(grilla)
    imprimir_grilla(grilla)
    print(" Entrada: [columna,fila,valor]", "\n", "Para salir: o")
    while True:

        datos_del_usuario = str(input("Entrada: "))
        if datos_del_usuario == "o":
            return
        else:
            lista_de_datos = datos_del_usuario.split(",")

            #Chequea que la lista este bien
            if chequeos_de_datos(lista_de_datos, columnas, filas):
                columna = int(lista_de_datos[0])
                fila = int(lista_de_datos[1])
                valor = lista_de_datos[2]
            
                #Cambia la grilla
                if valor == "1" or valor == "0" or valor == " ":
                    grilla = cambiar_valores(grilla, columna, fila, valor)
                    imprimir_grilla(grilla)

                    #Si la grilla esta ganada sale del ciclo
                    if unruly.grilla_terminada(grilla):
                        break

                    #Si no esta ganada pide el reingreso de los datos
                    else:
                        print(" Entrada: [columna,fila,valor]", "\n", "Para salir: o")

        #Si la condicion de grilla_terminada no se cumple vuelve al inico
        continue
    print("Ganaste. :D")            
            
            

main()