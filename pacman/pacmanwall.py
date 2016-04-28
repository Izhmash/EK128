import os
import random
import pygame

# Nice class to hold a wall rect
class Wall(pygame.sprite.Sprite):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 20, 20)

# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

# Set up the display
pygame.display.set_caption("Get to the red square!")
screen = pygame.display.set_mode((800,600))

clock = pygame.time.Clock()
walls = [] # List to hold the walls

# Holds the level layout in a list of strings.
level = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"            W            WW             ",
"   WWWW     W             W     WWWWWW  ",
"   W     WWWW   WWW   W              WWW",
"WWWW        W     W   W                 ",
"            W     W   WWWWWW   WWW      ",
"                  W       WW   W     WWW",
"     W            W       WW   W     W  ",
"     WW   WWW     WWWWWW  WW   W     W  ",
"            W                  WWW   W  ",
"WWW                            WWW   W  ",
"      WWWWWW     WWW                 W  ",
"      W          W         WW        W  ",
"      W          W         WW     WWWW  ",
"      WWW      WWW              WW      ",
"                     WWW        WW      ",
"WWW                    W         WWW    ",
"  WWWWWWW      W       WWW       WWW    ",
"        W    WWW                        ",
"        W    W                          ",
"     WWWW    W    W    WWWW    W     W  ",
"             WWWWWW       W    W     W  ",
"  W              WW       WWWWWW    WW  ",
"  WW                  W       W     W   ",
"   W   WW   WW        W             W   ",
"        W             W        E        ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

# Parse the level string above. W = wall, E = exit
x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 20, 20)
        x += 20
    y += 20
    x = 0

running = False
while not running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = True
    
    clock.tick(60)
    
    # Draw the scene
    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (136,0,137), wall.rect)
    pygame.draw.rect(screen, (255, 0, 0), end_rect)
    pygame.display.flip()

pygame.quit()
