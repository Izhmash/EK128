from SpriteSheet import SpriteSheet
import sys
import os
import pygame
import random
from level import level


BACKGROUND = pygame.image.load('blackbox.jpg')
BACKGROUND = pygame.transform.scale(BACKGROUND, (800, 600))
BACKGROUND_RECT = BACKGROUND.get_rect()


class Fruit(pygame.sprite.Sprite):
    def __init__(self, x0, y0):
        pygame.sprite.Sprite.__init__(self)
        self.ss = SpriteSheet('pacmansprites2.png')
        self.image = self.ss.get_image(175, 165, 15, 15)
        self.rect = self.image.get_rect(x=x0, y=y0)
        self.eaten = False


    def checkCollision(self, sprite):
        if self.rect.colliderect(sprite.rect):
            self.eaten = True
            print("Collision")


    def checkWallCollision(self, wallRects):
        for wall in wallRects:
            while self.rect.colliderect(wall.rect):
                self.rect.x += 15
                if self.rect.x > 799:
                    self.rect.x = 80
        for wall in wallRects:
            if self.rect.colliderect(wall.rect):
                return False
            else:
                return True
                
    def isEaten(self):
        return self.eaten 


# Remember: image is part of sprite, used for drawing 
class Pacman(pygame.sprite.Sprite):
    def __init__(self, x0, y0):
        pygame.sprite.Sprite.__init__(self)
        self.ss = SpriteSheet('pacmansprites2.png')
        self.leftAnim = [self.ss.get_image(25, 5, 15, 15),\
                    self.ss.get_image(5, 5, 15, 15),\
                    self.ss.get_image(45, 5, 15, 15)]
        self.rightAnim = [self.ss.get_image(25, 25, 15, 15),\
                    self.ss.get_image(5, 25, 15, 15),\
                    self.ss.get_image(45, 5, 15, 15)]
        self.upAnim = [self.ss.get_image(25, 45, 15, 15),\
                    self.ss.get_image(5, 45, 15, 15),\
                    self.ss.get_image(45, 5, 15, 15)]
        self.downAnim = [self.ss.get_image(25, 65, 15, 15),\
                    self.ss.get_image(5, 65, 15, 15),\
                    self.ss.get_image(45, 5, 15, 15)]
        self.leftV = -3
        self.rightV = 3
        self.upV = -3
        self.downV = 3
        self.image = self.leftAnim[1]
        self.imageIndex = 1 
        # self.rect = self.image.get_rect(x=x0, y=y0)
        self.rect = pygame.Rect(x0, y0, 30, 30)
        # self.radius = 5
        self.vX = self.rightV
        self.vY = 0
        self.timer = 0.0


    def move(self):
        self.image = pygame.transform.scale(self.animate(), (30, 30))
        self.rect.x += self.vX
        if self.rect.x > 800:
            self.rect.x = 1
        if self.rect.x < 0:
            self.rect.x = 799
        self.rect.y += self.vY
        if self.rect.y > 600:
            self.rect.y = 1
        if self.rect.y < 0:
            self.rect.y = 599
    

    
    def checkWallCollision(self, wallRects):
        for wall in wallRects:
            if self.rect.colliderect(wall.rect):
                if self.vX == self.rightV:
                    while self.rect.colliderect(wall.rect):
                        self.rect.x -= 1
                    self.rect.x -= 1
                    # self.vX = self.leftV
                    self.vY = 0
                if self.vX == self.leftV:
                    while self.rect.colliderect(wall.rect):
                        self.rect.x += 1
                    self.rect.x += 1
                    # self.vX = self.rightV
                    self.vY = 0
                if self.vY == self.downV:
                    while self.rect.colliderect(wall.rect):
                        self.rect.y -= 1
                    self.rect.y -= 1
                    # self.vY = self.upV
                    self.vX = 0
                if self.vY == self.upV:
                    while self.rect.colliderect(wall.rect):
                        self.rect.y += 1
                    self.rect.y += 1
                    # self.vY = self.downV
                    self.vX = 0

                print("Wall Collision")


    def animate(self):
        if self.vX == self.rightV:
            if self.currentTime - self.timer > 100:
                if self.imageIndex < len(self.rightAnim) - 1:
                    self.imageIndex += 1
                else: 
                    self.imageIndex = 0
                self.timer = self.currentTime   
            return self.rightAnim[self.imageIndex]
        elif self.vX == self.leftV:
            if self.currentTime - self.timer > 100:
                if self.imageIndex < len(self.leftAnim) - 1:
                    self.imageIndex += 1
                else: 
                    self.imageIndex = 0
                self.timer = self.currentTime   
            return self.leftAnim[self.imageIndex]
        elif self.vY == self.upV:
            if self.currentTime - self.timer > 100:
                if self.imageIndex < len(self.upAnim) - 1:
                    self.imageIndex += 1
                else: 
                    self.imageIndex = 0
                self.timer = self.currentTime   
            return self.upAnim[self.imageIndex]
        elif self.vY == self.downV:
            if self.currentTime - self.timer > 100:
                if self.imageIndex < len(self.downAnim) - 1:
                    self.imageIndex += 1
                else: 
                    self.imageIndex = 0
                self.timer = self.currentTime   
            return self.downAnim[self.imageIndex]


    def update(self, currentTime, keys, wallRects):
        self.currentTime = currentTime
        self.handleInput(keys)
        self.move()
        self.checkWallCollision(wallRects)



    def handleInput(self, keys):
        if keys[pygame.K_UP]:
            self.vY = self.upV
            self.vX = 0
        if keys[pygame.K_RIGHT]:
            self.vY = 0
            self.vX = self.rightV
        if keys[pygame.K_LEFT]:
            self.vY = 0
            self.vX = self.leftV
        if keys[pygame.K_DOWN]:
            self.vY = self.downV
            self.vX = 0


