#!/usr/bin/python

import pygame
from wall import *
from Player import *
from Rooms import *


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
SILVER = (171, 194, 190)
PINK = (246, 58, 122)
def main():



    pygame.init()


    screen = pygame.display.set_mode([800, 600])


    pygame.display.set_caption('Maze Runner')


    player = Player(50, 50)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)

    rooms = []

    room = Room1()
    rooms.append(room)

    room = Room2()
    rooms.append(room)

    room = Room3()
    rooms.append(room)

    room = Room4()
    rooms.append(room)

    room = Room5()
    rooms.append(room)

    room = TESTROOM()
    rooms.append(room)

    current_room_no = 0
    current_room = rooms[current_room_no]

    clock = pygame.time.Clock()

    done = False

    while not done:



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)



        player.move(current_room.wall_list)

        if player.rect.x < -15:
            if current_room_no == 0:
                current_room_no = 3
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 3:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 2:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 790
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 790

        if player.rect.x > 801:
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 1:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 2:
                current_room_no = 3
                current_room = rooms[current_room_no]
                player.rect.x = 0
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 0
#---------------------------------------------------------------------------------------------------------------------------------------------------------
        if player.rect.y < -15:
            if current_room_no == 3:
                current_room_no = 4
                current_room = rooms[current_room_no]
                player.rect.y = 590
            elif current_room_no == 4:
                current_room_no = 5
                current_room = rooms[current_room_no]
                player.rect.y = 590
            else:
                current_room_no = 3
                current_room = rooms[current_room_no]
                player.rect.y = 590

        if player.rect.y > 601:
            if current_room_no == 3:
                current_room_no = 5
                current_room = rooms[current_room_no]
                player.rect.y = 0
            elif current_room_no == 5:
                current_room_no = 4
                current_room = rooms[current_room_no]
                player.rect.y = 0
            else:
                current_room_no = 3
                current_room = rooms[current_room_no]
                player.rect.y = 0



        screen.fill(BLACK)

        if current_room_no == 5:

            f1 = pygame.font.Font(None, 36)
            text1 = f1.render('TEST', 1, (RED))
 
            
 
            screen.blit(text1, (350, 250))
            

 
        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
