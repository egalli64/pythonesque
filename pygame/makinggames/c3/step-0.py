"""
Memory Puzzle - A simple memory matching game

From: Making Games with Python & Pygame by Al Sweigart - https://inventwithpython.com/pygame/
My reviewed version: https://github.com/egalli64/pythonesque/pygame/makinggames

Step 0: basic setup
"""

import pygame

# frame setup (slow motion - usually FPS is at least 60)
FPS = 10

# screen constants: size (in pixel), title, colors (RGB)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

SCREEN_TITLE = "Memory Game"

NAVYBLUE = (60, 60, 100)
BACKGROUND_COLOR = NAVYBLUE

# global pygame variables: frame clock and screen setup
# notice: encapsulation in a class would be a more robust option
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def main():
    """complete game setup and run the main game loop"""
    pygame.display.set_caption(SCREEN_TITLE)

    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(FPS)

    print("Done!")
    pygame.quit()


if __name__ == "__main__":
    main()
