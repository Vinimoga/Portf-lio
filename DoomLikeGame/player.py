from settings import *
import pygame as pg
import math

class Player:
    def __init__(self,game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.speed = PLAYER_SPEED

    def movement(self):
        #print(PLAYER_POS)
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0

        keys = pg.key.get_pressed()
        if keys[pg.K_LSHIFT]:
            speed = (self.speed + 0.003) * self.game.delta_time
        else:
            speed = self.speed * self.game.delta_time

        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        if keys[pg.K_w]:
            #print('w foi apertado')
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_a]:
            dy += -speed_cos
            dx += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_d]:
            dy += speed_cos
            dx += -speed_sin

        self.check_wall_collision(dx,dy)


        #print(self.x,self.y)

        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau

        #print(self.angle)

    def check_wall(self,x,y):
        return (x,y) not in self.game.map.world_map

    def check_wall_collision(self,dx,dy):
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x),int(self.y + dy)):
            self.y += dy



    def draw(self):

        #pg.draw.line(self.game.screen, 'red', (self.x * FAKEWIDTH, self.y * FAKEHEIGHT),
        #             (self.x * FAKEWIDTH + WIDTH * math.cos(self.angle),
        #              self.y * FAKEHEIGHT + WIDTH * math.sin(self.angle)), 2)

        pg.draw.circle(self.game.screen, 'green', (self.x * FAKEWIDTH, self.y * FAKEHEIGHT), 15)


    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)