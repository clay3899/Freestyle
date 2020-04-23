
import pygame
import random
import math
from pygame.locals import *
from pygame import mixer

ScreenX = 960
ScreenY = 720
FPS = 30

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 0)
LBROWN = (181, 101, 29)
DBROWN = (101, 67, 33)


#initialize pygame and create window
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((ScreenX, ScreenY))
pygame.display.set_caption("Calling all Champions")
clock = pygame.time.Clock()

class player:
    def __init__(self, movementX, movementY):
        self.movement = movement
        
    
    def set_location(self,x, y):
        self.x = x
        self.y = y
        self.xMovement = 0
        self.yMovement = 0

    def keys(self):
        k = pygame.key.get_pressed()
        
        if k[K_LEFT]: 
            self.xMovement = -self.movement
        if k[K_RIGHT]: 
            self.xMovement = self.movement
        if k[K_UP]:
            self.yMovement = -self.movement
        if k[K_DOWN]:
            self.yMovement = self.movement    

    def move(self):
        self.x += self.xMovement
        
        if self.x > 1216:
            self.x = 1216
        if self.x < 0:
            self.x = 0
        
        self.y += self.yMovement
        
        if self.y > 1216:
            self.y = 1216
        if self.y < 0:
            self.y = 0

    def draw(self, image):
       display = pygame.display.get_surface()

       display.blit(image, (self.x, self.y))
        

    def do(self):
        self.keys()
        self.move()
        self.draw()

class enemy(object): 
    def __init__(self,x,y):  # initial position
        self.x = x 
        self.y = y
    def move(self, speed=5): # chase movement
        # Movement along x direction
        if self.x > px:
            self.x -= speed
        elif self.x < px:
            self.x += speed
        # Movement along y direction
        if self.y < py:
            self.y += speed
        elif self.y > py:
            self.y -= speed

class button():
    def __init__(self, color, x,y,width,height,text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, outline=None):
        # Call this to draw the button on the screen
        if outline:
            pygame.draw.rect(screen, outline, (self.x-2,self.y-2,self.width+4,self.height+4), 0)

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.Font('fonts/Dreamwood.ttf', 24)
            text = font.render(self.text, 1, (BLACK))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinate
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        
        return False


all_sprites = pygame.sprite.Group()



# Game Loop
running = True

while running == True:
    #keep loop running at right speed
    clock.tick(FPS)
    
    #process input
    for event in pygame.event.get():
        # check for close
        if event.type == pygame.QUIT:
            running = False




    #update
    all_sprites.update()

    #draw / render
    
    all_sprites.draw(screen)

    screen.fill(BLACK)
    
    
    
    
    
    
    
    
    
    
    

   
    # do this last
    pygame.display.flip()


pygame.quit()