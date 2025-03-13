import os
import sys
import pygame as pg

import src.pages.menu as menu

import src.pages.mochila as mochila

import src.pages.game as game

from sys import exit
from pygame.locals import *

import src.back.mechanics as mech

pg.init()

screen = pg.display.set_mode((mech.altura, mech.largura))
pg.display.set_caption('POKEMON FIRE/RED DEEPWEB')

def main():
    cena_atual = 'menu'

   # Dicionário que mapeia cenas para funções correspondentes
    cenas = {
    'menu': menu.menu,        # Chama a função menu() dentro do módulo menu.py
    'mochila': mochila.mochila,  # Chama a função mochila() dentro do módulo mochila.py
    'game': game.game       # Chama a função start() dentro do módulo game.py
    }


    while True:
        print(f'Executando cena: {cena_atual}')

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            
        if cena_atual == "sair":
            print("adios\n")
            pg.quit()
            sys.exit()

        # Verifica se a cena atual está no dicionário
        if cena_atual in cenas:
            cena_atual = cenas[cena_atual](screen)
        else:
            print(f"Cena inválida: {cena_atual}")
            break

#if __name__ == "_main_":
main()