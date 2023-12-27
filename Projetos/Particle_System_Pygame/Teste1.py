# libraries
from Particle import *

# import time

# setup
pygame.init()
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()


class Particle_System:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()
        self.running = True
        self.particle_creation()

    @staticmethod
    def particle_creation():

        for i in range(number_of_particles):
            copy = True
            particulas.append(Particle(screen))
            particulas[i].get_color()

            # Let's make sure we don't spawn any particle inside another.
            while copy:

                copy = False
                particulas[i].get_pos()

                print('Valor do i:', i)
                particulas[i].status()

                x, y = particulas[i].pos
                radius = particulas[i].radius

                for j in range(len(particulas)):
                    if i != j:
                        r = radius + particulas[j].radius
                        if (x - r) < particulas[j].pos[0] < (x + r) and (y - r) < particulas[j].pos[1] < (y + r):
                            copy = True

    def simulation(self):
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # RENDER
        for i in range(number_of_particles):
            particulas[i].draw()

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60


system = Particle_System()
while system.running:
    system.simulation()

pygame.quit()  # end
