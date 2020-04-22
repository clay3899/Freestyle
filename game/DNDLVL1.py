import pygame
import random
import math

# initialize pygame
pygame.init()


#create the screen
screen = pygame.display.set_mode((1280, 960))


# The Button Class is taken with Gratitude from Tech with Tim on YouTube
# https://www.youtube.com/watch?v=4_9twnEduF
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
            text = font.render(self.text, 1, (0,0,0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinate
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        
        return False


# Title and Icon

pygame.display.set_caption("Calling all Champions")
icon = pygame.image.load('images/crown.png')
pygame.display.set_icon(icon)

enemy_spawnX = [192, 256, 320, 384, 448, 512, 576, 640, 704]
enemy_spawnY = [0, 64, 128, 192, 256, 320, 384, 448, 512, 576, 640, 704]


# Player
playerImg = pygame.image.load('images/knight.png')
playerX = 0
playerY = 0
playerX_change = 64
playerY_change = 64


# Player Movement and moves left

player_movement = 30
moves = (player_movement/5)

movesfont = pygame.font.Font('fonts/MidnightMinutes.ttf', 32) 
moveX = 1088
moveY = 20

# Enemy
enemyImg= []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
enemy_movement = []
enemy_moves = []
number_of_enemies = 4

for i in range(number_of_enemies):
    enemyImg.append(pygame.image.load('images/goblin.png'))
    enemyX.append(random.choice(enemy_spawnX))
    enemyY.append(random.choice(enemy_spawnY))  
    enemyX_change.append(64)
    enemyY_change.append(64)
    enemy_movement.append(30)
    enemy_moves.append(enemy_movement[i]/5)

# background

background = pygame.image.load("images/map1.png").convert()

def show_moves(x, y):
    move_count = movesfont.render("Moves Left    " + str(int(moves)), True, (255,255,255))
    screen.blit(move_count, (x, y))

def enemy(x,y,i):
    screen.blit(enemyImg[i], (x,y))

def player(x,y):
    screen.blit(playerImg, (x, y))

# game loop
running = True

EndTurn = button((181, 101, 29), 1142, 886, 128, 64, 'End Turn')

while running:
    # RGB
    screen.fill((0,0,0))

    #background Image
    screen.blit(background, (0,0))

    for event in pygame.event.get():

        pos = pygame.mouse.get_pos()


        if event.type == pygame.QUIT:
            running = False
        
        # click end turn
        if event.type == pygame.MOUSEBUTTONDOWN:
            if EndTurn.isOver(pos):
                for i in range(number_of_enemies):
                    enemyX[i] -= enemyX_change[i]
                    moves = (player_movement/5)
        if event.type == pygame.MOUSEMOTION:
            if EndTurn.isOver(pos):
                EndTurn.color = (101, 67, 33)
            else:
                EndTurn.color = (181, 101, 29)



        # if keystroke is pressed 1 time
        if event.type == pygame.KEYUP:
            if moves > 0: 
                if event.key == pygame.K_LEFT:
                    playerX -= playerX_change
                    moves -= 1
                    if playerX < 0:
                        playerX = 0
                        moves +=1
                    for i in range(number_of_enemies):
                        if playerX == enemyX[i] and playerY == enemyY[i]:
                            playerX += playerX_change 
                            moves +=1
                if event.key == pygame.K_RIGHT:
                    playerX += playerX_change
                    moves -= 1
                    if playerX > 1216:
                        playerX = 1216
                        moves +=1
                    for i in range(number_of_enemies):
                        if playerX == enemyX[i] and playerY == enemyY[i]:
                            playerX -= playerX_change 
                            moves +=1
    
                if event.key == pygame.K_UP:
                    playerY -= playerY_change
                    moves -= 1
                    if playerY < 0:
                        playerY = 0
                        moves +=1
                    for i in range(number_of_enemies):
                        if playerX == enemyX[i] and playerY == enemyY[i]:
                            playerY += playerY_change 
                            moves +=1
                
                if event.key == pygame.K_DOWN:
                    playerY += playerY_change
                    moves -= 1
                    if playerY > 896:
                        playerY = 896
                        moves +=1
                    for i in range(number_of_enemies):
                        if playerX == enemyX[i] and playerY == enemyY[i]:
                            playerY -= playerY_change 
                            moves +=1

    
    
    player(playerX, playerY)
    for i in range(number_of_enemies):
        enemy(enemyX[i], enemyY[i], i)
    EndTurn.draw(screen)
    show_moves(moveX, moveY)
    pygame.display.update()
    

    
   
    


