import pygame
from Objects.Variables import *

class Trail(pygame.sprite.Sprite):
    def __init__(self, *groups, planet):
        super(Trail, self).__init__(*groups)
        self.positions = []
        self.surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        self.rect = self.surf.get_rect()
        self.colour = planet.colour
        self.planet = planet

    def update(self):
        self.positions.append((self.planet.rect.centerx, self.planet.rect.centery))

        for i in range(len(self.positions)):
            if i < 2: continue
            pygame.draw.line(self.surf, self.colour, self.positions[i-1], self.positions[i], 1)