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

    running = True
    while running:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update

        # Draw
        screen.fill(BACKGROUND_COLOR)
        screen.blit(defender_image, defender_rect)

        window.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
    print("Done.")
