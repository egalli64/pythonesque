"""
Master Python by making 5 games - 4: Platformer

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=26735s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Platform
Google Drive: https://drive.google.com/drive/folders/1FCSPHzD9R4RBUypDTB_FIfwlyiCLA5WN

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame


class CameraGroup(pygame.sprite.Group):
    def __init__(self, viewport: pygame.Rect):
        super().__init__()
        self.viewport = viewport

    def camera_draw(self, screen, target_pos):
        offset = pygame.Vector2()
        offset.x = -(target_pos[0] - self.viewport.centerx)
        offset.y = -(target_pos[1] - self.viewport.centery)

        for sprite in self:
            screen.blit(sprite.image, sprite.rect.topleft + offset)
