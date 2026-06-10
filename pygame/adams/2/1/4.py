"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Multiple windows
"""

import pygame

FPS = 30

WIN_SIZE = (300, 100)
WIN_POSS = ((500, 50), (820, 50))
TITLES = ("Main Window", "Side Window")
BACKGROUND_COLORS = ((0, 255, 0), (255, 0, 0))


def main():
    windows = {
        pygame.Window(TITLES[0], WIN_SIZE, WIN_POSS[0]),
        pygame.Window(TITLES[1], WIN_SIZE, WIN_POSS[1]),
    }

    def handle_events() -> bool:
        """Run the event loops, return False in case of termination request"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Closing last window:", event)
                return False
            elif event.type == pygame.WINDOWCLOSE:
                print("Close request from window", event.window.id)
                event.window.hide()
                windows.discard(event.window)
        return True

    clock = pygame.time.Clock()
    background_colors = {w.id: c for w, c in zip(windows, BACKGROUND_COLORS)}

    while handle_events():
        clock.tick(FPS)

        for window in windows:
            screen = window.get_surface()
            screen.fill(background_colors[window.id])
            window.flip()


if __name__ == "__main__":
    pygame.init()

    try:
        main()
    finally:
        pygame.quit()
        print("Done.")
