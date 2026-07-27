"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Sound effects
"""
from enum import Enum

import pygame

FPS = 30
WIN_SIZE = (400, 200)
TITLE = "Sound effects"


class Sound(Enum):
    BUBBLE = "sounds/plop.mp3"
    CLASH = "sounds/glass.wav"


class Game:
    BACKGROUND_COLOR = "black"
    FONT_SIZE = 40
    TEXT_COLOR = "red"
    VOLUME_STEP = 0.05

    @classmethod
    def load_resources(cls) -> None:
        cls._font = pygame.font.Font(None, cls.FONT_SIZE)
        cls._sounds = {sound: pygame.mixer.Sound(sound.value) for sound in Sound}

    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen
        viewport = self.screen.get_rect()
        self.running = True

        self.displayed_volume = Game._sounds[Sound.BUBBLE].get_volume()
        text = f"Volume: {self.displayed_volume:.2f}"
        self.info = self._font.render(text, True, Game.TEXT_COLOR)
        self.info_rect = self.info.get_rect(center=viewport.center)

    def handle_events(self) -> None:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.running = False
                case pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                case pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        Game._sounds[Sound.BUBBLE].play()
                    elif event.button == pygame.BUTTON_RIGHT:
                        Game._sounds[Sound.CLASH].play()
                case pygame.MOUSEWHEEL:
                    self.change_volume(event.y)

    def change_volume(self, delta: int) -> None:
        volume = pygame.mixer.Sound.get_volume(Game._sounds[Sound.BUBBLE]) + delta * Game.VOLUME_STEP
        volume = max(0.0, min(1.0, volume))
        for sound in Game._sounds.values():
            sound.set_volume(volume)

    def draw(self) -> None:
        self.screen.fill(self.BACKGROUND_COLOR)
        volume = Game._sounds[Sound.BUBBLE].get_volume()
        if volume != self.displayed_volume:
            text = f"Volume: {volume:.2f}"
            self.info = self._font.render(text, True, Game.TEXT_COLOR)
            self.displayed_volume = volume

        self.screen.blit(self.info, self.info_rect)
        self.window.flip()

    def run(self) -> None:
        clock = pygame.time.Clock()

        while self.running:
            clock.tick(FPS)
            self.handle_events()
            self.draw()


# noinspection DuplicatedCode
if __name__ == "__main__":
    pygame.init()
    pg_window = pygame.Window(TITLE, WIN_SIZE)
    pg_screen = pg_window.get_surface()

    Game.load_resources()

    try:
        Game(pg_window, pg_screen).run()
    finally:
        pygame.quit()
        print("Done.")
