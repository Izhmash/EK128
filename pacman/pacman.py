from SpriteSheet import SpriteSheet
import sys
import os
import pygame


BACKGROUND = pygame.image.load('pacmansprites2.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (800, 600))
BACKGROUND_RECT = BACKGROUND.get_rect()

# Remember: image is part of sprite, used for drawing 
class Pacman(pygame.sprite.Sprite):
    def __init__(self, x0, y0):
        pygame.sprite.Sprite.__init__(self)
        self.ss = SpriteSheet('pacmansprites2.png')
        self.leftAnim = [self.ss.get_image(20, 0, 20, 20),\
                    self.ss.get_image(0, 0, 20, 20),\
                    self.ss.get_image(40, 0, 20, 20)]
        self.rightAnim = [self.ss.get_image(20, 20, 20, 20),\
                    self.ss.get_image(0, 20, 20, 20),\
                    self.ss.get_image(40, 0, 20, 20)]
        self.upAnim = [self.ss.get_image(20, 40, 20, 20),\
                    self.ss.get_image(0, 40, 20, 20),\
                    self.ss.get_image(40, 0, 20, 20)]
        self.downAnim = [self.ss.get_image(20, 60, 20, 20),\
                    self.ss.get_image(0, 60, 20, 20),\
                    self.ss.get_image(40, 0, 20, 20)]
        self.leftV = -2
        self.rightV = 2
        self.upV = -2
        self.downV = 2
        self.image = self.leftAnim[1]
        self.imageIndex = 1 
        self.rect = self.image.get_rect(x=x0, y=y0)
        self.vX = self.rightV
        self.vY = 0
        self.timer = 0.0


    def move(self):
        self.image = self.animate()
        self.rect.x += self.vX
        self.rect.y += self.vY


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


    def update(self, currentTime, keys):
        self.currentTime = currentTime
        self.handleInput(keys)
        self.move()



    def handleInput(self, keys):
        if keys[pygame.K_UP]:
            self.vY = self.upV
            self.vX = 0
        elif keys[pygame.K_RIGHT]:
            self.vY = 0
            self.vX = self.rightV
        elif keys[pygame.K_LEFT]:
            self.vY = 0
            self.vX = self.leftV
        elif keys[pygame.K_DOWN]:
            self.vY = self.downV
            self.vX = 0


class Game(object):
    def __init__(self):
        self.screen = self.initPygame()
        self.screenRect = self.screen.get_rect()
        self.pacmanGroup = self.initPacman()
        self.done = False
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.currentTime = 0.0
        # self.pacman = Pacman(100, 500)

   
    def initPacman(self):
        spriteGroup = pygame.sprite.Group()
        pacman = Pacman(0, 0)
        spriteGroup.add(pacman)
        return spriteGroup


    def initPygame(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.set_caption('Pac-Man')
        screen = pygame.display.set_mode((800, 600))
        return screen
    
    
    def update(self):
        while not self.done:
            self.currentTime = pygame.time.get_ticks()
            self.keys = self.getUserInput()
            self.pacmanGroup.update(self.currentTime, self.keys)
            self.screen.blit(BACKGROUND, BACKGROUND_RECT)
            self.pacmanGroup.draw(self.screen)
            pygame.display.update()
            self.clock.tick(self.fps)


    def getUserInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

        keys = pygame.key.get_pressed()
        return keys 


game = Game()
game.update()
