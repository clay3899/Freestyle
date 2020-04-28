import random

#game options/settimgs
TITLE = "No Ordinary Princess"
WIDTH = 960
HEIGHT = 720
FPS = 60



# Player Properties

PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = .5
PLAYER_JUMP = 18


# starting platforms

PLATFORM_LIST = [(0, HEIGHT- 40, WIDTH, 40), 
                (WIDTH /2 - 50, HEIGHT *3/4, 100, 20),
                (WIDTH - 100, HEIGHT - 360, 100, 20),
                (WIDTH - 100, HEIGHT - 540, 100, 20),
                (WIDTH/4, HEIGHT * random.randint(25,50)/100, 200, 20)]

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LBROWN = (181, 101, 29)
DBROWN = (101, 67, 33)
