import pygame
Pink= (10,20,30)
class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super(Coins,self).__init__()
        # width = 10
        # height = 10
        # self.image = pygame.Surface([width, height])
        #self.image.fill(Pink)
        self.image = pygame.image.load('coins.png')
        self.score = 0
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        

