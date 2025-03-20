#ESTE ARQUIVO FICARA RESPONSÁVEL POR LER O CSV E MONTAR AS VARIAVEIS DOS POKEMONS :D
import os
import sys
import pygame as pg
#import pandas as pd

def get_pokemon_info(pokemon_name, dataframe):
    pokemon = dataframe[dataframe['nome'].str.lower() == pokemon_name.lower()]

    if pokemon.empty:
        return None

    pokemon = pokemon.iloc[0]
    
    tipos = pokemon['tipos'].replace("[", "").replace("]", "").replace("'", "").split(", ")
    habilidades = pokemon['habilidades'].replace("[", "").replace("]", "").replace("'", "").split(", ")
    
    stats = pokemon['stats']
    stats = stats.replace("{", "").replace("}", "").split(", ")
    stats_dict = {}
    for stat in stats:
        chave, valor = stat.split(": ")
        stats_dict[chave.strip("'")] = int(valor)

    return {
        'id': int(pokemon['id']),
        'nome': pokemon['nome'],
        'tipos': tipos,
        'habilidade1': habilidades[0] if len(habilidades) > 0 else None,
        'habilidade2': habilidades[1] if len(habilidades) > 1 else None,
        'hp': stats_dict.get('hp', 0),
        'attack': stats_dict.get('attack', 0),
        'image': pg.image.load(f"./src/art/pokemons/png_static_pokemons/{int(pokemon['id'])}.png"),
        'capturado': False
    }
'''
df = pd.read_csv("./src/styles/Pokedex/pokedex.csv")


blastoise = get_pokemon_info("blastoise", df)
charizard = get_pokemon_info("charizard", df)
charmander = get_pokemon_info("charmander", df)
garchomp = get_pokemon_info("garchomp", df)
gyarados = get_pokemon_info("gyarados", df)
igglybuff = get_pokemon_info("igglybuff", df)
machamp = get_pokemon_info("machamp", df)
mewtwo = get_pokemon_info("mewtwo", df)
pikachu = get_pokemon_info("pikachu", df)
rayquaza = get_pokemon_info("rayquaza", df)
venusaur = get_pokemon_info("venusaur", df)

blastoise['capturado'] = True
rayquaza['capturado'] = True
mewtwo['capturado'] = True'
'''