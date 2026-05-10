"""
Animation

From: Making Games with Python & Pygame by Al Sweigart - https://inventwithpython.com/pygame/
"""

import pygame

pygame.init()

SCREEN_SIZE = (400, 300)
SCREEN_TITLE = "Animation"
WHITE = (255, 255, 255)
# this pathname is relative to the current startup folder
CAT_IMG = "pygame/makinggames/img/cat.png"

# frame setup (usually FPS is at least 60)
FPS = 30
# clock helps maintain a stable frame pacing
clock = pygame.time.Clock()

# set up the window
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption(SCREEN_TITLE)

# load the cat image, set its initial position and direction
cat = pygame.image.load(CAT_IMG)
cat_x = 10
cat_y = 10
direction = "right"

# the main game loop
running = True
while running:
    # clean up the screen
    screen.fill(WHITE)

    # adjust the cat position/direction
    if direction == "right":
        cat_x += 5
        if cat_x == 280:
            direction = "down"
    elif direction == "down":
        cat_y += 5
        if cat_y == 220:
            direction = "left"
    elif direction == "left":
        cat_x -= 5
        if cat_x == 10:
            direction = "up"
    elif direction == "up":
        cat_y -= 5
        if cat_y == 10:
            direction = "right"

    # bit block transfer from cat to screen, in the given position
    screen.blit(cat, (cat_x, cat_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # end of the game loop:
    # (1) push the changes from the back buffer to the screen
    pygame.display.update()
    # (2) delay the loop to keep the required FPS (when possible)
    clock.tick(FPS)

print("Done!")
pygame.quit()
