#!/usr/bin/python
'''последовательность создания двери
что должно быть:
	1)рисунок двери
	2)некоторая зона тригер
	3) движение стены

с чего стоит начать
	динамичная стена
'''


import pygame
from wall import *

class dore(pygame.sprite.Sprite):
	
	def __init__(self, x, y, width, height, color):

		super().__init__() #рисовка двери

		self.image = pygame.Surface([width, height]) #создание поверхности
        self.image.fill(color) #заполнить цветом


        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


    def triger(self, x, y, width, height):

		self.image = pygame.Surface([width, height]) #создание поверхности
