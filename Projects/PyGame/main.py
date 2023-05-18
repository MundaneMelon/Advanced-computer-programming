import pygame
import sys
from game import *

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
game = Game('Images/jerma.jpg', 'Images/black_background.png', 'Images/pizza.png')
game.resize_images()
check = True
moveSpeed = 10

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() # shutdown game completely

        if event.type == pygame.MOUSEBUTTONDOWN:
            game.mouse_inputs()

        if check:
            pass #wat
        else:
            game.resize_images()



    game.show_background(screen)

    if game.active:
        game.show_pizza(screen)
        game.print_cookie_text(screen)
        game.print_header(screen)

    pygame.display.update()
    clock.tick(200)