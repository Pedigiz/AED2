import pygame as pg

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

# TIRAR ISSO DAQUI PARA UMA PASTA DIFERENTE

#Importamos o módulo sys para utilizar o valor de infinito (sys.maxsize) na inicialização das distâncias
import sys

#Definimos a função dijkstra que implementa o algoritmo de Dijkstra. Essa função recebe o grafo e o vértice de origem como parâmetros.
def calcular_dijkstra(grafo, origem):

  #Inicializamos as distâncias para todos os vértices como infinito, exceto para o vértice de origem que é definido como zero
  distancias = {v: sys.maxsize for v in grafo}
  distancias[origem] = 0

  # Conjunto de vértices visitados
  visitados = set()

  while visitados != set(distancias):
      # Encontra o vértice não visitado com menor distância atual
      vertice_atual = None
      menor_distancia = sys.maxsize
      for v in grafo:
          if v not in visitados and distancias[v] < menor_distancia:
              vertice_atual = v
              menor_distancia = distancias[v]

      # Marca o vértice atual como visitado
      visitados.add(vertice_atual)

      # Atualiza as distâncias dos vértices vizinhos
      for vizinho, peso in grafo[vertice_atual].items():
          if distancias[vertice_atual] + peso < distancias[vizinho]:
              distancias[vizinho] = distancias[vertice_atual] + peso

  # Retorna as distâncias mais curtas a partir da origem
  return distancias

regioes = {
  'Alola': {'Kanto': 5, 'Galar': 3, 'Sinnoh': 2},
  'Kanto': {'Alola': 5, 'Galar': 2, 'Unova': 4},
  'Galar': {'Alola': 3, 'Kanto': 2, 'Sinnoh': 1},
  'Sinnoh': {'Alola': 2, 'Galar': 1, 'Unova': 7},
  'Unova': {'Kanto': 4, 'Sinnoh': 7}
}

# Ponto de partida
origem = 'Kanto'

# Chamando o algoritmo de Dijkstra para encontrar os caminhos mais curtos a partir de A
caminhos_mais_curto = calcular_dijkstra(regioes, origem)

# Exibindo os caminhos mais curtos
for destino, distancia in caminhos_mais_curto.items():
  print(f"Caminho mais curto de {origem} para {destino}: {distancia}")



