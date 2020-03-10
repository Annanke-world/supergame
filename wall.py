#!/usr/bin/python

import pygame


PINK = (246, 58, 122)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

class Wall(pygame.sprite.Sprite):

	

    def __init__(self, x, y, width, height, color):



        super().__init__() #это используется 


        self.image = pygame.Surface([width, height]) #создание поверхности
        self.image.fill(color) #заполнить цветом


        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x	
