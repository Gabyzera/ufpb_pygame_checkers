import pygame

pygame.init()
##Tabela de cores
preto = (0,0,0)
marrom  = (150, 75, 0)
bege = (245, 245, 220)
azul = (0,225,255)
##
tamanho = 70 ##tamanho de cada quadrado 
linhas_colunas = 8

tela = pygame.display.set_mode(((linhas_colunas+2) * tamanho, (linhas_colunas+2)*tamanho))
nome = pygame.display.set_caption('Xadrez')

#adicionando sprites:
bispo_branco = pygame.transform.scale(pygame.image.load("assets/sprites/bispo_v2.png"), (tamanho -2, tamanho -2))
torre_branco = pygame.transform.scale(pygame.image.load("assets/sprites/torre_v2.png"), (tamanho -2, tamanho - 2))
cavalo_branco = pygame.transform.scale(pygame.image.load("assets/sprites/cavalo_v2.png"), (tamanho -2, tamanho - 2))
rainha_branco = pygame.transform.scale(pygame.image.load("assets/sprites/rainha_v2.png"), (tamanho -2, tamanho - 2))
rei_branco = pygame.transform.scale(pygame.image.load("assets/sprites/rei_v2.png"), (tamanho -2, tamanho - 2))
peao_branco = pygame.transform.scale(pygame.image.load("assets/sprites/peao_v2.png"), (tamanho -2, tamanho - 2))
bispo_preto = pygame.transform.scale(pygame.image.load("assets/sprites/bispo_v1.png"), (tamanho -2, tamanho -2))
torre_preto = pygame.transform.scale(pygame.image.load("assets/sprites/torre_v1.png"), (tamanho -2, tamanho - 2))
cavalo_preto = pygame.transform.scale(pygame.image.load("assets/sprites/cavalo_v1.png"), (tamanho -2, tamanho - 2))
rainha_preto = pygame.transform.scale(pygame.image.load("assets/sprites/rainha_v1.png"), (tamanho -2, tamanho - 2))
rei_preto = pygame.transform.scale(pygame.image.load("assets/sprites/rei_v1.png"), (tamanho -2, tamanho - 2))
peao_preto = pygame.transform.scale(pygame.image.load("assets/sprites/peao_v1.png"), (tamanho -2, tamanho - 2))

tela.fill(preto)

count = 0
for i in range(1,linhas_colunas+1):
    for j in range(1,linhas_colunas+1):
        if count % 2 == 0:
            pygame.draw.rect(tela, bege,[tamanho*j,tamanho*i,tamanho,tamanho])
        else:
            pygame.draw.rect(tela, marrom, [tamanho*j,tamanho*i,tamanho,tamanho])
        count += 1
    count -= 1
     
#pecas brancas:
tela.blit(torre_branco, (tamanho*1 + 1, tamanho*8 + 1))
tela.blit(torre_branco, (tamanho*8 + 1, tamanho*8 + 1))
tela.blit(cavalo_branco, (tamanho*2 + 1, tamanho*8 + 1))
tela.blit(cavalo_branco, (tamanho*7 + 1, tamanho*8 + 1))
tela.blit(bispo_branco, (tamanho*3 + 1, tamanho*8 + 1))
tela.blit(bispo_branco, (tamanho*6 + 1, tamanho*8 + 1))
tela.blit(rainha_branco, (tamanho*4 + 1, tamanho*8 + 1))
tela.blit(rei_branco, (tamanho*5 + 1, tamanho*8 + 1))
for i in range(1,9):
    tela.blit(peao_branco, (tamanho*i + 1, tamanho*7 + 1))

#pecas pretas:
tela.blit(torre_preto, (tamanho*1 + 1, tamanho*1 + 1))
tela.blit(torre_preto, (tamanho*8 + 1, tamanho*1 + 1))
tela.blit(cavalo_preto, (tamanho*2 + 1, tamanho*1 + 1))
tela.blit(cavalo_preto, (tamanho*7 + 1, tamanho*1 + 1))
tela.blit(bispo_preto, (tamanho*3 + 1, tamanho*1 + 1))
tela.blit(bispo_preto, (tamanho*6 + 1, tamanho*1 + 1))
tela.blit(rainha_preto, (tamanho*4 + 1, tamanho*1 + 1))
tela.blit(rei_preto, (tamanho*5 + 1, tamanho*1 + 1))
for i in range(1,9):
    tela.blit(peao_preto, (tamanho*i + 1, tamanho*2 + 1))

pygame.draw.rect(tela,bege,[tamanho,tamanho,linhas_colunas*tamanho,linhas_colunas*tamanho],1)

pygame.display.update()

