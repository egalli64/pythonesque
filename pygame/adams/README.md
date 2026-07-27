# Introduction to Pygame-ce by Ralf Adams

- https://github.com/adamsralf/pygame_book
- My notes: https://github.com/egalli64/pythonesque/ pygame/adams folder
- Ensure pygame is available: pip install pygame-ce

# Chapter 2 - Basics
## Section 1 - Kind of Hello World!
- 1: [Hello pygame](c2/s01/e1.py) - init and quit
- 2: [Hello again, pygame](c2/s01/e2.py) - Window
- 3: [It's me again, pygame](c2/s01/e3.py) - Clock
- 4: [Multiple windows](c2/s01/e4.py) - WINDOWCLOSE event

## Section 2 - Graphic primitives
- 1: [Introduction](c2/s02/e1.py) - functions in module draw 
- 2: [Particle swarm /1](c2/s02/e2.py) - draw.circle, pygame mouse support
- 3: [Particle swarm /2](c2/s02/e3.py) - some randomness
- 4: [Particle swarm /3](c2/s02/e4.py) - mutable particles, fountain effect
- 5: [Particle swarm /4](c2/s02/e5.py) - add x-scattering
- 6: [Particle swarm /6](c2/s02/e6.py) - more features added
- 7: [Landscape example](c2/s02/e7.py)

## Section 3 - Load and blit bitmaps
- 1: [Load and blit](c2/s03/e1.py)
- 2: [Partial blitting](c2/s03/e2.py)
- 3: [Message boxes](c2/s03/e3.py)
- 4: [Landscape blit](c2/s03/e4.py) - !!! Caching surfaces is not useful in such simple cases !!!

## Section 4 - Moving bitmaps
- 1: [Using Rect and its attributes](c2/s04/e1.py)
- 2: [Speed in pixel for frame](c2/s04/e2.py) - simple but unreliable
- 3: [Normalizing speed](c2/s04/e3.py) - pixel for second, based on delta time, using FRect

## Section 5 - Class Sprite
- 1: [Defender as a Sprite](c2/s05/e1.py)
- 2: [Sprite collision](c2/s05/e2.py)
- 3: [Sprite Group](c2/s05/e3.py)
- 4: [A Game class](c2/s05/e4.py) - encapsulating the game framework in a class
- 5: [Add/remove sprite to group](c2/s05/e5.py)

## Section 6 Handling keyboard input
- 1: [Control direction by keys](c2/s06/e1.py)
- 2: [Modifier keys - shift](c2/s06/e2.py)
- 3: [Polling key status](c2/s06/e3.py) - key.get_pressed()

## Section 7 Text output using fonts
- 1: [Simple text rendering](c2/7/1.py)
- 2: [Text as a Sprite](c2/7/2.py)
- 3: [List of installed fonts](c2/7/3.py)
- 4: [Using locally installed fonts](c2/7/4.py)

## Section 8 Collision Detection
- 1: [Types of collision](c2/8/1/main.py)
- 2: [Collision with a group](c2/8/2/game.py)

## Section 9 Time-based Actions
- 1: [The need of having a break](c2/9/1.py)
- 2: [Timed continuous fire](c2/9/2.py) Using time.get_ticks

## Section 10 Mouse
- 1: [Mouse actions](c2/a/1/game.py)
- 2: [Simple double click](c2/a/2.py)
- 3: [Custom double click](c2/a/3.py)

## Section 11 Sound
- 1: [Background music](c2/b/1.py)
- 2: [Effects](c2/b/2.py)
- 3: [Stereo sound](c2/b/3/game.py)

## Section 12 Events
- 1: [Printing events](c2/c/1.py)
- 2: [User defined events](c2/c/2.py)
- 3: [Periodic events](c2/c/3.py)

# Chapter 3 - Techniques
## Section 1 - Animation
- 1: [A running cat](3/1/1/game.py) - by time.get_ticks()
- 2: [Exploding rocks](3/1/2/game.py)
- 3: [Colliding rocks](3/1/3/game.py)
- 1: [A running cat](3/1/4/game.py) - by dt from main loop

## Section 2 - Tileset
- 1 [Extract a tile from a tileset](3/2/1.py)

# Chapter 4 - Examples
- 1: [Pong](4/pong/game.py)
- 2: [Bubbles](4/bubbles/game.py)
- 3: [Moon Lander](4/moonlander/game.py)
