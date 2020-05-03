import random
import pygame
from pygame import *
from os import path

#game options/settimgs
TITLE = 'Champions are Coming'
WIDTH = 960
HEIGHT = 720
FPS = 60

# Player Properties

PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = .7
PLAYER_JUMP = 18
PLAYER_HEALTH = 100

# Arrows
ARROW_SPEED = 13
ARROW_DAMAGE = 10
SHOT_TIME = 400

# Enemy Health
ENEMY_HEALTH = 0

#Fireball
FIREBALL_SPEED = 5
FIREBALL_DAMAGE = 10

# starting platforms
PLATFORM_LIST = [(0, HEIGHT- 5, WIDTH, 10), 
                (WIDTH - 620, HEIGHT *3/4, 100, 5),
                (WIDTH - 120, HEIGHT - 360, 100, 5),
                (WIDTH - 155, HEIGHT - 540, 75, 5),
                (WIDTH - random.randint(475,500), HEIGHT - 300, 75, 5),
                (WIDTH/4, HEIGHT - random.randint(475,500), 200, 5)]

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LBROWN = (181, 101, 29)
DBROWN = (101, 67, 33)
YELLOW = (255, 255, 0)


# variable for image file path
img_dir = path.join(path.dirname(__file__), 'images')

#Story for Scrolling Text
STORY = '''
        Three evil wizards are about to attack your village! 


        They are currently at the edge of the forest...

        You have time to stop them, but must hurry!


        Will you be the hero and save your village? 

        Or will you let it be burned by the wizards' magic?


        Use the arrow keys to move and jump

        and the spacebar to shoot arrows!


        It is your time to let the wizards know that

        A Champion is Coming to foil their plan!


        Press Enter to Save Your Village
        '''