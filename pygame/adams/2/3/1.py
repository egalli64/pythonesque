"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Load and Blit Bitmaps
"""

import pygame

FPS = 30
TITLE = "Load and Draw of Bitmaps"
WIN_SIZE = (600, 400)
WIN_POS = (10, 50)
BACKGROUND_COLOR = "white"

SPRITE_DELTA_Y = 10

ALIEN_IMAGE = "../images/alien_big.png"
ALIEN_SIZE = (50, 45)
ALIEN_TRANSPARENT_COLOR = "black"
ALIEN_COUNT = 7
ALIEN_GAP = (WIN_SIZE[0] - ALIEN_COUNT * ALIEN_SIZE[0]) // (ALIEN_COUNT + 1)

DEFENDER_IMAGE = "../images/defender.png"
DEFENDER_SIZE = (30, 30)
DEFENDER_POS = (
    (WIN_SIZE[0] - DEFENDER_SIZE[0]) // 2,  # center
    WIN_SIZE[1] - DEFENDER_SIZE[1] - SPRITE_DELTA_Y,  # bottom
)


def main():
    window = pygame.Window(TITLE, WIN_SIZE, WIN_POS)
    screen = window.get_surface()
    clock = pygame.time.Clock()

    # make use of the alpha channel for transparency
    defender_image = pygame.image.load(DEFENDER_IMAGE).convert_alpha()
    defender_image = pygame.transform.scale(defender_image, DEFENDER_SIZE)

    # don't preserve transparency
    alien_image = pygame.image.load(ALIEN_IMAGE).convert()
    # make a color in the image transparent
    alien_image.set_colorkey(ALIEN_TRANSPARENT_COLOR)
    alien_image = pygame.transform.scale(alien_image, ALIEN_SIZE)

    while handle_events():
        clock.tick(FPS)

        screen.fill(BACKGROUND_COLOR)
        for i in range(ALIEN_COUNT):
            pos = (i + 1) * ALIEN_GAP + i * ALIEN_SIZE[0], SPRITE_DELTA_Y
            screen.blit(alien_image, pos)
        screen.blit(defender_image, DEFENDER_POS)
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
