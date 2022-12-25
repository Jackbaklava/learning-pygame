import pygame
from pygame.locals import (K_UP, K_DOWN, K_RIGHT, K_LEFT)
import random as r
from config import WIDTH, HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self):
        # Calls the __init__ method of the parent class
        super().__init__()
        # This surface is displayed on screen
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((255, 255, 255))
        # When you call this method, pygame creates a new rect with the size of the surface and the coordinates 0, 0. To give the rect other coords, parameters like center and topleft can be used
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        # move and move_ip (move in place) are the same except for move returns a new rect
        # Note: coordinates start from the top left of the screen
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)

        # To prevent player from going off screen
        # top, bottom, right, and left refer to sides
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0



class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(
            center=(
                r.randint(WIDTH+20, WIDTH+100),
                r.randint(0, HEIGHT)
            )
        )
        self.speed = r.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        # Remove sprite if it goes out of the screen
        if self.rect.right < 0:
            self.kill()
