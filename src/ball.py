import pygame

from colors import COLORS

class Ball:
  x: float
  y: float
  size: float

  def __init__(self, x: int, y: int, size: int):
    self.x = x
    self.y = y
    self.size = size

  def draw(self, screen: pygame.Surface): 
    pygame.draw.circle(screen, COLORS['white'], (self.x, self.y), radius=self.size)