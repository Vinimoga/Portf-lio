import numpy as np
from Settings import *
import pygame

class Particle:
    def __init__(self, surface):
        self.pos = None
        self.color = None
        self.surface = surface
        self.radius = 5

    def get_pos(self):
        self.pos = [np.random.randint(self.radius, width - self.radius), np.random.randint(self.radius, height - self.radius)]

    def give_pos(self, pos):
        self.pos = pos

    def get_color(self):
        self.color = list(np.random.choice(range(256), size=3))

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.pos, self.radius)

    def status(self):
        print(f'position: {self.pos}     color: {self.color}')

    def movement(self):
        pass
