import pygame
# import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

class Planet(pygame.sprite.Sprite):
  def __init__(self, color, speed):
    super(Planet, self).__init__()
    self.color = color
    self.speed = speed

    self.surf = pygame.Surface([15,15])
    self.surf.fill(BLACK)
    self.surf.set_colorkey(BLACK)
  
    self.rect = self.surf.get_rect(
      center = (
        (SCREEN_WIDTH-self.surf.get_width())/2,
        (SCREEN_HEIGHT-self.surf.get_height())/2 + 20
      )
    )

    self.x_forward = True
    self.y_forward = True

    # pygame.math.Vector2()

    half_of_size = self.surf.get_width() // 2

    pygame.draw.circle(self.surf, self.color, (half_of_size, half_of_size), half_of_size)

  def update(self):
    time = (pygame.time.get_ticks() / 1000)/ 60* 20
    x = (1/2) * self.speed * (time**2)
    y = (1/2) * self.speed * (time**2)

    if (self.rect.right >= SCREEN_WIDTH):
      self.x_forward = False
    elif (self.rect.left <= 0):
      self.x_forward = True
    if (self.rect.bottom >= SCREEN_HEIGHT):
      self.y_forward = False
    elif (self.rect.top <= 0):
      self.y_forward = True
    
    self.rect.move_ip(((-1)**(self.x_forward+1)) * x, ((-1)**(self.y_forward+1)) * y)

#Initialization
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

planet = Planet(WHITE, 1)
all_sprites = pygame.sprite.Group()
all_sprites.add(planet)

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
    elif event.type == pygame.QUIT:
      running = False

  planet.update()

  screen.fill(BLACK)

  for entity in all_sprites:
    screen.blit(entity.surf, entity.rect)

  pygame.display.flip()

pygame.quit()