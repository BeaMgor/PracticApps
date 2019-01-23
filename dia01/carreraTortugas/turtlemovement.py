import pygame, sys
from pygame.locals import *  #para importa palabras tipo KEYDOWN es un módulo especifico
import random

class Runner(): #creamos corredor
    __customes = ("turtle","fish","prawn","moray","octopus")
    
    def __init__(self, x=0, y=0):
        
        ixCustome = random.randint(0 , 4)
        self.custome = pygame.image.load("images/{}.png".format(self.__customes [ixCustome]))
        self.position = [x,y]
        self.name= ""

class Game():

    def __init__(self):#inicalizamos pygame
        self.__screen = pygame.display.set_mode((640, 480)) #creamos la pantalla
        self.__background = pygame.image.load("images/background.png")#importamos la imagien
        pygame.display.set_caption("Carrera de bichos")
        
        self.runner = Runner (320,240)
        
    def start(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event == KEYDOWN: #que se mueva pulsando una tecla
                    if event.key == K_UP: #SE BUSCA EN PYGAME KEYS
                        #mover hacia arriba el runner
                        #¿cómo movemos el runner hacía arriba?
                        self.runner.position[1] -= 5 #lo mueve de cinco en cinco 
                    
                    elif event.key == K_DOWN:
                        self.runner.position[1] += 5
                        #mover abajao
                    elif event.key == K_LEFT:
                        self.runner.position[0] -= 5
                    elif event.key == K_RIGHT:
                        self.runner.position[0] += 5
                    else:
                        pass
                    
                    
                self.__screen.blit(self.__background, (0,0))
                self.__screen.blit(self.runner.custome, self.runner.position)
         
                pygame.display.flip()
         
         
print ("my name is {}".format(__name__))

         
if __name__ == '__main__':
    game = Game()
    pygame.font.init()
    game.start()
        
 #terminado       