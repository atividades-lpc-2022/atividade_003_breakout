from typing import Sequence
from ball import Ball
from block import Block
from colors import COLORS
from paddle import Paddle
from screen import Screen
import pygame

is_running = True
game_clock = pygame.time.Clock()

FPS = 60
COLUMN_BLOCKS = 14
LINE_BLOCKS = 8
BLOCK_GAP = 1

def set_global_events():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      global is_running
      is_running = False

def loop():
  screen = Screen(600, 720)
  paddle = Paddle((screen.width / 2) - 30, 0.9 * screen.height, 60, 15)
  ball = Ball((screen.width / 2), (screen.height / 2), 10)

  blocks: Sequence[Block] = []

  block_width = (screen.width - COLUMN_BLOCKS * BLOCK_GAP) / COLUMN_BLOCKS
  block_height = 15

  for line in range(LINE_BLOCKS, LINE_BLOCKS * 2):
    if line == 8: color = 'red'
    elif line == 10: color = 'orange'
    elif line == 12: color = 'green'
    elif line == 14: color = 'yellow'
    for column in range(COLUMN_BLOCKS):
      blocks.append(Block(column * (block_width + BLOCK_GAP), line * (block_height + 2), block_width, block_height, COLORS[color]))

  while is_running:
    screen.draw()
    paddle.draw(screen.surface)
    ball.draw(screen.surface)
    for block in blocks:
      block.draw(screen.surface)
    pygame.display.flip()
    game_clock.tick(FPS)

def main():
  pygame.init()
  set_global_events()
  loop()
  pygame.quit()

main()