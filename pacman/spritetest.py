from SpriteSheet import SpriteSheet
import pygame


screen = pygame.display.set_mode((640, 480))

ss = SpriteSheet('pacmansprites2.png')

image = ss.get_image(85, 0, 25, 25)

running = 1
clock = pygame.time.Clock()

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    screen.fill(pygame.Color('black'))
    screen.blit(image, (0, 0))
    pygame.display.flip()
    clock.tick(60)
