import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0,0)
YELLOW = (255,255,0)
SOME = (125,125,125) 
SCREEN_WIDTH = 1200
SCREEN_HEIGHT =1000

class Donkey(pygame.sprite.Sprite):
    def __init__(self):
        super(Donkey,self).__init__()
        # width = 10
        # height = 10
        # self.image = pygame.Surface([width, height])
        # self.image.fill(SOME)
        self.image = pygame.image.load('dk.png')
        self.score = 0
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = SCREEN_HEIGHT-852
        self.level = None
 
        # Set speed vector of fireball
        self.change_x = 2
       
    def update(self):

        if self.rect.x < 200 or self.rect.x > 800:
            self.change_x *= -1
        self.rect.x += self.change_x
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
                self.change_x *= -1
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
                self.change_x *= -1