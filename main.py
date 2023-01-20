import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
rect = pygame.Rect(40, 40, 120, 120)
color = (0, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            color = (255, 255, 255)
        if event.type == pygame.KEYUP: 
            i=5
            color = (200, 255, 100)
            rect = pygame.Rect(140, 140, 120, 120)
            color = (100, 100, 200)
    pygame.draw.rect(screen, color, rect, 0)
    pygame.display.flip()
