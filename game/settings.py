import random

#game options/settimgs
TITLE = "No Ordinary Princess"
ScreenX = 1024
ScreenY = 720
FPS = 60


# Player Properties

PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = .5
PLAYER_JUMP = 18


# starting platforms

PLATFORM_LIST = [(0, ScreenY- 40, ScreenX, 40), 
                (ScreenX /2 - 50, ScreenY *3/4, 100, 20),
                (ScreenX - 100, ScreenY - 360, 100, 20),
                (ScreenX - 100, ScreenY - 540, 100, 20),
                (ScreenX/4, ScreenY * random.randint(25,50)/100, 200, 20)]

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LBROWN = (181, 101, 29)
DBROWN = (101, 67, 33)
