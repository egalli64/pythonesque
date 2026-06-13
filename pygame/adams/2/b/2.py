"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Sound effects
"""

from os import path
import pygame


class Game:
    FPS = 30
    WINDOW: pygame.Rect = pygame.Rect(0, 0, 400, 200)
    VOLUME_STEP = 0.05

    def __init__(self) -> None:
        self.window = pygame.Window(
            size=Game.WINDOW.size, title="Sound Background Music"
        )
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()
        self.font_bigsize = pygame.font.Font(pygame.font.get_default_font(), 40)
        self.running = True
        self.pause = False
        self.sounds()

    def sounds(self) -> None:
        self.bubble = pygame.mixer.Sound("sounds/plop.mp3")
        self.clash = pygame.mixer.Sound("sounds/glass.wav")

    def watch_for_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # left
                    self.bubble.play()
                elif event.button == 3:  # right
                    self.clash.play()
                elif event.button == 4:  # up
                    self.volume_alter(Game.VOLUME_STEP)
                elif event.button == 5:  # down
                    self.volume_alter(-Game.VOLUME_STEP)

    def volume_alter(self, delta: float) -> None:
        volume = self.bubble.get_volume() + delta
        self.bubble.set_volume(volume)
        self.clash.set_volume(volume)

    def draw(self) -> None:
        self.screen.fill("black")
        volume = self.bubble.get_volume()
        volume_surface = self.font_bigsize.render(f"Volume: {volume:.2f}", True, "red")
        volume_rect = volume_surface.get_rect()
        volume_rect.center = Game.WINDOW.center
        self.screen.blit(volume_surface, volume_rect)
        self.window.flip()

    def run(self):
        self.running = True
        while self.running:
            self.watch_for_events()
            self.draw()
            self.clock.tick(Game.FPS)


if __name__ == "__main__":
    pygame.init()

    try:
        Game().run()
    finally:
        pygame.quit()
        print("Done.")
