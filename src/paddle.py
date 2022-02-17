from pygame import Rect, Surface
from colors import COLORS
import pygame

class Paddle:
  x: int
  y: int
  width: int
  height: int
  rect: Rect

  def __init__(self, x: int, y: int, width: int, height: int):
    self.x = x
    self.y = y
    self.width = width
    self.height = height

  def draw(self, screen: Surface):
    self.rect = pygame.draw.rect(screen,COLORS["blue"],pygame.Rect(self.x, self.y, self.width, self.height))