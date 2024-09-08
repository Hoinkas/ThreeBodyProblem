import pygame
from Objects.Variables import *
from Objects.Trail import Trail

class Planet(pygame.sprite.Sprite):
  group = pygame.sprite.Group()

  def __init__(self, colour, pos):
    super(Planet, self).__init__()
    Planet.group.add(self)
    self.trail = Trail(Planet.group, planet=self)
    self.colour = colour
    self.speed = 1

    self.surf = pygame.Surface([15, 15])
    self.surf.fill(BLACK)
    self.surf.set_colorkey(BLACK)
          
    self.rect = self.surf.get_rect(center = pos)
    self.pos = pygame.math.Vector2(pos)

    self.x_forward = True
    self.y_forward = True

    half_of_size = self.surf.get_width() // 2
    pygame.draw.circle(self.surf, self.colour, (half_of_size, half_of_size), half_of_size)

  def update(self):
    time = pygame.time.get_ticks() / 1000
    acc = pygame.math.Vector2((1 / 2) * self.speed * (time ** 2))

    print(self.getAllOtherSprites())

    if self.rect.right >= SCREEN_WIDTH:
      self.x_forward = False
    elif self.rect.left <= 0:
      self.x_forward = True
      
    if self.rect.bottom >= SCREEN_HEIGHT:
      self.y_forward = False
    elif self.rect.top <= 0:
      self.y_forward = True
    
    self.rect.move_ip(((-1) ** (self.x_forward + 1)) * acc.x, ((-1) ** (self.y_forward + 1)) * acc.y)

  def getAllOtherSprites(self):
    return [sprite for sprite in Planet.group if type(sprite) is Planet and sprite != self]