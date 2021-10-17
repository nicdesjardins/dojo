import pygame

RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

BADDY_COLOR = RED
HERO_COLOR = BLUE
BACKGROUND_COLOR = WHITE

WIN_WIDTH = 1280
WIN_HEIGHT = 720
WIN_TITLE = "Squarey"

class SquareyGame(object):
      
      def __init__(self) -> None:
            self.initVars()
            self.initGame()
            self.runGame()

      def initVars(self):
          self.heroX = 100
          self.heroY = 100
          self.baddyX = 300
          self.baddyY = 300
          self.heroVelocity = 6
          self.velocityMultiplier = 1
          self.baddyVelocity = 4
          self.run = True

      def initGame(self):
          pygame.init()
          self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
          pygame.display.set_caption(WIN_TITLE)
      
      def fillWindowBlack(self):
            self.win.fill(BACKGROUND_COLOR)

      def gameOver(self):
            print('kthxbai!')
            self.run = False

      def runGame(self):
            while self.run:
                  
                  pygame.time.delay(100)

                  self.baddyTracksHero()
                  
                  self.handleGameEvents()

                  self.handleKeyPressed()
                  
                  self.draw_game()
      
      def handleGameEvents(self):
          for event in pygame.event.get():
                if event.type == pygame.QUIT:
                      self.gameOver()

      def baddyTracksHero(silf):

            if silf.baddyIsLeftOfHero(): 
                  silf.moveBaddyToRight()

            elif silf.baddyIsRightOfHero():
                  silf.moveBaddyToLeft()

            elif silf.baddyIsAboveHero(): 
                  silf.moveBaddyDown()

            elif silf.baddyIsBelowHero():
                  silf.moveBaddyUp()

            else:
                  silf.gameOver()     

      def handleKeyPressed(self):
            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                  self.velocityMultiplier = 2
            else:
                  self.velocityMultiplier = 1

            if keys[pygame.K_LEFT]:
                  self.heroX -= self.heroVelocity

            if keys[pygame.K_RIGHT]:
                  self.heroX += self.heroVelocity
                        
            if keys[pygame.K_UP]:
                  self.heroY -= self.heroVelocity
                        
            if keys[pygame.K_DOWN]:
                  self.heroY += self.heroVelocity
      
      def set_velocityMultiplier(self, value):
            self._velocityMultiplier = value
      def get_velocityMultiplier(self):
            return self._velocityMultiplier
      velocityMultiplier = property(get_velocityMultiplier, set_velocityMultiplier)

      def set_heroVelocity(self, value):
            self._heroVelocity = value
      def get_heroVelocity(self):
            return self._heroVelocity * self.velocityMultiplier

      heroVelocity = property(get_heroVelocity, set_heroVelocity)

      def draw_game(self):
            self.fillWindowBlack()
            self.drawHero()
            self.drawBaddy()
            pygame.display.update()
      
      def moveBaddyUp(self):
          self.baddyY = self.baddyY - self.baddyVelocity

      def moveBaddyDown(self):
          self.baddyY = self.baddyY + self.baddyVelocity

      def moveBaddyToLeft(self):
          self.baddyX = self.baddyX - self.baddyVelocity

      def moveBaddyToRight(self):
          self.baddyX = self.baddyX + self.baddyVelocity

      def baddyIsBelowHero(self):
          return self.baddyY > self.heroY + 10

      def baddyIsAboveHero(self):
          return self.baddyY < self.heroY - 10

      def baddyIsRightOfHero(self):
          return self.baddyX > self.heroX + 10

      def baddyIsLeftOfHero(self):
          return self.baddyX < self.heroX - 10
            
      def drawBaddy(self):
            pygame.draw.rect(self.win, BADDY_COLOR, (self.baddyX, self.baddyY, 40, 40))

      def drawHero(self):
            pygame.draw.rect(self.win, HERO_COLOR, (self.heroX, self.heroY, 20, 20))

if __name__ == '__main__':
      SquareyGame()