import pygame
from fireball import Fireball
from coins import Coins
from player import Player
from donkey import Donkey
import sys
from queen import Queen
from platform import Platform
from Levelnum import Level_num
from ladders import Ladders
import random
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 0)
YELLOW = (255,255,0) 
SCREEN_WIDTH = 1200
SCREEN_HEIGHT =1000


def main():
    pygame.init()
 
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Donkey Kong")
    
    
    score=0
                
    player = Player()
    player.score = score             
    current_level = Level_num(player)

    don = Donkey()
    don.level = current_level
    current_level.donkey.add(don)

    k = 845
    for i in range(1):
        for j in range(10):
            fireball = Fireball()
            fireball.rect.x = random.randint(300,800)
            fireball.rect.y = SCREEN_HEIGHT - k
            fireball.level = current_level
            fireball.player = player
            fireball.donkey = don
            current_level.fireball_list.add(fireball)
            k-=80

    k=845
    for i in range(10):
        for j in range(2):
            coin = Coins()
            coin.rect.x = random.randint(300,800)
            coin.rect.y = SCREEN_HEIGHT - random.randint(k,k+50)
            current_level.coins_list.add(coin)
        k-=80

    q = Queen()
    current_level.queen.add(q)

    active_sprite_list = pygame.sprite.Group()

    player.level = current_level


    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - 2*player.rect.height
    active_sprite_list.add(player)


    done = False

    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.go_left()
                if event.key == pygame.K_d:
                    player.go_right()
                if event.key == pygame.K_w:
                    player.go_down()
                if event.key == pygame.K_s:
                    player.go_up()
                if event.key == pygame.K_SPACE:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_d and player.change_x > 0:
                    player.stop()
                if event.key == pygame.K_w and player.change_y < 0:
                    player.stop()
                if event.key == pygame.K_s and player.change_y > 0:
                    player.stop()
        
        
            # if not player.chances:
            #     game = False
            #     break 
        active_sprite_list.update()

        current_level.update()

        #fireball_group.update()

        if player.rect.right > SCREEN_WIDTH:
            player.rect.right = SCREEN_WIDTH

        if player.rect.left < 0:
            player.rect.left = 0
        
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        clock.tick(60)

        pygame.display.flip()
pygame.quit()
 
if __name__ == "__main__":
    main()
