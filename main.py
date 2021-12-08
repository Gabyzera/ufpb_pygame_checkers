import pygame
from pontuacao import ponts
from movimentacao import move, select, pode_comer
from iniciar_jogo import Start, tamanho

pygame.init()

modo = 1
sprites = [None]*4
posicoes, sprites[0],sprites[1],sprites[2],sprites[3] = Start(modo)  # Iniciando o Jogo
jogo = True
selecao = ()  # Tupla para armazenar selecao do jogador inicialmente vazia
possibilidades = [] ## lista para armazenar para onde o jogador podera se movimentar, inicialmente vazia
turno = 1 ## Turno que ira iniciar nas brancas
OldPos = 0 ## Posicao anterior
comida = [0] ## Pecas que podem ser capturadas
comer = 0 ## contador de possibilidades de captura
sopro = False ## Verificador caso haja possibilidade de captura faça com que o jogador seja obrigado a capturar
while jogo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo = False

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            location = pygame.mouse.get_pos()  # (x, y) localização do mouse
            coluna = location[0] // tamanho
            linha = location[1] // tamanho
            if selecao == (linha, coluna):
                if selecao == (0, 3) or selecao == (0, 4) or selecao == (0, 5) or selecao == (0, 6):  # Recomeçar
                    posicoes,sprites[0],sprites[1],sprites[2],sprites[3] = Start(modo)
                    turno = 1
                if selecao == (0, 1) or selecao == (0, 0):
                    modo = -modo
                    posicoes,sprites[0],sprites[1],sprites[2],sprites[3] = Start(modo)
                    turno = 1
                elif 0 not in selecao:  # movendo 
                    posicoes, turno, possibilidades, OldPos = move(selecao, OldPos, posicoes, turno, possibilidades, comida, comer, sprites)
                selecao = ()  # tornar seleçao vazia
                ponts(posicoes)
                sopro = pode_comer(turno, posicoes, possibilidades) 

            else:
                selecao = (linha, coluna)
                print(selecao)
                if selecao in posicoes.values():  # Apenas se a peca selecionada for a de seu turno
                    for i in range(len(list(posicoes.values()))):
                        if (list(posicoes.values())[i] == selecao) and (((turno == 1) and ('clara' in list(posicoes.keys())[i])) or ((turno == -1) and ('escura' in list(posicoes.keys())[i]))):
                            possibilidades, OldPos, comida, comer = select(selecao, posicoes, possibilidades, turno, sopro, True)
            pygame.display.update()

pygame.quit()