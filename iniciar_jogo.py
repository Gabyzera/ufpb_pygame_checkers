import pygame

# Tabela de cores
preto = (0, 0, 0)
marrom = (150, 75, 0)
bege = (245, 245, 220)
azul = (0, 225, 255)
verde = (0, 255, 0)

tamanho = 70  # tamanho de cada quadrado
linhas_colunas = 8
tela = pygame.display.set_mode(((linhas_colunas + 2) * tamanho, (linhas_colunas + 2) * tamanho))
nome = pygame.display.set_caption('Damas | Chekers')

# Funcoes
def Start(modo):
    tela.fill(preto)
    tela.blit(pygame.font.SysFont('Comic Sans MS', 30).render('RECOMEÇAR', False, azul), (250, 15))
    tela.blit(pygame.font.SysFont('Comic Sans MS', 30).render('UFPB', False, bege), (550, 15))
    tela.blit(pygame.transform.scale(pygame.image.load("assets/sprites/ufpb.png"), (tamanho, tamanho)), (tamanho * 9, tamanho * 0))
    pygame.draw.ellipse(tela, verde, [15, tamanho * 3 + 15, 40, 40])

    # adicionando sprites:
    if modo == 1:
        tela.blit(pygame.font.SysFont('Comic Sans MS', 30).render('3° IDADE', False, azul), (0, 15))
        dama_clara = pygame.transform.scale(pygame.image.load("assets/sprites/dama_v4.png"), (tamanho - 2, tamanho - 2))
        dama_escura = pygame.transform.scale(pygame.image.load("assets/sprites/dama_v3.png"), (tamanho - 2, tamanho - 2))
        rainha_clara = pygame.transform.scale(pygame.image.load("assets/sprites/rainha_v4.png"), (tamanho - 2, tamanho - 2))
        rainha_escura = pygame.transform.scale(pygame.image.load("assets/sprites/rainha_v3.png"), (tamanho - 2, tamanho - 2))
    else:
        tela.blit(pygame.font.SysFont('Comic Sans MS', 30).render('CLASSICO', False, azul), (0, 15))
        dama_clara = pygame.transform.scale(pygame.image.load("assets/sprites/dama_v2.png"), (tamanho - 2, tamanho - 2))
        dama_escura = pygame.transform.scale(pygame.image.load("assets/sprites/dama_v1.png"), (tamanho - 2, tamanho - 2))
        rainha_clara = pygame.transform.scale(pygame.image.load("assets/sprites/rainha_v2.png"), (tamanho - 2, tamanho - 2))
        rainha_escura = pygame.transform.scale(pygame.image.load("assets/sprites/rainha_v1.png"), (tamanho - 2, tamanho - 2))

    count = 0
    for i in range(1, linhas_colunas + 1):
        for j in range(1, linhas_colunas + 1):
            if count % 2 == 0:
                pygame.draw.rect(tela, bege, [tamanho * j, tamanho * i, tamanho, tamanho])
            else:
                pygame.draw.rect(tela, marrom, [tamanho * j, tamanho * i, tamanho, tamanho])
            count += 1
        count -= 1

    # colocando pecas:
    for i in range(2, 9, 2):
        tela.blit(dama_clara, (tamanho * i + 1, tamanho * 7 + 1))
        tela.blit(dama_escura, (tamanho * i + 1, tamanho * 1 + 1))
        tela.blit(dama_escura, (tamanho * i + 1, tamanho * 3 + 1))
    for i in range(1, 9, 2):
        tela.blit(dama_escura, (tamanho * i + 1, tamanho * 2 + 1))
        tela.blit(dama_clara, (tamanho * i + 1, tamanho * 6 + 1))
        tela.blit(dama_clara, (tamanho * i + 1, tamanho * 8 + 1))
    tela.blit(dama_clara, (tamanho * 0 + 1, tamanho * 4 + 1))
    tela.blit(pygame.font.SysFont('Comic Sans MS', 30).render('0', False, bege), (25, 360))
    tela.blit(dama_escura, (tamanho * 9 + 1, tamanho * 4 + 1))
    tela.blit(pygame.font.SysFont('Comic Sans MS', 30).render('0', False, bege), (655, 360))

    pygame.display.update()

    # Guardando posições iniciais das peças no sistema
    posicoes_iniciais = {'Pdama_clara01': (6, 1), 'Pdama_clara02': (6, 3), 'Pdama_clara03': (6, 5),
                         'Pdama_clara04': (6, 7), 'Pdama_clara05': (7, 2), 'Pdama_clara06': (7, 4),
                         'Pdama_clara07': (7, 6), 'Pdama_clara08': (7, 8), 'Pdama_clara09': (8, 1),
                         'Pdama_clara10': (8, 3), 'Pdama_clara11': (8, 5), 'Pdama_clara12': (8, 7),
                         'Pdama_escura01': (3, 2), 'Pdama_escura02': (3, 4), 'Pdama_escura03': (3, 6), 'Pdama_escura04': (3, 8),
                         'Pdama_escura05': (2, 1), 'Pdama_escura06': (2, 3), 'Pdama_escura07': (2, 5), 'Pdama_escura08': (2, 7),
                         'Pdama_escura09': (1, 2), 'Pdama_escura10': (1, 4), 'Pdama_escura11': (1, 6),
                         'Pdama_escura12': (1, 8)}

    return posicoes_iniciais, dama_clara, dama_escura, rainha_clara, rainha_escura