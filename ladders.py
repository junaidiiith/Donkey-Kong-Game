import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 0)
YELLOW = (255,255,0) 
SCREEN_WIDTH = 1200
SCREEN_HEIGHT =1000
class Ladders(pygame.sprite.Sprite):
 
    def __init__(self,width,height):
        super(Ladders,self).__init__()
 
        self.image = pygame.Surface([width,height])
        self.image.fill(YELLOW)
 
        self.rect = self.image.get_rect()
