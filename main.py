# Imports
import pygame
from pygame.locals import (KEYDOWN, QUIT, K_ESCAPE)
from config import WIDTH, HEIGHT
from sprites import Player, Enemy

pygame.init()


# The screen is also a surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Amazing Game")
clock = pygame.time.Clock()

# Assigns a unique code to the custom event
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 750)

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game event loop
running = True
while running:
    for event in pygame.event.get():
        # Check if game is closed
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

        elif event.type == ADDENEMY:
            enemy = Enemy()
            enemies.add(enemy)
            all_sprites.add(enemy)

    # Returns a dictionary
    keys_pressed = pygame.key.get_pressed()
    player.update(keys_pressed)
    enemies.update()

    screen.fill((0, 0, 0))

    # Copies one surface to another
    for sprite in all_sprites:
        screen.blit(sprite.surf, sprite.rect)

    # Updates the screen
    pygame.display.flip()
    # Maintains the FPS at 30
    clock.tick(30)


pygame.quit()