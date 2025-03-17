#Importamos o módulo sys para utilizar o valor de infinito (sys.maxsize) na inicialização das distâncias
import sys
import config

# Leitura dos arquivos
def lerArquivo():
  grafo = dict()
  listapokemon = list()
  with open ('./src/config/config_1.txt', 'r') as arquivo: # Abrir os arquivos
    for linha in arquivo:
      if linha:
        if "[" not in linha and "]" not in linha and not linha.isdigit():
          listapokemon.append(linha) # Primeiro da lista sempre vai ser o inicial.
        if "[" in linha and "]" in linha:
          partes = linha.split('[', -1)
          if len(partes) == 3: # Sem isso aqui nao funciona ?????
            c1 = partes[1].split(']')[0]
            peso = partes[1].split(']')[1]
            c2 = partes[2].split(']')[0]
            grafo[c1] = peso
            grafo[c2] = peso
  print (grafo)
lerArquivo()

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

