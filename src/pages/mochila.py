import pygame as pg
import time
import sys
import os
import math


import src.styles.imagens as imagem
import src.styles.color as color
import src.back.mechanics as mech
import src.back.MontarPokemons as pokemon

pokemon_posicoes = {
    'charizard': (91, 104),
    'charmander': (302, 115),
    'venusaur': (494, 111),
    'blastoise': (701, 109),
    'pikachu': (80, 275),
    'igglybuff': (275, 275),
    'gyarados': (460, 255),
    'rayquaza': (640, 220),
    'garchomp': (50, 450),
    'mewtwo': (270, 460),
    'machamp': (512, 505)
}

def mochila(screen):
    indice_frame = 0
    running = True
    clock = pg.time.Clock()

    pg.display.set_caption('POKEMON FIRE/RED DEEPWEB')

    #Redimencionar imagem do gato xd
    mochila_gato_meme = pg.transform.scale(imagem.show_pokemons_backpack, (200, 200))
    inventario_scale = pg.transform.scale(imagem.inventario, (800, 600))

    #Carregar os sprites dos pokemons
    #Explicação das linhas:
    #os.listdir: Lista todos os arquivos na pasta
    #os.path.join(charizardSprite, f) junta o caminho do arquivo
    base_dir = os.path.dirname(__file__)
    
    for i in ['charizard', 'charmander', 'venusaur', 'blastoise', 'pikachu', 'igglybuff', 'gyarados', 'rayquaza',
              'garchomp', 'mewtwo', 'machamp']:
        caminho_completo = os.path.join(base_dir, "..", "art", "pokemons", "sprites", f"{i}_sprite")
        
        poke_sprite = sorted([(os.path.join(caminho_completo, f), int(f.split('\\')[-1].split('.')[0])) for f in os.listdir(caminho_completo)], key=lambda x: x[1])
        
        sprites = ([pg.image.load(os.path.join(f[0])) for f in poke_sprite])

        match i:
            case "charizard":
                charizard_sprite = sprites
            case "charmander":
                charmander_sprite = sprites
            case "venusaur":
                venusaur_sprite = sprites
            case "blastoise":
                blastoise_sprite = sprites
            case "pikachu":
                pikachu_sprite = sprites
            case "igglybuff":
                igglybuff_sprites = sprites
            case "gyarados":
                gyarados_sprite = sprites
            case "rayquaza":
                rayquaza_sprite = sprites
            case "garchomp":
                garchomp_sprite = sprites
            case "mewtwo":
                mewtwo_sprite = sprites
            case "machamp":
                machamp_sprite = sprites

    while running:
        screen.fill(color.black)  # Pintar fundo de preto
        screen.blit(inventario_scale, (0,0))
        screen.blit(mochila_gato_meme, (600,400))

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                mensagemDosPokemonsParaBatalha = pokemonsBatalha()  
                     
            if event.type == pg.QUIT:
                return 'sair'

        keys = pg.key.get_pressed()
        if keys[pg.K_i] and 'mochila':
            time.sleep(0.1)
            return 'game'  # Voltar para o jogo
        
        #-------------------------DESENHAR OS SPRITES-------------------------------------
        if (pokemon.charizard['capturado'] == True):     # X e Y
            screen.blit(charizard_sprite[indice_frame], (50, 10))  #Desenhar o frame atual
        else:
            screen.blit(pokemon.charizard['image'], (50, 50))

        if (pokemon.charmander['capturado'] == True):
            screen.blit(charmander_sprite[indice_frame], (280, 80))
        else:
            screen.blit(pokemon.charmander['image'], (260, 80))

        if (pokemon.venusaur['capturado'] == True):
            screen.blit(venusaur_sprite[indice_frame], (450, 60))
        else:
            screen.blit(pokemon.venusaur['image'], (450, 60))

        if (pokemon.blastoise['capturado'] == True):
            screen.blit(blastoise_sprite[indice_frame], (650, 60))
        else:
            screen.blit(pokemon.blastoise['image'], (650, 60))

        if (pokemon.pikachu['capturado'] == True):
            screen.blit(pikachu_sprite[indice_frame], (80, 275))
        else:
            screen.blit(pokemon.pikachu['image'], (60, 275))

        if (pokemon.igglybuff['capturado'] == True):
            screen.blit(igglybuff_sprites[indice_frame], (275, 275))
        else:
            screen.blit(pokemon.igglybuff['image'], (255, 275))

        if (pokemon.gyarados['capturado'] == True):
            screen.blit(gyarados_sprite[indice_frame], (460, 255))
        else:
            screen.blit(pokemon.gyarados['image'], (460, 255))

        if (pokemon.rayquaza['capturado'] == True):
            screen.blit(rayquaza_sprite[indice_frame], (640, 220))
        else:
            screen.blit(pokemon.rayquaza['image'], (640, 250))

        if (pokemon.garchomp['capturado'] == True):
            screen.blit(garchomp_sprite[indice_frame], (50, 450))
        else:
            screen.blit(pokemon.garchomp['image'], (50, 450))

        if (pokemon.mewtwo['capturado'] == True):
            screen.blit(mewtwo_sprite[indice_frame], (270, 460))
        else:
            screen.blit(pokemon.mewtwo['image'], (260, 460))

        if (pokemon.machamp['capturado'] == True):
            screen.blit(machamp_sprite[indice_frame], (460, 460))
        else:
            screen.blit(pokemon.machamp['image'], (460, 460))

        # Atualizar frame
        indice_frame = (indice_frame + 1) % 46 #São 46 imagens de pokemons em cada sprite
        #---------------------------------------------------------------------------------

        pg.display.flip()  # Atualizar tela
        clock.tick(20)  # Limitar a 60 FPS  -- Aqui é 10 pra nn bugar 

        if mech.popup_text and mech.popup_timer > 0:
            mech.exibir_popup(screen, mech.popup_text)
            mech.popup_timer -= 1
    
        def pokemonsBatalha():
            raio = 50
            pokemonsSetados = list()
            mech.verificaMouse()
            clique_x, clique_y = mech.mouse_pos

            for nome, (px, py) in pokemon_posicoes.items():
                distancia = math.sqrt((clique_x - px) ** 2 + (clique_y - py) ** 2)
                if len(pokemonsSetados) >= 3:
                    pokemonsSetados.pop(0)
                    if distancia <= raio and getattr(pokemon, nome)['capturado']:
                        print(f"{nome.upper()} foi selecionado!")
                        pokemonsSetados.append(getattr(pokemon, nome))

                if distancia <= raio and getattr(pokemon, nome)['capturado']:
                    print(f"{nome.upper()} foi selecionado!")
                    pokemonsSetados.append(getattr(pokemon, nome))

            pokemons_nomes = [p['nome'] for p in pokemonsSetados]
            return f"Pokémons escolhidos: {', '.join(pokemons_nomes)}"


    return 'menu'  # Se sair do loop, pode retornar para o menu


