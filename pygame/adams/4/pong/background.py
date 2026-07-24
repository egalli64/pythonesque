"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Pong background
"""
import pygame


class Background(pygame.sprite.Sprite):
    COLOR = "darkred"
    NET_COLOR = "gray"

    image: pygame.Surface
    rect: pygame.Rect

    def __init__(self, viewport: pygame.Rect) -> None:
        super().__init__()
        self.image = pygame.Surface(viewport.size).convert()
        self.image.fill(Background.COLOR)
        self.rect = self.image.get_rect()

        net_rect = pygame.Rect(0, 50, 2, 30)
        net_rect.centerx = viewport.centerx
        while net_rect.bottom < viewport.bottom:
            pygame.draw.rect(self.image, Background.NET_COLOR, net_rect, 0)
            net_rect.move_ip(0, 40)

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)
