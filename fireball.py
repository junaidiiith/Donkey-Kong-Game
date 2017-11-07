import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 0)
YELLOW = (255,255,0) 
SCREEN_WIDTH = 1200
SCREEN_HEIGHT =1000

class Fireball(pygame.sprite.Sprite):
    def __init__(self):
        super(Fireball,self).__init__()
        # width = 10
        # height = 10
        # self.image = pygame.Surface([width, height])
        # self.image.fill(BLACK)
        self.image = pygame.image.load('fireball.png')
        self.score = 0
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        self.level = None
        self.donkey = None
 
        # Set speed vector of fireball
        self.change_x = 2
        self.change_y = 0
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .6
 
        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def update(self):

        self.calc_grav()
 
        # Move left/right

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
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0
        if self.rect.x <= 35 and self.rect.y > SCREEN_HEIGHT - 65:
            self.rect.x = self.donkey.rect.x
            self.rect.y = self.donkey.rect.y 
        if self.rect.x >= SCREEN_WIDTH - 35:
            self.change_x *= -1
        if self.rect.x <= 35:
            self.change_x *= -1
        
        



