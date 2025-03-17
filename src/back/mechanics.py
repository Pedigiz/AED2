import pygame as pg
import src.back.grafo as grafo

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


# X : Y Valores de onde estarao os "ginasios"
valores_regioes = {
                    "Alola" : (557,235),
                    "Kanto" : (1092,196),
                    "Galar" : (1126,365),
                    "Sinnoh" : (492,453),
                    "Unova" : (608,761)
                }

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
        
#Verificacao de Onde o mouse esta sendo clicado para poder inserir os pokemons mais facilmente
def verificaMouse():
    mouse_pos = pg.mouse.get_pos()
    mouse_pos_mundo = pg.Vector2(mouse_pos[0] + camera_x, mouse_pos[1] + camera_y)
    print(f"Mouse na tela: {mouse_pos}, Mouse no mundo: {mouse_pos_mundo}")

def popUp():
    None

def calculaDistaciaRegioes (grafoRegioes, regiaoAtual):
    distancia_atual = calcular_dijkstra(grafoRegioes, regiaoAtual)
    print (distancia_atual)