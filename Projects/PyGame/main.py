import pygame
import sys
from game import *

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
game = Game('Images/jerma.jpg', 'Images/black_background.png')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() # shutdown game completely

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.show_jerma(screen)
                print("Uhhhhhh")
            if event.key == pygame.K_w:
                game.jerma_pos[0] -= 10
                game.jerma_pos[1] -= 10


    game.show_background(screen)
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
