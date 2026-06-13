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
        self.font = pygame.font.Font(None, 40)

        self.bubble = pygame.mixer.Sound(Game.EFFECT_BUBBLE)
        self.clash = pygame.mixer.Sound(Game.EFFECT_CLASH)

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
                elif event.button == 4:  # up
                    self.volume_alter(Game.VOLUME_STEP)
                elif event.button == 5:  # down
                    self.volume_alter(-Game.VOLUME_STEP)
                elif event.type == pygame.MOUSEWHEEL:
                    self.change_volume(event.y)

        return True

    def change_volume(self, delta):
        volume = pygame.mixer.music.get_volume() + delta * Game.VOLUME_STEP
        volume = pygame.math.clamp(volume, 0.0, 1.0)
        pygame.mixer.music.set_volume(volume)  # clamped to [0, 1] by pygame


    def volume_alter(self, delta: float) -> None:
        volume = self.bubble.get_volume() + delta
        self.bubble.set_volume(volume)
        self.clash.set_volume(volume)

    def draw(self) -> None:
        self.screen.fill(self.BACKGROUND_COLOR)
        volume = self.bubble.get_volume()
        text = f"Volume: {volume:.2f}"
        volume_surface = self.font.render(text, True, Game.TEXT_COLOR)
        volume_rect = volume_surface.get_rect()
        volume_rect.center = Game.WIN_RECT.center
        self.screen.blit(volume_surface, volume_rect)
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
