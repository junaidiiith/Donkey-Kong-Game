import pygame
import sys
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 0)
YELLOW = (255,255,0) 
SCREEN_WIDTH = 1200
SCREEN_HEIGHT =1000

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player,self).__init__()
        # width = 10
        # height = 10
        # self.image = pygame.Surface([width, height])
        # self.image.fill(RED)
#        self.chances = 3
        
        self.image = pygame.image.load('player.png')
        self.score = 0
        self.rect = self.image.get_rect()

        self.change_x = 0
        self.change_y = 0
        self.flag=0
        self.fl=0
        self.chances = 3
        self.level = None
 
    def update(self):
        ladder_hit_list = pygame.sprite.spritecollide(self,self.level.ladder_list,False)
        if len(ladder_hit_list) == 1:
            self.flag=1
        else :
            self.flag = 0
        if not self.flag : 
            self.calc_grav()
 
        self.rect.x += self.change_x
 
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right
        self.rect.y += self.change_y
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            self.change_y = 0
        blocks = pygame.sprite.spritecollide(self,self.level.coins_list,True)
        for x in blocks:
            self.score += 20
            print self.score
        
        if pygame.sprite.spritecollide(self,self.level.fireball_list,False):
            print "Score = %s" %(self.score)
            sys.exit()
        
        if pygame.sprite.spritecollide(self,self.level.donkey,False):
            #print "Game Over"
            print "Score = %s" %(self.score)
            sys.exit()
        
        if pygame.sprite.spritecollide(self,self.level.queen,False):
            print "Congratulations you won the game"
            print "Score = %s" %(self.score)
            sys.exit()
 
    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
 
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
 
    def jump(self):
        ladder_hit_list = pygame.sprite.spritecollide(self,self.level.ladder_list,False)
        if not ladder_hit_list:
            self.rect.y += 2
            platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            self.rect.y -= 2
 
            if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
                self.change_y = -5
        else:
            self.change_y = 0
    def go_left(self):
        self.change_x -= 2
 
    def go_right(self):
        self.change_x += 2
 
    def stop(self):
        self.change_x = 0

    def go_up(self):
        self.change_y += 2
        
    def go_down(self):
        self.change_y -= 2
