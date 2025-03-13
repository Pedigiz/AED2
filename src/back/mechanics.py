import pygame as pg

#Tamanho da tela
altura, largura = 800, 600

#Tamanho do mapa
altura_mapa, largura_mapa = 1600, 1200

#Camera
camera_x, camera_y = 0, 0

#Config do player (bola)
raio = 10
speed = 10
x_player, y_player = 0, 0

#Posição inicial do circulo
x_player = altura / 2
y_player = largura / 2


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
