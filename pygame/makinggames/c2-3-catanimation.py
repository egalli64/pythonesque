"""
Animation

From: Making Games with Python & Pygame by Al Sweigart - https://inventwithpython.com/pygame/
My reviewed version: https://github.com/egalli64/pythonesque/pygame/makinggames
"""

import pygame

pygame.init()

SCREEN_SIZE = (400, 300)
SCREEN_TITLE = "Animation"
WHITE = (255, 255, 255)
# this pathname is relative to the current startup folder
CAT_IMG = "pygame/makinggames/img/cat.png"
CAT_MOVE = 5

CAT_MIN_X = 10
CAT_MAX_X = 270
CAT_MIN_Y = 10
CAT_MAX_Y = 220

CAT_INIT_X = CAT_MIN_X
CAT_INIT_Y = CAT_MIN_Y


class Direction:
    RIGHT = "right"
    LEFT = "left"
    UP = "up"
    DOWN = "down"


# frame setup (usually FPS is at least 60)
FPS = 30
# clock helps maintain a stable frame pacing
clock = pygame.time.Clock()

# set up the window
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(SCREEN_TITLE)

# load the cat image, set its initial position and direction
cat = pygame.image.load(CAT_IMG).convert()
cat_x = CAT_INIT_X
cat_y = CAT_INIT_Y
cat_direction = Direction.RIGHT

# the main game loop
running = True
while running:
    # delay the loop to keep the required FPS (when possible)
    clock.tick(FPS)

    # clean up the screen
    screen.fill(WHITE)

    # adjust the cat position/direction
    if cat_direction == Direction.RIGHT:
        cat_x += CAT_MOVE
        if cat_x >= CAT_MAX_X:
            cat_direction = Direction.DOWN
    elif cat_direction == Direction.DOWN:
        cat_y += CAT_MOVE
        if cat_y >= CAT_MAX_Y:
            cat_direction = Direction.LEFT
    elif cat_direction == Direction.LEFT:
        cat_x -= CAT_MOVE
        if cat_x <= CAT_MIN_X:
            cat_direction = Direction.UP
    elif cat_direction == Direction.UP:
        cat_y -= CAT_MOVE
        if cat_y <= CAT_MIN_Y:
            cat_direction = Direction.RIGHT

    # bit block transfer from cat to screen, in the given position
    screen.blit(cat, (cat_x, cat_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # end of the game loop: push the changes from the back buffer to the screen
    pygame.display.flip()

print("Done!")
pygame.quit()
