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


def quadrado(square, border):  # Pinta quadrado limpo novamente:
    if border == True and 0 not in square and 9 not in square:
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
        tela.blit(pygame.font.SysFont('Comic Sans MS', 60).render(('As claras venceram.'), False, bege), (100, 280))
        tela.blit(pygame.font.SysFont('Comic Sans MS', 60).render(('Parabéns!!!'), False, bege), (230, 370))
        tela.blit(pygame.font.SysFont('Comic Sans MS', 30).render('Jogar novamente', False, azul), (250, 15))
        pygame.mixer.music.load("Wearethechampions.mp3")
        pygame.mixer.music.play(1)

    if pont_escuras == 12:
        tela.fill(preto) 
        tela.blit(pygame.font.SysFont('Comic Sans MS', 60).render(('As escuras venceram.'), False, bege), (100, 280))
        tela.blit(pygame.font.SysFont('Comic Sans MS', 60).render(('Parabéns!!!'), False, bege), (230, 370))
        tela.blit(pygame.font.SysFont('Comic Sans MS', 30).render('Jogar novamente', False, azul), (250, 15))
        pygame.mixer.music.load("Wearethechampions.mp3")
        pygame.mixer.music.play(1)

def select(pos, possibilidades, turn):
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

    if 'Pdama_clara' in peca:  # movimento dama escura
        if ((pos[0] - 1), (pos[1] + 1)) in values:  # Se houver um inimigo para comer na direita
            for i in range(len(values)):
                if (values[i] == ((pos[0] - 1), (pos[1] + 1))) and ('escura' in keys[i]) and (
                (pos[0] - 2), (pos[1] + 2)) not in values and (pos[0] - 2) != 0 and (pos[0] - 2) != 9 and (
                        pos[1] + 2) != 0 and (pos[1] + 2) != 9:
                    comida.append([keys[i], values[i]])
                    comer += 1
                    pygame.draw.rect(tela, azul, [tamanho * (pos[1] + 2), tamanho * (pos[0] - 2), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] - 2), (pos[1] + 2)))

        if ((pos[0] - 1), (pos[1] - 1)) in values:  # Se houver um inimigo para comer na esquerda
            for i in range(len(values)):
                if (values[i] == ((pos[0] - 1), (pos[1] - 1))) and ('escura' in keys[i]) and (
                (pos[0] - 2), (pos[1] - 2)) not in values and (pos[0] - 2) != 0 and (pos[0] - 2) != 9 and (
                        pos[1] - 2) != 0 and (pos[1] - 2) != 9:
                    comida.append([keys[i], values[i]])
                    comer += 1
                    pygame.draw.rect(tela, azul, [tamanho * (pos[1] - 2), tamanho * (pos[0] - 2), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] - 2), (pos[1] - 2)))

        if ((pos[0] + 1), (pos[1] + 1)) in values:  # Se houver um inimigo para comer no canto inferior direito
            for i in range(len(values)):
                if (values[i] == ((pos[0] + 1), (pos[1] + 1))) and ('escura' in keys[i]) and (
                (pos[0] + 2), (pos[1] + 2)) not in values and (pos[0] + 2) != 0 and (pos[0] + 2) != 9 and (
                        pos[1] + 2) != 0 and (pos[1] + 2) != 9:
                    comida.append([keys[i], values[i]])
                    comer += 1
                    pygame.draw.rect(tela, azul, [tamanho * (pos[1] + 2), tamanho * (pos[0] + 2), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] + 2), (pos[1] + 2)))

        if ((pos[0] + 1), (pos[1] - 1)) in values:  # Se houver um inimigo para comer no canto inferior esquerdo
            for i in range(len(values)):
                if (values[i] == ((pos[0] + 1), (pos[1] - 1))) and ('escura' in keys[i]) and (
                (pos[0] + 2), (pos[1] - 2)) not in values and (pos[0] + 2) != 0 and (pos[0] + 2) != 9 and (
                        pos[1] - 2) != 0 and (pos[1] - 2) != 9:
                    comida.append([keys[i], values[i]])
                    comer += 1
                    pygame.draw.rect(tela, azul, [tamanho * (pos[1] - 2), tamanho * (pos[0] + 2), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] + 2), (pos[1] - 2)))

        if comer == 0: ## apenas se a peca não tiver que comer nenhuma outra o movimento normal sera usado
            if (((pos[0] - 1), pos[1] + 1) not in values) and (pos[0] - 1) != 0 and (pos[0] - 1) != 9 and (pos[1] + 1) != 0 and (pos[1] + 1) != 9:  # Movimento comum
                pygame.draw.rect(tela, azul, [tamanho * (pos[1] + 1), tamanho * (pos[0] - 1), tamanho, tamanho], 5)
                possibilidades.append(((pos[0] - 1), (pos[1] + 1)))

            if (((pos[0] - 1), pos[1] - 1) not in values) and (pos[0] - 1) != 0 and (pos[0] - 1) != 9 and (pos[1] - 1) != 0 and (pos[1] - 1) != 9:  # Movimento comum
                pygame.draw.rect(tela, azul, [tamanho * (pos[1] - 1), tamanho * (pos[0] - 1), tamanho, tamanho], 5)
                possibilidades.append(((pos[0] - 1), (pos[1] - 1)))

    if 'Pdama_escura' in peca:  # movimento da dama escura
        if ((pos[0] + 1), (pos[1] + 1)) in values:  # Se houver um inimigo para comer na direita
            for i in range(len(values)):
                if (values[i] == ((pos[0] + 1), (pos[1] + 1))) and ('clara' in keys[i]) and (
                (pos[0] + 2), (pos[1] + 2)) not in values and (pos[0] + 2) != 0 and (pos[0] + 2) != 9 and (
                        pos[1] + 2) != 0 and (pos[1] + 2) != 9:
                    comida.append([keys[i], values[i]])
                    comer += 1
                    pygame.draw.rect(tela, azul, [tamanho * (pos[1] + 2), tamanho * (pos[0] + 2), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] + 2), (pos[1] + 2)))

        if ((pos[0] + 1), (pos[1] - 1)) in values:  # Se houver um inimigo para comer na esquerda
            for i in range(len(values)):
                if (values[i] == ((pos[0] + 1), (pos[1] - 1))) and ('clara' in keys[i]) and (
                (pos[0] + 2), (pos[1] - 2)) not in values and (pos[0] + 2) != 0 and (pos[0] + 2) != 9 and (
                        pos[1] - 2) != 0 and (pos[1] - 2) != 9:
                    comida.append([keys[i], values[i]])
                    comer += 1
                    pygame.draw.rect(tela, azul, [tamanho * (pos[1] - 2), tamanho * (pos[0] + 2), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] + 2), (pos[1] - 2)))

        if ((pos[0] - 1), (pos[1] + 1)) in values:  # Se houver um inimigo para comer no canto inferior direito
            for i in range(len(values)):
                if (values[i] == ((pos[0] - 1), (pos[1] + 1))) and ('clara' in keys[i]) and (
                (pos[0] - 2), (pos[1] + 2)) not in values and (pos[0] - 2) != 0 and (pos[0] - 2) != 9 and (
                        pos[1] + 2) != 0 and (pos[1] + 2) != 9:
                    comida.append([keys[i], values[i]])
                    comer += 1
                    pygame.draw.rect(tela, azul, [tamanho * (pos[1] + 2), tamanho * (pos[0] - 2), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] - 2), (pos[1] + 2)))

        if ((pos[0] - 1), (pos[1] - 1)) in values:  # Se houver um inimigo para comer no canto inferior esquerdo
            for i in range(len(values)):
                if (values[i] == ((pos[0] - 1), (pos[1] - 1))) and ('clara' in keys[i]) and (
                 (pos[0] - 2), (pos[1] - 2)) not in values and (pos[0] - 2) != 0 and (pos[0] - 2) != 9 and (
                        pos[1] - 2) != 0 and (pos[1] - 2) != 9:
                    comida.append([keys[i], values[i]])
                    comer += 1
                    pygame.draw.rect(tela, azul, [tamanho * (pos[1] - 2), tamanho * (pos[0] - 2), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] - 2), (pos[1] - 2)))

        if comer == 0:
            if (((pos[0] + 1), pos[1] + 1) not in values) and (pos[0] + 1) != 0 and (pos[0] + 1) != 9 and (pos[1] + 1) != 0 and (pos[1] + 1) != 9:  # Movimento comum
                pygame.draw.rect(tela, azul, [tamanho * (pos[1] + 1), tamanho * (pos[0] + 1), tamanho, tamanho], 5)
                possibilidades.append(((pos[0] + 1), (pos[1] + 1)))

            if (((pos[0] + 1), pos[1] - 1) not in values) and (pos[0] + 1) != 0 and (pos[0] + 1) != 9 and (pos[1] - 1) != 0 and (pos[1] - 1) != 9:  # Movimento comum
                pygame.draw.rect(tela, azul, [tamanho * (pos[1] - 1), tamanho * (pos[0] + 1), tamanho, tamanho], 5)
                possibilidades.append(((pos[0] + 1), (pos[1] - 1)))

    # modificar:
    if 'rainha' in peca:  # movimento da rainha:
        exe1,exe2,exe3,exe4 = True,True,True,True
        for casa in range(1, 9): 
            #direita inferior
            if exe1 == True and (((pos[0] + casa), pos[1] - casa) not in values) and (pos[0] + casa) != 0 and (pos[0] + casa) != 9 and (pos[1] - casa) != 0 and (pos[1] - casa) != 9:  # Movimento comum
              pygame.draw.rect(tela, azul, [tamanho * (pos[1] - casa), tamanho * (pos[0] + casa), tamanho, tamanho], 5)
              possibilidades.append(((pos[0] + casa), (pos[1] - casa)))
            elif exe1 == True and ((pos[0] + casa), pos[1] - casa) in values:
                exe1 = False
                for i in range(len(values)): 
                    if values[i] == ((pos[0] + casa), pos[1] - casa) and (('clara' in keys[i] and turn == -1) or ('escura' in keys[i] and turn == 1)) and ((pos[0] + (casa+1)), (pos[1] - (casa + 1))) not in values and ((pos[0] + (casa+1))) != 0 and ((pos[0] + (casa+1))) != 9 and ((pos[1] - (casa+1))) != 0 and ((pos[1] - (casa+1))) != 9:
                        comida.append([keys[i], values[i]])
                        comer += 1
                        pygame.draw.rect(tela, azul, [tamanho * (pos[1] - (casa + 1)), tamanho * (pos[0] + (casa+1)), tamanho, tamanho], 5)
                        possibilidades.append(((pos[0] + (casa+1)), (pos[1] - (casa + 1))))

            #esquerda inferior 
            if exe2 == True and (((pos[0] - casa), pos[1] + casa) not in values) and (pos[0] - casa) != 0 and (pos[0] - casa) != 9 and (pos[1] + casa) != 0 and (pos[1] + casa) != 9:  # Movimento comum
              pygame.draw.rect(tela, azul, [tamanho * (pos[1] + casa), tamanho * (pos[0] - casa), tamanho, tamanho], 5)
              possibilidades.append(((pos[0] - casa), (pos[1] + casa)))
            elif ((pos[0] - casa), pos[1] + casa) in values:
                exe2 = False
                for i in range(len(values)):
                    if values[i] == ((pos[0] - casa), pos[1] + casa) and (('clara' in keys[i] and turn == -1) or ('escura' in keys[i] and turn == 1)) and ((pos[0] - (casa+1)), (pos[1] + (casa + 1))) not in values and ((pos[0] - (casa+1))) != 0 and ((pos[0] - (casa+1))) != 9 and ((pos[1] - (casa+1))) != 0 and ((pos[1] - (casa+1))) != 9:
                        comida.append([keys[i], values[i]])
                        comer += 1
                        pygame.draw.rect(tela, azul, [tamanho * (pos[1] + (casa + 1)), tamanho * (pos[0] - (casa+1)), tamanho, tamanho], 5)
                        possibilidades.append(((pos[0] - (casa+1)), (pos[1] + (casa + 1))))

            #direita superior
            if exe3 == True and (((pos[0] + casa), pos[1] + casa) not in values) and (pos[0] + casa) != 0 and (pos[0] + casa) != 9 and (pos[1] + casa) != 0 and (pos[1] + casa) != 9:  # Movimento comum
              pygame.draw.rect(tela, azul, [tamanho * (pos[1] + casa), tamanho * (pos[0] + casa), tamanho, tamanho], 5)
              possibilidades.append(((pos[0] + casa), (pos[1] + casa)))
            elif ((pos[0] + casa), pos[1] + casa) in values:
                exe3 = False
                for i in range(len(values)):
                    if values[i] == ((pos[0] + casa), pos[1] + casa) and (('clara' in keys[i] and turn == -1) or ('escura' in keys[i] and turn == 1)) and ((pos[0] + (casa+1)), (pos[1] + (casa + 1))) not in values and (pos[0] + (casa+1)) != 0 and (pos[0] + (casa+1)) != 9 and (pos[1] + (casa+1)) != 0 and (pos[1] + (casa+1)) != 9:
                        comida.append([keys[i], values[i]])
                        comer += 1
                        pygame.draw.rect(tela, azul, [tamanho * (pos[1] + (casa + 1)), tamanho * (pos[0] + (casa+1)), tamanho, tamanho], 5)
                        possibilidades.append(((pos[0] + (casa+1)), (pos[1] + (casa + 1))))

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
            peca = keys[j]
            posicoes[peca] = pos  # Mudando a posicao

            if pos[0] == 1 and turn == 1 and 'dama' in peca:  #se tiver dama clara no final do tabuleiro -> rainha clara
                rainha = 'Prainha_clara' + peca[-1] + peca[-2]
                posicoes[rainha] = posicoes[keys[j]]
                del posicoes[keys[j]]
                peca = rainha

            if pos[0] == 8 and turn == -1 and 'dama' in peca:  # se tiver dama escura no final do tabuleiro -> rainha escura
                rainha = 'Prainha_escura' + peca[-1] + peca[-2]
                posicoes[rainha] = posicoes[keys[j]]
                del posicoes[keys[j]]
                peca = rainha

    if comer != 0:
        valores = []
        valores = select(pos, possibilidades, turn)
        for p in range(len(valores[0])):  # Limpando selecao falsa
            quadrado(valores[0][p], True)
        if valores[-1] == 0:
            turn = -turn  # Mudando o turno
    else:
        turn = -turn  # Mudando o turno

    quadrado(Old_Pos, False)  # limpando local anterior da peca

    # Colocando a peca na nova posicao
    if 'dama_clara' in peca:
        tela.blit(dama_clara, (tamanho * pos[1] + 1, tamanho * pos[0] + 1))
    if 'dama_escura' in peca:
        tela.blit(dama_escura, (tamanho * pos[1] + 1, tamanho * pos[0] + 1))
    if 'rainha_clara' in peca:
        tela.blit(rainha_clara, (tamanho * pos[1] + 1, tamanho * pos[0] + 1))
    if 'rainha_escura' in peca:
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
                else:  # movendo 
                    posicoes, turno, possibilidades, OldPos = move(selecao, OldPos, posicoes, turno, possibilidades, comida, comer)
                selecao = ()  # tornar seleçao vazia
                ponts(posicoes) 



            else:
                selecao = (linha, coluna)
                print(selecao)
                if selecao in posicoes.values():  # Apenas se a peca selecionada for a de seu turno
                    for i in range(len(list(posicoes.values()))):
                        if (list(posicoes.values())[i] == selecao) and (((turno == 1) and ('clara' in list(posicoes.keys())[i])) or ((turno == -1) and ('escura' in list(posicoes.keys())[i]))):
                            possibilidades, OldPos, comida, comer = select(selecao, possibilidades, turno)
            pygame.display.update()

pygame.quit()