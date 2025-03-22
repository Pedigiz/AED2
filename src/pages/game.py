import pygame as pg
import time
import sys

import src.styles.imagens as imagem
import src.styles.color as color
import src.back.mechanics as mech
import src.back.grafo as grafo
import src.back.MontarPokemons as pokemon

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
        
        #Mapa_paint
        if keys[pg.K_m] and 'game':
            time.sleep(0.2)
            return 'mapa_paint'

        # Inserir os botoes para poder capturar os pokemons selvagens
        mech.insereBotoes(screen)

        # Desenhar o círculo (Player)
        estado_jogador = animacaoJogador(keys)
        contador_fps += 1
        screen.blit(animacoes[estado_jogador][indice], ((mech.x_player - mech.camera_x) - 50, (mech.y_player - mech.camera_y) - 60))
        if (contador_fps >= fps_delay):
            indice = (indice + 1) % len(imagem.idle) #8 frames
            contador_fps = 0       


        # Verificar proximidade com ginásios
        for chave0, tupla in mech.valores_regioes.items():
            x_ginasio, y_ginasio = tupla
            jogador_proximo = mech.proximoDoObjeto(
                (mech.x_player + mech.raio) // 2, (mech.y_player + mech.raio) // 2,
                (x_ginasio + mech.raio2) // 2, (y_ginasio + mech.raio2) // 2,
                mech.raio2
            )

            # Parte do algoritmo de dijktra para procurar o menor caminho
            for chave0,tupla in mech.valores_regioes.items():
                x_ginasio, y_ginasio = tupla
                jogadorProximoGinasio = mech.proximoDoObjeto(((mech.x_player + mech.raio) // 2), ((mech.y_player + mech.raio) // 2), ((x_ginasio+mech.raio2)//2), ((y_ginasio+mech.raio2)//2 ), mech.raio2)

                if jogadorProximoGinasio:
                    todasAsDistanciasGinasios = grafo.calculaDistanciasGinasios()
                    for chave, valor in todasAsDistanciasGinasios.items():
                        if chave == chave0 and jogador_proximo:
                            #Batalha
                            if keys[pg.K_p] and 'game':
                                time.sleep(0.2)
                                return 'batalha'
                            if keys[pg.K_e]:
                                menor_valor = min(v for k, v in valor.items() if v > 0)
                                menor_chave = [k for k, v in valor.items() if v == menor_valor]
                                mech.popup_text = f"De {chave} -> Para {menor_chave} Valor: {menor_valor}"
                                mech.popup_timer = 120  # Duração do popup em frames (~2 segundos)

        # Verficar se o jogador esta na posicao do pokemon para a funcao de captura do pokemon
        for chavePokemon, tuplaPokemon in mech.valores_pokemons.items():
            x_pokemon, y_pokemon = tuplaPokemon
            jogadorProximoPokemon = mech.proximoDoObjeto(((mech.x_player + mech.raio) // 2), ((mech.y_player + mech.raio) // 2), ((x_pokemon+mech.raio2)//2), ((y_pokemon+mech.raio2)//2 ), mech.raio2)

            if jogadorProximoPokemon: # Aqui retorna true quando o jogador ta "perto" do ponto de interrogacao
                if keys[pg.K_e]:
                        if not(getattr(pokemon, chavePokemon)['capturado']):
                            if mech.capturaPokemon(chavePokemon): # Passar o pokemon a ser capturado pela funcao
                                    mech.popup_text = f"Pokemon {chavePokemon} capturado!"
                                    mech.exibir_popup(screen, mech.popup_text )
                                    mech.removeBotaoPokemon(chavePokemon)
                                    mech.insereBotoes(screen)  
                                    mech.popup_timer = 120  # Duração do popup em frames (~2 segundos)
                                    pg.time.wait(500)
                            else:
                                mech.popup_text = f"Pokemon {chavePokemon} nao capturado, tente novamente!"
                                mech.exibir_popup(screen, mech.popup_text )
                                mech.popup_timer = 120  # Duração do popup em frames (~2 segundos)
                                pg.time.wait(500)

        # Desenhar o círculo (Player)
        estado_jogador = animacaoJogador(keys)
        contador_fps += 1
        screen.blit(animacoes[estado_jogador][indice], ((mech.x_player - mech.camera_x) - 50, (mech.y_player - mech.camera_y) - 60))
        if (contador_fps >= fps_delay):
            indice = (indice + 1) % len(imagem.idle) #8 frames
            contador_fps = 0       

        # Exibir popup se necessário
        if mech.popup_text and mech.popup_timer > 0:
            mech.exibir_popup(screen, mech.popup_text)
            mech.popup_timer -= 1

        pg.time.Clock().tick(60)  # 60 FPS
        pg.display.flip()
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