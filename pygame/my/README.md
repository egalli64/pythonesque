# A few simple PyGame apps

Tested on pygame-ce 2.5.7, Python 3.14

## [Hello PyGame](hello.py)

- Start and initialize PyGame in the \_\_main__ block
  - try a call to main() and finally quit PyGame
- In the main function:
  - Create a window with a hello title, size 300x300, in the upper left display corner, like 50x50
  - Get the window surface, it represents the screen where we are going to draw stuff
  - Get a clock, will call tick() on it, to reduce the app CPU load
- Define the main loop, ruled by a running flag
  - Invoke tick on the clock for a given FPS (could be very low, for what we care here)
  - Define the event loop
    - It is going to set the running flag to False if the user quit or Esc the app
  - No logic is present in this app, nothing to update
  - Fill the screen with a background color
  - Update the display surface to the window 

## [Bouncing Ball](bb/game.py)

- In a 800x600 window
- There is a colored (red) ball
    - with radius 20px, placed in the window center
    - moving with initial velocity (200, -100)
- The ball should never leave the window
    - It is expected to keep its speed, inverting its direction
- Controls
    - Space: change the ball color randomly
    - Up/Down Arrow: change the speed by 10% (faster/slower)
        - But it should not get too fast/slow
    - R: reset to the original state
    - P: pause/unpause the game
    - Left click: move the ball to the cursor
- Display
    - Render the ball speed in a window corner
