import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_render import *


class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()
        self.cont_time = 0


    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.raycast = RayCasting(self)

    def update(self):
        self.player.update()
        self.raycast.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        self.counting_time()
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def counting_time(self):
        self.cont_time += self.delta_time
        if self.cont_time >= 1000:
            #print('one second')
            self.raycast.timed_flash()
            self.cont_time = 0

    def draw(self):
        self.screen.fill('black')
        #self.player.draw()
        #self.map.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_F1):
                pg.quit()
                sys.exit()


    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()
