import pygame as pg
from settings import *
from os import path

vec = pg.math.Vector2
img_dir = path.join(path.dirname(__file__), 'images')




# from KidsCanCode
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
        self.health = PLAYER_HEALTH
        self.radius = 15 
    
    def jump(self):
        
        self.rect.y += 1

        hits = pg.sprite.spritecollide(self,self.game.platforms, False)
        self.rect.y -= 1
        
        if hits:
            self.vel.y = -PLAYER_JUMP
    
        
    
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
        self.health = ENEMY_HEALTH
        

        
    def update(self):
        if self.health <= 0:
            self.kill()
    
    def draw_health(self):
        if self.health > 60:
            col = GREEN
        elif self.health > 30:
            col = YELLOW
        else:
            col = RED

        width = int(self.rect.width * self.health/ENEMY_HEALTH)
        width2 = int(self.rect.width)
        self.health_bar = pg.Rect(0, 0, width, 7)
        self.total = pg.Rect(0,0, width2, 7)
        if self.health < ENEMY_HEALTH:
            pg.draw.rect(self.image, BLACK, self.total)
            pg.draw.rect(self.image, col, self.health_bar)
        

class Arrow(pg.sprite.Sprite):
    def __init__(self, x, y, img):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(path.join(img_dir, img)).convert_alpha()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.centerx = x
        self.pos = vec(x, y)
        self.vel = vec(ARROW_SPEED,-3)
        self.acc = vec(0,0)
    
    def update(self):
        
        # equations of motion
        self.acc = vec(0, PLAYER_GRAV)
        self.acc.x += self.vel.x
        self.vel.y += self.acc.y
        self.pos += self.vel + 0.5 * self.acc
        
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y - 32

        if self.rect.x > WIDTH + 100:
            self.kill()
        if self.rect.y > HEIGHT + 100:
            self.kill()

        pass
       
class Fireball(pg.sprite.Sprite):
    def __init__(self, x, y, img):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(path.join(img_dir, img)).convert_alpha()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.centerx = x
        self.pos = vec(x, y)
        self.vel = vec(-FIREBALL_SPEED,0)
        self.acc = vec(0,0)
    
    def update(self):
        
        # equations of motion
        self.acc = vec(0, 0.008)
        self.acc.x += self.vel.x
        self.vel.y += self.acc.y
        self.pos += self.vel + 0.5 * self.acc
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y - 64
        pass
               
        
    


        
        

             