import pygame, sys


class Game():
    runner = []
    __startLine = 20
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Carrera de bichos")
        self.background = pygame.image.load("images/background.png")
    
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
            
            self.__screen.blit(self.background, (0,0))
            
            pygame.display.flip()
    
        pygame.quit()
        sys.exit()
    
if __name__== '__main__':
    game = Game()
    pygame.init()
    game.competir()