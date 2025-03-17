#Importamos o módulo sys para utilizar o valor de infinito (sys.maxsize) na inicialização das distâncias
import sys
import src.back.config as config


# Leitura dos arquivos
arquivo =  open ("", "r") # Abrir os arquivos






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

# Definindo o grafo com as conexões e custos
grafo = {
  'Alola': {'Kanto': 5, 'Galar': 3, 'Sinnoh': 2},
  'Kanto': {'Alola': 5, 'Galar': 2, 'Sinnoh': 4},
  'Galar': {'Alola': 3, 'Kanto': 2, 'Sinnoh': 1},
  'Sinnoh': {'Alola': 2, 'Galar': 1, 'Kanto': 7},
  'Unova': {} # Ver aqui se faz sentido ter peso
  }

# Ponto de partida
origem = 'Alola'

# Chamando o algoritmo de Dijkstra para encontrar os caminhos mais curtos a partir de A
caminhos_mais_curto = calcular_dijkstra(grafo, origem)

# Exibindo os caminhos mais curtos
for destino, distancia in caminhos_mais_curto.items():
  print(f"Caminho mais curto de {origem} para {destino}: {distancia}")