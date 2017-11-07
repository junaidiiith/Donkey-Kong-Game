import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 0)
YELLOW = (255,255,0) 
SCREEN_WIDTH = 1200
SCREEN_HEIGHT =1000

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super(Platform,self).__init__()
 
        self.image = pygame.image.load('platform.png')
        #self.image.fill(GREEN)
 
        self.rect = self.image.get_rect()
       
        
