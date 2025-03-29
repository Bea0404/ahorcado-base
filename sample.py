import pygame as pg
from hangman import utils
from hangman.constants import GRAPHICS, WINDOW_H, WINDOW_W


# inicialización
pg.init()
display = pg.display.set_mode((WINDOW_W, WINDOW_H), 0, 32)
pg.display.set_caption('Juego del ahorcado')
clock = pg.time.Clock()
font_name = pg.font.get_default_font()
font = pg.font.SysFont(font_name, 70)
letters_font = pg.font.SysFont(font_name, 60)

counter = 0
status = -1
playing = True

palabra = 'casa'
solucion = ''

incorrecto = ''
correcto = ''

for letra in palabra:
    solucion += '-'



def comprobar_letra(palabra, solucion, pulsado):
    for i, letra in enumerate(palabra):
        if letra == pulsado:
            solucion = solucion[:i] + letra + solucion[i+1:]
    return solucion

# bucle principal

while playing:
    #clock.tick(20)
    counter += 1

    # evento para salir al cerrar la ventana
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
        elif event.type == pg.KEYDOWN:
            pulsado = pg.key.name(event.key)
            solucion = comprobar_letra(palabra, solucion, pulsado)
            

    # dibuja el ahorcado completo desactivado
    utils.draw_base(display, 30)

    # cada segundo activa una parte del ahorcado
    # simulando la evolución del juego
    # if counter % 20 == 0:
    #     status += 1
    # if counter > 220:
    #     status = -1

    for index, key in enumerate(GRAPHICS):
        if index <= status:
            utils.draw_part(display, key, True, 30)

    # dibuja una palabra de prueba a medio adivinar
    
    # palabra = 'CASA'
    # palabra = '----'

    utils.draw_word(display, font, solucion)

    # dibuja el abecedario con algunas letras probadas
    # erróneas y otras letras válidas

    utils.draw_letters(display, letters_font, 360, 50, incorrecto, correcto)
    #TODO:  Adivinar letras  jugador 2 - Pulsas un letra del teclado
    #       comprobar si la letra pulsada esta en la palabra que se introdujo, si es asi se pinta en verde ("a") y se 
    #       muestra en la palabra a adivinar ('-A-A'), sino en rojo ("amu") y se pinta una parte del ahorcado -> status + 1


    pg.display.flip()
