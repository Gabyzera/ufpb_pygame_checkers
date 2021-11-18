import pygame 

pygame.init()
largura = 600
altura = 600
preto = (0, 0, 0)
branco = (255, 255, 255)
tamanho = 75
linhas_colunas = 8

tela = pygame.display.set_mode((linhas_colunas * tamanho, (linhas_colunas+1)*tamanho))
nome = pygame.display.set_caption('Xadrez')
tela.fill(preto)
pygame.draw.rect(tela, branco, (0,0,75,75),0)
pygame.draw.rect(tela, branco, (150,0,75,75),0)
pygame.draw.rect(tela, branco, (300,0,75,75),0)
pygame.draw.rect(tela, branco, (450,0,75,75),0)
pygame.draw.rect(tela, branco, (600,0,75,75),0)
pygame.draw.rect(tela, branco, (75,75,75,75),0)
pygame.draw.rect(tela, branco, (225,75,75,75),0)
pygame.draw.rect(tela, branco, (375,75,75,75),0)
pygame.draw.rect(tela, branco, (525,75,75,75),0)
pygame.draw.rect(tela, branco, (0,150,75,75),0)
pygame.draw.rect(tela, branco, (150,150,75,75),0)
pygame.draw.rect(tela, branco, (300,150,75,75),0)
pygame.draw.rect(tela, branco, (450,150,75,75),0)
pygame.draw.rect(tela, branco, (600,150,75,75),0)
pygame.draw.rect(tela, branco, (75,225,75,75),0)
pygame.draw.rect(tela, branco, (225,225,75,75),0)
pygame.draw.rect(tela, branco, (375,225,75,75),0)
pygame.draw.rect(tela, branco, (525,225,75,75),0)
pygame.draw.rect(tela, branco, (0,300,75,75),0)
pygame.draw.rect(tela, branco, (150,300,75,75),0)
pygame.draw.rect(tela, branco, (300,300,75,75),0)
pygame.draw.rect(tela, branco, (450,300,75,75),0)
pygame.draw.rect(tela, branco, (600,300,75,75),0)
pygame.draw.rect(tela, branco, (75,375,75,75),0)
pygame.draw.rect(tela, branco, (225,375,75,75),0)
pygame.draw.rect(tela, branco, (375,375,75,75),0)
pygame.draw.rect(tela, branco, (525,375,75,75),0)
pygame.draw.rect(tela, branco, (0,450,75,75),0)
pygame.draw.rect(tela, branco, (150,450,75,75),0)
pygame.draw.rect(tela, branco, (300,450,75,75),0)
pygame.draw.rect(tela, branco, (450,450,75,75),0)
pygame.draw.rect(tela, branco, (600,450,75,75),0)
pygame.draw.rect(tela, branco, (75,525,75,75),0)
pygame.draw.rect(tela, branco, (225,525,75,75),0)
pygame.draw.rect(tela, branco, (375,525,75,75),0)
pygame.draw.rect(tela, branco, (525,525,75,75),0)

pygame.display.update()

jogo = True
while jogo:
    for evento in pygame.event.get():
        if (evento.type == pygame.QUIT):
            jogo = False

pygame.quit()