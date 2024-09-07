import pygame
import random
from Objects.Planet import Planet
from Objects.Variables import *

# Initialization
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("One Body Problem")

all_sprites = pygame.sprite.Group()

for counter in range(0, 2):
  width = random.randint(0, SCREEN_WIDTH)
  height = random.randint(0, SCREEN_HEIGHT)
  planet = Planet(all_sprites, colour=COLOURS[counter], pos=(width, height))

clock = pygame.time.Clock()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
    elif event.type == pygame.QUIT:
      running = False

  screen.fill(BLACK)
  all_sprites.update()

  for entity in all_sprites:
    screen.blit(entity.surf, entity.rect)

  pygame.display.flip()
  clock.tick(60)

pygame.quit()