import pygame as pg
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))  # Ajuste o número de parents conforme necessário

import src.back.estruturas as estruturas

#Tamanho da tela
altura, largura = 800, 600

#Raio de proximidade para interagir com o ginasio ou pokemon
raio2 = 35

#Tamanho do mapa
altura_mapa, largura_mapa = 1600, 1200

#Camera
camera_x, camera_y = 0, 0
camera_centro = pg.Vector2( (altura/2) , (largura/2) )

#Config do player (bola)
raio = 10
speed = 10
x_player, y_player = 0, 0

#Posição inicial do circulo
x_player = altura / 2
y_player = largura / 2
PosicaoJogador = pg.Vector2(x_player, y_player)

#Movimentação do personagem
def movimentarJogador(keys):
    global x_player, y_player, camera_x, camera_y   #Deu mó BO sem isso

    if keys[pg.K_w] and y_player - speed - raio >= 0:
        y_player -= speed 
    if keys[pg.K_s] and y_player + speed + raio <= 1200:
        y_player += speed
    if keys[pg.K_a] and x_player - speed - raio >= 0:
        x_player -= speed 
    if keys[pg.K_d] and x_player + speed + raio <= 1400:
        x_player += speed

    #Atualiza a posição da câmera
    camera_x = max(0, min(x_player - largura // 2, largura_mapa - largura))
    camera_y = max(0, min(y_player - altura // 2, (altura_mapa - 200) - altura))

def proximoDoObjeto(x_jogador, y_jogador, x_objeto, y_objeto, raio2):
    distancia = ((x_jogador - x_objeto) ** 2 + (y_jogador - y_objeto) ** 2) ** 0.5
    return distancia <= raio2 # ´Só vai retornar se isso for verdade
        
#Verificacao de Onde o mouse esta sendo clicado

def verificaMouse():
    mouse_pos = pg.mouse.get_pos()
    mouse_pos_mundo = pg.Vector2(mouse_pos[0] + camera_x, mouse_pos[1] + camera_y)
    print(f"Mouse na tela: {mouse_pos}, Mouse no mundo: {mouse_pos_mundo}")
    
    '''
    for ginasio in estruturas.ginasios:
        if (ginasio["pos"].x <= mouse_pos_mundo.x <= ginasio["pos"].x + ginasio["tamanho"].x and
            ginasio["pos"].y <= mouse_pos_mundo.y <= ginasio["pos"].y + ginasio["tamanho"].y):
            print(f"Ginásio em {ginasio['pos']} clicado!")

    for pokemon in estruturas.pokemons:
        if (pokemon["pos"].x <= mouse_pos_mundo.x <= pokemon["pos"].x + pokemon["tamanho"].x and
            pokemon["pos"].y <= mouse_pos_mundo.y <= pokemon["pos"].y + pokemon["tamanho"].y):
            print(f"Pokemon em {pokemon['pos']} clicado!")


def insereBotoes(screen):
    for ginasio in estruturas.ginasios:
        botao_pos_tela = (ginasio["pos"] - PosicaoJogador) * 2 + camera_centro
        screen.blit(ginasio["imagem"], (botao_pos_tela.x, botao_pos_tela.y))
    
    for pokemon in estruturas.pokemons:
        botao_pos_tela = (pokemon["pos"] - PosicaoJogador) * 2 + camera_centro
        screen.blit(pokemon["imagem"], (botao_pos_tela.x, botao_pos_tela.y))
'''