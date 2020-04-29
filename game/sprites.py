import pygame as pg
from settings import *
from os import path

vec = pg.math.Vector2
img_dir = path.join(path.dirname(__file__), 'images')

# All comes from KidsCanCode
class Player(pg.sprite.Sprite):
    def __init__(self, game, img):
        self.game = game
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((32,32))
        self.image = pg.image.load(path.join(img_dir, img)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    
    def jump(self):
        
        self.rect.y += 1

        hits = pg.sprite.spritecollide(self,self.game.platforms, False)
        self.rect.y -= 1
        
        if hits:
            self.vel.y = -PLAYER_JUMP
    
    def fire(self):
       pass
        
    
    def update(self):
        self.acc = vec(0,PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC

        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC


        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # Nothing passed the sides
        self.rect.midbottom = self.pos

        if self.pos.x > WIDTH:
            self.pos.x  = WIDTH
        if self.pos.x < 0:
            self.pos.x = 0

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Source: https://opensource.com/article/18/5/pygame-enemy
class Enemy(pg.sprite.Sprite):
    def __init__(self,x,y, img): #add an img attribute
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(path.join(img_dir, img)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



class Arrow(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface(5,1)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.pos = vec(x, y)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    
    def update(self):
        pass
       
         
        
    


        
        

             