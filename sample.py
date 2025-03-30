import pygame as pg
from hangman import utils
from hangman.constants import BLACK, GRAPHICS, WHITE, WINDOW_H, WINDOW_W


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
game_over = False

palabra = 'ordenador'
solucion = '-' * len(palabra)

incorrecto = ''
correcto = ''

def comprobar_letra(letra, palabra, solucion):
    """
    Comprueba si la letra está en la palabra y actualiza la solución.

    :param letra: La letra pulsada por el usuario.
    :param palabra: La palabra a adivinar.
    :param solucion: La solución actual con guiones.
    :return: La solución actualizada y un booleano indicando si la letra estaba en la palabra.
    """
    nueva_solucion = list(solucion)  # Convertir solucion a una lista para modificarla
    letra_encontrada = False
    for i, caracter in enumerate(palabra):
        if caracter == letra:
            nueva_solucion[i] = letra  # Actualizar la letra en la posición correcta
            letra_encontrada = True
    return ''.join(nueva_solucion), letra_encontrada  # Convertir la lista de nuevo a una cadena

def mostrar_fin_partida(display, font, texto):
    img = font.render(texto, True, WHITE)
    x = (WINDOW_W - img.get_width()) // 2
    y = WINDOW_H // 2 -20
    display.blit(img, (x, y))


def mostrar_fin_partida2(display, font, texto):
    img = font.render(texto, True, WHITE)
    x = (WINDOW_W - img.get_width()) // 2
    y2 = WINDOW_H // 2 + 40
    display.blit(img, (x, y2))


# bucle principal

while playing:
    clock.tick(20)
    counter += 1

    # evento para salir al cerrar la ventana
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            playing = False
        elif event.type == pg.KEYDOWN and not game_over:
            pulsado = pg.key.name(event.key)
            solucion, letra_encontrada = comprobar_letra(pulsado, palabra, solucion)
            if letra_encontrada:
                correcto += pulsado
            else:
                incorrecto += pulsado
                status += 1

    display.fill(BLACK)

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
    

    # Comprobar si el jugador ha ganado o perdido

    if '-' not in solucion:
        mostrar_fin_partida(display, font, '¡Has ganado!')
        game_over = True
    elif status >= len(GRAPHICS) - 1:
        mostrar_fin_partida(display, font, '¡Has perdido!')
        mostrar_fin_partida2(display, font, f'La palabra era: {palabra}') 
        game_over = True


    pg.display.flip()

pg.quit()