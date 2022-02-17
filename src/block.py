from pygame import Color, Surface
import pygame


class Block:
  x: float
  y: float
  width: float
  height: float
  color: Color

  def __init__(self, x: int, y: int, width: int, height: int, color: Color):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.color = color

  def draw(self, screen: Surface):
    self.rect = pygame.draw.rect(screen,self.color,pygame.Rect(self.x, self.y, self.width, self.height))