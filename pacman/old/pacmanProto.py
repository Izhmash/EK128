import pygame
import math

screen = pygame.display.set_mode((640, 400))
running = 1
clock = pygame.time.Clock()

xPos = 0
yPos = 0

dir = 2
while running:
    clock.tick(60)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = 0
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dir = 0
            elif event.key == pygame.K_RIGHT:
                dir = 2
            elif event.key == pygame.K_DOWN:
                dir = 3
            elif event.key == pygame.K_UP:
                dir = 1
    
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 102), (xPos, yPos), 10)

    if dir == 0:
        xPos -= 2
        pygame.draw.arc(screen, (0, 0, 0), (xPos - 30, yPos - 30, 60, 60), 3*math.pi/4, 5*math.pi/4, 30)
    elif dir == 1:
        yPos -= 2
        pygame.draw.arc(screen, (0, 0, 0), (xPos - 30, yPos - 30, 60, 60), math.pi/4, 3*math.pi/4, 30)
    elif dir == 2:
        xPos += 2
        pygame.draw.arc(screen, (0, 0, 0), (xPos - 30, yPos - 30, 60, 60), -math.pi/4, math.pi/4, 30)
    elif dir == 3:
        yPos += 2
        pygame.draw.arc(screen, (0, 0, 0), (xPos - 30, yPos - 30, 60, 60), 5*math.pi/4, 7*math.pi/4, 30)

    pygame.display.update()


    
