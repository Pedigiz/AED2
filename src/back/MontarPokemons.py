#ESTE ARQUIVO FICARA RESPONSÁVEL POR LER O CSV E MONTAR AS VARIAVEIS DOS POKEMONS :D
import os
import sys
import pygame as pg
import pandas as pd
import random

def get_pokemon_info(id, dataframe):
    pokemon = dataframe[dataframe['id'] == id]

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
        'habilidade2': habilidades[1] if len(habilidades) > 1 else "Attack",
        'hp': stats_dict.get('hp', 0),
        'attack': stats_dict.get('attack', 0),
        'image': pg.image.load(f"./src/art/pokemons/png_static_pokemons/{int(pokemon['id'])}.png"),
        'capturado': False
    }

df = pd.read_csv("./src/styles/Pokedex/pokedex.csv")


blastoise = get_pokemon_info(9, df)   #blastoise == 9
charizard = get_pokemon_info(6, df)   #charizard == 6
charmander = get_pokemon_info(4, df) #charmander == 4
garchomp = get_pokemon_info(445, df)     #garchomp == 445
gyarados = get_pokemon_info(130, df)     #gyarados == 130
igglybuff = get_pokemon_info(174, df)   #igglybuff == 174
machamp = get_pokemon_info(68, df)       #machamp == 68
mewtwo = get_pokemon_info(150, df)         #mewtwo == 150
pikachu = get_pokemon_info(25, df)       #pikachu == 25
rayquaza = get_pokemon_info(384, df)     #rayquaza == 384
venusaur = get_pokemon_info(3, df)     #venusaur == 3

pokemons_ids = [random.randint(1, 499) for i in range(50)]

pokemon_adversarios = [get_pokemon_info(poke_id, df) for poke_id in pokemons_ids]