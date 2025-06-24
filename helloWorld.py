#escrevendo o meu primeiro codigo
print("Meu primeiro codigo no Galileu")

import pygame

pygame.init()

iniciado = True

while iniciado:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            iniciado = False
