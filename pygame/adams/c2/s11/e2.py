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
BACKGROUND_COLOR = "black"
FONT_SIZE = 40
TEXT_COLOR = "red"
VOLUME_STEP = 0.05


class Sound(Enum):
    BUBBLE = "sounds/plop.mp3"
    CLASH = "sounds/glass.wav"


class Game:
    @classmethod
    def load_resources(cls) -> None:
        cls._font = pygame.font.Font(None, FONT_SIZE)
        cls._sounds = {sound: pygame.mixer.Sound(sound.value) for sound in Sound}

    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen
        viewport = self.screen.get_rect()
        self.running = True

        self.displayed_volume = Game._sounds[Sound.BUBBLE].get_volume()
        text = f"Volume: {self.displayed_volume:.2f}"
        self.info = Game._font.render(text, True, TEXT_COLOR)
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
                    Game.change_volume(event.y)

    @staticmethod
    def change_volume(delta: int) -> None:
        volume = pygame.mixer.Sound.get_volume(Game._sounds[Sound.BUBBLE]) + delta * VOLUME_STEP
        for sound in Game._sounds.values():
            sound.set_volume(volume)  # clamped to [0.0, 1.0] by pygame

    def draw(self) -> None:
        self.screen.fill(BACKGROUND_COLOR)
        volume = Game._sounds[Sound.BUBBLE].get_volume()
        if volume != self.displayed_volume:
            text = f"Volume: {volume:.2f}"
            self.info = Game._font.render(text, True, TEXT_COLOR)
            self.displayed_volume = volume

        self.screen.blit(self.info, self.info_rect)
        self.window.flip()

    def run(self) -> None:
        clock = pygame.time.Clock()

        while self.running:
            clock.tick(FPS)
            self.handle_events()
            self.draw()


if __name__ == "__main__":
    pygame.init()

    try:
        main_window = pygame.Window(TITLE, WIN_SIZE)
        main_surface = main_window.get_surface()

        Game.load_resources()

        Game(main_window, main_surface).run()
    finally:
        pygame.quit()
