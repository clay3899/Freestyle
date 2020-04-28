import pygame as pg
import random
import math
from pygame.locals import *
from pygame import mixer
import os
from os import path
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # initialiaze game window, etc.
        self.running = True
        pg.init()
        pg.mixer.init()
        #display_screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pass
    
    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.enemy = Enemy(850, 600, 'wizard.png')
        self.all_sprites.add(self.enemy) 
        
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
      
        self.run()
        pass

    def run(self):
        # game loop
        
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

        pass
    
    def update(self):
        # game loop -- updates
        self.all_sprites.update()
        #check if player hits platform if falling
        
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
                self.player.acc.y = 0        
    
    def events(self):
        # game loop -- events
        for event in pg.event.get():

            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                    self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.player.jump()
            if event.type == pg.KEYUP:
                    self.player.fire()
        
    
    def draw(self):
        # game loop -- draw
        self.screen.fill(BLACK) #can change the background of the screen here
        
        self.all_sprites.draw(self.screen)
        
        # after drawing
        pg.display.flip()

    
    def start_screen(self):
        # game splash
        
        
        pass
    
    def end_screen(self):
        pass


g = Game()
g.start_screen()
while g.running:
    g.new()
    g.end_screen()

pg.quit()