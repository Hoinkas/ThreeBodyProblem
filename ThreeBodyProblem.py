import pygame
from ThreeBodyProblem.Objects.Planet import Planet
from ThreeBodyProblem.Objects.Variables import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK

# Initialization
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("One Body Problem")

all_sprites = pygame.sprite.Group()
planet = Planet(WHITE, 1, all_sprites)

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
  planet.update()

  for entity in all_sprites:
    screen.blit(entity.surf, entity.rect)

  pygame.display.flip()
  clock.tick(60)

pygame.quit()