import pygame as pg
import time
import sys
import os

import src.styles.imagens as imagem
import src.styles.color as color
import src.back.mechanics as mech

import src.back.mechanics as mech

def mochila(screen):
    indice_frame = 0
    running = True
    clock = pg.time.Clock()

    pg.display.set_caption('POKEMON FIRE/RED DEEPWEB')

    #Redimencionar imagem do gato xd
    mochila_gato_meme = pg.transform.scale(imagem.show_pokemons_backpack, (200, 200))
    inventario_scale = pg.transform.scale(imagem.inventario, (800, 600))


    #Carregar os sprites dos pokemons
    #Explicação das linhas:
    #os.listdir: Lista todos os arquivos na pasta
    #os.path.join(charizardSprite, f) junta o caminho do arquivo
    base_dir = os.path.dirname(__file__)
    
    for i in ['charizard']:
        caminho_completo = os.path.join(base_dir, "..", "art", "pokemons", "sprites", f"{i}_sprite")
        
        charizard_sprite = sorted([(os.path.join(caminho_completo, f), int(f.split('\\')[-1].split('.')[0])) for f in os.listdir(caminho_completo)], key=lambda x: x[1])

        charizard_sprite = [pg.image.load(os.path.join(f[0])) for f in charizard_sprite]

    while running:
        screen.fill(color.black)  # Pintar fundo de preto

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 'sair'

        keys = pg.key.get_pressed()
        if keys[pg.K_i] and 'mochila':
            time.sleep(0.1)
            return 'game'  # Voltar para o jogo
        
        screen.blit(inventario_scale, (0,0))
        screen.blit(mochila_gato_meme, (600,400))

        #-------------------------DESENHAR OS SPRITES-------------------------------------
        screen.blit(charizard_sprite[indice_frame], (50, 10))  #Desenhar o frame atual

        # Atualizar frame
        indice_frame = (indice_frame + 1) % len(charizard_sprite) 

        #---------------------------------------------------------------------------------



        pg.display.flip()  # Atualizar tela
        clock.tick(20)  # Limitar a 60 FPS  -- Aqui é 10 pra nn bugar 

    return 'menu'  # Se sair do loop, pode retornar para o menu
