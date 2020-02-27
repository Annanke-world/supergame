#!/usr/bin/python

import pygame

class Wall(pygame.sprite.Sprite):


    def __init__(self, x, y, width, height, color):



        super().__init__() #это используется 


        self.image = pygame.Surface([width, height]) #создание поверхности
        self.image.fill(color) #заполнить цветом


        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x