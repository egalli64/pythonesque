"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Normalizing speed - pixel for second
Time between frames, aka delta time, comes from clock.tick() - consider it "good enough"
Using FRect to let pygame to take care of position rounding issues
"""

import pygame

FPS = 30  # different FPS should give close enough results

TITLE = "Defender Movement"
WIN_SIZE = (120, 650)
WIN_POS = (10, 50)
BACKGROUND_COLOR = "white"

DEFENDER_FILENAME = "../images/defender.png"
DEFENDER_SIZE = (30, 30)
DEFENDER_SPEED = 200  # pixel/second

LINE_COLOR = "red"
LINE_START = (0, WIN_SIZE[1] // 2)
LINE_END = (WIN_SIZE[0], WIN_SIZE[1] // 2)
LINE_WIDTH = 2

RUNTIME_MS = 1500  # ms


# noinspection DuplicatedCode
def main():
    window = pygame.Window(TITLE, WIN_SIZE, WIN_POS)
    screen = window.get_surface()
    screen_rect = screen.get_rect()
    clock = pygame.time.Clock()

    defender_image = pygame.image.load(DEFENDER_FILENAME).convert_alpha()
    defender_image = pygame.transform.scale(defender_image, DEFENDER_SIZE)
    defender_rect = pygame.FRect(defender_image.get_rect())  # FRect keeps sub-pixel precision
    defender_rect.midbottom = screen_rect.centerx, screen_rect.bottom - 5
    defender_speed = DEFENDER_SPEED
    direction = -1  # moving up

    elapsed = 0
    running = True
    while running:
        dt = clock.tick(FPS) / 1000  # delta time in seconds
        running = handle_events()

        elapsed += dt
        if elapsed >= RUNTIME_MS / 1000:
            defender_speed = 0

        # Update
        defender_rect.top += direction * defender_speed * dt
        if defender_rect.bottom >= screen_rect.bottom or defender_rect.top <= screen_rect.top:
            defender_rect.clamp_ip(screen_rect)
            direction *= -1

        # Draw
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.line(screen, LINE_COLOR, LINE_START, LINE_END, LINE_WIDTH)

        # blit handles the FRect to Rect conversion
        screen.blit(defender_image, defender_rect)
        window.flip()

    print(f"Defender center y after {RUNTIME_MS / 1000:.2f} secs is {defender_rect.centery}")


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
