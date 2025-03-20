import pygame as pg

pg.init()

fonte = pg.font.SysFont("courier new", 20)

red = (255,0,0)
black = (0,0,0)
white = (255,255,255)
green = (0, 255, 0)
blue = (0, 0, 255)

def botao(screen, texto, x, y, largura, altura, cor_borda, cor_texto, cor_fundo, acao):
    global fonte
    texto_surface = fonte.render(texto, True, cor_texto)
    texto_rect = texto_surface.get_rect(center=(x + largura // 2, y + altura // 2))

    # Desenha o botão
    pg.draw.rect(screen, cor_fundo, (x, y, largura, altura))
    pg.draw.rect(screen, cor_borda, (x, y, largura, altura), 3)  # Borda do botão
    screen.blit(texto_surface, texto_rect)

    # Verifica se o mouse está sobre o botão e se o clique foi feito
    mouse_pos = pg.mouse.get_pos()
    mouse_click = pg.mouse.get_pressed()

    if (x <= mouse_pos[0] <= x + largura) and (y <= mouse_pos[1] <= y + altura):
        if mouse_click[0]:  # Se o clique do botão esquerdo do mouse for detectado
            return True  # O botão foi pressionado
    return False