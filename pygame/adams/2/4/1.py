"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Using Rect and its attributes
"""

import pygame

FPS = 30

TITLE = "Defender Movement"
WIN_RECT = pygame.Rect(0, 0, 600, 100)
WIN_POS = (10, 50)
BACKGROUND_COLOR = "white"

DEFENDER_IMAGE = "../images/defender.png"
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

        # check the newly generated x value before changing the defender position
        # new_x = defender_rect.x + defender_x_direction * DEFENDER_SPEED
        # if new_x + DEFENDER_SIZE[0] >= WIN_RECT.right:  # clamp right
        #     defender_x_direction = DIRECTION_LEFT
        #     defender_rect.right = WIN_RECT.right
        # elif new_x <= WIN_RECT.left:  # clamp left
        #     defender_x_direction = DIRECTION_RIGHT
        #     defender_rect.left = WIN_RECT.left
        # else:
        #     defender_rect.x = new_x

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
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
    print("Done.")
