import pygame as pg

mapa = pg.image.load("./src/art/mapa/MAPA_POKEMON.jpg")

menu_meme = pg.image.load("./src/art/menus/menu.jpg")

show_pokemons_backpack = pg.image.load("./src/art/menus/show_pokemons.jpg")

inventario = pg.image.load("./src/art/menus/inventario4x3.png")

idle = []
walkUp = []
walkDown = []
walkLeftDown = []
walkRightDown = []
walkLeftUp = []
walkRightUp = []

for i in range(1, 8) :
    idle.append(pg.transform.scale(pg.image.load(f"./src/art/player/Walk/Idle_Down/{i}.png"), (96, 128)))
    walkUp.append(pg.transform.scale(pg.image.load(f"./src/art/player/Walk/walk_Up/{i}.png"), (96, 128)))
    walkDown.append(pg.transform.scale(pg.image.load(f"./src/art/player/Walk/walk_Down/{i}.png"), (96, 128)))
    walkLeftDown.append(pg.transform.scale(pg.image.load(f"./src/art/player/Walk/walk_Left_Down/{i}.png"), (96, 128)))
    walkRightDown.append(pg.transform.scale(pg.image.load(f"./src/art/player/Walk/walk_Right_Down/{i}.png"), (96, 128)))
    walkLeftUp.append(pg.transform.scale(pg.image.load(f"./src/art/player/Walk/walk_Left_Up/{i}.png"), (96, 128)))
    walkRightUp.append(pg.transform.scale(pg.image.load(f"./src/art/player/Walk/walk_Right_Up/{i}.png"), (96, 128)))