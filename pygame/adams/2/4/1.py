"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Using Rect and its attributes
"""

import pygame

FPS = 30

TITLE = "Defender Movement"
WIN_SIZE = (400, 100)
WIN_POS = (10, 50)
BACKGROUND_COLOR = "white"

DEFENDER_IMAGE = "../images/defender.png"
DEFENDER_SIZE = (30, 30)
Y_GAP = 5

DEFENDER_SPEED = 2


def main():
    window = pygame.Window(TITLE, WIN_SIZE, WIN_POS)
    screen = window.get_surface()
    screen_rect = screen.get_rect()
    clock = pygame.time.Clock()

    defender_image = pygame.image.load(DEFENDER_IMAGE).convert_alpha()
    defender_image = pygame.transform.scale(defender_image, DEFENDER_SIZE)
    defender_rect = defender_image.get_rect()
    defender_rect.midbottom = screen_rect.centerx, screen_rect.height - Y_GAP
    direction = 1  # moving right

    running = True
    while running:
        clock.tick(FPS)
        running = handle_events()

        # Update
        # instead of checking the newly generated x value before changing the defender position
        # working on a new Rect shifted by an x, y offset is usually handier
        candidate = defender_rect.move(direction * DEFENDER_SPEED, 0)
        if candidate.right >= screen_rect.right:  # clamp right
            direction *= -1
            candidate.right = screen_rect.right
        elif candidate.left <= screen_rect.left:  # clamp left
            direction *= -1
            candidate.left = screen_rect.left
        defender_rect = candidate

        # Draw
        screen.fill(BACKGROUND_COLOR)
        screen.blit(defender_image, defender_rect)
        window.flip()


# noinspection DuplicatedCode
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
