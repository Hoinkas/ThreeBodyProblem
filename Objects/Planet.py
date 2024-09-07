import pygame
from ThreeBodyProblem.Objects.Variables import *
from ThreeBodyProblem.Objects.Trail import Trail

class Planet(pygame.sprite.Sprite):
  def __init__(self, color, speed, *groups):
    super(Planet, self).__init__(*groups)
    self.color = color
    self.speed = speed
    self.trail = Trail(*groups)  # Add trail to the same groups

    self.surf = pygame.Surface([15, 15])
    self.surf.fill(BLACK)
    self.surf.set_colorkey(BLACK)
  
    self.rect = self.surf.get_rect(
      center = (
        (SCREEN_WIDTH - self.surf.get_width()) / 2,
        (SCREEN_HEIGHT - self.surf.get_height()) / 2 + 20
      )
    )

    self.x_forward = True
    self.y_forward = True

    half_of_size = self.surf.get_width() // 2

    pygame.draw.circle(self.surf, self.color, (half_of_size, half_of_size), half_of_size)

  def update(self):
    time = pygame.time.get_ticks() / 1000
    x = (1 / 2) * self.speed * (time ** 2)
    y = (1 / 2) * self.speed * (time ** 2)

    if self.rect.right >= SCREEN_WIDTH:
      self.x_forward = False
    elif self.rect.left <= 0:
      self.x_forward = True
      
    if self.rect.bottom >= SCREEN_HEIGHT:
      self.y_forward = False
    elif self.rect.top <= 0:
      self.y_forward = True
    
    self.rect.move_ip(((-1) ** (self.x_forward + 1)) * x, ((-1) ** (self.y_forward + 1)) * y)
    self.trail.update(self.rect.centerx, self.rect.centery)