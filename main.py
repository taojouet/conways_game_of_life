import pygame
import numpy as np


color1 = (255, 0, 0)
color2 = (0, 255, 0)

colors = [color1, color2]

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # pygame.time.wait(2000)

    screen.fill("gray")

    for x in range(0, 1280, 90):
        pygame.draw.line(screen, "black", [x, 0], [x, 720], width=1)

    for y in range(0, 720, 90):
        pygame.draw.line(screen, "black", [0, y], [1280, y], width=1)
    
    pygame.display.flip()
    
    clock.tick(60)  # limits FPS to 60


pygame.quit()
