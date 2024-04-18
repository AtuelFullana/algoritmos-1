from typing import List
import random

#Ejercicio 1-1
def producto(numero1:float,numero2:float)->float:
    """Recibe por parametro dos numeros y devuelve su producto"""
    print (numero1 * numero2)
    return numero1 * numero2

#Ejercicio 1-2
def main():
    n1 = int(input("Ingrese el primer numero: "))
    n2 = int(input("Ingrese el segundo numero: "))
    return producto(n1,n2)

#Ejercicio 1-3
def perimetro_rectangulo(base,altura):
    return base * 2 + altura * 2

def area_rectangulo(base,altura):
    print(base * altura)
    return base * altura

#Ejercicio 1-5
def factorial(numero):
    resultado = 1
    for i in range(1,numero):
        resultado += i * (resultado)
    return resultado

#Ejercicio 1-6
def operaciones(numero1,numero2):
    print(numero1 + numero2)
    print(numero1 / numero2)
    print(numero1 - numero2)
    print(numero1 * numero2)
    
def tabla_multiplicar(numero):
    for i in range(1,11):
        print(numero, "x", i, "=", numero * i)

#Ejercicio 1-7
def palabra_mil_veces(palabra):
    for i in range(1,1001):
        print(palabra, end=" ")

#RPL
def factorial(numero):
    suma = 1
    for i in range(1,numero+1):
        suma = suma * i
    return suma

def tabla_multiplicar(numero):
    for i in range(1,11):
        print(numero, "x", i, "=", numero * i)

def palabra_cien_veces():
    palabra = input("Ingrese una palabra: ")
    for i in range(0,100):
        print(palabra, end="")

