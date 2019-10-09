#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *
from configuracion import *
from extras import *

from funcionesVACIAS import *

def main():
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()

        #Preparar la ventana
        pygame.display.set_caption("Noticias de Ayer...")
        screen = pygame.display.set_mode((ANCHO, ALTO))

        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial

        puntos = 0
        palabraUsuario = ""


        diarios=lector("diario")
        titulos=lector("titulo")
        notas=lector("nota")

        indice=seleccion(notas)  #elige una noticia al azar

        palabrasTitulares=seleccionDePalabras(titulos, indice) #elige 3 palabras del titular

        diario=diarios[indice] #carga el diario que saco la nota

        dibujar(screen, palabraUsuario, palabrasTitulares, diario, puntos,segundos)

        while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            if True:
            	fps = 3

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    palabraUsuario += letra

                    if e.key == K_BACKSPACE:
                        palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]

                    if e.key == K_RETURN:
                        #chequea si es correcta y suma o resta puntos
                        if palabraUsuario!="":
                            puntos += procesar(palabraUsuario, indice, titulos, notas, palabrasTitulares)

                            indice=seleccion(notas) #elige una noticia al azar

                            palabrasTitulares=seleccionDePalabras(titulos, indice) #elige 3 palabras del titular

                            diario=diarios[indice] #carga el diario que saco la nota

                        if palabraUsuario=="": # si no escribe nada cambia de noticia
                            #cambia la noticia elegida

                            indice=seleccion(notas) #elige una noticia al azar

                            palabrasTitulares=seleccionDePalabras(titulos, indice) #elige 3 palabras del titular

                            diario=diarios[indice]  #carga el diario que saco la nota

                        palabraUsuario = ""

            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)

            #Dibujar de nuevo todo
            dibujar(screen, palabraUsuario, palabrasTitulares, diario, puntos,segundos)

            pygame.display.flip()

        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return

        archivo.close()

#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()
