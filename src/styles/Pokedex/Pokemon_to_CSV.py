import requests
import pandas as pd

def obter_dados_pokemon(pokemon):
      url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}/"
      resposta = requests.get(url)

      if resposta.status_code == 200:
          dados = resposta.json() #O método .json() interpreta o conteúdo da resposta como um JSON e converte para uma estrutura que a gente consegue ler
                                  #Como dicionários ou listas

          #GAMBIARRA, NEM SEI PQ TA AQUI
          #Compressão de dict. Extrai os stats do Pokémon da resposta JSON e cria um dicionário contendo os nomes dos stats como chaves e os valores base desses stats como valores.
          stats = {stat['stat']['name']: stat['base_stat'] for stat in dados['stats']} #dict para os stats dos pokemons

          pokedex = {
              'id': dados['id'],
              'nome': dados['name'],
              'peso': dados['weight'],
              'altura': dados['height'],

              #Como o pokemon pode ter +1 tipos, hab, moves, armazena eles em lista e dicionario
              'tipos': [tipo['type']['name'] for tipo in dados['types']],
              'habilidades': [habilidade['ability']['name'] for habilidade in dados['abilities']],
              #'movimentos': [{'nome': movimento['move']['name'], 'tipo': movimento['move']['name']} for movimento in dados['moves']],
              'stats': stats
          }
          return pokedex
      else:
          print("Erro no numero" + pokemon + "\n")
          return None
      
def imprime_dados_pokemon(pokemon_pesquisa):
  print("\nInformações do Pokémons:")
  print(f"ID: {pokemon_pesquisa['id']}")
  print(f"Nome: {pokemon_pesquisa['nome']}")
  print(f"Peso: {pokemon_pesquisa['peso']/10} kgs")
  print(f"Altura: {pokemon_pesquisa['altura']/10} metros")
  print("\nTipos:", ", ".join(pokemon_pesquisa['tipos']))
  print("\nHabilidades:", ", ".join(pokemon_pesquisa['habilidades']))
  print("\nStats:")
  for stat_name, value in pokemon_pesquisa['stats'].items():
      print(f"  {stat_name}: {value}")


#Pegar uns 50 pokemons #FODA
numero_pokemons = 500
pokedex = [] #Criar uma lista para guardar os dicionarios

for pokemon in range(1, numero_pokemons):
    info_pokemon = obter_dados_pokemon(pokemon)

    if(info_pokemon):
        pokedex.append(info_pokemon)


#Salvar em CSV
df = pd.DataFrame(pokedex)
df.to_csv("pokedex.csv", index=False, encoding="utf-8")

print("\nPokédex salva como 'pokedex.csv'!")