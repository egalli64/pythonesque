# Introduction to Pygame-ce by Ralf Adams

- https://github.com/adamsralf/pygame_book
- My notes: https://github.com/egalli64/pythonesque/ pygame/adams folder
- Ensure pygame is available: pip install pygame-ce

# Chapter 2 - Basics
## Section 1 - Kind of Hello World!
- 1: [Hello pygame](2/1/1.py) - init and quit
- 2: [Hello again, pygame](2/1/2.py) - Window
- 3: [It's me again, pygame](2/1/3.py) - Clock
- 4: [Multiple windows](2/1/4.py) - WINDOWCLOSE event

## Section 2 - Graphic primitives
- 1: [Introduction](2/2/1.py) - functions in module draw 
- 2: [Particle swarm /1](2/2/2.py) - draw.circle, pygame mouse support
- 3: [Particle swarm /2](2/2/3.py) - some randomness
- 4: [Particle swarm /3](2/2/4.py) - mutable particles, fountain effect
- 5: [Particle swarm /4](2/2/5.py) - add x-scattering
- 6: [Particle swarm /6](2/2/6.py) - more features added
- 7: [Landscape example](2/2/7.py)

## Section 3 - Load and blit bitmaps
- 1: [Load and blit](2/3/1.py)
- 2: [Partial blitting](2/3/2.py)
- 3: [Message boxes](2/3/3.py)
- 4: [Landscape blit](2/3/4.py) - !!! Caching surfaces is not useful in such simple cases !!!

## Section 4 - Moving bitmaps
- 1: [Using Rect and its attributes](2/4/1.py)
- 2: [Speed in pixel for frame](2/4/2.py) - simple but unreliable
- 3: [Normalizing speed](2/4/3.py) - pixel for second, based on delta time, using FRect

## Section 5 - Class Sprite
- 1: [Defender as a Sprite](2/5/1.py)
- 2: [Sprite collision](2/5/2.py)
- 3: [Sprite Group](2/5/3.py)
- 4: [A Game class](2/5/4.py) - encapsulating the game framework in a class
- 5: [Add/remove sprite to group](2/5/5.py)

## Section 6 Handling keyboard input
- 1: [Control direction by keys](2/6/1.py)
- 2: [Modifier keys - shift](2/6/2.py)
- 3: [Polling key status](2/6/3.py) - key.get_pressed()

## Section 7 Text output using fonts
- 1: [Simple text rendering](2/7/1.py)
- 2: [Text as a Sprite](2/7/2.py)
- 3: [List of installed fonts](2/7/3.py)
- 4: [Using locally installed fonts](2/7/4.py)

## Section 8 Collision Detection
- 1: [Types of collision](2/8/1.py)
- 2: [Collision with a group](2/8/1.py)

## Section 9 Time-based Actions
- 1: [The need of having a break](2/9/1.py)
- 2: [Timed continous fire](2/9/2.py) Using time.get_ticks

## Section 10 Mouse
- 1: [Mouse actions](2/a/1.py)
- 2: [Simple double click](2/a/2.py)
- 3: [Custom double click](2/a/3.py)

## Section 11 Sound
- 1: [Background music](2/b/1.py)
- 2: [Effects](2/b/2.py)
- 3: [Stereo sound](2/b/3.py)
