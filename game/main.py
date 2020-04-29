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
        self.enemies = pg.sprite.Group()
        self.arrows = pg.sprite.Group()
        self.player = Player(self, 'archer.png')
        self.all_sprites.add(self.player)
        self.enemy1 = Enemy(680, 655, 'wizard.png')
        self.enemy2 = Enemy(WIDTH - 100, HEIGHT - 420, 'wizard.png')
        self.enemy3 = Enemy(WIDTH - 155, HEIGHT - 600, 'wizard.png')
        self.all_sprites.add(self.enemy1, self.enemy2, self.enemy3) 
        self.enemies.add(self.enemy1, self.enemy2, self.enemy3)
        self.previous_time = pg.time.get_ticks()
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
            hits = pg.sprite.spritecollide(self.player, self.platforms, False,)
        
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
                self.player.acc.y = 0        
    
        hits = pg.sprite.groupcollide(self.enemies, self.arrows, False, True)
        for hit in hits:
            hit.health -= ARROW_DAMAGE

        hits = pg.sprite.groupcollide(self.platforms, self.arrows, False, True)
        for hit in hits:
            hit.acc = (0,0)
            hit.vel = (0,0)


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
                if event.key == pg.K_SPACE:
                    self.current_time = pg.time.get_ticks()
                    if self.current_time - self.previous_time > SHOT_TIME:   
                        self.previous_time = self.current_time
                        self.fire()


    
    def draw(self):
        # game loop -- draw
    
        
        
        
        self.background_image = pg.image.load("game\images\Forest.jpg").convert()
        self.screen.blit(self.background_image, [0, 0])
        self.all_sprites.draw(self.screen)
        
        
        
        
        # after drawing
        pg.display.flip()

    
    def start_screen(self):
        # game splash
        
        #self.background = pg.image.load('game\images\Home_Screen.jpg').convert()
        #self.background = pg.transform.scale(self.background, (WIDTH, HEIGHT))
        #self.screen.blit(self.background,[0,0])
        #self.draw_text("Are You Ready for the Challenge?", 35, WIDTH/2, HEIGHT/2 -100, WHITE)
        #self.draw_text("If so, press [ENTER] to begin", 35, WIDTH/2, (HEIGHT/2), WHITE)
        #self.draw_text("If not, press [Q] to quit", 35, WIDTH/2, (HEIGHT/2) + 100, WHITE)
        #self.draw_text("MOVE: USE ARROWS", 35, 630, 550, WHITE)
        #self.draw_text("FIRE: USE SPACE", 35, 630, 600, WHITE )
        
        #pg.mixer.music.load('game\sounds\Destiny.mp3')
        #pg.mixer.music.set_volume(0.5)
        #pg.mixer.music.play(-1)
        #pg.display.update()

        #pg.display.flip()
        #self.wait_for_key()


    #def wait_for_key(self):
        #waiting= True
        #while waiting:
          #  self.clock.tick(FPS)
          #  for event in pg.event.get():
          #      if event.type == pg.QUIT:
          #          waiting = False
          #          self.running = False
          #      elif event.type == pg.KEYDOWN:
          #          if event.key == pygame.K_RETURN:
          #              waiting = False
          #          elif event.key == pygame.K_q:
          #              waiting = False
          #              self.running = False
        pass
    def draw_text(self, text, size, x, y, color):

        font = pg.font.Font(pg.font.match_font('cambria'), size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)  
       
       
        pass
    
    def fire(self):
        arrow = Arrow(int(self.player.rect.centerx),int(self.player.rect.centery), 'uber_tiny.png')
        self.all_sprites.add(arrow)
        self.arrows.add(arrow)
        
    def end_screen(self):
        pass


g = Game()
g.start_screen()
while g.running:
    g.new()
    g.end_screen()

pg.quit()