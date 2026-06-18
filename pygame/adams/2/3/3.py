"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Message Boxes
"""

import pygame

FPS = 30
TITLE = "Message Boxes"
WIN_SIZE = (300, 100)
BACKGROUND_COLOR = "white"

MB_INFO = "This is an info message box."
MB_WARN = "This is a warning message box. Proceed?"
MB_ERR = "This is an error message box."


def main():
    window = pygame.Window(TITLE, WIN_SIZE)
    screen = window.get_surface()
    clock = pygame.time.Clock()

    while handle_events():
        clock.tick(FPS)
        screen.fill(BACKGROUND_COLOR)
        window.flip()


def handle_events() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
            elif event.key == pygame.K_1:
                pygame.display.message_box("Information", MB_INFO)
            elif event.key == pygame.K_2:
                btns = ["Yes", "No"]
                x = pygame.display.message_box("Warning", MB_WARN, "warn", buttons=btns)
                print("User selected:", x)
            elif event.key == pygame.K_3:
                pygame.display.message_box("Error", MB_ERR, "error")
    return True


if __name__ == "__main__":
    pygame.init()

    try:
        main()
    finally:
        pygame.quit()
        print("Done.")
