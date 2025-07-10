import pygame

rodando = True
pygame.init()

tela = pygame.display.set_mode((800, 600))

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando == False


tela.fill(250, 250, 250)