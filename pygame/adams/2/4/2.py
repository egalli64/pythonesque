"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Normalizing speed - pixel for second vs pixel for frame
Measuring the speed in pixel for frame makes the game speed machine dependent.
"""

import pygame

FPS = 30  # change FPS to get different results

TITLE = "Defender Movement"
WIN_RECT = pygame.Rect(0, 0, 120, 650)
WIN_POS = (10, 50)
BACKGROUND_COLOR = "white"

DEFENDER_IMAGE = "../images/defender.png"
DIRECTION_DOWN = 1
DIRECTION_UP = -1


LIMIT = 5000


def main():
    window = pygame.Window(TITLE, WIN_RECT.size, WIN_POS)
    screen = window.get_surface()
    clock = pygame.time.Clock()

    defender_image = pygame.image.load(DEFENDER_IMAGE).convert_alpha()
    defender_image = pygame.transform.scale(defender_image, (30, 30))
    defender_rect = defender_image.get_rect()
    defender_rect.centerx = WIN_RECT.centerx
    defender_rect.bottom = WIN_RECT.bottom - 5
    defender_speed = 2
    defender_y_direction = DIRECTION_UP

    start_time = pygame.time.get_ticks()
    while handle_events():
        clock.tick(FPS)

        if pygame.time.get_ticks() > start_time + LIMIT:
            defender_speed = 0

        # Update
        defender_rect.top += defender_y_direction * defender_speed
        if defender_rect.bottom >= WIN_RECT.bottom:
            defender_y_direction = DIRECTION_UP
        elif defender_rect.top <= 0:
            defender_y_direction = DIRECTION_DOWN

        # Draw
        screen.fill(BACKGROUND_COLOR)
        screen.blit(defender_image, defender_rect)
        window.flip()

    print(f"top={defender_rect.top}")


def handle_events() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


if __name__ == "__main__":
    pygame.init()

    try:
        main()
    finally:
        pygame.quit()
        print("Done.")
