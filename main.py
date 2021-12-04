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

# Funcoes
def Start(modo):
    tela.fill(preto)
    tela.blit(pygame.font.SysFont('Comic Sans MS', 30).render('RECOMEÇAR', False, azul), (250, 15))
    tela.blit(pygame.font.SysFont('Comic Sans MS', 30).render('UFPB', False, bege), (550, 15))
    tela.blit(pygame.transform.scale(pygame.image.load("assets/sprites/ufpb.png"), (tamanho, tamanho)), (tamanho * 9, tamanho * 0))

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
    tela.blit(pygame.font.SysFont('Comic Sans MS', 30).render('0', False, bege), (30, 360))
    tela.blit(dama_escura, (tamanho * 9 + 1, tamanho * 4 + 1))
    tela.blit(pygame.font.SysFont('Comic Sans MS', 30).render('0', False, bege), (660, 360))

    pygame.display.update()

    # Guardando posições iniciais das peças no sistema
    posicoes_iniciais = {'Pdama_branca1': (6, 1), 'Pdama_branca2': (6, 3), 'Pdama_branca3': (6, 5),
                         'Pdama_branca4': (6, 7), 'Pdama_branca5': (7, 2), 'Pdama_branca6': (7, 4),
                         'Pdama_branca7': (7, 6), 'Pdama_branca8': (7, 8), 'Pdama_branca9': (8, 1),
                         'Pdama_branca10': (8, 3), 'Pdama_branca11': (8, 5), 'Pdama_branca12': (8, 7),
                         'Pdama_preta1': (3, 2), 'Pdama_preta2': (3, 4), 'Pdama_preta3': (3, 6), 'Pdama_preta4': (3, 8),
                         'Pdama_preta5': (2, 1), 'Pdama_preta6': (2, 3), 'Pdama_preta7': (2, 5), 'Pdama_preta8': (2, 7),
                         'Pdama_preta9': (1, 2), 'Pdama_preta10': (1, 4), 'Pdama_preta11': (1, 6),
                         'Pdama_preta12': (1, 8)}

    return posicoes_iniciais, dama_clara, dama_escura, rainha_clara, rainha_escura


def quadrado(square, border):  # Pinta quadrado limpo novamente:
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


def ponts(posicoes):
    pont_claras = 0
    pont_escuras = 0
    claras = list(posicoes.values())[12:]
    escuras = list(posicoes.values())[:12]
    for p in claras:
        if p == None:
            pont_claras += 1
    for p in escuras:
        if p == None:
            pont_escuras += 1

    pygame.draw.rect(tela, preto, [tamanho * 9, tamanho * 5, tamanho, tamanho])
    pygame.draw.rect(tela, preto, [tamanho * 0, tamanho * 5, tamanho, tamanho])
    tela.blit(pygame.font.SysFont('Comic Sans MS', 30).render(str(pont_claras), False, bege), (30, 360))
    tela.blit(pygame.font.SysFont('Comic Sans MS', 30).render(str(pont_escuras), False, bege), (660, 360))

