#Importamos o módulo sys para utilizar o valor de infinito (sys.maxsize) na inicialização das distâncias
import sys

listaGinasios = ["alola","kanto","johto", "hoenn", "sinnoh"]

# Leitura dos arquivos
def lerArquivo():
  global grafo
  global ginasioinicial
  global pokemoninicial
  global pokemonfinal
  global grafo
  grafo = dict()
  listapokemon = list()
  with open ('./src/config/config_1.txt', 'r') as arquivo: # Abrir os arquivos
    conteudo = arquivo.read().replace("[","").replace("]", "").split("\n",-1)
    
    ginasioinicial = conteudo[0]
    pokemoninicial = conteudo[2] 
    pokemonfinal = conteudo[-1] # Contem o pokemon do ultimo ginasio

    for linha in conteudo[3: -1]:
      partes = linha.split()
      #print(partes)
      if len(partes) == 3: # Sem isso aqui nao funciona ?????
        c1 = partes[0]
        peso = int(partes[1])
        c2 = partes[2]

        if c1 not in grafo:
          grafo[c1] = {}
        if c2 not in grafo:
          grafo[c2] = {}

        # Adicionando conexão bidirecional
        grafo[c1][c2] = peso
        grafo[c2][c1] = peso
    
    #print(grafo)
    
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

      if vertice_atual is None:  # Se não houver vértice acessível, para o loop
        break

      # Marca o vértice atual como visitado
      visitados.add(vertice_atual)
      # Atualiza as distâncias dos vértices vizinhos
      for vizinho, peso in grafo[vertice_atual].items():
          if distancias[vertice_atual] + peso < distancias[vizinho]:
              distancias[vizinho] = distancias[vertice_atual] + peso

  # Retorna as distâncias mais curtas a partir da origem
  return distancias

# Como sabemos que vamos usar podemos calcular o dikstra para cada "origem" vou salvar um calculo de todos
def calculaDistanciasGinasios(): # Esta me retornando um dicionario
  resultados = dict() 
  for ginasios in listaGinasios:
    resultados [ginasios] = calcular_dijkstra(grafo,ginasios)
  return resultados

print (calculaDistanciasGinasios())