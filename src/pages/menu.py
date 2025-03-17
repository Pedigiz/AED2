import pygame as pg
import src.styles.color as color
import src.styles.imagens as imagem
import src.back.mechanics as mech

def menu(screen):

    screen.fill(color.black)
    pg.display.set_caption('POKEMON FIRE/RED DEEPWEB')

    #Teste nn sei, não consigo colocar imagem no fundo pqp
    menu_scale_certo = pg.transform.scale(imagem.menu_meme, (mech.altura, mech.largura))

    run = True

    while run:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                return 'sair'

        #Imagem de fundo do menu
        screen.blit(menu_scale_certo, (0, 0))

        # Dicionário de opções
        acao = {
            'INICIAR': 'game',
            'SAIR': 'sair'
        }

        # Verifica se o botão foi pressionado
        for i, (texto, acao) in enumerate(acao.items()):
            # Desenha os botões na tela
            if color.botao(screen, texto, 500, 400 + i * 100, 200, 50, color.blue, color.black, color.white, acao):
                return acao  # Retorna a ação associada ao botão

        # Atualiza a tela para refletir as mudanças
        pg.display.flip()

    # Se o loop terminar, retorna a ação para sair
    return 'sair'
