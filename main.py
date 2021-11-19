import pygame 

pygame.init()
branco = (255,255,255)
marrom  = (150, 75, 0)
bege = (245, 245, 220)
tamanho = 70
linhas_colunas = 8

tela = pygame.display.set_mode(((linhas_colunas+2) * tamanho, (linhas_colunas+2)*tamanho))
nome = pygame.display.set_caption('Xadrez')

#pecas brancas:
bispo = pygame.transform.scale(pygame.image.load("assets/sprites/bispo_v2.png"), (tamanho -2, tamanho -2))
torre = pygame.transform.scale(pygame.image.load("assets/sprites/torre_v2.png"), (tamanho -2, tamanho - 2))
cavalo = pygame.transform.scale(pygame.image.load("assets/sprites/cavalo_v2.png"), (tamanho -2, tamanho - 2))
rainha = pygame.transform.scale(pygame.image.load("assets/sprites/rainha_v2.png"), (tamanho -2, tamanho - 2))
rei = pygame.transform.scale(pygame.image.load("assets/sprites/rei_v2.png"), (tamanho -2, tamanho - 2))
peao = pygame.transform.scale(pygame.image.load("assets/sprites/peao_v2.png"), (tamanho -2, tamanho - 2))

#pecas pretas:
bispo_preto = pygame.transform.scale(pygame.image.load("assets/sprites/bispo_v1.png"), (tamanho -2, tamanho -2))
torre_preto = pygame.transform.scale(pygame.image.load("assets/sprites/torre_v1.png"), (tamanho -2, tamanho - 2))
cavalo_preto = pygame.transform.scale(pygame.image.load("assets/sprites/cavalo_v1.png"), (tamanho -2, tamanho - 2))
rainha_preto = pygame.transform.scale(pygame.image.load("assets/sprites/rainha_v1.png"), (tamanho -2, tamanho - 2))
rei_preto = pygame.transform.scale(pygame.image.load("assets/sprites/rei_v1.png"), (tamanho -2, tamanho - 2))
peao_preto = pygame.transform.scale(pygame.image.load("assets/sprites/peao_v1.png"), (tamanho -2, tamanho - 2))

tela.fill(branco)

count = 0
for i in range(1,linhas_colunas+1):
    for z in range(1,linhas_colunas+1):
        if count % 2 == 0:
            pygame.draw.rect(tela, bege,[tamanho*z,tamanho*i,tamanho,tamanho])
        else:
            pygame.draw.rect(tela, marrom, [tamanho*z,tamanho*i,tamanho,tamanho])
        count +=1
    count-=1
#pecas brancas:
tela.blit(torre, (tamanho*1 + 1, tamanho*8 + 1))
tela.blit(torre, (tamanho*8 + 1, tamanho*8 + 1))
tela.blit(cavalo, (tamanho*2 + 1, tamanho*8 + 1))
tela.blit(cavalo, (tamanho*7 + 1, tamanho*8 + 1))
tela.blit(bispo, (tamanho*3 + 1, tamanho*8 + 1))
tela.blit(bispo, (tamanho*6 + 1, tamanho*8 + 1))
tela.blit(rainha, (tamanho*4 + 1, tamanho*8 + 1))
tela.blit(rei, (tamanho*5 + 1, tamanho*8 + 1))
tela.blit(peao, (tamanho*1 + 1, tamanho*7 + 1))
tela.blit(peao, (tamanho*2 + 1, tamanho*7 + 1))
tela.blit(peao, (tamanho*3 + 1, tamanho*7 + 1))
tela.blit(peao, (tamanho*4 + 1, tamanho*7 + 1))
tela.blit(peao, (tamanho*5 + 1, tamanho*7 + 1))
tela.blit(peao, (tamanho*6 + 1, tamanho*7 + 1))
tela.blit(peao, (tamanho*7 + 1, tamanho*7 + 1))
tela.blit(peao, (tamanho*8 + 1, tamanho*7 + 1))

#pecas pretas:
tela.blit(torre_preto, (tamanho*1 + 1, tamanho*1 + 1))
tela.blit(torre_preto, (tamanho*8 + 1, tamanho*1 + 1))
tela.blit(cavalo_preto, (tamanho*2 + 1, tamanho*1 + 1))
tela.blit(cavalo_preto, (tamanho*7 + 1, tamanho*1 + 1))
tela.blit(bispo_preto, (tamanho*3 + 1, tamanho*1 + 1))
tela.blit(bispo_preto, (tamanho*6 + 1, tamanho*1 + 1))
tela.blit(rainha_preto, (tamanho*4 + 1, tamanho*1 + 1))
tela.blit(rei_preto, (tamanho*5 + 1, tamanho*1 + 1))
tela.blit(peao_preto, (tamanho*1 + 1, tamanho*2 + 1))
tela.blit(peao_preto, (tamanho*2 + 1, tamanho*2 + 1))
tela.blit(peao_preto, (tamanho*3 + 1, tamanho*2 + 1))
tela.blit(peao_preto, (tamanho*4 + 1, tamanho*2 + 1))
tela.blit(peao_preto, (tamanho*5 + 1, tamanho*2 + 1))
tela.blit(peao_preto, (tamanho*6 + 1, tamanho*2 + 1))
tela.blit(peao_preto, (tamanho*7 + 1, tamanho*2 + 1))
tela.blit(peao_preto, (tamanho*8 + 1, tamanho*2 + 1))


pygame.draw.rect(tela,bege,[tamanho,tamanho,linhas_colunas*tamanho,linhas_colunas*tamanho],1)

pygame.display.update()

jogo = True
while jogo:
    for evento in pygame.event.get():
        if (evento.type == pygame.QUIT):
            jogo = False

pygame.quit()