def select(pos, possibilidades):
    print('run')
    keys = list(posicoes.keys())
    values = list(posicoes.values())
    peca = ''
    comida = [0]
    comer = 0

    for i in range(len(values)):  # mostrando qual peca foi selecionada
        if values[i] == pos:
            peca = keys[i]

    if possibilidades != []:  # Limpando selecoes
        for p in range(len(possibilidades)):
            quadrado(possibilidades[p], True)
        possibilidades = []

    if 'Pdama_branca' in peca:  # movimento do peao branco
        if ((pos[0] - 1), (pos[1] + 1)) in values:  # Se houver um inimigo para comer na direita
            for i in range(len(values)):
                if (values[i] == ((pos[0] - 1), (pos[1] + 1))) and ('preta' in keys[i]) and (
                (pos[0] - 2), (pos[1] + 2)) not in values and (pos[0] - 2) != 0 and (pos[0] - 2) != 9 and (
                        pos[1] + 2) != 0 and (pos[1] + 2) != 9:
                    comida.append([keys[i], values[i]])
                    comer += 1
                    pygame.draw.rect(tela, azul, [tamanho * (pos[1] + 2), tamanho * (pos[0] - 2), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] - 2), (pos[1] + 2)))

        if ((pos[0] - 1), (pos[1] - 1)) in values:  # Se houver um inimigo para comer na esquerda
            for i in range(len(values)):
                if (values[i] == ((pos[0] - 1), (pos[1] - 1))) and ('preta' in keys[i]) and (
                (pos[0] - 2), (pos[1] - 2)) not in values and (pos[0] - 2) != 0 and (pos[0] - 2) != 9 and (
                        pos[1] - 2) != 0 and (pos[1] - 2) != 9:
                    comida.append([keys[i], values[i]])
                    comer += 1
                    pygame.draw.rect(tela, azul, [tamanho * (pos[1] - 2), tamanho * (pos[0] - 2), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] - 2), (pos[1] - 2)))

        if ((pos[0] + 1), (pos[1] + 1)) in values:  # Se houver um inimigo para comer no canto inferior direito
            for i in range(len(values)):
                if (values[i] == ((pos[0] + 1), (pos[1] + 1))) and ('preta' in keys[i]) and (
                (pos[0] + 2), (pos[1] + 2)) not in values and (pos[0] + 2) != 0 and (pos[0] + 2) != 9 and (
                        pos[1] + 2) != 0 and (pos[1] + 2) != 9:
                    comida.append([keys[i], values[i]])
                    comer += 1
                    pygame.draw.rect(tela, azul, [tamanho * (pos[1] + 2), tamanho * (pos[0] + 2), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] + 2), (pos[1] + 2)))

        if ((pos[0] + 1), (pos[1] - 1)) in values:  # Se houver um inimigo para comer no canto inferior esquerdo
            for i in range(len(values)):
                if (values[i] == ((pos[0] + 1), (pos[1] - 1))) and ('preta' in keys[i]) and (
                (pos[0] + 2), (pos[1] - 2)) not in values and (pos[0] + 2) != 0 and (pos[0] + 2) != 9 and (
                        pos[1] - 2) != 0 and (pos[1] - 2) != 9:
                    comida.append([keys[i], values[i]])
                    comer += 1
                    pygame.draw.rect(tela, azul, [tamanho * (pos[1] - 2), tamanho * (pos[0] + 2), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] + 2), (pos[1] - 2)))

        if (((pos[0] - 1), pos[1] + 1) not in values) and (pos[0] - 1) != 0 and (pos[0] - 1) != 9 and (
                pos[1] + 1) != 0 and (pos[1] + 1) != 9:  # Movimento comum
            pygame.draw.rect(tela, azul, [tamanho * (pos[1] + 1), tamanho * (pos[0] - 1), tamanho, tamanho], 5)
            possibilidades.append(((pos[0] - 1), (pos[1] + 1)))

        if (((pos[0] - 1), pos[1] - 1) not in values) and (pos[0] - 1) != 0 and (pos[0] - 1) != 9 and (
                pos[1] - 1) != 0 and (pos[1] - 1) != 9:  # Movimento comum
            pygame.draw.rect(tela, azul, [tamanho * (pos[1] - 1), tamanho * (pos[0] - 1), tamanho, tamanho], 5)
            possibilidades.append(((pos[0] - 1), (pos[1] - 1)))

    if 'Pdama_preta' in peca:  # movimento do peao preto
        if ((pos[0] + 1), (pos[1] + 1)) in values:  # Se houver um inimigo para comer na direita
            for i in range(len(values)):
                if (values[i] == ((pos[0] + 1), (pos[1] + 1))) and ('branca' in keys[i]) and (
                (pos[0] + 2), (pos[1] + 2)) not in values and (pos[0] + 2) != 0 and (pos[0] + 2) != 9 and (
                        pos[1] + 2) != 0 and (pos[1] + 2) != 9:
                    comida.append([keys[i], values[i]])
                    comer += 1
                    pygame.draw.rect(tela, azul, [tamanho * (pos[1] + 2), tamanho * (pos[0] + 2), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] + 2), (pos[1] + 2)))

        if ((pos[0] + 1), (pos[1] - 1)) in values:  # Se houver um inimigo para comer na esquerda
            for i in range(len(values)):
                if (values[i] == ((pos[0] + 1), (pos[1] - 1))) and ('branca' in keys[i]) and (
                (pos[0] + 2), (pos[1] - 2)) not in values and (pos[0] + 2) != 0 and (pos[0] + 2) != 9 and (
                        pos[1] - 2) != 0 and (pos[1] - 2) != 9:
                    comida.append([keys[i], values[i]])
                    comer += 1
                    pygame.draw.rect(tela, azul, [tamanho * (pos[1] - 2), tamanho * (pos[0] + 2), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] + 2), (pos[1] - 2)))

        if ((pos[0] - 1), (pos[1] + 1)) in values:  # Se houver um inimigo para comer no canto inferior direito
            for i in range(len(values)):
                if (values[i] == ((pos[0] - 1), (pos[1] + 1))) and ('branca' in keys[i]) and (
                (pos[0] - 2), (pos[1] + 2)) not in values and (pos[0] - 2) != 0 and (pos[0] - 2) != 9 and (
                        pos[1] + 2) != 0 and (pos[1] + 2) != 9:
                    comida.append([keys[i], values[i]])
                    comer += 1
                    pygame.draw.rect(tela, azul, [tamanho * (pos[1] + 2), tamanho * (pos[0] - 2), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] - 2), (pos[1] + 2)))

        if ((pos[0] - 1), (pos[1] - 1)) in values:  # Se houver um inimigo para comer no canto inferior esquerdo
            for i in range(len(values)):
                if (values[i] == ((pos[0] - 1), (pos[1] - 1))) and ('branca' in keys[i]) and (
                 (pos[0] - 2), (pos[1] - 2)) not in values and (pos[0] - 2) != 0 and (pos[0] - 2) != 9 and (
                        pos[1] - 2) != 0 and (pos[1] - 2) != 9:
                    comida.append([keys[i], values[i]])
                    comer += 1
                    pygame.draw.rect(tela, azul, [tamanho * (pos[1] - 2), tamanho * (pos[0] - 2), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] - 2), (pos[1] - 2)))

        if (((pos[0] + 1), pos[1] + 1) not in values) and (pos[0] + 1) != 0 and (pos[0] + 1) != 9 and (
                pos[1] + 1) != 0 and (pos[1] + 1) != 9:  # Movimento comum
            pygame.draw.rect(tela, azul, [tamanho * (pos[1] + 1), tamanho * (pos[0] + 1), tamanho, tamanho], 5)
            possibilidades.append(((pos[0] + 1), (pos[1] + 1)))

        if (((pos[0] + 1), pos[1] - 1) not in values) and (pos[0] + 1) != 0 and (pos[0] + 1) != 9 and (
                pos[1] - 1) != 0 and (pos[1] - 1) != 9:  # Movimento comum
            pygame.draw.rect(tela, azul, [tamanho * (pos[1] - 1), tamanho * (pos[0] + 1), tamanho, tamanho], 5)
            possibilidades.append(((pos[0] + 1), (pos[1] - 1)))

    # modificar:
    if 'rainha_branca' in peca:  # movimento da rainha branca:
        for c in range(len(values)):
            if (pos[0] + c, pos[1] + c) in values:  # Se houver inimigo para comer na diagonal inferior direita
                for i in range(len(values)):
                    if values[i] == (pos[0] + c, pos[1] + c) or values[i] == (pos[0] + 1, pos[1] - c) and \
                            'preta' in keys[i] and (pos[0] + c + 1, pos[1] + c + 1) not in values and \
                            pos[0] + c != 0 and pos[0] + c != 9 and pos[1] + c != 0 and \
                            pos[1] + c != 9:
                        comida.append([keys[i], values[i]])
                        comer += 1
                        pygame.draw.rect(tela, azul, [tamanho * (pos[1] + c + 1), tamanho * (pos[0] + c + 1), tamanho,
                                                      tamanho], 5)
                        possibilidades.append(((pos[0] + c + 1), (pos[1] + c + 1)))

    return possibilidades, pos, comida, comer


