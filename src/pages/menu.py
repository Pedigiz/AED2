import pygame as pg
import src.styles.color as color

def menu(screen):
    run = True
    while run:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                return 'sair'

        # Preenche a tela com a cor de fundo
        screen.fill(color.black)

        # Dicionário de opções
        acao = {
            'INICIAR': 'game',
            'SAIR': 'sair'
        }

        # Verifica se o botão foi pressionado
        for i, (texto, acao) in enumerate(acao.items()):
            # Desenha os botões na tela
            if color.botao(screen, texto, 300, 200 + i * 100, 200, 50, color.red, color.white, color.black, acao):
                return acao  # Retorna a ação associada ao botão

        # Atualiza a tela para refletir as mudanças
        pg.display.flip()

    # Se o loop terminar, retorna a ação para sair
    return 'sair'
