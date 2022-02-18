from screen import Screen
import pygame

from colors import COLORS

class Ball:
  x: float
  y: float
  size: float
  x_velocity: float
  y_velocity: float

  def __init__(self, x: int, y: int, size: int, initial_velocity: float):
    self.x = x
    self.y = y
    self.size = size
    self.x_velocity = initial_velocity
    self.y_velocity = initial_velocity

  def increase_velocity(self, velocity: float):
    self.velocity += velocity

  def detect_screen_collision(self, screen: Screen):
    if self.x == 0 or self.x == screen.width:
      self.x_velocity *= -1
    if self.y == 0 or self.y == screen.height:
      self.y_velocity *= -1

  def draw(self, screen: Screen):
    self.detect_screen_collision(screen)
    self.x += 1 * self.x_velocity
    self.y += 1 * self.y_velocity
    
    pygame.draw.circle(
      screen.surface, 
      COLORS['white'], 
      (self.x, self.y), 
      radius=self.size)