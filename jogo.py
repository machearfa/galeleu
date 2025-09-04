import pygame

pygame.init()

largura = 800  
tamanho = 600  
screen = pygame.display.set_mode((largura, tamanho))

pygame.display.set_caption("My Pygame Window")

player_x = 350
player_y = 250
player_width = 100
player_height = 100

velocidade = 10

player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

rodando = True

while rodando:

    tecla = []

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                tecla.append(event)
                print(tecla)
                player_x += velocidade

            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                tecla.append(event)
                print(tecla)
                player_x -= velocidade

            if event.key == pygame.K_w or event.key == pygame.K_UP:
                tecla.append(event)
                print(tecla)
                player_y -= velocidade
            
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                tecla.append(event)
                print(tecla)
                player_y += velocidade


    player_rect.x = player_x
    player_rect.y = player_y

    screen.fill((100, 255, 100))
    pygame.draw.rect(screen, (255, 168, 0), player_rect)

    pygame.display.flip()

pygame.quit()