def move(pos, Old_Pos, posicoes, turn, possibilidades, comida, comer):

    for p in range(len(possibilidades)):  # Limpando selecao
        quadrado(possibilidades[p], True)

    peca = ''
    keys = list(posicoes.keys())
    values = list(posicoes.values())

    if pos not in possibilidades and pos != Old_Pos:  # Para que o jogador siga as regras
        pygame.mixer.music.load("assets/sounds/wrong.ogg")
        pygame.mixer.music.play(1)
        return posicoes, turn, possibilidades, Old_Pos

    if pos in possibilidades and pos != Old_Pos:
        pygame.mixer.music.load("assets/sounds/move.ogg")
        pygame.mixer.music.play(1)

    if comer != 0 and pos != Old_Pos:
        if comer == 1:
            posicoes[comida[1][0]] = None
            quadrado(comida[1][1], False)
        if comer == 2:
            for c in range(comer):
                if pos == possibilidades[c]:
                    posicoes[comida[c + 1][0]] = None
                    quadrado(comida[c + 1][1], False)

    for j in range(len(values)):  # Mostrando qual peca vai ser movida
        if values[j] == Old_Pos:
            print(values[j], keys[j])
            peca = keys[j]
            posicoes[peca] = pos  # Mudando a posicao

            if pos[0] == 1 and turn == 1:  #se tiver dama branca no final do tabuleiro -> rainha branca
                posicoes['rainha_branca'] = posicoes[keys[j]]
                del posicoes[keys[j]]
                peca = 'rainha_branca'

            if pos[0] == 8 and turn == -1:  # se tiver dama preta no final do tavuleiro -> rainha preta
                posicoes['rainha_preta'] = posicoes[keys[j]]
                del posicoes[keys[j]]
                peca = 'rainha_preta'


    print(peca)

    if pos != Old_Pos:
        turn = -turn  # Mudando o turno


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

    return posicoes, turn, possibilidades, Old_Pos ## trocar ultimo valor por 'pos' para resolver erro

