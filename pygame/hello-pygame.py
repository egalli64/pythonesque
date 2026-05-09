"""
Pygame quickstart: https://www.pygame.org/docs/
My notes: https://github.com/egalli64/pythonesque/pygame

Example file showing a circle moving on screen
"""

import pygame

# display constants
BACKGROUND = "purple"
FOREGROUND = "red"
DISPLAY_SIZE = (1280, 720)

# frame per second setting
FPS = 30

# pygame setup
pygame.init()

# set the program window
screen = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption("Move the circle (wasd)")

# used to keep an eye on the FPS
clock = pygame.time.Clock()

# no initial movement (just for code clarity)
delta_time = 0

# set the starting circle position in the middle of the screen
position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

print("Ready.")

running = True
while running:
    # poll for events
    for event in pygame.event.get():
        # pygame.QUIT event means the user clicked X to close your window
        if event.type == pygame.QUIT:
            running = False

    # clean the screen with the background color
    screen.fill(BACKGROUND)
    # place the circle in the current position on the screen
    pygame.draw.circle(screen, FOREGROUND, position, 40)

    # we get in keys a frozen snapshot of the current keyboard state
    # change the circle position if any key in "w s a d" is pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        position.y -= 300 * delta_time
    if keys[pygame.K_s]:
        position.y += 300 * delta_time
    if keys[pygame.K_a]:
        position.x -= 300 * delta_time
    if keys[pygame.K_d]:
        position.x += 300 * delta_time

    # put the changes on screen (in one shot)
    pygame.display.flip()

    # try to keep a smooth animation
    # delta time in seconds since last frame - aiming to framerate-independent movement
    delta_time = clock.tick(FPS) / 1000

print("Terminating.")
pygame.quit()
