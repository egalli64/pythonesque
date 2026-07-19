"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Background music
"""
import pygame

FPS = 30
WIN_SIZE = (400, 200)
TITLE = "Sound Background Music"
VOLUME_STEP = 0.05


def change_music_volume(delta: int) -> None:
    volume = pygame.mixer.music.get_volume() + delta * VOLUME_STEP
    pygame.mixer.music.set_volume(volume)  # clamped to [0, 1] by pygame


class Game:
    BACKGROUND_COLOR = "white"
    FONT_SIZE = 40
    TEXT_COLOR = "red"
    MUSIC_FILE = "sounds/lucifer.mid"
    VOLUME_DEFAULT = 0.05
    VOLUME_FADEOUT = 5000  # ms

    @classmethod
    def load_resources(cls) -> None:
        pygame.mixer.music.load(cls.MUSIC_FILE)
        cls._font = pygame.font.Font(None, cls.FONT_SIZE)

    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen
        self.viewport = self.screen.get_rect()
        self.running = True
        self.paused = False

        self.cur_volume = Game.VOLUME_DEFAULT
        pygame.mixer.music.set_volume(self.cur_volume)
        pygame.mixer.music.play(loops=-1)  # forever

        text = f"Volume: {self.cur_volume:.2f}"
        self.info = Game._font.render(text, True, Game.TEXT_COLOR)
        self.info_rect = self.info.get_rect(center=self.viewport.center)

    def handle_events(self) -> None:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.running = False
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            self.running = False
                        case pygame.K_f:
                            pygame.mixer.music.fadeout(Game.VOLUME_FADEOUT)
                            print("Fadeout")
                        case pygame.K_j:
                            pygame.mixer.music.play(loops=-1)  # forever
                            self.paused = False
                            print("Play")
                        case pygame.K_p:
                            self.toggle_pause()
                case pygame.MOUSEWHEEL:
                    change_music_volume(event.y)

    def toggle_pause(self) -> None:
        if self.paused:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
        self.paused = not self.paused
        print("Pause is now", "on" if self.paused else "off")

    def draw(self) -> None:
        self.screen.fill(Game.BACKGROUND_COLOR)
        volume = pygame.mixer.music.get_volume()
        if volume != self.cur_volume:
            text = f"Volume: {volume:.2f}"
            self.info = Game._font.render(text, True, Game.TEXT_COLOR)
            self.cur_volume = volume

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