modo = -1
posicoes,dama_clara, dama_escura, rainha_clara,rainha_escura = Start(modo)  # Iniciando o Jogo
jogo = True
selecao = ()  # tupla para armazenar selecao do jogador
possibilidades = []
turno = 1
OldPos = 0
comida = [0]
comer = 0
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
                    posicoes,dama_clara, dama_escura, rainha_clara,rainha_escura = Start(modo)
                    turno = 1
                if selecao == (0, 1) or selecao == (0, 0):
                    modo = -modo
                    posicoes,dama_clara, dama_escura, rainha_clara,rainha_escura = Start(modo)
                    turno = 1
                else:  # Movendo
                    posicoes, turno, possibilidades, OldPos = move(selecao, OldPos, posicoes, turno, possibilidades, comida, comer)
                selecao = ()  # tornar seleçao vazia
                ponts(posicoes)

            else:
                selecao = (linha, coluna)
                print(selecao)
                if selecao in posicoes.values():  # Apenas se a peca selecionada for a de seu turno
                    for i in range(len(list(posicoes.values()))):
                        if (list(posicoes.values())[i] == selecao) and (
                                ((turno == 1) and ('branca' in list(posicoes.keys())[i])) or (
                                (turno == -1) and ('preta' in list(posicoes.keys())[i]))):
                            possibilidades, OldPos, comida, comer = select(selecao, possibilidades)
            pygame.display.update()

pygame.quit()