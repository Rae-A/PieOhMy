import pygame
pygame.init()
screen = pygame.display.set_mode((600, 500))
PieOhMyBackground = pygame.image.load('PieOhMyBackground.jpg')

while True:
     
     screen.blit(PieOhMyBackground, (0, 0))
     pygame.display.update()
     for event in pygame.event.get():
         if (event.type == pygame.QUIT):
                pygame.quit()
                quit()