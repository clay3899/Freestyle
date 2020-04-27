import pygame
import random
import math
from pygame.locals import *
from pygame import mixer
import os
from os import path


ScreenX = 960
ScreenY = 720
FPS = 60

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

# set up assets

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")
sounds_folder = os.path.join(game_folder, "sounds")

#classes
knight = "spellun-run.png"
wizard = "wizard.png"
goblin = "goblin.png"
archer = "archer.png"


# tools
sword = "sword_normal.png"

fireball = "Fireball1.png"


class Player(pygame.sprite.Sprite):
    # sprite for the player
    
    def __init__(self, job, movement, weapon):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, job)).convert()
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image, (64,64))
        self.rect = self.image.get_rect()
        self.radius = self.radius = int(self.rect.width * .95 / 2)
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.center = (100, 100)
        self.movement = movement
        self.movementy = 5
        self.speedx = 0
        self.speedy= 0
        self.weapon= weapon
    def update(self):
        self.speedx = 0
        self.speedy= 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -self.movement
        if keystate[pygame.K_RIGHT]:
            self.speedx = self.movement
        if keystate[pygame.K_UP]:
            self.speedy = -self.movement
        if keystate[pygame.K_DOWN]:
            self.speedy =  self.movement
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > ScreenX:
            self.rect.right = ScreenX
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > (ScreenY):
            self.rect.bottom = ScreenY
        if self.rect.top < 0:
            self.rect.top = 0
    def attack(self):
        
        
        weapon = Weapon(self.weapon, self.rect.centerx, self.rect.centery)
        all_sprites.add(weapon)
        weapons.add(weapon)

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
        
        if self.x > ScreenX - 64:
            self.x = ScreenX - 64
        if self.x < 0:
            self.x = 0
        
        self.y += self.yMovement
        
        if self.y > ScreenY - 64:
            self.y = ScreenY -64
        if self.y < 0:
            self.y = 0

    def draw(self, image):
       display = pygame.display.get_surface()

       display.blit(image, (self.x, self.y))
        

    def do(self):
        self.keys()
        self.move()
        self.draw()

class Mob(pygame.sprite.Sprite): 
    def __init__(self, job, movement, player):  # initial position
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, job)).convert()
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image, (64,64))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .95 / 2)
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randint(500, ScreenX)
        self.rect.y = random.randint(0, ScreenY)
        self.movement = movement
        self.speedy = self.movement
        self.speedx = self.movement

    def update(self):
        
        if self.rect.y < player.rect.y:
            self.rect.y += self.speedy
        if self.rect.y > player.rect.y:
            self.rect.y += -self.speedy
        if self.rect.x < player.rect.x:
            self.rect.x += self.speedx
        if self.rect.x > player.rect.x:
            self.rect.x += -self.speedx

class Weapon(pygame.sprite.Sprite):
    def __init__(self, tool, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, tool)).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedx = 10
        self.speedy = 0
        self.positionx = x
    
    def update(self):
        
       
                     
        self.rect.x += self.speedx
        
        if self.rect.left > self.positionx + 240:
            self.kill()
        


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

background = pygame.image.load(path.join(img_folder, "map1.png")).convert()
background_rect =  background.get_rect()

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()


# Mob Spawn Function
def newmob(monster, speed, player):
    m = Mob(monster, speed, player)
    all_sprites.add(m)
    mobs.add(m)


#PLAYER CREATION

player = Player(knight, 5, sword)
all_sprites.add(player)

weapons = pygame.sprite.Group()

for i in range(3):
    newmob(goblin, 3, player)


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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.attack()



    #update
    all_sprites.update()

    # check to see if mob hit player

    hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)

    if hits:
        hit_sound = mixer.Sound(os.path.join(sounds_folder, "get_hit.ogg"))
        pygame.mixer.music.set_volume(0.1)
        hit_sound.play()

        
         
    
    # check to see if weapon hit mob
    hits = pygame.sprite.groupcollide(mobs, weapons, True, True)

    for hit in hits:
        hit_sound = mixer.Sound(os.path.join(sounds_folder, "dirtwalk.ogg"))
        hit_sound.play()
        newmob(goblin, 3, player)




    #draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)

    
    
    
    
    
    
    
    
    
    
    
    

   
    # do this last
    pygame.display.flip()


pygame.quit()