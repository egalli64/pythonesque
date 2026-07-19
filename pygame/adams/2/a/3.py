"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Double click - customized
"""
import pygame

FPS = 30
WIN_SIZE = (400, 100)
TITLE = "Double click me"
BACKGROUND_COLOR = "white"

DOUBLE_CLICK_TIME = 300  # ms
DOUBLE_CLICK_DISTANCE = 8  # pixels


def main(window: pygame.Window, screen: pygame.Surface) -> None:
    clock = pygame.time.Clock()

    last_click_time = 0
    # initialize the last click position out of viewport
    last_click_pos = pygame.Vector2(-DOUBLE_CLICK_DISTANCE, -DOUBLE_CLICK_DISTANCE)

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
                case pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                case pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        # left mouse click detected now
                        now = pygame.time.get_ticks()

                        if now <= last_click_time + DOUBLE_CLICK_TIME:
                            distance = pygame.Vector2(event.pos).distance_to(last_click_pos)
                            if distance <= DOUBLE_CLICK_DISTANCE:
                                print("Double click")
                            else:
                                print("A click far away enough from the previous one")
                        else:
                            print("A new single click")

                        last_click_time = now
                        last_click_pos = pygame.Vector2(event.pos)

        screen.fill(BACKGROUND_COLOR)
        window.flip()


if __name__ == "__main__":
    pygame.init()
    pg_window = pygame.Window(TITLE, WIN_SIZE)
    pg_screen = pg_window.get_surface()

    try:
        main(pg_window, pg_screen)
    finally:
        pygame.quit()
        print("Done.")
