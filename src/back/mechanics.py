import pygame as pg
from random import randint
import src.back.grafo as grafo
import src.styles.color as color

# Funcoes para fazer o popup
popup_text = None
popup_timer = 0


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
                    "alola" : (557,235),
                    "kanto" : (1092,196),
                    "johto" : (1126,365),
                    "hoenn" : (492,453),
                    "sinnoh" : (608,761)
                }

valores_pokemons = {'charizard' : (1245, 1135),
                    'charmander': (1323, 652), 
                    'venusaur' : (1267, 95),
                    'blastoise' : (904, 90),
                    'pikachu' : (780, 720), 
                    'igglybuff': (514, 925),
                    'gyarados': (570, 1150), 
                    'rayquaza': (334, 670),
                    'garchomp': (116,1018), 
                    'mewtwo': (122, 732), 
                    'machamp': (128, 370)
}

# Remover botoes quando tentar capturar o pokemon
botoes_visiveis = set(valores_pokemons.keys())  # Começa com todos os botões
pokemons_capturados = list()  # Lista dos pokemons que estao capturados 


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
    return distancia <= raio2 # Só vai retornar se isso for verdade
        
#Verificacao de Onde o mouse esta sendo clicado para poder inserir os pokemons mais facilmente
def verificaMouse():
    mouse_pos = pg.mouse.get_pos()
    mouse_pos_mundo = pg.Vector2(mouse_pos[0] + camera_x, mouse_pos[1] + camera_y)
    print(f"Mouse na tela: {mouse_pos}, Mouse no mundo: {mouse_pos_mundo}")

def exibir_popup(screen, mensagem):
    text_surface = color.fonte.render(mensagem, True, color.white)

    # Criar retângulo do popup
    popup_rect = pg.Rect(50, 50, 650, 50)
    pg.draw.rect(screen, color.black, popup_rect)  # Fundo preto

    # Desenhar borda branca ao redor
    pg.draw.rect(screen, color.white, popup_rect, 2)

    # Desenhar texto sobre o retângulo
    screen.blit(text_surface, (65, 65))

def insereBotoes (screen):
    imageexclamacao = pg.image.load("./src/art/pokemons/icone_exclamacao-removebg-preview.png").convert_alpha()
    imageexclamacao = pg.transform.scale(imageexclamacao, (20, 20))  # Redimensiona a imagem
    for nome, posicao in valores_pokemons.items():
        if nome in botoes_visiveis:    
            # Calcula a posição relativa ao centro da câmera
            posicao_com_camera = (posicao[0] - camera_x, posicao[1] - camera_y)
            # Desenha o botão na tela ajustada pela câmera
            screen.blit(imageexclamacao, posicao_com_camera)

def capturaPokemon(pokemon):
    porcentagemCaptura = randint(0,100)
    if porcentagemCaptura >= 67:
        # Aqui dar um popup que o pokemon escapou
        return False
    else:
        pokemons_capturados.append(pokemon)
        print(pokemons_capturados)
        return True
    
def removeBotaoPokemon(pokemon):
    if pokemon in botoes_visiveis:
        botoes_visiveis.remove(pokemon)