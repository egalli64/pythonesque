"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Message Boxes
"""

import pygame

FPS = 30

TITLE = "Message Boxes"
WIN_SIZE = (200, 200)
BACKGROUND_COLOR = "white"

MB_INFO = "This is an info message box."
MB_WARN = "This is a warning message box. Proceed?"
MB_ERR = "This is an error message box."


def main():
    pygame.init()
    window = pygame.Window(TITLE, WIN_SIZE)
    screen = window.get_surface()
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_1:
                    pygame.display.message_box("Information", MB_INFO)
                elif event.key == pygame.K_2:
                    btns = ["Yes", "No"]
                    x = pygame.display.message_box("⚠", MB_WARN, "warn", buttons=btns)
                    print("User selected:", x)
                elif event.key == pygame.K_3:
                    pygame.display.message_box("Error", MB_ERR, "error")

        screen.fill(BACKGROUND_COLOR)
        window.flip()
        clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    main()
    print("Done")
