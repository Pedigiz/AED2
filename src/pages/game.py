import pygame as pg
import time
import sys

import src.styles.imagens as imagem
import src.styles.color as color
import src.back.mechanics as mech
import src.back.grafo as grafo

#Inicializar
#Config básicas do pygame
def game(screen):
    #pg.init()  # Sempre começa o game aqui
    #screen = pg.display.set_mode((mech.altura, mech.largura))
    pg.display.set_caption('POKEMON FIRE/RED DEEPWEB')
    clock = pg.time.Clock()
    running = True

    #Variaveis responsaveis por animar o personagem
    #Criar um dicionario de animações
    animacoes = {
    'cima': imagem.walkUp,
    'baixo': imagem.walkDown,
    'esquerda': imagem.walkLeftDown,
    'direita': imagem.walkRightDown,
    'parado': imagem.idle
    }
    indice = 0
    fps_delay = 10
    contador_fps = 0
    estado_jogador = 'parado'

    #CARREGAR A ANIMAÇÃO ANTES

    #Mapa
    screen.fill(color.black)
    mapa_main = pg.transform.scale(imagem.mapa, (mech.altura_mapa, mech.largura_mapa))

    #Loop infinito
    while running:
        # pygame.QUIT se clicar no X o jogo fecha
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 'sair'
            
            if event.type == pg.MOUSEBUTTONDOWN:
                mech.verificaMouse()

        screen.blit(mapa_main, (-mech.camera_x, -mech.camera_y))

        #Movimentar jogador
        keys = pg.key.get_pressed()
        mech.movimentarJogador(keys)

        #Mochila
        if keys[pg.K_i] and 'game':
            time.sleep(0.2)
            return 'mochila'  # Voltar para o jogo




        # Desenhar o círculo (Player)
        estado_jogador = animacaoJogador(keys)
        contador_fps += 1
        screen.blit(animacoes[estado_jogador][indice], (mech.x_player - mech.camera_x, mech.y_player - mech.camera_y))
        if (contador_fps >= fps_delay):
            indice = (indice + 1) % len(imagem.idle) #8 frames
            contador_fps = 0       





        for chave,tupla in mech.valores_regioes.items():
            x_ginasio, y_ginasio = tupla
            jogador_proximo = mech.proximoDoObjeto(((mech.x_player + mech.raio) // 2), ((mech.y_player + mech.raio) // 2), ((x_ginasio+mech.raio2)//2), ((y_ginasio+mech.raio2)//2 ), mech.raio2)


            if jogador_proximo:
                #mech.popUp(tupla, x_ginasio, y_ginasio)
                if keys[pg.K_e]:
                    print(chave)
                    # Esta printando varias vezes, arruma isto
        regiaoAtual = 'Alola'
        
        pg.time.Clock().tick(60) #60 fps
        pg.display.flip()  # Atualizar
        pg.time.wait(1)

    return 'menu'

def animacaoJogador(keys):
    estado_jogador = 'parado'
    
    if keys[pg.K_w]:
        estado_jogador = 'cima'
    if keys[pg.K_s]:
        estado_jogador = 'baixo'
    if keys[pg.K_a]:
        estado_jogador = 'esquerda' 
    if keys[pg.K_d]:
        estado_jogador = 'direita'

    return estado_jogador