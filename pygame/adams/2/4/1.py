"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Using Rect and its attributes
"""

import pygame

FPS = 30

TITLE = "A Peaceful Day"
WIN_RECT = pygame.Rect(0, 0, 600, 100)
WIN_POS = (10, 50)
BACKGROUND_COLOR = "white"

DEFENDER_IMAGE = "../3/images/defender.png"
DEFENDER_SIZE = (30, 30)

DEFENDER_SPEED = 2

DIRECTION_RIGHT = 1
DIRECTION_LEFT = -1


def main():
    pygame.init()
    window = pygame.Window(TITLE, WIN_RECT.size, WIN_POS)
    screen = window.get_surface()
    clock = pygame.time.Clock()

    defender_image = pygame.image.load(DEFENDER_IMAGE).convert_alpha()
    defender_image = pygame.transform.scale(defender_image, DEFENDER_SIZE)
    defender_rect = defender_image.get_rect()
    defender_rect.centerx = WIN_RECT.centerx
    defender_rect.bottom = WIN_RECT.height - 5
    defender_x_direction = DIRECTION_RIGHT

    running = True
    while running:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update
        defender_rect.left += defender_x_direction * DEFENDER_SPEED
        if defender_rect.right >= WIN_RECT.right:
            defender_x_direction = DIRECTION_LEFT
        elif defender_rect.left <= WIN_RECT.left:
            defender_x_direction = DIRECTION_RIGHT

        # Draw
        screen.fill(BACKGROUND_COLOR)
        screen.blit(defender_image, defender_rect)

        window.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
    print("Done.")
