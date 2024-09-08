import pygame
import random
from Objects.Planet import Planet
from Objects.Variables import *

# Initialization
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("One Body Problem")

def initializePlanets():
  Planet.restart()
  
  for counter in range(0, 2):
    width = random.randint(0, SCREEN_WIDTH/2)
    height = random.randint(0, SCREEN_HEIGHT/2)
    Planet(colour=COLOURS[counter], pos=(width, height))

clock = pygame.time.Clock()

running = True
while running:
  dt = clock.tick(60) / 1000

  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      if event.key == pygame.K_r:
        initializePlanets()
    elif event.type == pygame.QUIT:
      running = False

  screen.fill(BLACK)
  Planet.group.update(dt)

  for entity in Planet.group:
    screen.blit(entity.surf, entity.rect)

  pygame.display.flip()
  clock.tick(600)

pygame.quit()