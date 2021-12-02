import pygame

pygame.init()
# Tabela de cores
preto = (0, 0, 0)
marrom = (150, 75, 0)
bege = (245, 245, 220)
azul = (0, 225, 255)

tamanho = 70  # tamanho de cada quadrado
linhas_colunas = 8

tela = pygame.display.set_mode(((linhas_colunas + 2) * tamanho, (linhas_colunas + 2) * tamanho))
nome = pygame.display.set_caption('Damas | Chekers')

# adicionando sprites:
dama_clara = pygame.transform.scale(pygame.image.load("assets/sprites/dama_v2.png"), (tamanho - 2, tamanho - 2))
dama_escura = pygame.transform.scale(pygame.image.load("assets/sprites/dama_v1.png"), (tamanho - 2, tamanho - 2))
rainha_clara = pygame.transform.scale(pygame.image.load("assets/sprites/rainha_v1.png"), (tamanho - 2, tamanho - 2))
rainha_escura = pygame.transform.scale(pygame.image.load("assets/sprites/rainha_v2.png"), (tamanho - 2, tamanho - 2))

# Funcoes
def Start():
    tela.fill(preto)
    tela.blit(pygame.font.SysFont('Comic Sans MS', 30).render('RECOMEÇAR', False, azul), (250, 15))

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
    for i in range(2, 9,2):
        tela.blit(dama_clara, (tamanho * i + 1, tamanho * 7 + 1))
        tela.blit(dama_escura, (tamanho * i + 1, tamanho * 1 + 1))
        tela.blit(dama_escura, (tamanho * i + 1, tamanho * 3 + 1))
    for i in range(1, 9, 2):
        tela.blit(dama_escura, (tamanho * i + 1, tamanho * 2 + 1))
        tela.blit(dama_clara, (tamanho * i + 1, tamanho * 6 + 1))
        tela.blit(dama_clara, (tamanho * i + 1, tamanho * 8 + 1))

    pygame.display.update()

    # Guardando posições iniciais das peças no sistema
    posicoes_iniciais = {'Pdama_branca1': (6, 1), 'Pdama_branca2':(6,3), 'Pdama_branca3':(6,5), 'Pdama_branca4':(6,7), 'Pdama_branca5':(7,2), 'Pdama_branca6':(7,4),'Pdama_branca7':(7,6), 'Pdama_branca8':(7,8),'Pdama_branca9':(8,1),'Pdama_branca10':(8,3),'Pdama_branca11':(8,5),'Pdama_branca12':(8,7), 'Pdama_preta1': (3, 2), 'Pdama_preta2':(3,4), 'Pdama_preta3':(3,6), 'Pdama_preta4':(3,8), 'Pdama_preta5':(2,1), 'Pdama_preta6':(2,3),'Pdama_preta7':(2,5), 'Pdama_preta8':(2,7),'Pdama_preta9':(1,2),'Pdama_preta10':(1,4),'Pdama_preta11':(1,6),'Pdama_preta12':(1,8)}

    return posicoes_iniciais


def quadrado(square, border):   # Pinta quadrado limpo novamente:
    if border == True:
        if ((((square[0]) % 2) == 0) and (((square[1]) % 2) != 0)) or (
                (((square[0]) % 2) != 0) and (((square[1]) % 2) == 0)):
            pygame.draw.rect(tela, marrom, [tamanho * (square[1]), tamanho * (square[0]), tamanho, tamanho], 5)
        else:
            pygame.draw.rect(tela, bege, [tamanho * (square[1]), tamanho * (square[0]), tamanho, tamanho], 5)
    elif border == False:
        if ((((square[0]) % 2) == 0) and (((square[1]) % 2) != 0)) or (
                (((square[0]) % 2) != 0) and (((square[1]) % 2) == 0)):
            pygame.draw.rect(tela, marrom, [tamanho * (square[1]), tamanho * (square[0]), tamanho, tamanho])
        else:
            pygame.draw.rect(tela, bege, [tamanho * (square[1]), tamanho * (square[0]), tamanho, tamanho])


