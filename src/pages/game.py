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

    #Mapa
    screen.fill(color.black)
    mapa_main = pg.transform.scale(imagem.mapa, (mech.altura_mapa, mech.largura_mapa))

    #Loop infinito
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 'sair'
            if event.type == pg.MOUSEBUTTONDOWN:
                mech.verificaMouse()

        screen.blit(mapa_main, (-mech.camera_x, -mech.camera_y))

        # Movimentar jogador
        keys = pg.key.get_pressed()
        mech.movimentarJogador(keys)

        # Mochila
        if keys[pg.K_i]:
            time.sleep(0.2)
            return 'mochila'

        # Desenhar o jogador
        pg.draw.circle(screen, color.red, (mech.x_player - mech.camera_x, mech.y_player - mech.camera_y), mech.raio)

        # Verificar proximidade com ginásios
        for chave0, tupla in mech.valores_regioes.items():
            x_ginasio, y_ginasio = tupla
            jogador_proximo = mech.proximoDoObjeto(
                (mech.x_player + mech.raio) // 2, (mech.y_player + mech.raio) // 2,
                (x_ginasio + mech.raio2) // 2, (y_ginasio + mech.raio2) // 2,
                mech.raio2
            )

            if jogador_proximo:
                todasAsDistanciasGinasios = grafo.calculaDistanciasGinasios()
                for chave, valor in todasAsDistanciasGinasios.items():
                    if chave == chave0 and jogador_proximo:
                        if keys[pg.K_e]:
                            menor_valor = min(v for k, v in valor.items() if v > 0)
                            menor_chave = [k for k, v in valor.items() if v == menor_valor]
                            mech.popup_text = f"De {chave} -> Para {menor_chave} com valor: {menor_valor}"
                            mech.popup_timer = 120  # Duração do popup em frames (~2 segundos)

        # Exibir popup se necessário
        if mech.popup_text and mech.popup_timer > 0:
            mech.exibir_popup(screen, mech.popup_text)
            mech.popup_timer -= 1

        pg.time.Clock().tick(60)  # 60 FPS
        pg.display.flip()
        pg.time.wait(1)

    return 'menu'