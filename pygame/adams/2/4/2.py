"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Normalizing speed - pixel for second vs pixel for frame
Measuring the speed in pixel for frame makes the game speed machine dependent.
"""

import pygame

FPS = 30  # change FPS to get different results

TITLE = "Defender Movement"
WIN_SIZE = (120, 650)
WIN_POS = (10, 50)
BACKGROUND_COLOR = "white"

DEFENDER_IMAGE = "../images/defender.png"
DEFENDER_SIZE = (30, 30)
DEFENDER_SPEED = 2
INITIAL_Y_GAP = 5

RUNTIME_MS = 5000


# noinspection DuplicatedCode
def main():
    window = pygame.Window(TITLE, WIN_SIZE, WIN_POS)
    screen = window.get_surface()
    screen_rect = screen.get_rect()
    clock = pygame.time.Clock()

    defender_image = pygame.image.load(DEFENDER_IMAGE).convert_alpha()
    defender_image = pygame.transform.scale(defender_image, DEFENDER_SIZE)
    defender_rect = defender_image.get_rect()
    defender_rect.midbottom = screen_rect.centerx, screen_rect.bottom - INITIAL_Y_GAP
    defender_speed = DEFENDER_SPEED
    direction = -1  # moving up

    start_time = pygame.time.get_ticks()
    running = True
    while running:
        clock.tick(FPS)
        running = handle_events()

        elapsed = pygame.time.get_ticks() - start_time
        if elapsed >= RUNTIME_MS:
            defender_speed = 0

        # Update
        defender_rect.top += direction * defender_speed
        if defender_rect.bottom >= screen_rect.bottom or defender_rect.top <= 0:
            defender_rect.clamp_ip(screen_rect)
            direction *= -1

        # Draw
        screen.fill(BACKGROUND_COLOR)
        screen.blit(defender_image, defender_rect)
        window.flip()

    print(f"Defender top after {RUNTIME_MS / 1000:.2f} secs is {defender_rect.top}")

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