def select(pos, possibilidades, turn):

    keys = list(posicoes.keys())
    values = list(posicoes.values())
    peca = ''
    for i in range(len(values)):  # mostrando qual peca foi selecionada
        if values[i] == pos:
            peca = keys[i]

    if possibilidades != []:  # Limpando selecoes
        for p in range(len(possibilidades)):
            quadrado(possibilidades[p], True)
        possibilidades = []

    if 'Pdama_branca' in peca:  # movimento do peao
            if ((pos[0] - 1), (pos[1] + 1)) in values:  # Se houver um inimigo para comer na direita
                for i in range(len(values)):
                    if (values[i] == ((pos[0] - 1), (pos[1] + 1))) and ('preta' in keys[i]) and ((pos[0] - 2), (pos[1] + 2)) not in values and (pos[0] - 2) != 0 and (pos[0] - 2) != 9 and (pos[1] + 2) != 0 and (pos[1] + 2) != 9:
                        pygame.draw.rect(tela, azul, [tamanho * (pos[1] + 2), tamanho * (pos[0] - 2), tamanho, tamanho],5)
                        possibilidades.append(((pos[0] - 2), (pos[1] + 2)))

            elif ((pos[0] - 1), (pos[1] - 1)) in values:  # Se houver um inimigo para comer na esquerda
                for i in range(len(values)):
                    if (values[i] == ((pos[0] - 1), (pos[1] - 1))) and ('preta' in keys[i]) and ((pos[0] - 2), (pos[1] - 2)) not in values and (pos[0] - 2) != 0 and (pos[0] - 2) != 9 and (pos[1] - 2) != 0 and (pos[1] - 2) != 9:
                        pygame.draw.rect(tela, azul, [tamanho * (pos[1] - 2), tamanho * (pos[0] - 2), tamanho, tamanho],5)
                        possibilidades.append(((pos[0] - 2), (pos[1] - 2)))

            else:
                if (((pos[0] - 1), pos[1] +1) not in values) and (pos[0] - 1) != 0 and (pos[0] - 1) != 9 and (pos[1] +1) != 0 and (pos[1] +1) != 9:  # Movimento comum
                  pygame.draw.rect(tela, azul, [tamanho * (pos[1]+1), tamanho * (pos[0] - 1), tamanho, tamanho], 5)
                  possibilidades.append(((pos[0] - 1), (pos[1]+1)))
                if (((pos[0] - 1), pos[1] -1) not in values) and (pos[0] - 1) != 0 and (pos[0] - 1) != 9 and (pos[1] -1) != 0 and (pos[1] -1) != 9:  # Movimento comum
                  pygame.draw.rect(tela, azul, [tamanho * (pos[1]-1), tamanho * (pos[0] - 1), tamanho, tamanho], 5)
                  possibilidades.append(((pos[0] - 1), (pos[1]-1)))


    if 'Pdama_preta' in peca:  # movimento do peao preto
            if ((pos[0] + 1), (pos[1] + 1)) in values:  # Se houver um inimigo para comer na direita
                for i in range(len(values)):
                    if (values[i] == ((pos[0] + 1), (pos[1] + 1))) and ('branca' in keys[i]) and ((pos[0] + 2), (pos[1] + 2)) not in values and (pos[0] + 2) != 0 and (pos[0] + 2) != 9 and (pos[1] + 2) != 0 and (pos[1] + 2) != 9:
                        pygame.draw.rect(tela, azul, [tamanho * (pos[1] + 2), tamanho * (pos[0] + 2), tamanho, tamanho],5)
                        possibilidades.append(((pos[0] + 2), (pos[1] + 2)))

            elif ((pos[0] + 1), (pos[1] - 1)) in values:  # Se houver um inimigo para comer na esquerda
                for i in range(len(values)):
                    if (values[i] == ((pos[0] + 1), (pos[1] - 1))) and ('branca' in keys[i]) and ((pos[0] + 2), (pos[1] - 2)) not in values and (pos[0] + 2) != 0 and (pos[0] + 2) != 9 and (pos[1] - 2) != 0 and (pos[1] - 2) != 9:
                        pygame.draw.rect(tela, azul, [tamanho * (pos[1] - 2), tamanho * (pos[0] + 2), tamanho, tamanho],5)
                        possibilidades.append(((pos[0] + 2), (pos[1] - 2)))

            else:
                if (((pos[0] + 1), pos[1] +1) not in values) and (pos[0] + 1) != 0 and (pos[0] + 1) != 9 and (pos[1] +1) != 0 and (pos[1] +1) != 9:  # Movimento comum
                  pygame.draw.rect(tela, azul, [tamanho * (pos[1]+1), tamanho * (pos[0] + 1), tamanho, tamanho], 5)
                  possibilidades.append(((pos[0] + 1), (pos[1]+1)))
                if (((pos[0] + 1), pos[1] -1) not in values) and (pos[0] + 1) != 0 and (pos[0] + 1) != 9 and (pos[1] - 1) != 0 and (pos[1] -1) != 9:  # Movimento comum
                  pygame.draw.rect(tela, azul, [tamanho * (pos[1]-1), tamanho * (pos[0] + 1), tamanho, tamanho], 5)
                  possibilidades.append(((pos[0] + 1), (pos[1]-1)))

    return possibilidades, pos


