import pygame as pg
import sys

import src.styles.imagens as imagem
import src.styles.color as color
import src.back.mechanics as mech

#Inicializar
#Config básicas do pygame
pg.init()  # Sempre começa o game aqui
screen = pg.display.set_mode((mech.altura, mech.largura))
pg.display.set_caption('POKEMON FIRE/RED DEEPWEB')
running = True

#Mapa
screen.fill(color.cores["preto"])
mapa_main = pg.transform.scale(imagem.mapa, (mech.altura_mapa, mech.largura_mapa))

#Loop infinito
while running:
    # pygame.QUIT se clicar no X o jogo fecha
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.blit(mapa_main, (-mech.camera_x, -mech.camera_y))

    #Movimentar jogador
    keys = pg.key.get_pressed()
    mech.movimentarJogador(keys)
    if event.type == pg.MOUSEBUTTONDOWN: # Ver com a Fernanda
        mech.verificaMouse()

    # Desenhar o círculo (Player)
    pg.draw.circle(screen, color.cores["vermelho"], (mech.x_player - mech.camera_x, mech.y_player - mech.camera_y), mech.raio)
    
    for chave,tupla in mech.valores_ginasios.items():
        x_ginasio, y_ginasio = tupla
        jogador_proximo = mech.proximoDoObjeto(((mech.x_player + mech.raio) // 2), ((mech.y_player + mech.raio) // 2), ((x_ginasio+mech.raio2)//2), ((y_ginasio+mech.raio2)//2 ), mech.raio2)

        if jogador_proximo:
            mech.popUp(tupla, x_ginasio, y_ginasio)
            if keys[pg.K_e]:
                print(tupla)
    
    
    pg.time.Clock().tick(60) #60 fps
    pg.display.flip()  # Atualizar
    pg.time.wait(1)

pg.quit()
sys.exit()