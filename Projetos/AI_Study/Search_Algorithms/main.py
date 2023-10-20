import pygame as pg
from maze import *
from AI import *
from settings import *
import sys

class window():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.maze = maze(self)
        self.frontier = frontier(self)
        self.stack = explored_set()

    def update(self):
        self.screen.fill('black')
        self.maze.draw()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_F1):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()

if __name__ == '__main__':
    thing = window()
    thing.run()

