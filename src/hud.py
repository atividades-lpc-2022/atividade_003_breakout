import pygame

from colors import COLORS
from screen import Screen


def __draw_label__(screen: pygame.Surface, label: str, x: float, y: float, size: int):
    font = pygame.font.Font("src/assets/PressStart2P.ttf", size)
    text = font.render(label, True, COLORS["white"])
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    screen.blit(text, text_rect)


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

    def draw(self, screen: Screen):
        points_label = f"000{self.points}"[-3:]
        life_label = str(self.life)
        __draw_label__(
            screen.surface, points_label, screen.width * 0.2, screen.height * 0.15, 32
        )
        __draw_label__(
            screen.surface, life_label, screen.width * 0.8, screen.height * 0.15, 24
        )