class Wall(object):
    def __init__(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1], 20, 20)


class Game(object):
    def __init__(self):
        self.screen = self.initPygame()
        self.screenRect = self.screen.get_rect()
        self.pacmanGroup = self.initPacman()
        self.done = False
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.currentTime = 0.0
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.maxTime = 15000 # In ms
        self.timeLeft = self.maxTime - self.currentTime
        self.level = level
        self.walls = []
        self.initLevel()
        self.fruitGroup = self.initFruit()
        # self.pacman = Pacman(100, 500)


    def initLevel(self):
        x = y = 0
        for row in self.level:
            for col in row:
                if col == "W":
                    self.walls.append(Wall((x, y)))
                x += 20
            y += 20
            x = 0


    def initPacman(self):
        spriteGroup = pygame.sprite.Group()
        pacman = Pacman(50, 80)
        spriteGroup.add(pacman)
        # pacman2 = Pacman(40, 40)
        # spriteGroup.add(pacman2)
        return spriteGroup


    def initPygame(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.set_caption('Eat-Man Ultra')
        screen = pygame.display.set_mode((800, 600))
        return screen
    
   
    def initFruit(self):
        spriteGroup = pygame.sprite.Group()
        fruit = Fruit(100, 150)
        spriteGroup.add(fruit)
        cont = False
        while not cont:
            cont = fruit.checkWallCollision(self.walls)
        # fruit.checkWallCollision(self.walls)
        return spriteGroup


    def updateFruit(self):
        for fruit in self.fruitGroup:
            fruit.checkCollision(self.pacmanGroup.sprites()[0])
            if fruit.isEaten():
                self.fruitGroup.remove(fruit)
                self.score += 1
                self.maxTime += 2000
        if len(self.fruitGroup.sprites()) < 1:
            random.seed(self.currentTime)
            x = random.randint(40, 760)
            y = random.randint(100, 500)
            fruit = Fruit(x, y)
            self.fruitGroup.add(fruit)
            cont = False
            while not cont:
                cont = fruit.checkWallCollision(self.walls)


    def updateText(self):
        scoreText = self.font.render(str(self.score), 1, (255, 255, 255))
        scoreRect = scoreText.get_rect()
        scoreRect.centerx = 400
        scoreRect.centery = 580
        self.screen.blit(scoreText, scoreRect)

        enText = self.font.render("Energy", 1, (255, 255, 255))
        enRect = enText.get_rect()
        enRect.centerx = 600
        enRect.centery = 580
        self.screen.blit(enText, enRect)

        timeText = self.font.render(str(self.timeLeft), 1, (255, 255, 255))
        timeRect = timeText.get_rect()
        timeRect.centerx = 700
        timeRect.centery = 580
        self.screen.blit(timeText, timeRect)


    def update(self):
        while not self.done and self.timeLeft > 0:
            self.currentTime = pygame.time.get_ticks()
            self.timeLeft = self.maxTime - self.currentTime
            self.keys = self.getUserInput()
            self.pacmanGroup.update(self.currentTime, self.keys, self.walls)
            # pygame.draw.rect(self.screen, (0, 0, 255), self.pacmanGroup.sprites()[0].rect)
            # pygame.display.flip()
            self.updateFruit()
            self.screen.blit(BACKGROUND, BACKGROUND_RECT)
            for wall in self.walls:
                pygame.draw.rect(self.screen, (136, 0, 137), wall.rect)
            self.updateText()
            self.pacmanGroup.draw(self.screen)
            self.fruitGroup.draw(self.screen)
            pygame.display.update()
            self.clock.tick(self.fps)
        self.endScreen(self.keys)


    def getUserInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

        keys = pygame.key.get_pressed()
        return keys 

    
    def endScreen(self, keys):
        self.screen.blit(BACKGROUND, BACKGROUND_RECT)
        finishInfoText = self.font.render("Final Score:", 1, (255, 255, 255))
        finishInfoRect = finishInfoText.get_rect()
        finishInfoRect.centerx = 400
        finishInfoRect.centery = 260
        self.screen.blit(finishInfoText, finishInfoRect)
        finishText = self.font.render(str(self.score), 1, (255, 255, 255))
        finishRect = finishText.get_rect()
        finishRect.centerx = 400
        finishRect.centery = 300
        self.screen.blit(finishText, finishRect)
        enterText = self.font.render("Press enter to quit", 1, (255, 255, 255))
        enterRect = enterText.get_rect()
        enterRect.centerx = 400
        enterRect.centery = 360
        self.screen.blit(enterText, enterRect)
        pygame.display.update()
        disp = False
        while not keys[pygame.K_RETURN]:
            oldTime = pygame.time.get_ticks()
            timer = pygame.time.get_ticks() - oldTime
            keys = self.getUserInput()  
            while timer < 500 and not keys[pygame.K_RETURN]:
                timer = pygame.time.get_ticks() - oldTime
                if disp:
                    self.screen.blit(BACKGROUND, BACKGROUND_RECT)
                    self.screen.blit(finishInfoText, finishInfoRect)
                    self.screen.blit(finishText, finishRect)
                    self.screen.blit(enterText, enterRect)
                else: 
                    self.screen.blit(BACKGROUND, BACKGROUND_RECT)
                    self.screen.blit(finishInfoText, finishInfoRect)
                    self.screen.blit(finishText, finishRect)
                disp = not disp
            pygame.display.update()





game = Game()
game.update()
