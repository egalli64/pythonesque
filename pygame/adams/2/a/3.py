"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Double click - customized
"""

import pygame

FPS = 30

WIN_RECT = pygame.Rect(0, 0, 400, 100)
TITLE = "Double click me"
BACKGROUND_COLOR = "white"

DOUBLE_CLICK_TIME = 300  # ms
DOUBLE_CLICK_DISTANCE = 8  # pixels


def main():
    window = pygame.Window(TITLE, WIN_RECT.size)
    screen = window.get_surface()
    clock = pygame.time.Clock()

    last_click_time = 0
    last_click_pos = pygame.Vector2(-DOUBLE_CLICK_DISTANCE, -DOUBLE_CLICK_DISTANCE)

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # left mouse click detected now
                now = pygame.time.get_ticks()

                if now <= last_click_time + DOUBLE_CLICK_TIME:
                    distance = pygame.Vector2(event.pos).distance_to(last_click_pos)
                    if distance <= DOUBLE_CLICK_DISTANCE:
                        print("Double click")
                    else:
                        print("A click far away enough from the previous one")
                else:
                    print("A new single click")

                last_click_time = now
                last_click_pos = pygame.Vector2(event.pos)

        screen.fill(BACKGROUND_COLOR)
        window.flip()


if __name__ == "__main__":
    pygame.init()

    try:
        main()
    finally:
        pygame.quit()
        print("Done.")
