import pygame as pg
import time
import sys
import os

import src.styles.imagens as imagem
import src.styles.color as color
import src.back.mechanics as mech
import src.back.MontarPokemons as pokemon

def mapa_paint(screen):
    running = True
    clock = pg.time.Clock()

    pg.display.set_caption('POKEMON FIRE/RED DEEPWEB')

    while running:
        screen.fill(color.black)  # Pintar fundo de preto
        screen.blit(imagem.mapa_paint, (0,0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 'sair'
        
        keys = pg.key.get_pressed()
        if keys[pg.K_m] and 'mapa_paint':
            time.sleep(0.1)
            return 'game'  # Voltar para o jogo
        
        

        pg.display.flip()  # Atualizar tela
        clock.tick(20)  # Limitar a 60 FPS  -- Aqui é 10 pra nn bugar 

    return 'menu'  # Se sair do loop, pode retornar para o menu
