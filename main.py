# Imports
import pygame
from pygame.locals import (KEYDOWN, QUIT, K_ESCAPE)
from config import WIDTH, HEIGHT
from sprites import Player, Enemy, Cloud, sound_collision

pygame.init()

# The screen is also a surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Amazing Game")

# Assigns a unique code to the custom event
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 200)
ADDCLOUD = pygame.USEREVENT + 3
pygame.time.set_timer(ADDCLOUD, 2000)

# Sprites
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game variables
clock = pygame.time.Clock()
hearts = 3
score = 0
font = pygame.font.Font("freesansbold.ttf", 32)

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

    score += 1

    # Returns a dictionary
    keys_pressed = pygame.key.get_pressed()
    player.update(keys_pressed)
    enemies.update()
    clouds.update()

    screen.fill((135, 206, 250))

    # Copies one surface to another
    for sprite in all_sprites:
        screen.blit(sprite.surf, sprite.rect)
    for i in range(0, hearts):
        x = 10
        y = 40
        heart = pygame.transform.scale(pygame.image.load("assets/heart.png"), (40, 40)).convert()
        heart.set_colorkey((255, 255, 255))
        screen.blit(heart, (x+50*i, y))
    # Display the score
    score_counter = font.render(f"Score: {score}", True, (255, 234, 0))
    screen.blit(score_counter, (10, 10))

    # Check for collisions
    enemy_collided = pygame.sprite.spritecollideany(player, enemies)
    if enemy_collided:
        hearts -= 1
        enemy_collided.kill()
        sound_collision.play()

    if hearts == 0:
        player.kill()
        running = False

    # Updates the screen
    pygame.display.flip()
    # Maintains the FPS at 30
    clock.tick(30)


pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()
