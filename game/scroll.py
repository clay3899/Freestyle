import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode([960,720])

red = (255,0,0)
green = (0,255,0)

centerx, centery = screen.get_rect().centerx, screen.get_rect().centery
deltaY = centery + 20 

rolling_text = '''
placeholder
placeholder
placeholder
'''

running = True
while running:
    for event in pygame.event.get():
        if event.type==QUIT:
            running = False
        
    screen.fill(0)
    
    deltaY -=0.75 #adjusts speed of text
    msg_list = []
    pos_list = []
    i=0
    
    font = pygame.font.SysFont('courier',30)

    for line in rolling_text.split('\n'):
        msg = font.render(line,True, red)
        msg_list.append(msg)
        
        pos = msg.get_rect(center=(centerx,centery + deltaY + i*30)) 
        pos_list.append(pos)
        i = i+1

    if (centery + deltaY + 30*(len(rolling_text.split('\n'))) < 0):
        running = False


    for j in range(i):
        screen.blit(msg_list[j], pos_list[j])
    pygame.display.update()
pygame.quit()