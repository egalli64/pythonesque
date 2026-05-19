"""
Fonts

From: Making Games with Python & Pygame by Al Sweigart - https://inventwithpython.com/pygame/
"""

import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello World!")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

# load the pygame default font (aka "freesansbold.ttf") with the chosen size
font = pygame.font.Font(None, 32)
# render a text with the specified (smoothed) font and colors (generates a surface)
text_surface = font.render("Hello world!", True, GREEN, BLUE)
# generate a rectangle for the image, here specifying its center point
text_rect = text_surface.get_rect(center=(200, 150))

# main game loop
running = True
while running:
    screen.fill(WHITE)
    # push the text on the screen in the calculated position
    screen.blit(text_surface, text_rect)
    # or, in a more compact way
    screen.blit(font.render("Hello again", True, BLUE, GREEN), (136, 170))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

print("Done!")
pygame.quit()
