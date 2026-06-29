"""
Master Python by making 5 games - 4: Platformer

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=26735s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Platform
Google Drive: https://drive.google.com/drive/folders/1FCSPHzD9R4RBUypDTB_FIfwlyiCLA5WN

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

from sprite import AnimatedSprite


class Bee(AnimatedSprite):
    PATHNAME = "images/enemies/bee"

    @classmethod
    def load_resources(cls):
        cls._frames = cls.import_folder(Bee.PATHNAME)

    def __init__(self, pos, groups):
        super().__init__(pos, Bee._frames, groups)

    def update(self, dt):
        self.animate(dt)


class Worm(AnimatedSprite):
    PATHNAME = "images/enemies/worm"

    @classmethod
    def load_resources(cls):
        cls._frames = cls.import_folder(Worm.PATHNAME)

    def __init__(self, pos, groups):
        super().__init__(pos, Worm._frames, groups)

    def update(self, dt):
        self.animate(dt)
