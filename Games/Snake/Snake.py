import os
# os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import time

import random
from enum import Enum

BASE_SNAKE_WIDTH = 10
BASE_SNAKE_HEIGHT = 10
ENDGAME_MESSAGE_SECONDS = 1

class Direction(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
    NONE = "none"

class Coordonates(object):
    x = None
    y = None
    
    def __init__(self, x = None, y = None) -> None:
        self.x = x
        self.y = y

class Veolicity(object):
    horzVelocity = None
    vertVelocity = None
    
    def __init__(self, horzVelocity = 0, vertVelocity = 0) -> None:
        self.horzVelocity = horzVelocity
        self.vertVelocity = vertVelocity
        

class DirectionChange(object):
    
    direction = Direction.NONE
    coords = Coordonates()
    velocity = Veolicity()

    def __init__(self, direction, coords) -> None:
        self.direction = direction
        self.coords = coords
    

class SnakeTail(object):
    
    _direction = Direction.NONE
    x = None
    y = None
    vertVelocity = 0
    horzVelocity = 0
    width = BASE_SNAKE_WIDTH
    height = BASE_SNAKE_HEIGHT
    
    def get_direction(self):
        return self._direction
    def set_direction(self, direction):
        self._direction = direction
        
    direction = property(get_direction, set_direction)

    def __init__(self, direction, x, y, vertVelocity, horzVeolocity) -> None:
        self.direction = direction
        self.x = x
        self.y = y
        self.vertVelocity = vertVelocity
        self.horzVelocity = horzVeolocity    

class Snake(object):

    DISPLAY_WIDTH = 800
    DISPLAY_HEIGHT = 600
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BACKGROUND = WHITE
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    YELLOW = (200, 200, 0)
    STARTING_VELOCITY = 2
    

    def __init__(self):
        
        self.initialization()
        self.runGame()

    def initialization(self):
        self.snakeWidth = BASE_SNAKE_WIDTH
        self.snakeHeight = 10
        self.snakeX = (self.DISPLAY_WIDTH / 2) - (self.snakeWidth / 2)
        self.snakeY = 1
        self.snakeTails = []
        self.directionChangeCoords = []
        self.velocity = self.STARTING_VELOCITY
        self.setSnakeDirection(Direction.DOWN)
        self.snakeColor = self.BLUE
        self.gameOver = False
        self.END_GAME_MESSAGE = "Game Over"
        self.pointsEarned = 0
        self.placeFoodRandomly()
        self.foodWidth = 10
        self.foodHeight = 10
        self.foodColor = self.YELLOW

        self.initPyGame()
    
    def setSnakeDirection(self, direction):
        self.snakeDirection = direction
        if self.snakeDirection == Direction.DOWN:
            self.snakeVertVelocity = 1 * self.velocity
            self.snakeHorzVelocity = 0

        elif self.snakeDirection == Direction.UP:
            self.snakeVertVelocity = -1  * self.velocity
            self.snakeHorzVelocity = 0

        elif self.snakeDirection == Direction.LEFT:
            self.snakeVertVelocity = 0
            self.snakeHorzVelocity = -1  * self.velocity
            
        elif self.snakeDirection == Direction.RIGHT:
            self.snakeVertVelocity = 0
            self.snakeHorzVelocity = 1  * self.velocity
    
    def placeFoodRandomly(self):
        self.foodX = round(random.randrange(0, self.DISPLAY_WIDTH - self.snakeX) / 10.0) * 10.0
        self.foodY = round(random.randrange(0, self.DISPLAY_HEIGHT - self.snakeY) / 10.0) * 10.0
    
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

    def addSnakeTail(self):
        if len(self.snakeTails) == 0:
            
            xDiff = 0
            yDiff = 0

            if self.snakeDirection == Direction.UP:
                yDiff = self.snakeHeight

            elif self.snakeDirection == Direction.DOWN: # good
                yDiff = -self.snakeHeight

            elif self.snakeDirection == Direction.LEFT:
                xDiff = self.snakeWidth

            elif self.snakeDirection == Direction.RIGHT:
                xDiff = -self.snakeWidth

            self.snakeTails.append(
                SnakeTail(
                    self.snakeDirection,
                    self.snakeX + xDiff,
                    self.snakeY + yDiff,
                    self.snakeVertVelocity,
                    self.snakeHorzVelocity
                )
            )
        

    def runGame(self):
        while not self.gameOver:
            
            if self.hasQuitGame():
                self.END_GAME_MESSAGE = "kthxbai!"
                self.gameOver = True
            
            if self.snakeOverFood():
                print("yummy!")
                self.placeFoodRandomly()
                self.pointsEarned += 1
                self.addSnakeTail()
            
            self.handleKeys()
            self.moveSnakeInDirection()
            self.tailsFollowSnake()
            self.moveTailsInDirection()
            
            self.drawBG()
            self.drawFood()
            self.drawSnake()
            self.drawTails()

            pygame.display.update()
            
            if self.snakeIsOnTheEdge():
                self.gameOver = True
            
            self.clock.tick(30)

        self.endGame()

    def tailsFollowSnake(self):
        if len(self.snakeTails) > 0:
            snakeTail: SnakeTail
            for snakeTail in self.snakeTails:
                directionChangeCoords: DirectionChange
                for directionChangeCoords in self.directionChangeCoords:
                    if snakeTail.x == directionChangeCoords.coords.x and snakeTail.y == directionChangeCoords.coords.y:
                        snakeTail.direction = directionChangeCoords.direction

    def moveTailsInDirection(self):
        snakeTail: SnakeTail
        for snakeTail in self.snakeTails:
            snakeTail.x += snakeTail.horzVelocity
            snakeTail.y += snakeTail.vertVelocity

    def drawTails(self):
        snakeTail: SnakeTail
        for snakeTail in self.snakeTails:
            pygame.draw.rect(
                self.display,
                self.snakeColor,
                [
                    snakeTail.x,
                    snakeTail.y,
                    snakeTail.width,
                    snakeTail.height
                ]
            )

    def endGame(self):
        self.showEndGameMessage()
        pygame.display.update()
        time.sleep(ENDGAME_MESSAGE_SECONDS)
        pygame.quit()
    
    def showEndGameMessage(self):
        
        message = self.END_GAME_MESSAGE
        displayMessage = self.fontStyle.render(message, True, self.RED)
        messageBounds = displayMessage.get_bounding_rect()
        messagePosition = [
            self.DISPLAY_WIDTH/2 - messageBounds.width/2, 
            self.DISPLAY_HEIGHT/2 - messageBounds.height/2
        ]
        self.display.blit(displayMessage, messagePosition)

    def hasQuitGame(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False
    
    def snakeOverFood(self):
        return (
            (
                (
                    self.snakeX > self.foodX
                    and self.snakeX < (self.foodX + self.foodWidth)
                )
                or (
                    self.snakeX + self.snakeWidth > self.foodX
                    and self.snakeX + self.snakeWidth < (self.foodX + self.foodWidth)
                )
            )
            and (
                (
                    self.snakeY > self.foodY
                    and self.snakeY < (self.foodY + self.foodHeight)
                )
                or (
                    self.snakeY + self.snakeHeight > self.foodY
                    and self.snakeY + self.snakeHeight < (self.foodY + self.foodHeight)
                )
            )
        )
    
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
                self.snakeHeight
            ]
        )

    def drawFood(self):
        pygame.draw.rect(
            self.display, 
            self.foodColor, 
            [
                self.foodX, 
                self.foodY, 
                self.foodWidth, 
                self.foodHeight
            ]
        )

    def drawBG(self):
        pygame.draw.rect(self.display, self.BACKGROUND, [0, 0, self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT])

    def handleKeys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.setSnakeDirection(Direction.UP)
        elif keys[pygame.K_DOWN]:
            self.setSnakeDirection(Direction.DOWN)
        elif keys[pygame.K_LEFT]:
            self.setSnakeDirection(Direction.LEFT)
        elif keys[pygame.K_RIGHT]:
            self.setSnakeDirection(Direction.RIGHT)
        
        if len(self.snakeTails) > 0:
            self.directionChangeCoords.append(
                DirectionChange(
                    self.snakeDirection, 
                    [
                        self.snakeX
                        , self.snakeY
                    ]
                )
            )

    def moveSnakeInDirection(self):
        self.snakeX += self.snakeHorzVelocity
        self.snakeY += self.snakeVertVelocity
        

if __name__ == '__main__':
    Snake()
