from pygame import Color
import pygame
from ball import Ball
from screen import Screen

class Block:
  x: float
  y: float
  width: float
  height: float
  color: Color
  points: int

  def __init__(self, x: int, y: int, width: int, height: int, color: Color, points: int):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.color = color
    self.points = points

  def is_colliding(self, ball: Ball):
    x_is_colliding = self.x <= ball.x <= self.x + self.width
    y_is_colliding = self.y <= ball.y <= self.y + self.height
    return x_is_colliding and y_is_colliding

  def draw(self, screen: Screen):
    self.rect = pygame.draw.rect(
      screen.surface,
      self.color,
      pygame.Rect(self.x, self.y, self.width, self.height))