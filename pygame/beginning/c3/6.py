"""
Text to image

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame

NAME = "Emanuele Galli"
FILE_NAME = "name.png"
FONT_NAME = "arial"
BACKGROUND_COLOR = (255, 255, 255)  # white
FONT_COLOR = (0, 0, 0)  # black
FONT_SIZE = 64

pygame.init()

print("Available system fonts:", pygame.font.get_fonts())
print(f"The system font used for {FONT_NAME}:", pygame.font.match_font(FONT_NAME))

# Get the specified font, or something that should be like that.
# For a stable result, load a custom font instead - see font.Font()
font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
# generate a surface with the passed string displayed with the defined font (w/ antialiasing)
surface = font.render(NAME, True, FONT_COLOR, BACKGROUND_COLOR)

# save the surface in a file with the format defined by the extension
pygame.image.save(surface, FILE_NAME)
