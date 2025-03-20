import pygame as pg
import time
import sys
import os

import src.styles.imagens as imagem
import src.styles.color as color
import src.back.mechanics as mech
import src.back.MontarPokemons as pokemon

import src.back.mechanics as mech

def batalha(screen):
    running = True
    clock = pg.time.Clock()

    pg.display.set_caption('POKEMON FIRE/RED DEEPWEB')

    #Redimencionar imagem da arena
    arena_scale = pg.transform.scale(imagem.arena, (800, 600))

    while running:
        screen.fill(color.black)  # Pintar fundo de preto
        screen.blit(arena_scale, (0,0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 'sair'
        
        keys = pg.key.get_pressed()
        if keys[pg.K_p] and 'batalha':
            time.sleep(0.1)
            return 'game'  # Voltar para o jogo
        
        screen.blit(pokemon.rayquaza['image'], (130, 380))
        

        pg.display.flip()  # Atualizar tela
        clock.tick(20)  # Limitar a 60 FPS  -- Aqui é 10 pra nn bugar 

    return 'menu'  # Se sair do loop, pode retornar para o menu
