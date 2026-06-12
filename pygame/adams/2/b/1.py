"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Background music
"""

from typing import Any
import pygame


class Game:
    FPS = 30
    WIN_RECT: pygame.Rect = pygame.Rect(0, 0, 400, 200)
    BACKGROUND_COLOR = "white"
    TITLE = "Sound Background Music"
    FONT_SIZE = 40
    TEXT_COLOR = "red"
    MUSIC_FILE = "sounds/lucifer.mid"
    MUSIC_DEFAULT_VOLUME = 0.05
    VOLUME_STEP = 0.05

    def __init__(self) -> None:
        self.window = pygame.Window(Game.TITLE, Game.WIN_RECT.size)
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, Game.FONT_SIZE)
        self.pause = False
        self.sounds()

    def sounds(self) -> None:
        pygame.mixer.music.load(Game.MUSIC_FILE)
        pygame.mixer.music.set_volume(Game.MUSIC_DEFAULT_VOLUME)
        pygame.mixer.music.play(loops=-1)  # forever

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_f:
                    self.music_start_stop(fadeout=5000)
                elif event.key == pygame.K_j:
                    self.music_start_stop(loop=-1)
                elif event.key == pygame.K_p:
                    self.pause_alter()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 4:  # up
                    self.volume_alter(Game.VOLUME_STEP)
                elif event.button == 5:  # down
                    self.volume_alter(-Game.VOLUME_STEP)
        return True

    def music_start_stop(self, **kwargs: Any) -> None:
        if "fadeout" in kwargs.keys():
            pygame.mixer.music.fadeout(kwargs["fadeout"])
        if "loop" in kwargs.keys():
            pygame.mixer.music.play(kwargs["loop"], 0.0)

    def pause_alter(self) -> None:
        if self.pause:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
        self.pause = not self.pause

    def volume_alter(self, delta: float) -> None:
        volume = pygame.mixer.music.get_volume()
        volume += delta
        volume = pygame.math.clamp(volume, 0.0, 1.0)
        pygame.mixer.music.set_volume(volume)

    def draw(self) -> None:
        self.screen.fill(Game.BACKGROUND_COLOR)
        volume = pygame.mixer.music.get_volume()
        info = self.font.render(f"Volume: {volume:3.2f}", True, Game.TEXT_COLOR)
        info_rect = info.get_rect()
        info_rect.center = Game.WIN_RECT.center
        self.screen.blit(info, info_rect)

        self.window.flip()

    def run(self):
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
