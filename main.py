# Imports
import pygame
from pygame.locals import (KEYDOWN, QUIT, K_UP, K_DOWN, K_RIGHT, K_LEFT, K_ESCAPE)

pygame.init()

# Constants
WIDTH = 800
HEIGHT = 500

# The screen is also a surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Amazing Game")


# Game event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        if event.type == QUIT:
            running = False

    screen.fill((255, 255, 255))
    surf = pygame.Surface((50, 50))
    surf.fill((0, 0, 0))

    # Copies one surface to another
    screen.blit(surf, (WIDTH/2, HEIGHT/2))
    # Updates the screen
    pygame.display.flip()


pygame.quit()