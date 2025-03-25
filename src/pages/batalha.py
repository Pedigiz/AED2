import pygame as pg
import time
import sys
import os
import random
import math

import src.styles.imagens as imagem
import src.styles.color as color
import src.back.mechanics as mech
import src.back.MontarPokemons as pokemon
import src.pages.mochila as mochila

def batalha(screen):
    running = True
    clock = pg.time.Clock()

    #Aleatorizar pokemon adv
    poke_alea = random.randint(0, 49)
    pokemonAdv = pokemon.pokemon_adversarios[poke_alea]
    #Seu pokemon
    meuPokemon = mochila.pokemonsSetados[0]

    pg.display.set_caption('POKEMON FIRE/RED DEEPWEB')

    #Redimencionar imagem da arena
    arena_scale = pg.transform.scale(imagem.arena, (800, 600))

    while running:
        screen.fill(color.black)  # Pintar fundo de preto
        screen.blit(arena_scale, (0,-50))
        pg.draw.rect(screen, color.black, (0, 450, 800, 200))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 'sair'
        
        keys = pg.key.get_pressed()
        if keys[pg.K_p] and 'batalha':
            time.sleep(0.1)
            return 'game'  # Voltar para o jogo

        #PAINEL DE INFORMAÇOES ---------------------------
        screen.blit(pg.transform.scale(meuPokemon['image'], (150, 150)), (150, 300))

        Info_Batalha(screen, "HP: " + str(f'{meuPokemon['hp']:.2f}'), 10, 450)
        Info_Batalha(screen, "Attack: " + str(meuPokemon['attack']), 10, 480)
        Info_Batalha(screen, "Habilidade1: " + str(meuPokemon['habilidade1']), 10, 520)
        pg.draw.rect(screen, color.white, (5, 516, 350, 30), 2)
        Info_Batalha(screen, "Habilidade2: " + str(meuPokemon['habilidade2']), 10, 560)
        pg.draw.rect(screen, color.white, (5, 556, 350, 30), 2)

        #Pokemon adversario
        screen.blit(pg.transform.scale(pokemonAdv['image'], (150, 150)), (530, 300))

        Info_Batalha(screen, "HP: " + str(f'{pokemonAdv['hp']:.2f}'), 670, 450)
        Info_Batalha(screen, "Attack: " + str(pokemonAdv['attack']), 670, 480)
        Info_Batalha(screen, "Habilidade1: " + str(pokemonAdv['habilidade1']), 450, 520)
        pg.draw.rect(screen, color.white, (445, 516, 350, 30), 2)
        Info_Batalha(screen, "Habilidade2: " + str(pokemonAdv['habilidade2']), 450, 560)
        pg.draw.rect(screen, color.white, (445, 556, 350, 30), 2)
        #--------------------------------------------------


        #---------------------------BATALHA----------------------------------------------
        if keys[pg.K_1] and 'batalha':
            time.sleep(0.1)
            atacar(meuPokemon, pokemonAdv, screen, 1)

            pg.time.wait(1000)

            #Checar vida
            if (testeVida(meuPokemon, pokemonAdv, screen)):
                return 'game'

            #Pokemon adversarioataca
            habAdv = random.randint(1, 2)
            atacar(pokemonAdv, meuPokemon, screen, habAdv)

            #Checar vida
            if (testeVida(meuPokemon, pokemonAdv, screen)):
                return 'game'
            
        if keys[pg.K_2] and 'batalha':
            time.sleep(0.1)
            atacar(meuPokemon, pokemonAdv, screen, 2)

            #Checar vida
            if (testeVida(meuPokemon, pokemonAdv, screen)):
                return 'game'

            time.sleep(1)

            #Pokemon adversarioataca
            habAdv = random.randint(1, 2)
            atacar(pokemonAdv, meuPokemon, screen, habAdv)

            #Checar vida
            if (testeVida(meuPokemon, pokemonAdv, screen)):
                return 'game'

        #--------------------------------------------------------------------------------


        pg.display.flip()  # Atualizar tela
        clock.tick(20)  # Limitar a 60 FPS  -- Aqui é 10 pra nn bugar 


    return 'menu'  # Se sair do loop, pode retornar para o menu



def Info_Batalha(screen, mensagem, x, y):
    text_surface = color.fonte.render(mensagem, True, color.white)
    # Desenhar texto sobre o retângulo
    screen.blit(text_surface, (x, y))

def calculardano(attack):
    multiplicador_dano = random.uniform(0, 0.5)

    return multiplicador_dano * attack

def atacar(Pokemon_atacante, pokemon_apanhante, screen, habilidade):
    if habilidade == 1:
        mech.popup_text = str(Pokemon_atacante['nome']) + " atacou com " + str(Pokemon_atacante['habilidade1'])
    else:
        mech.popup_text = str(Pokemon_atacante['nome']) + " atacou com " + str(Pokemon_atacante['habilidade2'])

    mech.exibir_popup(screen, mech.popup_text)
    mech.popup_timer = 2000
    timerpopup(screen)
    
    pokemon_apanhante['hp'] -= calculardano(Pokemon_atacante['attack'])


def timerpopup(screen):
    while mech.popup_timer > 0:
        if mech.popup_text and mech.popup_timer > 0:
            mech.exibir_popup(screen, mech.popup_text)
            mech.popup_timer -= 1

            pg.display.flip()  # Atualizar tela


def testeVida(meuPokemon, pokemonAdv, screen):
    if ((meuPokemon['hp'] <= 0) and 'batalha'):
        mech.popup_text = "Você perdeu a batalha!"
        mech.exibir_popup(screen, mech.popup_text)
        mech.popup_timer = 2000
        timerpopup(screen)

        return True
    
    elif (pokemonAdv['hp'] <= 0):
        mech.popup_text = "Você ganhou a batalha!"
        mech.exibir_popup(screen, mech.popup_text)
        mech.popup_timer = 2000
        timerpopup(screen)

        return True
    
    return False