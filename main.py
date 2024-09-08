import pygame, random, math
from Objects.Planet import Planet
from Objects.Variables import *

# Initialization
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Two Body Problem")

def initializePlanets():
  Planet.restart()
  
  for counter in range(0, PLANETS_COUNT):
    width = random.randint(0, SCREEN_WIDTH/2)
    height = random.randint(0, SCREEN_HEIGHT/2)
    angle = random.uniform(0, 2.0* math.pi)
    speed = random.randint(0, 10)
    acc = pygame.Vector2(speed * math.cos(angle), speed * math.sin(angle))
    Planet(colour=COLOURS[counter], pos=(width, height), acc=acc)

clock = pygame.time.Clock()

RUNNING, PAUSE = 0, 1
state = RUNNING

while True:
  print(Planet.restartBool)
  if Planet.restartBool: initializePlanets()
  dt = clock.tick(60) / 1000

  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        pygame.quit()
      if event.key == pygame.K_r:
        initializePlanets()
      if event.key == pygame.K_SPACE:
        if state == PAUSE: state = RUNNING
        else: state = PAUSE
    elif event.type == pygame.QUIT:
      pygame.quit()

  screen.fill(BLACK)

  for entity in Planet.group:
    screen.blit(entity.surf, entity.rect)

  pygame.display.flip()
  clock.tick(600)

  if state == RUNNING:
    Planet.group.update(dt)

  # elif state == PAUSE: