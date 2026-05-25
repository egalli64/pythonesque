"""
Testing pressed keys

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BACKGROUND_COLOR = (255, 255, 255)  # white

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
font = pygame.font.SysFont("arial", 32)
FONT_HEIGHT = font.get_linesize()
FONT_COLOR = (0, 0, 0)  # black

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # detect any key pressing
        elif event.type == pygame.KEYDOWN:
            # Only the "standard" keys have a name
            key_name = pygame.key.name(event.key)
            print(key_name if len(key_name) else "Non-standard key")

    if running:
        screen.fill(BACKGROUND_COLOR)

        # return a sequence of boolean representing the state of each key in the keyboard
        keys = pygame.key.get_pressed()
        y = FONT_HEIGHT

        # this works for "normal" keys only
        count = 0
        for keycode in range(len(keys)):
            if keys[keycode]:
                count += 1
                key_name = pygame.key.name(keycode)
                if not key_name:
                    key_name = "Non-standard key"
                text_surface = font.render(f"{key_name} pressed", True, FONT_COLOR)
                screen.blit(text_surface, (8, y))
                y += FONT_HEIGHT

        if count:
            text_surface = font.render(f"{count} keys pressed", True, FONT_COLOR)
            screen.blit(text_surface, (8, y))
            y += FONT_HEIGHT

        # for special keys, use this approach
        if keys[pygame.K_LEFT and pygame.K_UP]:
            text_surface = font.render("left and up keys pressed", True, FONT_COLOR)
            screen.blit(text_surface, (8, y))

        pygame.display.flip()

print("Done")
pygame.quit()
