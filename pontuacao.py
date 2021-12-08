import pygame
from iniciar_jogo import tamanho, tela, bege, preto, azul

def ponts(posicoes):
    pont_claras = 0
    pont_escuras = 0
    values = list(posicoes.values())
    keys = list(posicoes.keys())
    for p in range(len(keys)):
        if 'clara' in keys[p]:
            if values[p] == None:
                pont_escuras += 1
        if 'escura' in keys[p]:
            if values[p] == None:
                pont_claras += 1

    pygame.draw.rect(tela, preto, [tamanho * 9, tamanho * 5, tamanho, tamanho])
    pygame.draw.rect(tela, preto, [tamanho * 0, tamanho * 5, tamanho, tamanho])
    tela.blit(pygame.font.SysFont('Comic Sans MS', 30).render(str(pont_claras), False, bege), (25, 360))
    tela.blit(pygame.font.SysFont('Comic Sans MS', 30).render(str(pont_escuras), False, bege), (655, 360))
    
    if pont_claras == 12:
        tela.fill(preto) 
        tela.blit(pygame.font.SysFont('Comic Sans MS', 60).render(('As claras venceram.'), False, bege), (90, 280))
        tela.blit(pygame.font.SysFont('Comic Sans MS', 60).render(('Parabéns!!!'), False, bege), (230, 370))
        tela.blit(pygame.font.SysFont('Comic Sans MS', 30).render('Jogar novamente', False, azul), (250, 15))
        pygame.mixer.music.load("assets\sounds\Wearethechampions.mp3")
        pygame.mixer.music.play(1)

    if pont_escuras == 12:
        tela.fill(preto) 
        tela.blit(pygame.font.SysFont('Comic Sans MS', 60).render(('As escuras venceram.'), False, bege), (100, 280))
        tela.blit(pygame.font.SysFont('Comic Sans MS', 60).render(('Parabéns!!!'), False, bege), (230, 370))
        tela.blit(pygame.font.SysFont('Comic Sans MS', 30).render('Jogar novamente', False, azul), (250, 15))
        pygame.mixer.music.load("assets\sounds\Wearethechampions.mp3")
        pygame.mixer.music.play(1)