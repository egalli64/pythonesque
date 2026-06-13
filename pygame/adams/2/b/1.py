"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Background music
"""

import pygame


class Game:
    FPS = 30
    WIN_RECT: pygame.Rect = pygame.Rect(0, 0, 400, 200)
    BACKGROUND_COLOR = "white"
    TITLE = "Sound Background Music"
    FONT_SIZE = 40
    TEXT_COLOR = "red"
    MUSIC_FILE = "sounds/lucifer.mid"
    VOLUME_DEFAULT = 0.05
    VOLUME_STEP = 0.05
    VOLUME_FADEOUT = 5000  # ms

    def __init__(self) -> None:
        self.window = pygame.Window(Game.TITLE, Game.WIN_RECT.size)
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, Game.FONT_SIZE)
        self.pause = False

        pygame.mixer.music.load(Game.MUSIC_FILE)
        pygame.mixer.music.set_volume(Game.VOLUME_DEFAULT)
        pygame.mixer.music.play(loops=-1)  # forever

        self.info = self.font.render("Volume: _.__", True, Game.TEXT_COLOR)
        self.info_rect = self.info.get_rect()
        self.info_rect.center = Game.WIN_RECT.center
        self.cur_volume = -1  # invalid volume

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_f:
                    pygame.mixer.music.fadeout(Game.VOLUME_FADEOUT)
                    print("Fadeout")
                elif event.key == pygame.K_j:
                    pygame.mixer.music.play(loops=-1)  # forever
                    print("Play")
                elif event.key == pygame.K_p:
                    self.pause_alter()
            elif event.type == pygame.MOUSEWHEEL:
                self.change_volume(event.y)
        return True

    def pause_alter(self) -> None:
        if self.pause:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
        self.pause = not self.pause
        print("Pause is now", "on" if self.pause else "off")

    def change_volume(self, delta):
        volume = pygame.mixer.music.get_volume() + delta * Game.VOLUME_STEP
        pygame.mixer.music.set_volume(volume)  # clamped to [0, 1] by pygame

    def draw(self) -> None:
        self.screen.fill(Game.BACKGROUND_COLOR)
        volume = pygame.mixer.music.get_volume()
        if volume != self.cur_volume:
            text = f"Volume: {volume:.2f}"
            self.info = self.font.render(text, True, Game.TEXT_COLOR)
            self.cur_volume = volume

        self.screen.blit(self.info, self.info_rect)
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
