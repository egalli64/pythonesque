"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Sound effects
"""

import pygame


class Game:
    FPS = 30
    WIN_RECT: pygame.Rect = pygame.Rect(0, 0, 400, 200)
    BACKGROUND_COLOR = "black"
    TITLE = "Sound effects"
    FONT_SIZE = 40
    TEXT_COLOR = "red"
    EFFECT_BUBBLE = "sounds/plop.mp3"
    EFFECT_CLASH = "sounds/glass.wav"

    VOLUME_STEP = 0.05

    def __init__(self) -> None:
        self.window = pygame.Window(Game.TITLE, Game.WIN_RECT.size)
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, Game.FONT_SIZE)

        self.bubble = pygame.mixer.Sound(Game.EFFECT_BUBBLE)
        self.clash = pygame.mixer.Sound(Game.EFFECT_CLASH)

        self.info = self.font.render("Volume: _.__", True, Game.TEXT_COLOR)
        self.info_rect = self.info.get_rect()
        self.info_rect.center = Game.WIN_RECT.center
        self.cur_volume = -1  # invalid volume

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # left
                    self.bubble.play()
                elif event.button == 3:  # right
                    self.clash.play()
            elif event.type == pygame.MOUSEWHEEL:
                self.change_volume(event.y)

        return True

    def change_volume(self, delta):
        volume = self.bubble.get_volume() + delta * Game.VOLUME_STEP
        self.bubble.set_volume(volume)
        self.clash.set_volume(volume)

    def draw(self) -> None:
        self.screen.fill(self.BACKGROUND_COLOR)
        volume = self.bubble.get_volume()
        if volume != self.cur_volume:
            text = f"Volume: {volume:.2f}"
            self.info = self.font.render(text, True, Game.TEXT_COLOR)
            self.cur_volume = volume

        self.screen.blit(self.info, self.info_rect)
        self.window.flip()

    def run(self):
        self.running = True
        while self.handle_events():
            self.clock.tick(Game.FPS)
            self.draw()


if __name__ == "__main__":
    pygame.init()

    try:
        Game().run()
    finally:
        pygame.quit()
        print("Done.")
