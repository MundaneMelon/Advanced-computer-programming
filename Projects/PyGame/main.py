import pygame
import sys
from game import *

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
game = Game('Images/jerma.jpg', 'Images/black_background.png', 'Images/pizza.jpg')
game.resize_images()
check = True
moveSpeed = 10

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() # shutdown game completely

        if check:
            game.jiggle_pizza()
            check = False
        else:
            game.resize_images()
            check = True



    game.show_background(screen)

    if game.active:
        game.show_jerma(screen)
        game.show_pizza(screen)
        game.update_jerma()

    pygame.display.update()
    clock.tick(60)