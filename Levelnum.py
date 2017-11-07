import pygame
from level import Level
from platform import Platform
from ladders import Ladders
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 0)
YELLOW = (255,255,0) 
SCREEN_WIDTH = 1200
SCREEN_HEIGHT =1000
class Level_num(Level):
 
    def __init__(self,player):
 
        Level.__init__(self, player)
        self.obstacles = [
                     [800,20,20,SCREEN_HEIGHT-120],
                     [200,20,860,SCREEN_HEIGHT-120],
                     [SCREEN_WIDTH-380,20,400,SCREEN_HEIGHT-220],
                     [150,20,210,SCREEN_HEIGHT-220],
                     [700,20,20,SCREEN_HEIGHT-320],
                     [300,20,760,SCREEN_HEIGHT-320],
                     [SCREEN_WIDTH-380,20,400,SCREEN_HEIGHT-420],
                     [200,20,160,SCREEN_HEIGHT-420],
                     [500,20,20,SCREEN_HEIGHT-520],
                     [400,20,560,SCREEN_HEIGHT-520],
                     [SCREEN_WIDTH-330,20,350,SCREEN_HEIGHT-620],
                     [100,20,210,SCREEN_HEIGHT-620],
                     [750,20,20,SCREEN_HEIGHT-720],
                     [200,20,810,SCREEN_HEIGHT-720],
                     [SCREEN_WIDTH-380,20,400,SCREEN_HEIGHT-820],
                     [150,20,210,SCREEN_HEIGHT-820],
                     [100,20,600,SCREEN_HEIGHT-920],
                     [200,20,740,SCREEN_HEIGHT-920],
                 ]
        self.ladders  = [
                [820,SCREEN_HEIGHT-120,55,100],
                [350,SCREEN_HEIGHT-220,55,100],
                [710,SCREEN_HEIGHT-320,55,100],
                [350,SCREEN_HEIGHT-420,55,100],
                [515,SCREEN_HEIGHT-520,55,100],
                [305,SCREEN_HEIGHT-620,55,100],
                [755,SCREEN_HEIGHT-720,55,100],
                [355,SCREEN_HEIGHT-820,55,100],
                [695,SCREEN_HEIGHT-920,55,100],
                [800,SCREEN_HEIGHT-220,55,30],
                [800,SCREEN_HEIGHT-160,55,20],
                [800,SCREEN_HEIGHT-620,55,30],
                [800,SCREEN_HEIGHT-560,55,20]
                
                
            ]
        L = [self.level[0],self.level[2]]
        for platform in L:
            k = platform[3]
            for i in range(platform[1]/16):
                block = Platform()
                block.rect.x = platform[2]
                block.rect.y = k
                self.platform_list.add(block)
                k+=16
        
        __level = [self.level[1],self.level[3]]
        for i in self.obstacles:
            __level.append(i)
 
        for platform in __level:
            __k = platform[2]
            for i in range(platform[0]/16):
                block = Platform()
                block.rect.x = __k
                block.rect.y = platform[3]
                block.player = self.player
                self.platform_list.add(block)
                __k+=16

        for ladder in self.ladders:
            block = Ladders(ladder[2],ladder[3])
            block.rect.x = ladder[0]
            block.rect.y = ladder[1]
            self.ladder_list.add(block)
