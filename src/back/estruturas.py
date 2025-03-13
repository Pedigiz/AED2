import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))  # Ajuste o número de parents conforme necessário


import pygame as pg
import src.styles.imagens as imagem

'''
# Lista de Ginasios e Pokemons Selvagens
ginasios = [
    {"pos": pg.Vector2(274, 322), "tamanho": pg.Vector2(90, 90), "imagem": imagem.imagemTransparente},
    {"pos": pg.Vector2(217.967, 193.6), "tamanho": pg.Vector2(90, 90), "imagem": imagem.imagemTransparente},
    {"pos": pg.Vector2(247.667, 99.9), "tamanho": pg.Vector2(90, 90), "imagem": imagem.imagemTransparente},
    {"pos": pg.Vector2(516.167, 97.5333), "tamanho": pg.Vector2(90, 90), "imagem": imagem.imagemTransparente},
    {"pos": pg.Vector2(526.767, 176.9), "tamanho": pg.Vector2(90, 90), "imagem": imagem.imagemTransparente},
]

pokemons = [
    {"pos": pg.Vector2(350, 100), "tamanho": pg.Vector2(20, 70), "imagem": imagem.imagemExclamacao},
    {"pos": pg.Vector2(123, 453), "tamanho": pg.Vector2(20, 70), "imagem": imagem.imagemExclamacao},
    {"pos": pg.Vector2(566, 433), "tamanho": pg.Vector2(20, 70), "imagem": imagem.imagemExclamacao},
    {"pos": pg.Vector2(650, 200), "tamanho": pg.Vector2(20, 70), "imagem": imagem.imagemExclamacao},
]
'''