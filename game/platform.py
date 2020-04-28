


#initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((ScreenX, ScreenY))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()

# game loop

running = True
while running:
    # keep loop running at FPS
    clock.tick(FPS)

    # process input(events)
    