##Guardando posições iniciais das peças no sistema
posicoes = {'Ptorre_preto1' : (1,1),'Ptorre_preto2':(1,8),'Pcavalo_preto1':(1,2),'Pcavalo_preto2':(1,7),'Pbispo_preto1':(1,3),'Pbispo_preto2':(1,6),'Prainha_preto':(1,4),'Prei_preto':(1,5),'Ppeao_preto1':(2,1),'Ppeao_preto2':(2,2),'Ppeao_preto3':(2,3),'Ppeao_preto4':(2,4),'Ppeao_preto5':(2,5),'Ppeao_preto6':(2,6),'Ppeao_preto7':(2,7),'Ppeao_preto8':(2,8),'Ptorre_branco1' : (8,1),'Ptorre_branco2':(8,8),'Pcavalo_branco1':(8,2),'Pcavalo_branco2':(8,7),'Pbispo_branco1':(8,3),'Pbispo_branco2':(8,6),'Prainha_branco':(8,4),'Prei_branco':(8,5),'Ppeao_branco1':(7,1),'Ppeao_branco2':(7,2),'Ppeao_branco3':(7,3),'Ppeao_branco4':(7,4),'Ppeao_branco5':(7,5),'Ppeao_branco6':(7,6),'Ppeao_branco7':(7,7),'Ppeao_branco8':(7,8)}
##
##Funcoes
def quadrado(square,border): ##Pinta quadrado limpo novamente:
    if border == True:
        if ((((square[0])%2) == 0) and (((square[1])%2) != 0)) or ((((square[0])%2) != 0) and (((square[1])%2) == 0)): 
            pygame.draw.rect(tela, marrom,[tamanho*(square[1]),tamanho*(square[0]),tamanho,tamanho],5)
        else:
            pygame.draw.rect(tela, bege,[tamanho*(square[1]),tamanho*(square[0]),tamanho,tamanho],5)
    else:
        if ((((square[0])%2) == 0) and (((square[1])%2) != 0)) or ((((square[0])%2) != 0) and (((square[1])%2) == 0)): 
            pygame.draw.rect(tela, marrom,[tamanho*(square[1]),tamanho*(square[0]),tamanho,tamanho])
        else:
            pygame.draw.rect(tela, bege,[tamanho*(square[1]),tamanho*(square[0]),tamanho,tamanho])
    pygame.display.update()        

def select(pos,possibilidades,turn):
    keys = list(posicoes.keys())
    values = list(posicoes.values())
    for i in range(len(values)): ## mostrando qual peca foi selecionada
        if values[i] == pos:
            peca = keys[i] 

    if possibilidades != []: ## Limpando selecoes
        for p in range(len(possibilidades)):
            quadrado(possibilidades[p],True)

    if turn == 1: ## Turno das brancas
        if 'Ppeao_branco' in peca: ##movimento do peao
            if ((pos[0]-1),(pos[1]+1)) in values: ## Se houver um inimigo para comer na direita
                for i in range(len(values)): 
                  if (values[i] == ((pos[0]-1),(pos[1]+1))) and ('preto' in keys[i]): 
                       pygame.draw.rect(tela, azul,[tamanho*(pos[1]+1),tamanho*(pos[0]-1),tamanho,tamanho],5)
                       pygame.display.update()
                       possibilidades.append(((pos[0]-1),(pos[1]+1)))

            if ((pos[0]-1),(pos[1]-1)) in values: ## Se houver um inimigo para comer na esquerda
                for i in range(len(values)):
                  if (values[i] == ((pos[0]-1),(pos[1]-1))) and ('preto' in keys[i]): 
                       pygame.draw.rect(tela, azul,[tamanho*(pos[1]-1),tamanho*(pos[0]-1),tamanho,tamanho],5)
                       pygame.display.update()
                       possibilidades.append(((pos[0]-1),(pos[1]-1)))
                
            if ((pos[0]-1),pos[1]) not in values: ## Movimento comum
                pygame.draw.rect(tela, azul,[tamanho*(pos[1]),tamanho*(pos[0]-1),tamanho,tamanho],5)
                pygame.display.update()
                possibilidades.append(((pos[0]-1),(pos[1])))

            if pos[0] == 7: ## Primeiro movimento do peao
                pygame.draw.rect(tela, azul,[tamanho*(pos[1]),tamanho*(pos[0]-2),tamanho,tamanho],5)
                pygame.display.update()
                possibilidades.append(((pos[0]-2),(pos[1])))     


    if turn == -1: ## Turno das pretas
        if 'Ppeao_preto' in peca: ##movimento do peao preto
            if ((pos[0]+1),(pos[1]-1)) in values: ## Se houver um inimigo para comer na direita
                for i in range(len(values)): 
                  print('run')
                  if (values[i] == ((pos[0]+1),(pos[1]-1))) and ('branco' in keys[i]): 
                       pygame.draw.rect(tela, azul,[tamanho*(pos[1]-1),tamanho*(pos[0]+1),tamanho,tamanho],5)
                       pygame.display.update()
                       possibilidades.append(((pos[0]+1),(pos[1]-1)))

            if ((pos[0]+1),(pos[1]+1)) in values: ## Se houver um inimigo para comer na esquerda
                for i in range(len(values)):
                  if (values[i] == ((pos[0]+1),(pos[1]+1))) and ('branco' in keys[i]): 
                       pygame.draw.rect(tela, azul,[tamanho*(pos[1]+1),tamanho*(pos[0]+1),tamanho,tamanho],5)
                       pygame.display.update()
                       possibilidades.append(((pos[0]+1),(pos[1]+1)))
                
            if ((pos[0]+1),pos[1]) not in values: ## Movimento padrão
                pygame.draw.rect(tela, azul,[tamanho*(pos[1]),tamanho*(pos[0]+1),tamanho,tamanho],5)
                pygame.display.update()
                possibilidades.append(((pos[0]+1),(pos[1]))) 

            if pos[0] == 2: ## Primeiro movimento do peao
                pygame.draw.rect(tela, azul,[tamanho*(pos[1]),tamanho*(pos[0]+2),tamanho,tamanho],5)
                pygame.display.update()
                possibilidades.append(((pos[0]+2),(pos[1])))           

    return possibilidades,pos
    
