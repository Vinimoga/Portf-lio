import pygame as pg
from AI import *

_ = False
First_map = [[_, _, _, _, _, _],
             [_, 1, 1, 1, 3, _],
             [_, 1, _, _, _, _],
             [_, 1, _, _, _, _],
             [_, 1, 1, 1, 2, _],
             [_, _, _, _, _, _]]


class maze():
    def __init__(self,window):
        self.window = window
        self.maze = First_map
        self.wall_map = {}
        self.get_wall_map()

    def get_wall_map(self):
        for j,row in enumerate(self.maze):
            for i,value in enumerate(row):
                if value == False:
                    self.wall_map[(i,j)] = value
                if value == 2:
                    self.initial_pos = (i,j)

                if value == 3:
                    self.final_pos = (i,j)



    def draw(self):
        for pos in self.wall_map:
            pg.draw.rect(self.window.screen,'darkgray',(pos[0]*50,pos[1]*50,50,50),2)
        pg.draw.rect(self.window.screen, 'red', (self.initial_pos[0] * 50, self.initial_pos[1] * 50, 50, 50), 2)
        pg.draw.rect(self.window.screen, 'blue', (self.final_pos[0] * 50, self.final_pos[1] * 50, 50, 50), 2)

    def solve(self):
        ''' finds the solution of the maze'''

        self.num_explored = 0

        start = node(state=self.initial_pos,parent=None,action=None)
        frontier = StackFrontier(end=self.final_pos)
        frontier.add(start)

        explored = explored_set()



