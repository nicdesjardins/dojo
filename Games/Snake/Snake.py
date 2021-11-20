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
    def __init__(self, direction, coords, velocity) -> None:
        self.direction = direction
        self.coords = coords
        self.velocity = velocity
    

class SnakeTail(object):
    _direction = Direction.NONE
    x = None
    y = None
    vertVelocity = 0
    horzVelocity = 0
    width = BASE_SNAKE_WIDTH
    height = BASE_SNAKE_HEIGHT
    directionChanges = []

    def __init__(self, direction, x, y, horzVeolocity, vertVelocity) -> None:
        self.direction = direction
        self.x = x
        self.y = y
        self.vertVelocity = vertVelocity
        self.horzVelocity = horzVeolocity

    def get_direction(self):
        return self._direction
    def set_direction(self, direction):
        self._direction = direction
    direction = property(get_direction, set_direction)    
    
class Snake(object):

    DISPLAY_WIDTH = 800
    DISPLAY_HEIGHT = 600
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BACKGROUND = WHITE
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    YELLOW = (200, 200, 0)
    STARTING_VELOCITY = 5
    

    def __init__(self):
        
        self.initialization()
        self.runGame()

    def initialization(self):
        self.snakeWidth = BASE_SNAKE_WIDTH
        self.snakeHeight = 10
        self.snakeX = (self.DISPLAY_WIDTH / 2) - (self.snakeWidth / 2)
        self.snakeY = 1
        self.snakeTails = []
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
        self.gamePaused = False
        self.initPyGame()
    
    def setSnakeDirection(self, direction):
        
        init = False
        if not hasattr(self, 'snakeDirection'):
            self.snakeDirection = direction
            init = True
        
        if init or self.snakeDirection != direction:
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
            
            if len(self.snakeTails) > 0:
                snakeTail: SnakeTail
                for snakeTail in self.snakeTails:
                    dirChange = DirectionChange(
                            self.snakeDirection, 
                            Coordonates(
                                self.snakeX
                                , self.snakeY
                            )
                            , Veolicity(self.snakeHorzVelocity, self.snakeVertVelocity)
                        )
                    snakeTail.directionChanges.append(dirChange)
                    self.dumpSnakeChanges()
    
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

    def runGame(self):
        while not self.gameOver:
            
            if self.hasQuitGame():
                self.END_GAME_MESSAGE = "kthxbai!"
                self.gameOver = True
            
            self.handlePauseKey()

            if not self.gamePaused:
                self.gamePlayIteration()
            
            self.clock.tick(30)

        self.endGame()

    def gamePlayIteration(self):

        if self.snakeOverFood():
            self.placeFoodRandomly()
            self.pointsEarned += 1
            self.addSnakeTail()
                
        self.handleDirectionKeys()
        # self.moveSnakeInDirection()
        # self.tailsFollowsHead()
        self.moveTailsInDirection()
                
        self.drawBG()
        self.drawFood()
        self.drawSnake()
        self.drawTails()

        pygame.display.update()
                
        if self.snakeIsOnTheEdge():
            self.gameOver = True

    def handlePauseKey(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.gamePaused = not self.gamePaused
    def handleDirectionKeys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.setSnakeDirection(Direction.UP)
        elif keys[pygame.K_DOWN]:
            self.setSnakeDirection(Direction.DOWN)
        elif keys[pygame.K_LEFT]:
            self.setSnakeDirection(Direction.LEFT)
        elif keys[pygame.K_RIGHT]:
            self.setSnakeDirection(Direction.RIGHT)
    def addSnakeTail(self):
        if len(self.snakeTails) == 0:
            
            xDiff = 0
            yDiff = 0

            if self.snakeDirection == Direction.UP:
                yDiff = self.snakeHeight

            elif self.snakeDirection == Direction.DOWN:
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
                    self.snakeHorzVelocity,
                    self.snakeVertVelocity
                )
            )
        else:
            xDiff = 0
            yDiff = 0
            
            lastSnakeTail: SnakeTail = self.snakeTails[len(self.snakeTails)-1]

            if lastSnakeTail.direction == Direction.UP:
                yDiff = lastSnakeTail.height

            elif lastSnakeTail.direction == Direction.DOWN: # good
                yDiff = -lastSnakeTail.height

            elif lastSnakeTail.direction == Direction.LEFT:
                xDiff = lastSnakeTail.width

            elif lastSnakeTail.direction == Direction.RIGHT:
                xDiff = -lastSnakeTail.width

            self.snakeTails.append(
                SnakeTail(
                    lastSnakeTail.direction,
                    lastSnakeTail.x + xDiff,
                    lastSnakeTail.y + yDiff,
                    lastSnakeTail.horzVelocity,
                    lastSnakeTail.vertVelocity
                )
            )
    def tailsFollowsHead(self):
        snakeTail: SnakeTail
        for snakeTail in self.snakeTails:
            if len(snakeTail.directionChanges) > 0:
                topDirectionChange: DirectionChange = snakeTail.directionChanges[0]
                if (
                    snakeTail.x == topDirectionChange.coords.x
                    and snakeTail.y == topDirectionChange.coords.y
                ):
                    snakeTail.direction = topDirectionChange.direction
                    snakeTail.horzVelocity = topDirectionChange.velocity.horzVelocity
                    snakeTail.vertVelocity = topDirectionChange.velocity.vertVelocity
                    snakeTail.directionChanges.pop(0)
                    
                    self.dumpSnakeChanges()

    def dumpSnakeChanges(self):
        snakeTail: SnakeTail
        print('---')

        for i, snakeTail in enumerate(self.snakeTails):

            print('snakeTail '+str(i))
            print('\t'+str(len(snakeTail.directionChanges))+' changes: ')
            
            directionChange: DirectionChange
            for ii, directionChange in enumerate(snakeTail.directionChanges):
                print('\t\t'+str(ii) + ' -> direction:'+str(directionChange.direction))

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
    
        
    def moveSnakeInDirection(self):
        self.snakeX += self.snakeHorzVelocity
        self.snakeY += self.snakeVertVelocity
        

if __name__ == '__main__':
    Snake()
