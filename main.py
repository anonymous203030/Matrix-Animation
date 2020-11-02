from random import randrange, choice

import pygame

from pygame.locals import *
from sys import exit


import pygame
from pygame.locals import *

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1000
time = 15
FONT_SIZE = (SCREEN_WIDTH - SCREEN_HEIGHT)  // 13

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

pygame.init()

font = pygame.font.SysFont('arial', FONT_SIZE, True, True)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Matrix Animation')



obj_list = []
repeat_list = []
number_of_obj = 20
generate = False

initial_time = 0
current_time = 0

class Codeline:
    def __init__(self):
        self.fill = 1
        self.ypos_list = []
        self.letters_list = []
        self.xpos = randrange(FONT_SIZE, SCREEN_WIDTH + FONT_SIZE, FONT_SIZE)
        self.ypos = randrange(FONT_SIZE, SCREEN_HEIGHT + FONT_SIZE, FONT_SIZE)
        self.ypos_list.append(self.ypos)


    def draw_codeline(self):
        randomic_letter = choice(letters)
        self.letters_list.append(randomic_letter)

        for msg, y in zip(self.letters_list, self.ypos_list):
            message = f'{msg}'
            text = font.render(message, True, GREEN)
            screen.blit(text, (self.xpos, y))


    def desloc_codeline(self):
        if self.ypos > SCREEN_HEIGHT or len(self.ypos_list) > 20:
            message = ''
            text = font.render(message, True, WHITE)
            screen.fill(BLACK, (self.xpos, self.ypos_list[0], text.get_width() + FONT_SIZE, text.get_height() * self.fill))

            if text.get_height() * self.fill > len(self.ypos_list) * text.get_height():
                self.letters_list.clear()
            else:
                self.fill += 1

        else:
            self.ypos += FONT_SIZE
            self.ypos_list.append(self.ypos)
            message = f'{self.letters_list[-1]}'
            text = font.render(message, True, WHITE)
            screen.fill(BLACK, (self.xpos, self.ypos_list[-1], text.get_width() + FONT_SIZE, text.get_height()  ))
            screen.blit(text, (self.xpos, self.ypos_list[-1]))

obj = Codeline()
def create_multiples_obj(obj_list, number_of_obj, generate):
    if generate:
        for i in range(number_of_obj):
            obj = Codeline()

            if obj.xpos in repeat_list:
                repeat_list.remove(obj.xpos)
                obj.letters_list.clear()
                del obj
            else:
                obj_list.append(obj)
                repeat_list.append(obj.xpos)

        for i in obj_list:
            i.draw_codeline()
            i.desloc_codeline()
    else:

        for i in obj_list:
            i.draw_codeline()
            i.desloc_codeline()


while True:
    clock.tick(time)
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    current_time = pygame.time.get_ticks()
    if current_time - initial_time > 200:
        generate = True
        initial_time = pygame.time.get_ticks()
    create_multiples_obj(obj_list, number_of_obj, generate)
    pygame.display.flip()