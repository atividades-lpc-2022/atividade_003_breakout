import pygame

from colors import COLORS
from screen import Screen

class HUD:
  points: int
  life: int

  def __init__(self):
    self.life = 0
    self.points = 0

  def reset(self):
    self.life = 0
    self.points = 0

  def increment_life(self):
    self.life += 1

  def decrement_life(self):
    if self.life != 0:
      self.life -= 1

  def increment_points(self, points: int):
    self.points += points

  def __draw_label__(self, screen: pygame.Surface, label: str, x: float, y: float, size: int):
    font = pygame.font.Font('src/assets/PressStart2P.ttf', size)
    text = font.render(label, True, COLORS['white'])
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)

  def draw(self, screen: Screen):
    points_label = f"000{self.points}"[-3:]
    life_label = str(self.life)
    self.__draw_label__(
      screen.surface, 
      points_label, 
      screen.width * 0.2, 
      screen.height * 0.15, 
      32)
    self.__draw_label__(
      screen.surface, 
      life_label, 
      screen.width * 0.8, 
      screen.height * 0.15, 
      24)