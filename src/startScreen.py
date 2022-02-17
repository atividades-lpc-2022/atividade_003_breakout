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

size = (800, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout - PyGame Edition - 2022.02.16")

# start message
start_font = pygame.font.Font('PressStart2P.ttf', 30)
start_text = start_font.render("PRESS BACKSPACE TO START", True, blue, gray)
start_text_rect = start_text.get_rect()
start_text_rect.center = (395, 430)

blink = True

# start screen
while True:
    screen.fill(black)

    headline_font = pygame.font.Font('PressStart2P.ttf', 30)
    headline_text = headline_font.render('BREAKOUT GAME', True, yellow)
    headline_text_rect = headline_text.get_rect()
    headline_text_rect.center = (400, 230)
    screen.blit(headline_text, headline_text_rect)

    pygame.display.update()

    # blinking start message
    blink = not blink

    if blink:
        start_text = start_font.render("PRESS BACKSPACE TO START", True, blue, gray)
        start_text_rect = start_text.get_rect()
        start_text_rect.center = (395, 430)
        screen.blit(start_text, start_text_rect)

    pygame.display.flip()
    pygame.time.wait(1000)