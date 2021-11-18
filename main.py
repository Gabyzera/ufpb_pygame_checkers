import pygame 

pygame.init()
largura = 600
altura = 600
preto = (0, 0, 0)
branco = (255, 255, 255)
tamanho = 75
linhas_colunas = 8

tela = pygame.display.set_mode(((linhas_colunas+2) * tamanho, (linhas_colunas+2)*tamanho))
nome = pygame.display.set_caption('Xadrez')

tela.fill(branco)

count = 0
for i in range(1,linhas_colunas+1):
    for z in range(1,linhas_colunas+1):
        if count % 2 == 0:
            pygame.draw.rect(tela, branco,[tamanho*z,tamanho*i,tamanho,tamanho])
        else:
            pygame.draw.rect(tela, preto, [tamanho*z,tamanho*i,tamanho,tamanho])
        count +=1
    count-=1

pygame.draw.rect(tela,preto,[tamanho,tamanho,linhas_colunas*tamanho,linhas_colunas*tamanho],1)

pygame.display.update()

jogo = True
while jogo:
    for evento in pygame.event.get():
        if (evento.type == pygame.QUIT):
            jogo = False

pygame.quit()