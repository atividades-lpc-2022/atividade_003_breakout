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
        headline_font = pygame.font.Font("PressStart2P.ttf", 25)
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
        start_font = pygame.font.Font("PressStart2P.ttf", 23)
        start_text = start_font.render("PRESS SPACE TO START", True, blue, gray)
        start_text_rect = start_text.get_rect()
        start_text_rect.center = (300, 550)
        screen.blit(start_text, start_text_rect)

    pygame.display.flip()
    pygame.time.wait(1000)

# 3 seconds to start
for e in range(3):

    screen.fill(black)

    seconds_font = pygame.font.Font("PressStart2P.ttf", 50)
    seconds_text = seconds_font.render(str(3 - e), True, white)
    seconds_text_rect = seconds_text.get_rect()
    seconds_text_rect.center = (300, 330)
    screen.blit(seconds_text, seconds_text_rect)

    pygame.display.update()

    pygame.time.wait(1000)
