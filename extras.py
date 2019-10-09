import pygame
from pygame.locals import *
from configuracion import *

def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_KP_MINUS:
        return("-")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")

def escribirEnPantalla(screen, palabra, posicion, tamano, color):
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), tamano)
    ren = defaultFont.render(palabra, 1, color)
    screen.blit(ren, posicion)

def dibujar(screen, palabraUsuario, palabrasTitulares, diario, puntos, segundos):

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    #Linea Horizontal
    pygame.draw.line(screen, (122,122,122), (0, ALTO-110) , (ANCHO, ALTO-110), 5)

    #Ora Linea Horizontal
    pygame.draw.line(screen, (122, 122, 122), (0, ALTO-180), (ANCHO, ALTO-180), 5)

    #muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario.capitalize(), 1, COLOR_USUARIO), (ANCHO//2-len(palabraUsuario)*TAMANNO_LETRA//4, 600))
    #muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO), (680, ALTO-80))
    #muestra los segundos y puede cambiar de color con el tiempo
    if(segundos<=10):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (88, ALTO-80))

    #muestra el nombre del diario
    screen.blit(defaultFont.render(diario.capitalize(), 1, COLOR_DIARIOS), (ANCHO//2-len(diario)*TAMANNO_LETRA//4,(TAMANNO_LETRA)-20))

    #muestra las palabras del titulo
    for i in range(len(palabrasTitulares)):
        screen.blit(defaultFontGrande.render(palabrasTitulares[i].capitalize(), 1, COLOR_LETRAS), (ANCHO//50,(TAMANNO_LETRA_GRANDE)*(5//2+i)))
    #muestra su longitud
##    screen.blit(defaultFontGrande.render(str(len(palabraActual)), 1, (200,20,10)), (ANCHO-400,ALTO-500))




