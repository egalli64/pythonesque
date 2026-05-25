# Beginnning Python Games Development with PyGame

- https://link.springer.com/book/10.1007/978-1-4842-0970-7
- https://github.com/Apress/beg-python-games-dev-2ed
- Ensure pygame is available: pip install pygame-ce

## Chapter 3 - Introducing Pygame

- 1 [Hello pygame](c3/1.py) - init / quit, display.set_mode, event.get, Surface.blit, display.flip
- 2 [Event logger](c3/2.py)
- 3 [Key events](c3/3.py) - KEYDOWN / KEYUP, K_LEFT, K_RIGHT, K_UP, K_DOWN, Surface.fill
- 4 [Full screen](c3/4.py) - display.set_mode FULLSCREEN flag
- 5 [Resizable screen](c3/5.py) - display.set_mode RESIZABLE flag, event type VIDEORESIZE, event.wait
- 6 [Text to image](c3/6.py) - font.SysFont, Font.render, image.save
- 7 [Scrolling text](c3/7.py) - event.wait w/timeout

## Chapter 4 - Creating Visuals

- 1 [Generate colors](c4/1.py) - Surface.set_at
- 2 [Choose a color](c4/2.py) - Rect, draw.rect, mouse.get_pos, mouse.get_pressed, draw.circle
- 3 [Make a color darker](c4/3.py)
- 4 [Saturating channels](c4/4.py)
- 5 [Linear interpolation](c4/5.py) - Aka lerp
- 6 [Blending colors by lerping](c4/6.py) - draw.polygon
- 7 [Setting pixels](c4/7.py) - Surface.set_at
- 8 [Setting pixels w/locking](c4/8.py) - Surface.lock, Surface.set_at and get_at
- 9 [Rectangle](c4/9.py) - draw.rect
- 10 [Polygon](c4/a.py) - draw.polygon, draw.circle
- 11 [Circle](c4/b.py) - draw.circle
- 12 [Ellipse](c4/c.py) - draw.ellipse
- 13 [Arc](c4/d.py) - draw.arc
- 14 [Line](c4/e.py) - draw.line
- 15 [Lines](c4/f.py) - draw.lines
- 16 [Antialiased line](c4/g.py) - draw.line, draw.aaline

## Chapter 5 - Making Things Move

- 1 [Simple movement](c5/1.py) - don't do that
- 2 [Time-Based Movement](c5/2.py) - better, still not good
- 3 [Speed comparision](c5/3.py) - mock to show the simple approach problem (introducing FPS too)
- 4 [Simple Diagonal Movement](c5/4.py) - common pygame approach
- 5 [Vector2](c5/5.py) - pygame.Vector2 (a 2D "thing" with vector operations)
- 6 [Algebraic vector with Vector2](c5/6.py) - overloaded - (\_\_sub\_\_) for Vector2 objects
- 8 [Vector2 magnitude](c5/8.py) - Vector2.magnitude
- 9 [Normalized vector](c5/9.py) - Vector2.normalize and normalize_ip
- 10 [Vector2 addition](c5/a.py) - overloaded + (\_\_add\_\_) for Vector2 objects
- 12 [Vector2 negation](c5/c.py) - overloaded unary - (\_\_neg\_\_) for Vector2 objects
- 13 [Vector2 multiplication and division](c5/d.py) - overloaded \* and \\ - (\_\_mult\_\_ and \_\_truediv\_\_) for Vector2 objects
- 14 [Calculating positions](c5/e.py) - using Vector2 features
- 16 [Time-based movement](c5/g.py) - using Vector2 features

## Chapter 6 - Accepting User Input

- 1 [Testing pressed keys](c6/1.py) - KEYDOWN event.type, key.get_pressed
- 2 [Arrow keys for movement](c6/2.py) - key.get_pressed, K_LEFT ..., Vector2.normalize_ip
