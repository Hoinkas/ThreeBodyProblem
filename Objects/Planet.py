import pygame
import math
from Objects.Variables import *
from Objects.Trail import Trail

class Planet(pygame.sprite.Sprite):
  group = pygame.sprite.Group()

  def restart():
    for sprite in Planet.group:
      sprite.kill()

  def __init__(self, colour, pos):
    super(Planet, self).__init__()
    Planet.group.add(self)

    self.surf = pygame.Surface([15, 15])
    self.surf.fill(BLACK)
    self.surf.set_colorkey(BLACK)
          
    self.rect = self.surf.get_rect(center = pos)
    self.pos = pygame.math.Vector2(pos)

    self.trail = Trail(Planet.group, planet=self)
    self.colour = colour
    self.speed = 1
    radius = self.surf.get_width() // 2
    density = 2000
    self.mass = (4/3) * math.pi * radius * 3 * density

    self.x_forward = True
    self.y_forward = True

    pygame.draw.circle(self.surf, self.colour, (radius, radius), radius)

  def update(self, dt):
    acc = self.calculateMathFormula()
    print('acc', acc, dt)

    if self.pos.x >= SCREEN_WIDTH:
      self.x_forward = False
      self.pos.x = SCREEN_WIDTH
    elif self.pos.x <= 0:
      self.x_forward = True
      self.pos.x = 0
      
    if self.pos.y >= SCREEN_HEIGHT:
      self.y_forward = False
      self.pos.y = SCREEN_HEIGHT
    elif self.pos.y <= 0:
      self.y_forward = True
      self.pos.y = 0

    accVector = pygame.Vector2(((-1) ** (self.x_forward + 1)) * acc.x, ((-1) ** (self.y_forward + 1)) * acc.y)
    
    print('pos', self.pos, accVector)
    self.pos += accVector
    
    self.rect.center = self.pos

  def getAllOtherPlanets(self):
    return [sprite for sprite in Planet.group if type(sprite) is Planet and sprite != self]
  
  def calculateMathFormula(self):
    G = 1
    newVector = pygame.math.Vector2(0,0)

    for planet in self.getAllOtherPlanets():
      r = planet.pos - self.pos
      distance = r.length()
      print('planets', planet.pos, self.pos)
      newVector += planet.mass * (r/(distance**3))
      print('newVector', newVector)

    return G * newVector