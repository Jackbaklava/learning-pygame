# Imports
import pygame
from pygame.locals import (KEYDOWN, QUIT, K_ESCAPE)
from config import WIDTH, HEIGHT
from sprites import Player, Enemy, Cloud, sound_move_up, sound_move_down, sound_collision

pygame.init()

# The screen is also a surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Amazing Game")
clock = pygame.time.Clock()

# Assigns a unique code to the custom event
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 750)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 2000)


enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
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

        elif event.type == ADDCLOUD:
            cloud = Cloud()
            clouds.add(cloud)
            all_sprites.add(cloud)

    # Returns a dictionary
    keys_pressed = pygame.key.get_pressed()
    player.update(keys_pressed)
    enemies.update()
    clouds.update()

    screen.fill((135, 206, 250))

    # Copies one surface to another
    for sprite in all_sprites:
        screen.blit(sprite.surf, sprite.rect)

    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        sound_move_up.stop()
        sound_move_down.stop()
        sound_collision.play()
        running = False

    # Updates the screen
    pygame.display.flip()
    # Maintains the FPS at 30
    clock.tick(30)

pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()