def move(pos,Old_Pos):
    keys = list(posicoes.keys())
    values = list(posicoes.values())
    if pos not in possibilidades: ## Para que o jogador siga as regras
        print('esse movimento não é aceito')    
        return

    if possibilidades != []: ##Limpando selecoes
        for p in range(len(possibilidades)):
            quadrado(possibilidades[p],True)

    for i in range(len(values)): ## mostrando qual peca vai ser movida
      if values[i] == Old_Pos:
        peca = keys[i]

    posicoes[peca] = pos ## Mudando a posicao

    pygame.mixer.music.load("assets/sounds/move.ogg")
    pygame.mixer.music.play(1)

    quadrado(Old_Pos,False) ##limpando local anterior da peca

    ## Colocando a peca na nova posicao
    if 'Ppeao_branco' in peca:
        tela.blit(peao_branco, (tamanho*pos[1] + 1, tamanho*pos[0] + 1))
    if 'Ptorre_branco' in peca:
        tela.blit(torre_branco, (tamanho*pos[1] + 1, tamanho*pos[0] + 1))
    if 'Pcavalo_branco' in peca:
        tela.blit(cavalo_branco, (tamanho*pos[1] + 1, tamanho*pos[0] + 1))
    if 'Pbispo_branco' in peca:
        tela.blit(bispo_branco, (tamanho*pos[1] + 1, tamanho*pos[0] + 1))
    if 'Prainha_branco' in peca:
        tela.blit(rainha_branco, (tamanho*pos[1] + 1, tamanho*pos[0] + 1))
    if 'Prei_preto' in peca:
        tela.blit(rei_branco, (tamanho*pos[1] + 1, tamanho*pos[0] + 1))
    if 'Ppeao_preto' in peca:
        tela.blit(peao_preto, (tamanho*pos[1] + 1, tamanho*pos[0] + 1))
    if 'Ptorre_branco' in peca:
        tela.blit(torre_preto, (tamanho*pos[1] + 1, tamanho*pos[0] + 1))
    if 'Pcavalo_preto' in peca:
        tela.blit(cavalo_preto, (tamanho*pos[1] + 1, tamanho*pos[0] + 1))
    if 'Pbispo_preto' in peca:
        tela.blit(bispo_preto, (tamanho*pos[1] + 1, tamanho*pos[0] + 1))
    if 'Prainha_preto' in peca:
        tela.blit(rainha_preto, (tamanho*pos[1] + 1, tamanho*pos[0] + 1))
    if 'Prei_preto' in peca:
        tela.blit(rei_preto, (tamanho*pos[1] + 1, tamanho*pos[0] + 1))
    ##
    
    pygame.display.update()
    return posicoes
##

jogo = True
selecao = () ##tupla para armazenar selecao do jogador
selecionado = False
possibilidades = []
turno = 1
while jogo:
    for evento in pygame.event.get():
        if (evento.type == pygame.QUIT):
            jogo = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            location = pygame.mouse.get_pos() #(x, y) localização do mouse
            coluna = location[0] // tamanho
            linha = location[1] // tamanho
            if selecao == (linha, coluna): # Quando o jogador clica em um local qualquer
                if selecionado == True: ##Começa o movimento
                  move(selecao,OldPos)
                  turno = -turno
                  selecao = () ##tornar seleçao vazia
                  possibilidades = [] ##Limpando possibilidades
                  selecionado = False
               
            else:
                selecao = (linha, coluna)
                print(selecao)
                if selecao in posicoes.values():
                    possibilidades, OldPos = select(selecao,possibilidades,turno)
                    selecionado = True
                    print(possibilidades)
                    print(posicoes)

pygame.quit()