import pygame 

pygame.init()

largura = 600
altura = 600

tela = pygame.display.set_mode((largura, altura))
nome = pygame.display.set_caption('Jogo de xadrez')

preto = (0, 0, 0)
branco = (255, 255, 255)

tamanho = pygame.Rect(0, 0, 75, 75)

pygame.draw.rect(tela, (branco), tamanho)