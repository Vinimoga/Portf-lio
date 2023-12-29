import pygame as pg
from settings import *

_ = False
mini_map = [
    [_, _, _, _, _, _, _, _, _, _, _, _],
    [_, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _],
    [_, 1, _, 1, _, 1, _, _, 1, _, 1, _],
    [_, 1, _, _, _, _, _, _, _, _, 1, _],
    [_, 1, _, _, _, _, _, 1, _, 1, 1, _],
    [_, 1, _, 1, _, 1, _, _, _, _, _, _],
    [_, 1, _, _, _, _, 1, _, 1, 1, 1, _],
    [_, 1, _, 1, _, _, _, _, _, _, 1, _],
    [_, 1, _, _, _, 1, _, _, _, 1, _, _],
    [_, 1, _, 1, _, _, _, 1, _, _, 1, _],
    [_, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _],
    [_, _, _, _, _, _, _, _, _, _, _, _]
]

class Map:
    def __init__(self,game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j,row in enumerate(self.mini_map):
            for i,value in enumerate(row):
                if value:
                    self.world_map[(i,j)] = value

    def draw(self):
        [pg.draw.rect(self.game.screen,'darkgray',(pos[0]*FAKEWIDTH,pos[1]*FAKEHEIGHT,FAKEWIDTH,FAKEHEIGHT),2)
         for pos in self.world_map]

    #Caso queira mudar o tamanho do mapa para caber na tela, basta alterar o terceiro termo, onde os números depois de
    #pos devem ser alterados para o valor : width/16, height/9


