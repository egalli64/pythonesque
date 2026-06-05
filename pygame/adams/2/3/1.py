"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Load and Blit Bitmaps
"""

import pygame
import config as cfg


def main():
    pygame.init()
    window = pygame.Window(cfg.TITLE, cfg.WIN_SIZE, cfg.WIN_POS)
    screen = window.get_surface()
    clock = pygame.time.Clock()

    # make use of the alpha channel for transparency
    defender_image = pygame.image.load(cfg.DEFENDER_IMAGE).convert_alpha()
    defender_image = pygame.transform.scale(defender_image, cfg.DEFENDER_SIZE)

    # don't preserve transparency
    alien_image = pygame.image.load(cfg.ALIEN_IMAGE).convert()
    # make a color in the image transparent
    alien_image.set_colorkey(cfg.ALIEN_TRANSPARENT_COLOR)
    alien_image = pygame.transform.scale(alien_image, cfg.ALIEN_SIZE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(cfg.BACKGROUND_COLOR)
        screen.blit(alien_image, cfg.ALIEN_POS)
        screen.blit(defender_image, cfg.DEFENDER_POS)

        window.flip()
        clock.tick(cfg.FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
    print("Done.")
