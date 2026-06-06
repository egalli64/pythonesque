"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Normalizing speed - pixel for second
Time between frames, aka delta time, comes from clock.tick() - consider it "good enough"
Using FRect to let pygame to take care of position rounding issues
"""

from time import time
import pygame

FPS = 30  # different FPS should give close enough results

TITLE = "Defender Movement"
WIN_RECT = pygame.Rect(0, 0, 120, 650)
WIN_POS = (10, 50)
BACKGROUND_COLOR = "white"

DEFENDER_IMAGE = "../images/defender.png"
DEFENDER_SIZE = (30, 30)
DEFENDER_DEFAULT_SPEED = 200  # pixel/second
DIRECTION_DOWN = 1
DIRECTION_UP = -1

LINE_COLOR = "red"
LINE_START = (0, WIN_RECT.centery)
LINE_END = (WIN_RECT.width, WIN_RECT.centery)
LINE_WIDTH = 2

LIMIT = 1500  # ms


def main():
    pygame.init()

    window = pygame.Window(TITLE, WIN_RECT.size, WIN_POS)
    screen = window.get_surface()
    clock = pygame.time.Clock()

    defender_image = pygame.image.load(DEFENDER_IMAGE).convert_alpha()
    defender_image = pygame.transform.scale(defender_image, DEFENDER_SIZE)
    defender_rect = pygame.FRect(defender_image.get_rect())
    defender_rect.centerx = WIN_RECT.centerx
    defender_rect.bottom = WIN_RECT.bottom - 5
    defender_speed = DEFENDER_DEFAULT_SPEED
    defender_y_direction = DIRECTION_UP

    start_time = pygame.time.get_ticks()
    running = True
    while running:
        dt = clock.tick(FPS) / 1000  # delta time, ms since the previous call

        if pygame.time.get_ticks() > start_time + LIMIT:
            defender_speed = 0
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update
        defender_rect.top += defender_y_direction * defender_speed * dt
        if defender_rect.bottom >= WIN_RECT.bottom:
            defender_y_direction = DIRECTION_UP
        elif defender_rect.top <= 0:
            defender_y_direction = DIRECTION_DOWN

        # Draw
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.line(screen, LINE_COLOR, LINE_START, LINE_END, LINE_WIDTH)

        screen.blit(defender_image, defender_rect)
        window.flip()
    print(f"center y={defender_rect.centery}")

    pygame.quit()


if __name__ == "__main__":
    main()
