from typing import List, Tuple, Any

import gamelib

import png

BORDE = 10

ANCHO_VENTANA = 420
ALTO_VENTANA = 490

ANCHO_TABLERO = 400
ALTO_TABLERO = 400

WHITE = '#ffffff'
BLACK = '#000000'
RED = '#ff0000'
GREEN = '#00ff00'
PURPLE = '#ff00ff'
BLUE = '#0000ff'
YELLOW = '#ffff00'
GUARDAR_PPM = 1
CARGAR_PPM = 2
GUARDAR_PNG = 3

def ancho_celda(cantidad_filas: int) -> int:
    '''Recibe la cantidad de filas y devuelve el ancho que tendran.'''
    return (ANCHO_TABLERO // cantidad_filas)

def alto_celda(cantidad_columnas: int) -> int:
    '''Recibe la cantidad de columnas y devuelve el alto que tendran.'''
    return (ALTO_TABLERO // cantidad_columnas)

def pixeles_a_tablero(pixeles_en_x: int,pixeles_en_y: int,ancho_celd: int,alto_celd: int) -> Tuple[int]:
    '''Recibe el numero de pixeles y devuelve las coordenadas de la celda'''
    columna = (pixeles_en_x - BORDE) // ancho_celd
    fila = (pixeles_en_y - BORDE) // alto_celd
    tupla = (columna, fila)
    return tupla

def tablero_a_pixeles(fila: int,columna: int,ancho_celd: int,alto_celd: int) -> Tuple[int]:
    '''Recibe la fila, la columna, el ancho y alto y devuelve una tupla con las coordenadas 
    del centro de la casilla en la ventana'''
    pixeles_en_x = ((fila) * ancho_celd) + ancho_celd // 2 + BORDE
    pixeles_en_y = ((columna) * alto_celd) + alto_celd // 2 + BORDE
    tupla_de_pixeles = (pixeles_en_x,pixeles_en_y)
    return tupla_de_pixeles

def dibujar_tablero(colores: dict,ancho_celd: int,alto_celd: int):
    '''Recibe un diccionario con el color de todas las casillas, el ancho y alto de las casillas y 
    crear el tablero con los colores correspondientes a las casillas'''
    for celda, color in colores.items():
        fila, columna = celda
        cantidad_columnas = ancho_celda(ancho_celd)
        cantidad_filas = alto_celda(alto_celd)
        pixeles_en_x, pixeles_en_y = tablero_a_pixeles(fila, columna,ancho_celd,alto_celd)
        pintar_celda(pixeles_en_x, pixeles_en_y, color,ancho_celd,alto_celd)

def pintar_celda(pixeles_en_x: int, pixeles_en_y: int, color: str,ancho_celd: int,alto_celd: int):
    '''Recibe una posicion, un texto que representa un color en formato hexadecimal,
    el ancho y el alto de la casilla y crea una nueva casilla con el color indicado.'''
    gamelib.draw_rectangle(pixeles_en_x - (ancho_celd // 2),pixeles_en_y - (alto_celd // 2),
                            pixeles_en_x + (ancho_celd // 2), pixeles_en_y + (alto_celd // 2), 
                            fill = color, outline = BLACK)

def diccionario_colores_por_celdas(cantidad_filas: int,cantidad_columnas: int) -> dict:
    '''Recibe la cantidad de filas y la cantidad de columnas y crea un diccionario 
    con todas las casillas y les asigna el color blanco'''
    colores_celdas = {}
    for fila in range(cantidad_filas):
        for columna in range(cantidad_columnas):
            colores_celdas[(columna, fila)] = '#ffffff'
    return colores_celdas

def crear_botones():
    '''Muestra en pantalla los botones'''
    for x in range(67,400,133):
        gamelib.draw_rectangle(x-50, 450, x+50, 470, outline=BLACK, fill=WHITE)
    gamelib.draw_text('1.Guardar PPM', 65, 460,size='10',fill=BLACK)
    gamelib.draw_text('2.Cargar PPM', 200, 460,size='10',fill=BLACK)
    gamelib.draw_text('3.Guardar PNG', 331, 460,size='10',fill=BLACK)

def color_actual(numero,primer_coordenada,segunda_coordenada,color):
    '''Recibe un numero, un color, y dos coordenadas y dibuja un cuadrado con el color pasado por parametro, en la posicion 
    de las coordenadas'''
    ancho_cuadrados = 30
    espacio_entre_botones = 5
    resultado = BORDE + (espacio_entre_botones * numero) + (numero * ancho_cuadrados)
    gamelib.draw_rectangle(resultado - 4, primer_coordenada - 4, resultado + ancho_cuadrados + 4, segunda_coordenada + 4, fill=color, outline='black')

def crear_botones_colores(numero:int=3,color:str=WHITE):
    '''Recibe un numero y un color, si el numero restando 4 se encuentra entre 0 y el 6, llama a la funcion
    color_actual y le pasa el numero, el color y las constantes y1 e y2, despues dibuja los botones de los colores.'''
    y1 = 415
    y2 = 445
    gamelib.draw_rectangle(6, y1-4, 254, y2+4, fill='grey',outline='grey')
    if numero == 0:
        numero = 6
    else:
        numero -= 4
    if numero >= 0 and numero < 7:
        color_actual(numero,y1,y2,color)
    gamelib.draw_rectangle(10, y1, 40, y2, fill=WHITE,outline=WHITE)
    gamelib.draw_text('4',25,430,fill=BLACK)
    gamelib.draw_rectangle(45, y1, 75, y2, fill=BLACK,outline=BLACK)
    gamelib.draw_text('5',60,430,fill=WHITE)
    gamelib.draw_rectangle(80, y1, 110, y2, fill=RED,outline=RED)
    gamelib.draw_text('6',95,430,fill=WHITE)
    gamelib.draw_rectangle(115, y1, 145, y2, fill=GREEN,outline=GREEN)
    gamelib.draw_text('7',130,430,fill=BLACK)
    gamelib.draw_rectangle(150, y1, 180, y2, fill=PURPLE,outline=PURPLE)
    gamelib.draw_text('8',165,430,fill=WHITE)
    gamelib.draw_rectangle(185, y1, 215, y2, fill=BLUE,outline=BLUE)
    gamelib.draw_text('9',200,430,fill=WHITE)
    gamelib.draw_rectangle(220, y1, 250, y2, fill=YELLOW,outline=YELLOW)
    gamelib.draw_text('0',235,430,fill=BLACK)

def paint_mostrar():
    '''dibuja la interfaz de la aplicación en la ventana'''
    gamelib.draw_begin()
    gamelib.draw_rectangle(0, 0, ANCHO_VENTANA, ALTO_VENTANA,fill='grey')
    crear_botones_colores()
    crear_botones()
    gamelib.draw_end()

def convertir_hex_a_decimal(colores: dict) -> dict:
    '''Recibe un diccionario con todas las casillas y sus respectivos colores en hexadecimal y 
    devuelve un diccionario nuevo con todas las casillas y sus respectivos colores en decimal'''
    celdas_colores = {}
    for clave,valor in colores.items():
        valor = str(valor)
        r = str(int(valor[1:3],16))
        g = str(int(valor[3:5],16))
        b = str(int(valor[5:7],16))
        celdas_colores[clave] = r,g,b
    return celdas_colores

def guardar_ppm(ruta: str, colores: dict, cantidad_filas: int, cantidad_columnas: int):
    '''Recibe una ruta, un diccionario de todas las casillas con sus respectivos colores,
    y la cantidad de filas y columna, y crea un archivo ppm'''
    try:
        with open(ruta,'w') as salida:
            salida.write('P3'+'\n')
            salida.write(str(cantidad_filas)+' '+str(cantidad_columnas)+'\n')
            salida.write('255\n')
            nuevos_colores = convertir_hex_a_decimal(colores)
            contador = 0
            for clave,valor in nuevos_colores.items():
                contador += 1
                r,g,b = valor
                if contador == (cantidad_filas):
                    contador = 0
                    salida.write(r+' '+g+' '+b+'\n')
                else:
                    salida.write(r+' '+g+' '+b+'    ')
    except PermissionError:
        gamelib.say('No se tienen los permisos necesarios para acceder a la ubicación seleccionada.')  
    except IOError:
        gamelib.say('No se guardo el archivo.')

                
def cargar_ppm(ruta: str):
    '''Recibe la ruta de un archivo y devuelve un diccionario con todas las casillas y 
    sus respectivos colores, la cantidad de filas y columnas'''
    try:
        with open(ruta) as entrada:
            diccionario = {}
            next(entrada)
            cantidad_filas, cantidad_columnas = entrada.readline().rstrip('\n').split(' ')
            cantidad_filas, cantidad_columnas = int(cantidad_filas), int(cantidad_columnas)
            maximo_color = int(next(entrada).rstrip('\n').split()[0])
            contador = -1
            for linea in entrada:
                lista_de_colores = linea.rstrip('\n').split()
                contador += 1
                color_de_celda = []
                for i in range(cantidad_filas):
                    indice_color = i * 3
                    if indice_color < len(lista_de_colores):
                        componente_color = []
                        for j in range(3):
                            if int(lista_de_colores[indice_color + j]) > maximo_color:
                                raise IOError()
                            componente_color.append(int(lista_de_colores[indice_color + j]))
                        color_de_celda.append(componente_color)
                    else:
                        break
                    for componente_color in color_de_celda:
                        r, g, b = componente_color
                        cadena_color = '#' + f'{r:02x}' + f'{g:02x}' + f'{b:02x}'
                        diccionario[(i, contador)] = cadena_color
            return diccionario,cantidad_filas, cantidad_columnas
    except FileNotFoundError:
        gamelib.say('No se encontro el archivo.')
    except PermissionError:
        gamelib.say('No se tienen los permisos necesarios para acceder a la ubicación seleccionada.')  
    except IOError:
        gamelib.say('No se guardo el archivo.')

def crear_paleta(diccionario: dict) -> List[List[int]]:
    '''Recibe un diccionario con todas las casillas y sus respectivos colores,
    y devuelve una lista de listas con todos los colores que aparecen'''
    lista_paleta = []
    lista_vacia = []
    for clave,valor in diccionario.items():
        for e in valor:
            if len(lista_vacia) != 3:
                lista_vacia.append(int(e))
                if len(lista_vacia) == 3:
                    if lista_vacia not in lista_paleta:
                        lista_paleta.append(lista_vacia)
                        lista_vacia = []
                    else:
                        lista_vacia = []
    return lista_paleta

def lista_en_decimal(colores: dict) -> List[List[int]]:
    '''Recibe un diccionario con todas las casillas y sus respectivos colores,
    y devuelve una lista de listas con todos los colores'''
    lista_decimal = []
    lista_vacia = []
    for clave,valor in colores.items():
        for e in valor:
            if len(lista_vacia) != 3:
                lista_vacia.append(int(e))
                if len(lista_vacia) == 3:
                    lista_decimal.append(lista_vacia)
                    lista_vacia = []
    return lista_decimal

def cambiar_elementos(lista_a_cambiar: List,lista_con_elementos: List,cantidad_filas: int) -> List[List[int]]:
    '''Recibe 2 listas y la cantidad de filas,crea una lista nueva, que contiene listas, donde la cantidad de elementos
    de esta lista depende de la cantidad de filas dadas por parametro, si algun elemento de la primer lista aparece 
    en la segunda,la cambia por la posicion de dicho elemento en la segunda columna'''
    lista_final = []
    lista_vacia = []
    contador = 0
    for x in range(len(lista_a_cambiar)):
        for n in range(len(lista_con_elementos)):
            if lista_a_cambiar[x] == lista_con_elementos[n]:
                lista_vacia.append(n)
                contador += 1
            if cantidad_filas == contador:
                lista_final.append(lista_vacia)
                lista_vacia = []
                contador = 0
    return lista_final

def verifica_formato(nombre: str,extension: str)-> bool:
    '''Recibe un nombre y una extensión y verifica que el nombre tenga esa extensión.'''
    if nombre == '' or nombre == None:
        return False
    if len(nombre.split('.')[1]) == 0:
        return False
    elif len(nombre.split('.')[1]) != 0:
        nombre = nombre.split('.')
        if str(nombre[1]) != extension:
            return False
    return True

def verificar_color_hexadecimal(color: str)-> bool:
    '''Recibe un color hexadecimal y verifica que este bien.'''
    color = color[1:].lower()
    if color != "":
        if len(color) == 6:
            for e in color:
                if e.isdigit() or e in ['abcdef']:
                    return True
    return False

def botones_de_colores(numero: int, color_anterior: str)-> str:
    '''Recibe un numero y un color, cambia la variable color,la devuelve, 
    y llama a la funcion crear_botones_colores'''
    if numero == 4:
        color_nuevo = '#'+str(gamelib.input('Ingresa el color(por defecto:"#rrggbb"):'))
        if color_nuevo == '#None':
            return color_anterior
        if not verificar_color_hexadecimal(color_nuevo):
            pass
    if numero == 5:
        color_nuevo = BLACK
    if numero == 6:
        color_nuevo = RED
    if numero == 7:
        color_nuevo = GREEN
    if numero == 8:
        color_nuevo = PURPLE
    if numero == 9:
        color_nuevo = BLUE
    if numero == 0:
        color_nuevo = YELLOW
    crear_botones_colores(numero,color_nuevo)
    return color_nuevo

def boton_guardar_ppm(colores: dict,ancho:int ,alto:int, nombre_archivo: str):
    '''Recibe los colores, el ancho, el alto y el nombre del archivo ppm, y lo crea.'''
    if nombre_archivo == None:
        return
    if verifica_formato(nombre_archivo,'ppm') == False:
        gamelib.say('Escribir una nombre valido.')
        return
    guardar_ppm(nombre_archivo, colores,ancho_celda(ancho),alto_celda(alto))
    gamelib.say('La imagen se a guardado.')

def boton_cargar_ppm(nombre_archivo: str)-> (dict,int,int):
    '''Recibe el nombre de un archivo y devuelve los colores, la cantidad de filas y columnas de dicho archivo'''
    if nombre_archivo == None:
        return
    if verifica_formato(nombre_archivo,'ppm') == False:
        gamelib.say('Escribir una nombre valido.')
        return
    diccionario_colores, cantidad_filas, cantidad_columnas = cargar_ppm(nombre_archivo)
    ancho_celd = ancho_celda(int(cantidad_filas))
    alto_celd = ancho_celda(int(cantidad_columnas))
    dibujar_tablero(diccionario_colores,ancho_celd,alto_celd)
    return diccionario_colores,ancho_celd,alto_celd

def boton_guardar_png(colores: dict, cantidad_filas: int, nombre: str):
    '''Recibe los colores de las celdas, la cantidad de filas y un nombre 
    y crea un archivo png con dicho nombre.'''
    if nombre == None:
        return
    if verifica_formato(nombre,'png') == False:
        gamelib.say('Escribir una nombre valido.')
        return
    diccionario_colores = convertir_hex_a_decimal(colores)
    paleta = crear_paleta(diccionario_colores)
    imagen = lista_en_decimal(diccionario_colores)
    imagen = cambiar_elementos(imagen, paleta,cantidad_filas)
    png.escribir(nombre, paleta, imagen)

def boton_del_mouse_apretado(pos_x: int, pos_y: int, ancho: int, alto: int, color: str, colores:dict):
    '''Recibe coordenadas en x e y, el ancho y el alto de las celdas, el color actual y un diccionario 
    con los colores de las celdas y modifica el color de la celda, dada por las coordenadas x e y, 
    por el color pasado por parametro.'''
    fila,columna = pixeles_a_tablero(pos_x, pos_y,ancho,alto)
    pixeles_en_x, pixeles_en_y = tablero_a_pixeles(fila, columna,ancho,alto)
    pintar_celda(pixeles_en_x, pixeles_en_y,color,ancho,alto)
    colores[fila, columna] = color

def main():
    gamelib.title('AlgoPaint')
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    ancho_celd = ancho_celda(20)
    alto_celd = alto_celda(20)

    color = WHITE

    paint_mostrar()

    boton_mouse_apretado = False

    #Celdas
    diccionario_colores = diccionario_colores_por_celdas(ancho_celd,alto_celd)
    dibujar_tablero(diccionario_colores,ancho_celd,alto_celd)
        
    while gamelib.loop(fps=15):

        #Eventos
        for ev in gamelib.get_events():
            x, y = ev.x, ev.y

            #Si apreta fuera del tablero no hace nada
            if (x < BORDE or x > (BORDE + ANCHO_TABLERO)-1) or (y < BORDE or y > (BORDE + ALTO_TABLERO)-1):
                continue

            #Si apreta el mouse dentro del tablero pinta la celda
            elif ev.type == gamelib.EventType.ButtonPress and ev.mouse_button == 1:
                boton_mouse_apretado = True
                boton_del_mouse_apretado(x, y,ancho_celd,alto_celd,color,diccionario_colores)

            #Si mantiene apretado el click del mouse dentro del tablero pinta todas las casillas por donde pase
            elif ev.type == gamelib.EventType.Motion:
                if boton_mouse_apretado:
                    boton_del_mouse_apretado(x, y,ancho_celd,alto_celd,color,diccionario_colores)

            #Si suelta el click del mouse deja de pintar
            elif ev.type == gamelib.EventType.ButtonRelease and ev.mouse_button == 1:
                boton_mouse_apretado = False
            
            elif ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
                return

            #Archivos
            elif ev.type == gamelib.EventType.KeyPress:

                try:
                    if ev.key.isnumeric() == False:
                        continue
                    if int(ev.key) == GUARDAR_PPM:
                        nombre_archivo = gamelib.input('Ruta del archivo(por defecto: "imagen.ppm"):')
                        boton_guardar_ppm(diccionario_colores,ancho_celd,alto_celd,nombre_archivo)
                    if int(ev.key) == CARGAR_PPM:
                        ruta = gamelib.input('Ruta del archivo(por defecto: "imagen.ppm"):')
                        if boton_cargar_ppm(ruta) != None:
                            diccionario_colores,ancho_celd,alto_celd = boton_cargar_ppm(ruta)
                    if int(ev.key) == GUARDAR_PNG:
                        ruta = gamelib.input('Ruta del archivo(por defecto: "imagen.png"):')
                        cantidad_filas = ALTO_TABLERO // alto_celd
                        boton_guardar_png(diccionario_colores, cantidad_filas, ruta)
                    
                    #Colores
                    if int(ev.key) >= 4 and int(ev.key) <= 9 or int(ev.key) == 0:
                        color = botones_de_colores(int(ev.key),color)
                        if color == 1:
                            color = WHITE

                except (TypeError,IndexError):
                    gamelib.say('Algo salio mal.')

gamelib.init(main)