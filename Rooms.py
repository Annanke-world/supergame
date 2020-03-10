#!/usr/bin/python

import pygame
from wall import *
from TEST import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
PINK = (246, 58, 122)
class Room(object):
    
    wall_list = None
    enemy_sprites = None

    def __init__(self):

        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()


class Room1(Room):
    def __init__(self):
        super().__init__()


        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [390, 50, 20, 580, RED]
                ]


        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room2(Room):

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, RED],
                 [0, 350, 20, 250, RED],
                 [780, 0, 20, 250, RED],
                 [780, 350, 20, 250, RED],
                 [20, 0, 760, 20, RED],
                 [20, 580, 760, 20, RED],
                 [190, 50, 20, 500, GREEN],
                 [590, 50, 20, 500, GREEN]
                ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room3(Room):

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, PURPLE],
                 [0, 350, 20, 250, PURPLE],
                 [780, 0, 20, 250, PURPLE],
                 [780, 350, 20, 250, PURPLE],
                 [20, 0, 760, 20, PURPLE],
                 [20, 580, 760, 20, PURPLE]
                ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        for x in range(100, 800, 100):
            for y in range(50, 451, 300):
                wall = Wall(x, y, 20, 200, RED)
                self.wall_list.add(wall)

        for x in range(150, 700, 100):
            wall = Wall(x, 200, 20, 200, WHITE)
            self.wall_list.add(wall)


class Room4(Room):

    def __init__(self):
        super().__init__()

 
        
        
 
        walls = [[0, 0, 20, 250, WHITE],#LL
                 [0, 350, 20, 250, WHITE],#
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 580, 330, 20, WHITE],
                 [0, 0, 350, 20, WHITE],
                 [450, 0, 350, 20, WHITE],
                 [450, 580, 330, 20, WHITE]
                 ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

class Room5(Room):

    def __init__(self):
        super().__init__()


        walls = [[0, 0, 20, 600, WHITE],
                 [780, 0, 20, 600, WHITE],
                 [20, 580, 330, 20, WHITE],
                 [0, 0, 350, 20, WHITE],
                 [450, 0, 350, 20, WHITE],
                 [450, 580, 330, 20, WHITE]
                  ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

class TESTROOM(Room):
    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 600, PINK],
                [780, 0 , 20, 600, PINK],
                [0, 0, 350, 20, PINK],
                [450, 0, 350, 20,PINK],
                [450, 580, 350, 20,PINK],
                [0, 580, 350, 20, PINK]
                ]

        dinamicwalls = [50,50,20,20,200,0,RED]


        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
