from SpriteSheet import SpriteSheet
import pygame


screen = pygame.display.set_mode((640, 480))

ss = SpriteSheet('pacmansprites2.png')

image0 = ss.get_image(0, 0, 20, 20)
image1 = ss.get_image(20, 0, 20, 20)
image2 = ss.get_image(40, 0, 20, 20)
image3 = ss.get_image(0, 20, 20, 20)

images = [image0, image1, image2]

running = 1
clock = pygame.time.Clock()

animCnt = 0
counter = 0
while running:
    animCnt = animCnt + 1
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    if animCnt % 4 == 0:
        screen.fill(pygame.Color('black'))
        screen.blit(images[counter], (0, 0))
        counter = counter + 1
    if counter == len(images):
        counter = 0
    pygame.display.flip()
    clock.tick(60)  # 16.67 ms per frame
