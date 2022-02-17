import pygame
from colors import COLORS

class Screen:
  width: int
  height: int
  surface: pygame.Surface

  def __init__(self, width: int, height: int):
    self.width = width
    self.height = height
    self.surface = pygame.display.set_mode(size=(width, height))
    pygame.display.set_caption("Breakout - LPC - Gabriel Lima e Guilherme Tapajós")

  def draw(self):
    background_image = pygame.image.load('src/assets/background.png')
    background_shape = background_image.get_rect()
    self.surface.fill(COLORS['black'])
    self.surface.blit(background_image, background_shape)
