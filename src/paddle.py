from pygame import Rect, Surface
from colors import COLORS
import pygame

from screen import Screen

class Paddle:
  x: int
  y: int
  width: int
  height: int
  velocity: float
  rect: Rect

  def __init__(self, x: int, y: int, width: int, height: int):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.velocity = 4

  def set_controls(self, screen: Screen):
    turn_right = pygame.key.get_pressed()[pygame.K_RIGHT]
    turn_left = pygame.key.get_pressed()[pygame.K_LEFT]
    if turn_left and self.x > 0: 
      self.x -= 1 * self.velocity
    elif turn_right and (self.x + self.width) < screen.width: 
      self.x += 1 * self.velocity

  def draw(self, screen: Screen):
    self.rect = pygame.draw.rect(
      screen.surface,
      COLORS["blue"],
      pygame.Rect(self.x, self.y, self.width, self.height))