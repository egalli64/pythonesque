"""
Marquee - scrolling text

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame

BACKGROUND_IMG = "pygame/beginning/img/sushiplate.jpg"
SCREEN_SIZE = (640, 480)
FONT_NAME = "arial"
FONT_SIZE = 80
FONT_BLUE = (0, 0, 255)  # blue
message = "This is a demonstration of the scrolly message script. "

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

# generate the text as a surface w/ Arial font
font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
text = font.render(message, True, FONT_BLUE)

x = 0
y = (SCREEN_SIZE[1] - text.get_height()) / 2

image = pygame.image.load(BACKGROUND_IMG).convert()

running = True
while running:
    # wait 10 ms for an event, otherwise return an event with type NOEVENT
    event = pygame.event.wait(10)

    if event.type == pygame.QUIT:
        running = False

    screen.blit(image)

    # scrolling the text to the left
    x -= 2
    if x < -text.get_width():
        x = 0

    screen.blit(text, (x, y))
    screen.blit(text, (x + text.get_width(), y))
    pygame.display.flip()

print("Done.")
pygame.quit()
