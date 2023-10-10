import pygame as pg
import sys
from Settings import *
from App import *

class App:
    def __init__(self):
        pg.init()                                       #Inicializa o Módulo do pygame
        self.app_screen = pg.display.set_mode(RES)      #Inicia uma tela de dismensões RES
        self.clock = pg.time.Clock()                    #Pega o clock
        self.app_screen.fill('black')                   #Preenche a tela com preto
        pg.display.set_caption('App_String')            #Escreve o nome da tela

    def update(self):
        pg.display.update()                             #da um uptade na tela
        self.clock.tick(FPS)                            #ajeita o fps da tela

    # Função de checagem se quer sair ou não do pygame
    def check_quit_event(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    # Função de rodar o programa
    def run(self):
        while True:
            self.check_quit_event()     #Checa se quer sair
            self.update()               #Faz o update




if __name__ == '__main__':
    app = App()         #Cria uma instância do app
    app.run()           #Manda ele rodar