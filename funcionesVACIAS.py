from principal import *
from configuracion import *
import random
import math


# -------------------     Lectura de Archivo  y separacion en listas -------------------------------------

def archivo_1(): #Base de datos con las noticias
    with open('noticias.csv', "r", encoding="latin1") as file:
        lector = file.readlines()
    return lector

def variable_a_numeros(variable): #pasa el parametro a numero , para que lea los ";" y pueda identificar las columnas en la funcion  lector
    if variable=="diario":
        variable=0
    elif variable=="titulo":
        variable=1
    elif variable=="nota":
        variable=3

    return variable

def lector(variable): #El parametro indica que es lo que se quiere buscar, sea "diario,titular,noticias"
    z=variable_a_numeros(variable)
    BDD=archivo_1()


    contador_de_coma = 0  #z=0 => diario               z=1 ==> titular                         z=3 ==> nota
    palabras = ""
    lista=[]
    linea_temporal = ""
    excluir=("|",'"',",","?","¿",":",".","\x94","\x93","!","¡")

    for x in range(1, len(BDD)):  #Busca por lineas en la Base de Datos(csv)
        linea_temporal = BDD[x]+";"
        for i in linea_temporal: #Busca por letras en las lineas, excluye las que no sirven y agrega las filas de la columna pedida
            if i in excluir:
                continue
            if i=="-":
                i=" "
            if i=="\n":
                i=";"
            if contador_de_coma==z and i==";":
                palabras=palabras.lower()
                lista.append(palabras)
                palabras=""
            if contador_de_coma==z and i != ";":
                palabras += i
            if i == ";":
                contador_de_coma += 1
        contador_de_coma=0

    return lista #devuelve las filas de las columnas especificadas


#------------------------ Selección de indice(listas), Tres palabras del titular ------------------------


def seleccion(notas): #Elige un indice al azar para notas.
    longitud=len(notas)
    select=random.randint(0,longitud-1)

    return select

def linea_a_lista(lista,indice): #Busca por letra hasta hacer una palabra y la guarda en la lista
    palabras=[]
    palabra=""

    for i in lista[indice]:
        if i!=" ":
            palabra+=i
        if i==" ":
            palabras.append(palabra)
            palabra=""
    palabras.append(palabra) #Para que agrege la ultima palabra, cuando termine el bucle

    return palabras


def seleccionDePalabras(lista,indice):

    oracion = linea_a_lista(lista, indice) #Pasa la oracion a una lista con palabras
    lista_max = [""]

    for i in oracion: #Selecciona las tres palabras con longitudes mayores
        if i not in lista_max:
            if len(i) > len(lista_max[0]):
                lista_max.insert(0, i)
            elif len(i) > len(lista_max[1]):
                lista_max.insert(1, i)
            elif len(i) > len(lista_max[2]):
                lista_max.insert(2, i)
            elif len(i) < len(lista_max[1]):
                lista_max.insert(3, i)
            else:
                lista_max.append(i)
    lista_max=lista_max[0:3]

    if lista_max[2]=='""':  #Filtra en el caso de un titular con dos palabras
        lista_max=lista_max[0:2]

    return lista_max


# ---------------------------------  Procesa lo ingresado por el usuario, y asigna puntos ----------------------------------------

def procesar(palabraUsuario, indice, titulos, notas, palabrasTitulares): #Confirma si es que la palabra del usuario esta
    verdadero_o_falso=False                                              #en la noticia
    puntaje=0

    if palabraUsuario in titulos[indice]:  #Confirma si la palabra usuario esta en las listas
        verdadero_o_falso=True

    elif palabraUsuario in notas[indice]:
        verdadero_o_falso=True

    if palabraUsuario in palabrasTitulares: #Rechaza si el usuario escribe una palabra en los titulares mostrados en pantalla
        puntaje=0
    elif verdadero_o_falso==True:
        puntaje+=10
    else:
        puntaje-=10

    return puntaje

