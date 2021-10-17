import pygame
import time
import os
import random

class Snake(object):

    DISPLAY_WIDTH = 800
    DISPLAY_HEIGHT = 600
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BACKGROUND = WHITE
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)

    def get_gameOver(self):
            return self._gameOver
    def set_gameOver(self, value):
        self._gameOver = value
    gameOver = property(get_gameOver, set_gameOver)
    
    def __init__(self):
        
        self.initialization()
        self.runGame()

    def initialization(self):
        self.snakeX = 200
        self.snakeY = 150
        self.snakeWidth = 10
        self.snakeLength = 10
        self.snakeColor = self.BLUE
        self.velocity = 5
        self.gameOver = False

        self.foodX = round(random.randrange(0, self.DISPLAY_WIDTH - self.snakeX) / 10.0) * 10.0
        self.foodY = round(random.randrange(0, self.DISPLAY_HEIGHT - self.snakeY) / 10.0) * 10.0
        self.foodWidth = 10
        self.foodHeight = 10
        self.foodColor = self.YELLOW

        self.initPyGame()
    
    def initPyGame(self):
        pygame.init()
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        self.fontStyle = pygame.font.SysFont(None, 50)
        self.centerWindow()
        self.display = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        
        pygame.display.update()

    def centerWindow(self):
        displayInfo = pygame.display.Info()
        self.SCREEN_WIDTH = displayInfo.current_w
        self.SCREEN_HEIGHT = displayInfo.current_h
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (
            self.SCREEN_WIDTH/2 - self.DISPLAY_WIDTH/2, 
            self.SCREEN_HEIGHT/2 - self.DISPLAY_HEIGHT/2
        )
    

    def runGame(self):
        while not self.gameOver:
            if self.hasQuitGame():
                self.gameOver = True
            self.handleKeys()
            self.drawBG()
            self.drawSnake()
            pygame.display.update()
            
            if self.snakeIsOnTheEdge():
                self.gameOver = True
            
            self.clock.tick(30)

        self.endGame()

    def endGame(self):
        self.showMessage("Game Over", self.RED)
        pygame.display.update()
        time.sleep(2)
        pygame.quit()

    def hasQuitGame(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    
    def snakeIsOnTheEdge(self):
        return (
            self.snakeX < 0
            or self.snakeX > self.DISPLAY_WIDTH
            or self.snakeY < 0
            or self.snakeY > self.DISPLAY_HEIGHT
        )

    def drawSnake(self):
        pygame.draw.rect(
            self.display, 
            self.snakeColor, 
            [
                self.snakeX, 
                self.snakeY, 
                self.snakeWidth, 
                self.snakeLength
            ]
        )

    def drawBG(self):
        pygame.draw.rect(self.display, self.BACKGROUND, [0, 0, self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT])

    def handleKeys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.snakeY -= self.velocity
        if keys[pygame.K_DOWN]:
            self.snakeY += self.velocity
        if keys[pygame.K_LEFT]:
            self.snakeX -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.snakeX += self.velocity

    def showMessage(self, message, color):
        displayMessage = self.fontStyle.render(message, True, color)
        messageBounds = displayMessage.get_bounding_rect()
        messagePosition = [
            self.DISPLAY_WIDTH/2 - messageBounds.width/2, 
            self.DISPLAY_HEIGHT/2 - messageBounds.height/2
        ]
        self.display.blit(displayMessage, messagePosition)
        

if __name__ == '__main__':
    Snake()
