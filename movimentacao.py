import pygame
from iniciar_jogo import tamanho, tela, marrom, bege, azul, preto, verde, Start

def quadrado(square, border):  # Pinta quadrado limpo novamente:
    if border == True and 0 not in square and 9 not in square:
        if ((((square[0]) % 2) == 0) and (((square[1]) % 2) > 0)) or (
                (((square[0]) % 2) > 0) and (((square[1]) % 2) == 0)):
            pygame.draw.rect(tela, marrom, [tamanho * (square[1]), tamanho * (square[0]), tamanho, tamanho], 5)
        else:
            pygame.draw.rect(tela, bege, [tamanho * (square[1]), tamanho * (square[0]), tamanho, tamanho], 5)
    elif border == False:
        if ((((square[0]) % 2) == 0) and (((square[1]) % 2) > 0)) or (
                (((square[0]) % 2) > 0) and (((square[1]) % 2) == 0)):
            pygame.draw.rect(tela, marrom, [tamanho * (square[1]), tamanho * (square[0]), tamanho, tamanho])
        else:
            pygame.draw.rect(tela, bege, [tamanho * (square[1]), tamanho * (square[0]), tamanho, tamanho])

def select(pos, posicoes, possibilidades, turn, sopro, desenhar):
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

    if 'Pdama_clara' in peca:  # movimento dama clara
        if ((pos[0] - 1), (pos[1] + 1)) in values:  # Se houver um inimigo para comer na direita
            for i in range(len(values)):
                if (values[i] == ((pos[0] - 1), (pos[1] + 1))) and ('escura' in keys[i]) and (
                (pos[0] - 2), (pos[1] + 2)) not in values and (pos[0] - 2) > 0 and (pos[0] - 2) < 9 and (
                        pos[1] + 2) > 0 and (pos[1] + 2) < 9:
                    comida.append([keys[i], values[i]])
                    comer += 1
                    if desenhar == True:
                        pygame.draw.rect(tela, azul, [tamanho * (pos[1] + 2), tamanho * (pos[0] - 2), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] - 2), (pos[1] + 2)))

        if ((pos[0] - 1), (pos[1] - 1)) in values:  # Se houver um inimigo para comer na esquerda
            for i in range(len(values)):
                if (values[i] == ((pos[0] - 1), (pos[1] - 1))) and ('escura' in keys[i]) and (
                (pos[0] - 2), (pos[1] - 2)) not in values and (pos[0] - 2) > 0 and (pos[0] - 2) < 9 and (
                        pos[1] - 2) > 0 and (pos[1] - 2) < 9:
                    comida.append([keys[i], values[i]])
                    comer += 1
                    if desenhar == True:
                        pygame.draw.rect(tela, azul, [tamanho * (pos[1] - 2), tamanho * (pos[0] - 2), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] - 2), (pos[1] - 2)))

        if ((pos[0] + 1), (pos[1] + 1)) in values:  # Se houver um inimigo para comer no canto inferior direito
            for i in range(len(values)):
                if (values[i] == ((pos[0] + 1), (pos[1] + 1))) and ('escura' in keys[i]) and (
                (pos[0] + 2), (pos[1] + 2)) not in values and (pos[0] + 2) > 0 and (pos[0] + 2) < 9 and (
                        pos[1] + 2) > 0 and (pos[1] + 2) < 9:
                    comida.append([keys[i], values[i]])
                    comer += 1
                    if desenhar == True:
                        pygame.draw.rect(tela, azul, [tamanho * (pos[1] + 2), tamanho * (pos[0] + 2), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] + 2), (pos[1] + 2)))

        if ((pos[0] + 1), (pos[1] - 1)) in values:  # Se houver um inimigo para comer no canto inferior esquerdo
            for i in range(len(values)):
                if (values[i] == ((pos[0] + 1), (pos[1] - 1))) and ('escura' in keys[i]) and (
                (pos[0] + 2), (pos[1] - 2)) not in values and (pos[0] + 2) > 0 and (pos[0] + 2) < 9 and (
                        pos[1] - 2) > 0 and (pos[1] - 2) < 9:
                    comida.append([keys[i], values[i]])
                    comer += 1
                    if desenhar == True:
                        pygame.draw.rect(tela, azul, [tamanho * (pos[1] - 2), tamanho * (pos[0] + 2), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] + 2), (pos[1] - 2)))

        if comer == 0 and sopro == False: ## apenas se a peca não tiver que comer nenhuma outra o movimento normal sera usado
            if (((pos[0] - 1), pos[1] + 1) not in values) and (pos[0] - 1) > 0 and (pos[0] - 1) < 9 and (pos[1] + 1) > 0 and (pos[1] + 1) < 9:  # Movimento comum
                if desenhar == True:
                    pygame.draw.rect(tela, azul, [tamanho * (pos[1] + 1), tamanho * (pos[0] - 1), tamanho, tamanho], 5)
                possibilidades.append(((pos[0] - 1), (pos[1] + 1)))

            if (((pos[0] - 1), pos[1] - 1) not in values) and (pos[0] - 1) > 0 and (pos[0] - 1) < 9 and (pos[1] - 1) > 0 and (pos[1] - 1) < 9:  # Movimento comum
                if desenhar == True:
                    pygame.draw.rect(tela, azul, [tamanho * (pos[1] - 1), tamanho * (pos[0] - 1), tamanho, tamanho], 5)
                possibilidades.append(((pos[0] - 1), (pos[1] - 1)))

    if 'Pdama_escura' in peca:  # movimento da dama escura
        if ((pos[0] + 1), (pos[1] + 1)) in values:  # Se houver um inimigo para comer na direita
            for i in range(len(values)):
                if (values[i] == ((pos[0] + 1), (pos[1] + 1))) and ('clara' in keys[i]) and (
                (pos[0] + 2), (pos[1] + 2)) not in values and (pos[0] + 2) > 0 and (pos[0] + 2) < 9 and (
                        pos[1] + 2) > 0 and (pos[1] + 2) < 9:
                    comida.append([keys[i], values[i]])
                    comer += 1
                    if desenhar == True:
                        pygame.draw.rect(tela, azul, [tamanho * (pos[1] + 2), tamanho * (pos[0] + 2), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] + 2), (pos[1] + 2)))

        if ((pos[0] + 1), (pos[1] - 1)) in values:  # Se houver um inimigo para comer na esquerda
            for i in range(len(values)):
                if (values[i] == ((pos[0] + 1), (pos[1] - 1))) and ('clara' in keys[i]) and (
                (pos[0] + 2), (pos[1] - 2)) not in values and (pos[0] + 2) > 0 and (pos[0] + 2) < 9 and (
                        pos[1] - 2) > 0 and (pos[1] - 2) < 9:
                    comida.append([keys[i], values[i]])
                    comer += 1
                    if desenhar == True:
                        pygame.draw.rect(tela, azul, [tamanho * (pos[1] - 2), tamanho * (pos[0] + 2), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] + 2), (pos[1] - 2)))

        if ((pos[0] - 1), (pos[1] + 1)) in values:  # Se houver um inimigo para comer no canto inferior direito
            for i in range(len(values)):
                if (values[i] == ((pos[0] - 1), (pos[1] + 1))) and ('clara' in keys[i]) and (
                (pos[0] - 2), (pos[1] + 2)) not in values and (pos[0] - 2) > 0 and (pos[0] - 2) < 9 and (
                        pos[1] + 2) > 0 and (pos[1] + 2) < 9:
                    comida.append([keys[i], values[i]])
                    comer += 1
                    if desenhar == True:
                        pygame.draw.rect(tela, azul, [tamanho * (pos[1] + 2), tamanho * (pos[0] - 2), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] - 2), (pos[1] + 2)))

        if ((pos[0] - 1), (pos[1] - 1)) in values:  # Se houver um inimigo para comer no canto inferior esquerdo
            for i in range(len(values)):
                if (values[i] == ((pos[0] - 1), (pos[1] - 1))) and ('clara' in keys[i]) and (
                 (pos[0] - 2), (pos[1] - 2)) not in values and (pos[0] - 2) > 0 and (pos[0] - 2) < 9 and (
                        pos[1] - 2) > 0 and (pos[1] - 2) < 9:
                    comida.append([keys[i], values[i]])
                    comer += 1
                    if desenhar == True:
                        pygame.draw.rect(tela, azul, [tamanho * (pos[1] - 2), tamanho * (pos[0] - 2), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] - 2), (pos[1] - 2)))

        if comer == 0 and sopro == False:
            if (((pos[0] + 1), pos[1] + 1) not in values) and (pos[0] + 1) > 0 and (pos[0] + 1) < 9 and (pos[1] + 1) > 0 and (pos[1] + 1) < 9:  # Movimento comum
                if desenhar == True:
                    pygame.draw.rect(tela, azul, [tamanho * (pos[1] + 1), tamanho * (pos[0] + 1), tamanho, tamanho], 5)
                possibilidades.append(((pos[0] + 1), (pos[1] + 1)))

            if (((pos[0] + 1), pos[1] - 1) not in values) and (pos[0] + 1) > 0 and (pos[0] + 1) < 9 and (pos[1] - 1) > 0 and (pos[1] - 1) < 9:  # Movimento comum
                if desenhar == True:
                    pygame.draw.rect(tela, azul, [tamanho * (pos[1] - 1), tamanho * (pos[0] + 1), tamanho, tamanho], 5)
                possibilidades.append(((pos[0] + 1), (pos[1] - 1)))

    # modificar:
    if 'rainha' in peca:  # movimento da rainha:
        for casa in range(1, 9): 

            for j in range(len(values)): 
                break_move = [False,False,False,False]

                if values[j] == ((pos[0] + casa), pos[1] - casa) and (('clara' in keys[j] and turn == -1) or ('escura' in keys[j] and turn == 1)) and ((pos[0] + (casa+1)), (pos[1] - (casa + 1))) not in values and ((pos[0] + (casa+1))) > 0 and ((pos[0] + (casa+1))) < 9 and ((pos[1] - (casa+1))) > 0 and ((pos[1] - (casa+1))) < 9:
                    comida.append([keys[j], values[j]])
                    comer += 1
                    if desenhar == True:
                        pygame.draw.rect(tela, azul, [tamanho * (pos[1] - (casa + 1)), tamanho * (pos[0] + (casa+1)), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] + (casa+1)), (pos[1] - (casa + 1))))

                if values[j] == ((pos[0] - casa), pos[1] + casa) and (('clara' in keys[j] and turn == -1) or ('escura' in keys[j] and turn == 1)) and ((pos[0] - (casa+1)), (pos[1] + (casa + 1))) not in values and ((pos[0] - (casa+1))) > 0 and ((pos[0] - (casa+1))) < 9 and ((pos[1] + (casa+1))) > 0 and ((pos[1] + (casa+1))) < 9:
                    comida.append([keys[j], values[j]])
                    comer += 1
                    if desenhar == True:
                        pygame.draw.rect(tela, azul, [tamanho * (pos[1] + (casa + 1)), tamanho * (pos[0] - (casa+1)), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] - (casa+1)), (pos[1] + (casa + 1))))

                if values[j] == ((pos[0] + casa), pos[1] + casa) and (('clara' in keys[j] and turn == -1) or ('escura' in keys[j] and turn == 1)) and ((pos[0] + (casa+1)), (pos[1] + (casa + 1))) not in values and ((pos[0] + (casa+1))) > 0 and ((pos[0] + (casa+1))) < 9 and ((pos[1] + (casa+1))) > 0 and ((pos[1] + (casa+1))) < 9:
                    comida.append([keys[j], values[j]])
                    comer += 1
                    if desenhar == True:
                        pygame.draw.rect(tela, azul, [tamanho * (pos[1] + (casa + 1)), tamanho * (pos[0] + (casa+1)), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] + (casa+1)), (pos[1] + (casa + 1))))

                if values[j] == ((pos[0] - casa), pos[1] - casa) and (('clara' in keys[j] and turn == -1) or ('escura' in keys[j] and turn == 1)) and ((pos[0] - (casa+1)), (pos[1] - (casa + 1))) not in values and ((pos[0] - (casa+1))) > 0 and ((pos[0] - (casa+1))) < 9 and ((pos[1] - (casa+1))) > 0 and ((pos[1] - (casa+1))) < 9:
                    comida.append([keys[j], values[j]])
                    comer += 1
                    if desenhar == True:
                        pygame.draw.rect(tela, azul, [tamanho * (pos[1] - (casa + 1)), tamanho * (pos[0] - (casa+1)), tamanho, tamanho], 5)
                    possibilidades.append(((pos[0] - (casa+1)), (pos[1] - (casa + 1))))

            #direita inferior
            if comer == 0 and sopro == False and (((pos[0] + casa), pos[1] - casa) not in values) and (pos[0] + casa) > 0 and (pos[0] + casa) < 9 and (pos[1] - casa) > 0 and (pos[1] - casa) < 9:  # Movimento comum
              if desenhar == True:
                  pygame.draw.rect(tela, azul, [tamanho * (pos[1] - casa), tamanho * (pos[0] + casa), tamanho, tamanho], 5)
              possibilidades.append(((pos[0] + casa), (pos[1] - casa)))

            #esquerda inferior 
            if comer == 0 and sopro == False and (((pos[0] - casa), pos[1] + casa) not in values) and (pos[0] - casa) > 0 and (pos[0] - casa) < 9 and (pos[1] + casa) > 0 and (pos[1] + casa) < 9:  # Movimento comum
              if desenhar == True: 
                pygame.draw.rect(tela, azul, [tamanho * (pos[1] + casa), tamanho * (pos[0] - casa), tamanho, tamanho], 5)
              possibilidades.append(((pos[0] - casa), (pos[1] + casa)))

            #direita superior
            if comer == 0 and sopro == False and (((pos[0] + casa), pos[1] + casa) not in values) and (pos[0] + casa) > 0 and (pos[0] + casa) < 9 and (pos[1] + casa) > 0 and (pos[1] + casa) < 9:  # Movimento comum
              if desenhar == True: 
                pygame.draw.rect(tela, azul, [tamanho * (pos[1] + casa), tamanho * (pos[0] + casa), tamanho, tamanho], 5)
              possibilidades.append(((pos[0] + casa), (pos[1] + casa)))

            # esquerda superior
            if comer == 0 and sopro == False and (((pos[0] - casa), pos[1] - casa) not in values) and (pos[0] - casa) > 0 and (pos[0] - casa) < 9 and (pos[1] - casa) > 0 and (pos[1] - casa) < 9:  # Movimento comum
              if desenhar == True: 
                pygame.draw.rect(tela, azul, [tamanho * (pos[1] - casa), tamanho * (pos[0] - casa), tamanho, tamanho], 5)
              possibilidades.append(((pos[0] - casa), (pos[1] - casa)))

    return possibilidades, pos, comida, comer

