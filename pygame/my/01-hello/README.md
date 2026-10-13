# Hello Pygame-CE

### [A minimal app](hello.py)

- Start and initialize PyGame in the main block
    - try a call to main () and finally quit PyGame
- In the main function:
    - Create a window with a hello title, size 300x300, in the upper left display corner, like 50x50
    - Get the window surface, it represents the screen where we are going to draw stuff
    - Get a clock, will call tick () on it, to reduce the app CPU load
- Define the main loop, ruled by a running flag
    - Invoke tick on the clock for a given FPS (could be very low, for what we care here)
    - Define the event loop
        - It is going to set the running flag to False if the user quit or Esc the app
    - No logic is present in this app, nothing to update
    - Fill the screen with a background color
    - Update the display surface to the window

### [A minimal Game class](hello_classy.py)

- Refactor the previous Hello World app wrapping the code in a Game class

## Extra

### [The legacy approach](x1_legacy.py)

- Using the pygame display module instead of the Window class

### [A resizable window](x2_sizing.py)

- Creating a resizable window, with min/max dimensions

### [A borderless window](x3_border.py)

- Creating a borderless window
