import pygame
color = (15,115,111)
Screen_width = 1200
Screen_height = 1000
class Queen(pygame.sprite.Sprite):
    def __init__(self):
        super(Queen,self).__init__()
        self.image = pygame.image.load('queen.png')
        self.rect = self.image.get_rect()
        self.rect.x = 650
    	self.rect.y = Screen_height - 950
        
        
         
       
        



