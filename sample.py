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

# bucle principal
while playing:
    clock.tick(20)
    counter += 1

    # evento para salir al cerrar la ventana
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False

    # dibuja el ahorcado completo desactivado
    utils.draw_base(display, 30)

    # cada segundo activa una parte del ahorcado
    # simulando la evolución del juego
    if counter % 20 == 0:
        status += 1
    if counter > 220:
        status = -1

    for index, key in enumerate(GRAPHICS):
        if index <= status:
            utils.draw_part(display, key, True, 30)

    # dibuja una palabra de prueba a medio adivinar
    utils.draw_word(display, font, '-ee---d---')

    # dibuja el abecedario con algunas letras probadas
    # erróneas y otras letras válidas
    utils.draw_letters(display, letters_font, 360, 50, 'amu', 'ed')

    pg.display.flip()
