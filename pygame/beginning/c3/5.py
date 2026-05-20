"""
Resizable screen

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame

BACKGROUND_IMG = "pygame/beginning/img/sushiplate.jpg"

pygame.init()
# here screen is resizable!
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
pygame.display.set_caption("Resizable window")
image = pygame.image.load(BACKGROUND_IMG).convert()

running = True
while running:
    # pure event-drive approach, wait for an event and react to it
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.VIDEORESIZE:
        # change the screen size as required by the user (e.g.: dragging the window border)
        screen_size = event.size
        screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
        pygame.display.set_caption("Window resized to " + str(screen_size))

    # cover the screen with multiple copies of the background image (when required)
    for y in range(0, screen_size[1], image.get_height()):
        for x in range(0, screen_size[0], image.get_width()):
            screen.blit(image, (x, y))

    pygame.display.update()

print("Done!")
pygame.quit()
