"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Blitting Part of a Bitmap
"""

import pygame

FPS = 30

TITLE = "Draw a Part of a Bitmap"
WIN_SIZE = (512, 512)

TILE_SIZE = (32, 32)
TILE_COLOR = "red"
TILE_SELECTED_WIDTH = 2
LAST_TILE_POS = (WIN_SIZE[0] - TILE_SIZE[0], WIN_SIZE[1] - TILE_SIZE[1])

IMAGE = "../images/forest_tiles.png"
BACKGROUND_COLOR = "white"


def main():
    window = pygame.Window(TITLE, WIN_SIZE)
    screen = window.get_surface()
    clock = pygame.time.Clock()

    image = pygame.image.load(IMAGE)
    pos = pygame.Vector2()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RIGHT:
                    pos.x += TILE_SIZE[0]
                elif event.key == pygame.K_LEFT:
                    pos.x -= TILE_SIZE[0]
                if event.key == pygame.K_DOWN:
                    pos.y += TILE_SIZE[1]
                if event.key == pygame.K_UP:
                    pos.y -= TILE_SIZE[1]
        pos.x = pygame.math.clamp(pos.x, 0, LAST_TILE_POS[0])
        pos.y = pygame.math.clamp(pos.y, 0, LAST_TILE_POS[1])

        screen.fill(BACKGROUND_COLOR)
        screen.blit(image)

        pygame.draw.rect(screen, TILE_COLOR, (pos, TILE_SIZE), TILE_SELECTED_WIDTH)
        screen.blit(image, LAST_TILE_POS, (pos, TILE_SIZE))

        window.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    pygame.init()

    try:
        main()
    finally:
        pygame.quit()
        print("Done.")
