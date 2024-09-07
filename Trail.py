import pygame
from Variables import *

class Trail(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(Trail, self).__init__(*groups)
        self.positions = []
        self.surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        self.rect = self.surf.get_rect()

    def update(self, x, y):
        self.positions.append((x, y))

        for i in range(len(self.positions)):
            if i < 2: continue
            pygame.draw.line(self.surf, WHITE, self.positions[i-1], self.positions[i], 1)