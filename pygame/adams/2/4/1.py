"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Using Rect and its attributes
"""

import pygame

FPS = 30

TITLE = "Defender Movement"
WIN_RECT = pygame.Rect(0, 0, 400, 100)
WIN_POS = (10, 50)
BACKGROUND_COLOR = "white"

DEFENDER_IMAGE = "../images/defender.png"
DEFENDER_SIZE = (30, 30)

DEFENDER_SPEED = 2

DIRECTION_RIGHT = 1
DIRECTION_LEFT = -1


def main():
    window = pygame.Window(TITLE, WIN_RECT.size, WIN_POS)
    screen = window.get_surface()
    clock = pygame.time.Clock()

    defender_image = pygame.image.load(DEFENDER_IMAGE).convert_alpha()
    defender_image = pygame.transform.scale(defender_image, DEFENDER_SIZE)
    defender_rect = defender_image.get_rect()
    defender_rect.centerx = WIN_RECT.centerx
    defender_rect.bottom = WIN_RECT.height - 5
    defender_x_direction = DIRECTION_RIGHT

    while handle_events():
        clock.tick(FPS)

        # Update
        # instead of checking the newly generated x value before changing the defender position
        # working on a new Rect shifted by an x, y offset is usually handier
        new_rect = defender_rect.move(defender_x_direction * DEFENDER_SPEED, 0)
        if new_rect.right >= WIN_RECT.right:  # clamp right
            defender_x_direction = DIRECTION_LEFT
            new_rect.right = WIN_RECT.right
        elif new_rect.left <= WIN_RECT.left:  # clamp left
            defender_x_direction = DIRECTION_RIGHT
            new_rect.left = WIN_RECT.left
        defender_rect = new_rect

        # Draw
        screen.fill(BACKGROUND_COLOR)
        screen.blit(defender_image, defender_rect)
        window.flip()


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
