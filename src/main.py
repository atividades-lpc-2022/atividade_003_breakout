from typing import Sequence
from ball import Ball
from block import Block
from colors import COLORS
from hud import HUD
from paddle import Paddle
from points import POINTS_VALUE
from screen import Screen
from sound import play_sound

import pygame

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
green = (0, 128, 0)
orange = (255, 165, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (128, 128, 128)

size = [600, 720]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout - LPC - Gabriel Lima e Guilherme Correia")

# start screen
pressedSPACE = False
blink = True

headline_list = ["B", "R", "E", "A", "K", "O", "U", "T", " ", "G", "A", "M", "E"]
colors = [red, orange, green, yellow]

add_x_letter = 0
ind_color = 0

while not pressedSPACE:
    screen.fill(black)

    # flashlight headline
    for e in headline_list:
        headline_font = pygame.font.Font("src/assets/PressStart2P.ttf", 25)
        headline_text = headline_font.render(e, True, colors[ind_color])
        headline_text_rect = headline_text.get_rect()
        headline_text_rect.center = (150 + add_x_letter, 350)
        screen.blit(headline_text, headline_text_rect)
        ind_color += 1

        add_x_letter += 25

        if ind_color == 3:
            ind_color = 0
    add_x_letter = 0
    pygame.display.update()

    pygame.draw.rect(screen, white, [0, 0, 600, 15])
    pygame.draw.rect(screen, white, [0, 0, 10, 700])
    pygame.draw.rect(screen, white, [590, 0, 20, 700])

    # drawing blocks
    add_height = 0
    color = colors[0]
    add_colors = 0
    for height in range(8):
        add_width = 0
        if height % 2 == 0:
            color = colors[0 + add_colors]
            add_colors += 1
        for row in range(2):
            for width in range(0, 588, 42):
                pygame.draw.rect(
                    screen, color, [0 + add_width, 90 + add_height, 42, 15]
                )
                add_width += 43
            add_height += 9
    # checking pressed button

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pressedSPACE = True

    # blinking start message
    blink = not blink

    if blink:
        start_font = pygame.font.Font("src/assets/PressStart2P.ttf", 23)
        start_text = start_font.render("PRESS SPACE TO START", True, blue, gray)
        start_text_rect = start_text.get_rect()
        start_text_rect.center = (300, 550)
        screen.blit(start_text, start_text_rect)

    pygame.display.flip()
    pygame.time.wait(1000)

# 3 seconds to start
for e in range(3):
    screen.fill(black)

    seconds_font = pygame.font.Font("src/assets/PressStart2P.ttf", 50)
    seconds_text = seconds_font.render(str(3 - e), True, white)
    seconds_text_rect = seconds_text.get_rect()
    seconds_text_rect.center = (300, 330)
    screen.blit(seconds_text, seconds_text_rect)

    pygame.display.update()

    pygame.time.wait(1000)

is_running = True
pause = False
game_clock = pygame.time.Clock()

FPS = 60
COLUMN_BLOCKS = 14
LINE_BLOCKS = 8
BLOCK_GAP = 1
MAX_LIFE = 4
paused = False
position_y = 0

def verify_global_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global is_running
            is_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                global paused
                paused = not paused


def loop():
    global x_velocity, y_velocity, position_y
    
    screen = Screen(600, 720)
    paddle = Paddle((screen.width / 2) - 30, 0.9 * screen.height, 60, 15)
    ball = Ball((screen.width / 2), (screen.height / 2), 10, 3)
    hud = HUD()
    position_y = 0
    blocks: Sequence[Block] = []

    block_width = (screen.width - COLUMN_BLOCKS * BLOCK_GAP) / COLUMN_BLOCKS
    block_height = 15

    for line in range(LINE_BLOCKS, LINE_BLOCKS * 2):
        if line == 8:
            color = 'red'
        elif line == 10:
            color = 'orange'
        elif line == 12:
            color = 'green'
        elif line == 14:
            color = 'yellow'
        for column in range(COLUMN_BLOCKS):
            blocks.append(Block(
                column * (block_width + BLOCK_GAP),
                line * (block_height + 2),
                block_width,
                block_height,
                COLORS[color],
                POINTS_VALUE[color]))

    while is_running:
        if hud.life == MAX_LIFE:
            return loop()

        verify_global_events()
        
        # pausing
        
        if paused is True:
            pygame.draw.rect(screen.surface, white, [270, 400, 20, 70])
            pygame.draw.rect(screen.surface, white, [305, 400, 20, 70])
            pygame.display.update()
            continue
        
        # increasing speed
        
        if 170 <= position_y <= 187:
            x_velocity = 0.6
            y_velocity = 0.6
            ball.x += 1 * ball.x_velocity
            ball.y += 1 * ball.y_velocity
        elif 136 <= position_y <= 153:
            x_velocity = 0.8
            y_velocity = 0.8
            ball.x += 1 * ball.x_velocity
            ball.y += 1 * ball.y_velocity
        elif 4 <= hud.points < 12:
            x_velocity = 0.1
            y_velocity = 0.1
            ball.x += 1 * ball.x_velocity
            ball.y += 1 * ball.y_velocity
        elif hud.points >= 12:
            x_velocity = 0.4
            y_velocity = 0.4
            ball.x += 1 * ball.x_velocity
            ball.y += 1 * ball.y_velocity

        paddle.set_controls(screen)

        paddle.check_collision(ball)
        ball.check_collision(screen, hud)
        for block in blocks:
            if block.is_colliding(ball):
                play_sound('src/assets/bounce.wav')
                position_y = block.y
                ball.invert_y_velocity()
                hud.increment_points(block.points)
                blocks.remove(block)

        screen.draw()
        paddle.draw(screen)
        for block in blocks:
            block.draw(screen)
        hud.draw(screen)
        ball.draw(screen)

        pygame.display.update()
        game_clock.tick(FPS)


def main():
    pygame.init()
    loop()
    pygame.quit()


main()