def es_primo(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def mi_abs(x):
    '''
    devuelve el valor absoluto de cualquier valor que reciba.
    '''
    if x < 0:
        return x * (-1)
    return x

def matriz_identidad(n):
    '''
    función que reciba por parámetro una dimensión n, e imprima la matriz identidad correspondiente a esa dimensión.
    '''
    for i in range(n):
        for c in range(n):
            if c == i:
                print("1", end=" ")
            elif c != n-1:
                print("0", end=" ")
            else:
                print("0")

def dia_semana(n):
    '''
    una función que reciba un número con el día del año n (de 1 a 366) y devuelva el día de la semana que le toca.
    '''
    if (n-1) % 7 == 0 or n == 1:
        return "lunes"
    elif (n-2) % 7 == 0 or n == 2:
        return "martes"
    elif (n-3) % 7 == 0 or n == 3:
        return "miércoles"
    elif (n-4) % 7 == 0 or n == 4:
        return "jueves"
    elif (n-5) % 7 == 0 or n == 5:
        return "viernes"
    elif (n-6) % 7 == 0 or n == 6:
        return "sábado"
    else:
        return "domingo"

def promedio(suma_de_notas,cant_notas):
    return suma_de_notas/cant_notas

def programa_promedios():
    '''
    Lee notas (de a una) del usuario, preguntando en cada paso si se desea continuar. Al finalizar, se imprime el promedio de las mismas.
    '''
    nota = int(input("Ingrese una nota: "))
    acumulador = 1
    centinela = str(input("Desea ingresar mas notas? (s/n): "))
    while centinela == "s":
        otra_nota = int(input("Ingrese una nota: "))
        acumulador += 1
        centinela = str(input("Desea ingresar mas notas? (s/n): "))
        nota = nota+ otra_nota
    print(f"El promedio es: {promedio(nota,acumulador)}")

def tuplas_a_diccionario(lista_a_modificar: list) -> dict:
    """Una función que reciba una lista de tuplas, y que devuelva un diccionario
    en donde las claves sean los primeros elementos de las tuplas, y los valores una lista con los
    segundos."""
    diccionario = {}
    for clave,valor in lista_a_modificar:
        if clave not in diccionario:
            diccionario[clave] = [valor]
        else:
            diccionario[clave].append(valor)
    return diccionario

def contar_palabras(texto: str)-> dict:
    """una función que reciba una cadena y devuelva un diccionario con la cantidad
    de apariciones de cada palabra en la cadena."""
    lista_con_palabras = texto.split()
    diccionario = {}
    for palabra in lista_con_palabras:
        if palabra not in diccionario:
            diccionario[palabra] = 1
        else:
            diccionario[palabra] += 1
    return diccionario

def contar_caracteres(texto: str)-> dict:
    """una función que cuente la cantidad de apariciones de cada
    caracter en una cadena de texto, y los devuelva en un diccionario."""
    diccionario = {}
    lista_con_palabras = texto.split()
    for palabra in lista_con_palabras:
        for letra in palabra:
            if letra not in diccionario:
                diccionario[letra] = 1
            else:
                diccionario[letra] += 1
    return diccionario

def contar_resultados_dados(n):
    """una función que reciba una cantidad de iteraciones de una tirada de dos 
    dados a realizar y devuelva la cantidad de veces que se observa cada valor."""
    resultado = {}
    for cantidad in range(n*2):
        dado = random.randint(1, 6)
        resultado[dado] = resultado.get(dado, 0) + 1
    return resultado

def obtener_cadenas_largas_por_caracter(texto):
    """una función que reciba un texto y para cada caracter presente en el texto
    devuelva la cadena más larga en la que se encuentra ese caracter.
    En el caso de que haya más de una cadena posible para elegir, se debe seleccionar la última."""
    resultado = {}
    palabras = texto.split()
    for palabra in palabras:
        for letras in palabra:
            if len(resultado.get(letras, " ")) <= len(palabra):
                resultado[letras] = palabra
    print(resultado)

def leer_primera_linea(nombre_archivo): 
    """devuelve el contenido de la primer línea del archivo, sin el salto de línea si lo tiene"""
    with open(nombre_archivo,"r") as archivo:
        linea = archivo.readline()
        return linea.rstrip("\n")

def escribir_en_archivo(contenido, nombre_archivo): 
    """escribe el valor de contenido al archivo nombre_archivo, reemplazando su contenido existente"""
    with open(nombre_archivo,"w") as archivo:
        archivo.writelines(contenido)
        return contenido

def head(nombre_archivo, N):
    """recibe un nombre de archivo y un número N e imprima las primeras N líneas del archivo."""
    with open(nombre_archivo,"r") as archivo:
        contador = 0
        for linea in archivo:
            if contador == N:
                return
            print(linea.rstrip("\n"))
            contador += 1

def cp(archivo_origen, archivo_destino):
    """copia todo el contenido de un archivo llamado archivo_origen (sea de texto o binario)
    a otro llamado archivo_destino, de modo que quede exactamente igual."""
    with open(archivo_origen) as origen, open(archivo_destino,"a") as destino:
        for linea in origen:
            destino.write(linea)
        return destino

def wc(nombre_archivo):
    '''
    Dado un archivo de texto, lo procesa e imprime por pantalla cuántas líneas,
    cuantas palabras y cuántos caracteres contiene el archivo.
    '''
    with open(nombre_archivo) as archivo:
        lineas = 0
        palabras = 0
        caracteres = 0
        for linea in archivo:
            lineas += 1
            palabras = len(linea.split(" ")) + palabras
            for c in linea:
                caracteres +=1
        print("Cantidad de líneas:", lineas)
        print("Cantidad de palabras:", palabras)
        print("Cantidad de caracteres:", caracteres)

def grep(nombre_archivo, cadena):
    """recibe una cadena y un archivo e imprima
    las líneas del archivo que contienen la cadena recibida."""
    with open(nombre_archivo) as archivo:
        lineas = 0
        for linea in archivo:
            linea = linea.split(" ")
            lineas += 1
            if cadena in linea:
                linea = " ".join(linea).rstrip("\n")
                print(linea)

def rot13(archivo_origen, archivo_destino):
    """ """
    with open(archivo_origen) as archivo:
        print(archivo.tell())


class Punto:
    """
    Representación de un punto en el plano en
    coordenadas cartesianas (x, y)
    """

    def __init__(self, x, y):
        """
        Constructor de Punto. x e y deben ser numéricos
        """
        self.x = x
        self.y = y
    
    
    def distancia(self, otro):
        """
        Devuelve la distancia entre ambos puntos.
        """
        return ((otro.x - self.x) ** 2 + (otro.y - self.y) ** 2) ** 0.5


    def restar(self, otro):
        """
        Devuelve el Punto que resulta de la resta
        entre dos puntos.
        """
        return Punto(
            self.x - otro.x,
            self.y - otro.y,
            )


    def norma(self):
        """
        Devuelve la norma del vector que va desde el origen
        hasta el punto.
        """
        return(self.x ** 2 + self.y ** 2) ** 0.5

class Fraccion:
    '''
    Clase para representar una fraccion entre dos numeros
    '''

    def __init__(self, num, den):
        '''
        Inicializa la fraccion dado el numerador y el denominador
        '''
        self.num = num
        self.den = den

    def __str__(self):
        '''
        Cadena de la fraccion con el formato `num/den`
        '''
        return f"{self.num}/{self.den}"

    def simplificar(self):
        '''
        Modifica la misma fraccion para que el numerador y
        el denominador estén simplificados
        '''
        if self.num < self.den:
            for i in range(self.num,1,-1):
                if self.num % i == 0 and self.den % i == 0:
                    self.num = int(self.num / i)
                    self.den = int(self.den / i)
        elif self.num > self.den:
            for i in range(self.den,1,-1):
                if self.num % i == 0 and self.den % i == 0:
                    self.num = int(self.num / i)
                    self.den = int(self.den / i)
        else:
            self.num = 1
            self.den = 1
        return Fraccion(self.num, self.den)

    def __add__(self, f2):
        '''
        Devuelve una nueva fraccion, dada por la suma
        entre la fraccion actual y `f2`.
        La fraccion resultante es simplificada.
        '''
        if self.den != f2.den:
            for i in range(100):
                if self.den * i == f2.den * i:
                    self.den = i
            self.num = (self.den * f2.num + self.num * f2.den)
        else:
            self.num = (self.num + f2.num)
        return Fraccion.simplificar(self)

    def __mul__(self, f2):
        '''
        Devuelve una nueva fraccion, dada por la
        multiplicacion entre la fraccion actual y `f2`.
        La fraccion resultante es simplificada.
        '''
        self.num = self.num * f2.num
        self.den = self.den * f2.den
        return Fraccion.simplificar(self)

class CajaFuerte:
    '''
    DOC: Completar
    '''
    def __init__(self,clave,abierta = False, vacio = True):
        self.clave = clave
        self.abierta = abierta
        self.vacio = vacio

    def abrir(self,clave):
        if self.clave != clave:
            raise Exception (": La clave es inválida")
        self.abierta = True
    
    def esta_abierta(self):
        print(self.abierta)
    
    def cerrar(self):
        self.abierta = False

    def guardar(self,objeto):
        if self.vacio == False:
            raise Exception (": No se puede guardar más de una cosa")
        elif self.abierta == False:
            raise Exception (": La caja fuerte está cerrada")
        self.vacio = False

    def sacar(self):
        if self.abierta == False:
            raise Exception (": La caja fuerte está cerrada")
        if self.vacio == True:
            raise Exception (": No hay nada para sacar") 
        self.vacio = True   

class ListaEnlazada:

    def extend(self, lista_aux):
        '''
        DOC: Completar
        '''
        if lista_aux.__len__() == 0:
            return
        if self.__len__() == 0:
            act = lista_aux.prim
            while act.prox != None:
                act = act.prox
            self.cant = lista_aux.__len__()
        else:
            act = self.prim
            while act.prox != None:
                act = act.prox
            act.prox = lista_aux.prim
            self.cant = self.__len__() + lista_aux.__len__()

    def __str__(self):
        '''
        DOC: Completar
        '''
        resultado = []
        if self.__len__() == 0:
            print("hola")
            return str(resultado)
        act = self.prim
        while act.prox is not None:
            resultado.append(act.dato)
            act = act.prox
        resultado.append(act.dato)
        return str(resultado)
    

    def __init__(self):
        # prim es un _Nodo o None
        self.prim = None
        self.cant = 0

    def append(self, dato):
        nuevo = _Nodo(dato)
        if not self.prim:
            self.prim = nuevo
        else:
            act = self.prim
            while act.prox:
                act = act.prox
            # act es el ultimo nodo
            act.prox = nuevo
        self.cant += 1

    def __len__(self):
        return self.cant

class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

L1 = []
L2 = [4,5,6]
L1.extend(L2)
L2.append(9)
print(L1.__str__())
print(L2.__str__())