def move(pos, Old_Pos, posicoes, turn, possibilidades, comida, comer, sprites):
    dama_clara = sprites[0]
    dama_escura = sprites[1]
    rainha_clara = sprites[2]
    rainha_escura = sprites[3]

    for p in range(len(possibilidades)):  # Limpando selecao
        quadrado(possibilidades[p], True)

    peca = ''
    keys = list(posicoes.keys())
    values = list(posicoes.values())

    if pos in possibilidades and pos != Old_Pos:
        pygame.mixer.music.load("assets/sounds/move.ogg")
        pygame.mixer.music.play(1)
    else:
        if pos not in possibilidades and pos != Old_Pos:
            pygame.mixer.music.load("assets/sounds/wrong.ogg")
            pygame.mixer.music.play(1)
        return posicoes, turn, possibilidades, Old_Pos

    if comer != 0 and pos != Old_Pos:
        if comer == 1:
            posicoes[comida[1][0]] = None
            quadrado(comida[1][1], False)
        if comer == 2:
            for c in range(comer):
                if pos == possibilidades[c]:
                    posicoes[comida[c + 1][0]] = None
                    quadrado(comida[c + 1][1], False)

    for j in range(len(values)):  # Achando qual peca vai ser movida
        if values[j] == Old_Pos:
            peca = keys[j] ## Criando uma variavel com o nome da peca que sera movida
            posicoes[peca] = pos  # Mudando a posicao da peca na memoria

            if pos[0] == 1 and turn == 1 and 'dama' in peca:  #se tiver dama clara no final do tabuleiro -> rainha clara
                rainha = 'Prainha_clara' + peca[-1] + peca[-2]
                posicoes[rainha] = posicoes[keys[j]]
                del posicoes[keys[j]]
                peca = rainha

            if pos[0] == 8 and turn == -1 and 'dama' in peca:  # se tiver dama escura no final do tabuleiro -> rainha escura
                rainha = 'Prainha_escura' + peca[-1] + peca[-2] 
                posicoes[rainha] = posicoes[keys[j]] ## É criada uma nova peca chamada de rainha + a numeração da peca que virou rinha na memoria
                del posicoes[keys[j]] ## A antiga dama é deletada da memoria
                peca = rainha 

    if comer != 0: ## Caso uma peca tenha sido capturada
        valores = []
        valores = select(pos, posicoes, possibilidades, turn, False, False) ## Checa se a peca ainda pode continuar capturando
        if valores[-1] == 0: ## Caso não possa, muda de turno
            turn = -turn
    else:
        turn = -turn  # Mudando o turno
    
    pygame.draw.rect(tela, preto, [tamanho * 9, tamanho * 3, tamanho, tamanho])
    pygame.draw.rect(tela, preto, [0, tamanho * 3, tamanho, tamanho])
    if turn == 1: ## mostrando de quem é o turno
        pygame.draw.ellipse(tela, verde, [15, tamanho * 3 + 15, 40, 40])
    else:
        pygame.draw.ellipse(tela, verde, [tamanho * 9 + 15, tamanho * 3 + 15, 40, 40])

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

## Verificador de sopro
def pode_comer(turn, posicoes, possibilidades):
    keys = list(posicoes.keys())
    values = list(posicoes.values())

    verificador = False
    for peca in range(len(values)):
     if values[peca] != None:
        if ('clara' in keys[peca] and turn == 1) or ('escura' in keys[peca] and turn == -1):
            valores = []
            valores = select(values[peca], posicoes, possibilidades, turn, False, False)
            if valores[3] != 0:
                verificador = True
    return verificador