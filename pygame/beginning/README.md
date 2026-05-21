# Beginnning Python Games Development with PyGame

- https://link.springer.com/book/10.1007/978-1-4842-0970-7
- https://github.com/Apress/beg-python-games-dev-2ed
- Ensure pygame is available: pip install pygame-ce

## Chapter 3 - Introducing Pygame

- 1 [Hello pygame](c3/1.py) - init / quit; display.set_mode; event.get; Surface.blit; display.flip
- 2 [Event logger](c3/2.py)
- 3 [Key events](c3/3.py) - KEYDOWN / KEYUP; K_LEFT, K_RIGHT, K_UP, K_DOWN; Surface.fill
- 4 [Full screen](c3/4.py) - display.set_mode FULLSCREEN flag
- 5 [Resizable screen](c3/5.py) - display.set_mode RESIZABLE flag; event type VIDEORESIZE
- 6 [Text to image](c3/6.py) - font.SysFont; Font.render; image.save
- 7 [Scrolling text](c3/7.py) - event.wait() w/ timeout

## Chapter 4 - Creating Visuals

- 1 [Generate colors](c4/1.py) - Surface.set_at
- 2 [Choose a color](c4/2.py) - Rect, draw.rect, mouse.get_pos, mouse.get_pressed, draw.circle
