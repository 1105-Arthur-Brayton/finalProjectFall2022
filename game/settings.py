# Game settings
 
# Window dimensions
WIDTH = 1280
HEIGHT = 720

FPS = 30


PLAYER_GRAVITY = 3

# Colors
# You can change these values, but then you'd be wrong
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)
TEAL = (177, 255, 255)

# Timer
FRAME = 1
TIMER = 0
RAMP = 150
# ramp sets the time in ticks when the score will decrease

# score. Starts at 5 because PhaseOne is slow
SCORE = 100000

# simplifies the spawn block
PhaseOne = SCORE <= 15
PhaseTwo = 15 <= SCORE <= 25
PhaseThree = 25 <= SCORE <= 35
PhaseFour = 35 <= SCORE <= 45
PhaseFive = 45 <= SCORE <= 55

if SCORE <= 15:
    Phase = 1
if 15 <= SCORE <= 25:
    Phase = 2
if 25 <= SCORE <= 35:
    Phase = 3
if 35 <= SCORE <= 45:
    Phase = 4
if 45 <= SCORE <= 55:
    Phase = 5