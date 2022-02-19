from hud import HUD
from screen import Screen
import pygame

from colors import COLORS

class Ball:
  x: float
  start_x: float
  start_y: float
  y: float
  size: float
  x_velocity: float
  y_velocity: float

  def __init__(self, x: int, y: int, size: int, initial_velocity: float):
    self.x = x
    self.y = y
    self.start_x = x
    self.start_y = y
    self.size = size
    self.x_velocity = initial_velocity
    self.y_velocity = initial_velocity

  def reset(self):
    self.x = self.start_x
    self.y = self.start_y

  def invert_x_velocity(self):
    self.x_velocity *= -1

  def invert_y_velocity(self):
    self.y_velocity *= -1

  def increase_x_velocity(self, velocity: float):
    self.x_velocity += velocity

  def increase_y_velocity(self, velocity: float):
    self.y_velocity += velocity

  def check_collision(self, screen: Screen, hud: HUD):
    if self.x == 0 or self.x == screen.width:
      self.invert_x_velocity()
    if self.y == 0:
      self.invert_y_velocity()
    elif self.y == screen.height:
      self.reset()
      hud.increment_life()

  def draw(self, screen: Screen):
    self.x += 1 * self.x_velocity
    self.y += 1 * self.y_velocity
    
    pygame.draw.circle(
      screen.surface, 
      COLORS['white'], 
      (self.x, self.y), 
      radius=self.size)