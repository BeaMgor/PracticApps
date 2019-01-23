import pygame, sys
import random

class Runner(): #creamos corredor
    __customes = ("turtle","fish","prawn","moray","octopus")
    
    def __init__(self, x=0, y=0): ##incializamos
        
        ixCustome = random.randint(0 , 4)
        self.custome = pygame.image.load("images/{}.png".format(self.__customes [ixCustome]))
        self.position = [x,y]
        self.name= ""
        
    def avanzar(self):
        self.position[0] += random.randint(1,6)
    
class Game():
    runners = []
    __posY=(200, 240, 280, 160) #posición de los runners
    __names = ("speedy", "lucera", "Alonso", "Torcuata")
    __startLine = 20 #creamos la pantalla con nuestras medidas
    __finishLine = 620
    
    def __init__(self):#inicalizamos pygame
        self.__screen = pygame.display.set_mode((640, 480)) #creamos la pantalla
        self.__background = pygame.image.load("background.png")#importamos la imagien
        pygame.display.set_caption("Carrera de bichos")
        
        #cramos los runners
        #runners.append(Runner(self.__starLine, 240))
        for i in range(4):
            theRunner = Runner(self.__startLine, self.__posY[i])
            theRunner.name = self.__names[i]
                                 
            self.runners.append(theRunner)
            
    def close(self):
        pygame.quit()
        sys.exit()
        
    
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                    
            #hacemos que avance
            for runner in self.runners:
                runner.avanzar()
                if runner.position[0] >= self.__finishLine:
                    
                    print ("{} ha ganado".format(runner.name))
                    gameOver = True
                  
            #refresca pantalla
            self.__screen.blit(self.__background, (0, 0))
            
            for runner in self.runners: #hacemos un ciclo para que recorra todos los corredores
                self.__screen.blit(runner.custome, runner.position)
                
            pygame.display.flip()
            
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
     
    
    
if __name__ == '__main__':
    game = Game()
    pygame.init()
    game.competir()
