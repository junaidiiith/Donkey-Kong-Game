import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 0)
YELLOW = (255,255,0) 
SCREEN_WIDTH = 1200
SCREEN_HEIGHT =1000
class Level(object):
 
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.ladder_list = pygame.sprite.Group()
        self.fireball_list = pygame.sprite.Group()
        self.coins_list = pygame.sprite.Group()
        self.donkey = pygame.sprite.Group()
        self.queen = pygame.sprite.Group()
        self.player = player
        self.level = [
                 [20,SCREEN_HEIGHT,0,0],
                 [SCREEN_WIDTH,20,20,SCREEN_HEIGHT-20],
                 [20,SCREEN_HEIGHT,SCREEN_WIDTH-20,0],
                 [SCREEN_WIDTH-20,20,20,0]
                 ]
         
        self.background = None
 
    def update(self):
        """ Update everything in this level."""
        self.ladder_list.update()
        self.platform_list.update()
        self.fireball_list.update()
        self.coins_list.update()
        self.donkey.update()
        
    def draw(self, screen):
        screen.fill(BLUE)
 
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.ladder_list.draw(screen)
        self.fireball_list.draw(screen)
        self.coins_list.draw(screen)
        self.donkey.draw(screen)
        self.queen.draw(screen)
        # #self.message("Score",RED,screen)
        # font = pygame.font.SysFont(None,25)
        # text = font.render("msg",True,color)
        # screen.blit(txt,200,20)



