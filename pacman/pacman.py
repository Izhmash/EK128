import sys
import os
import pygame

# Remember: image is part of sprite, used for drawing 
class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Pacman, self).__init__()

class Game(object):
    def __init__(self):
        self.screen = self.initPygame()

    def initPygame(self):
        pygame.init()
        pygame.display.set_caption('Pac-Man')
        screen = pygame.display.set_mode((800, 600))
        return screen