def move(pos, Old_Pos, posicoes, turn, possibilidades):

    for p in range(len(possibilidades)):  # Limpando selecao
        quadrado(possibilidades[p], True)

    keys = list(posicoes.keys())
    values = list(posicoes.values())

    if pos not in possibilidades and pos != Old_Pos:  # Para que o jogador siga as regras
        pygame.mixer.music.load("assets/sounds/wrong.ogg")
        pygame.mixer.music.play(1)
        return posicoes, turn, possibilidades

    if pos in possibilidades and pos != Old_Pos:
        pygame.mixer.music.load("assets/sounds/move.ogg")
        pygame.mixer.music.play(1)

    if pos != Old_Pos:
        print('aqui')
        turn = -turn  # Mudando o turno

    if pos in values:
        for i in range(len(values)):  # Retirando a peça anterior da memoria em caso de comer
            if values[i] == pos:
                posicoes[keys[i]] = None
                quadrado(pos, False)

    peca = ''
    for j in range(len(values)):  # Mostrando qual peca vai ser movida
        if values[j] == Old_Pos:
            peca = keys[j]
            posicoes[peca] = pos  # Mudando a posicao

    quadrado(Old_Pos, False)  # limpando local anterior da peca

    # Colocando a peca na nova posicao
    if 'dama_branca' in peca:
        tela.blit(dama_clara, (tamanho * pos[1] + 1, tamanho * pos[0] + 1))
    if 'dama_preta' in peca:
        tela.blit(dama_escura, (tamanho * pos[1] + 1, tamanho * pos[0] + 1))
    if 'rainha_branca' in peca:
        tela.blit(rainha_clara, (tamanho * pos[1] + 1, tamanho * pos[0] + 1))
    if 'rainha_preta' in peca:
        tela.blit(rainha_escura, (tamanho * pos[1] + 1, tamanho * pos[0] + 1))

    return posicoes, turn, possibilidades


posicoes = Start()  # Iniciando o Jogo
jogo = True
selecao = ()  # tupla para armazenar selecao do jogador
possibilidades = []
turno = 1
OldPos = 0
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
                    posicoes = Start()
                    turno = 1
                else:  # Movendo
                    posicoes, turno, possibilidades = move(selecao, OldPos, posicoes, turno, possibilidades)
                selecao = ()  # tornar seleçao vazia

            else:
                selecao = (linha, coluna)
                print(selecao)
                if selecao in posicoes.values():  # Apenas se a peca selecionada for a de seu turno
                    for i in range(len(list(posicoes.values()))):
                        if (list(posicoes.values())[i] == selecao) and (
                                ((turno == 1) and ('branca' in list(posicoes.keys())[i])) or (
                                (turno == -1) and ('preta' in list(posicoes.keys())[i]))):
                            possibilidades, OldPos = select(selecao, possibilidades, turno)
            pygame.display.update()

pygame.quit()
