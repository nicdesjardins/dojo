# Source: https://www.edureka.co/blog/snake-game-with-pygame/
import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

displayInfo = pygame.display.Info()
SCREEN_WIDTH = displayInfo.current_w
SCREEN_HEIGHT = displayInfo.current_h

displayWidth = SCREEN_WIDTH #600
displayHeight = SCREEN_HEIGHT #400
 
display = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Snake Game by Edureka')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
def drawSnake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [displayWidth / 6, displayHeight / 3])
 
 
def gameLoop():
    gameOver = False
    game_close = False
 
    x = displayWidth / 2
    y = displayHeight / 2
 
    x_velocity = 0
    y_velocity = 0
 
    snakeCoordList = []
    snakeLen = 1
 
    foodX = round(random.randrange(0, displayWidth - snake_block) / 10.0) * 10.0
    foodY = round(random.randrange(0, displayHeight - snake_block) / 10.0) * 10.0
 
    while not gameOver:
 
        while game_close == True:
            display.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
 
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        if x >= displayWidth or x < 0 or y >= displayHeight or y < 0:
            game_close = True
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_velocity = -snake_block
                    y_velocity = 0
                elif event.key == pygame.K_RIGHT:
                    x_velocity = snake_block
                    y_velocity = 0
                elif event.key == pygame.K_UP:
                    x_velocity = 0
                    y_velocity = -snake_block
                elif event.key == pygame.K_DOWN:
                    x_velocity = 0
                    y_velocity = snake_block
 
        
        x += x_velocity
        y += y_velocity
        display.fill(blue)
        pygame.draw.rect(display, green, [foodX, foodY, snake_block, snake_block])
        snakeHead = [x, y]
        snakeCoordList.append(snakeHead)
        if len(snakeCoordList) > snakeLen:
            del snakeCoordList[0]
 
        for item in snakeCoordList[:-1]: # iterate the array without the last element
            if item == snakeHead:
                game_close = True
 
        drawSnake(snake_block, snakeCoordList)
 
 
        pygame.display.update()
 
        if x == foodX and y == foodY:
            foodX = round(random.randrange(0, displayWidth - snake_block) / 10.0) * 10.0
            foodY = round(random.randrange(0, displayHeight - snake_block) / 10.0) * 10.0
            snakeLen += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
gameLoop()