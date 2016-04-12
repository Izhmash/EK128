import pygame
import math

screen = pygame.display.set_mode((640, 400))
running = 1
clock = pygame.time.Clock()

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    screen.fill((255, 255, 255))
    for i in range(0, 640, 3):
        clock.tick(30)
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 255, 102), (i, int(-abs(math.sin(i))*100 + 200)), 10)
        pygame.display.flip()
