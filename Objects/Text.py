import pygame
from Objects.Variables import *


class Text(pygame.sprite.Sprite):
    font = pygame.font.get_default_font()

    def __init__(self, group, planet):
        super(Text, self).__init__(group)
        self.descr = 'Statistics'
        self.rect = 0
        self.planet = planet
        self.bg = BLACK

    def update(self, dt):
        text = self.planet.pos
        self.txt_surf = Text.font.render(text, True, self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)

    def draw(self, screen):
        screen.blit(self.surface, self.rect)