import pygame
import sys
from game import *

pygame.init()
screen = pygame.display.set_mode((500, 500))

clock = pygame.time.Clock()
timer = 0

game = Game('cookie.png')

#Buttons
cursor = Upgrade(game, 15, "Cursor", 1, 0)
grandma = Upgrade(game, 100, "Grandma", 5, 1)
farm = Upgrade(game, 1100, "Cookie Farm", 20, 2)
mine = Upgrade(game, 12000, "Dough Mine", 90, 3)
factory = Upgrade(game, 130000, "Factory", 3500, 4)
portal = Upgrade(game, 1000000, "Portal", 65000, 5)


button_array = [cursor, grandma, farm, mine, factory, portal]
game.button_array = button_array

#Places to click
pizza_hitbox = pygame.Rect(25,65,200,200)
button_general_area = pygame.Rect(300, 0, 200, 500)
minus_button = pygame.Rect(383, 463, 30, 30)
plus_button = pygame.Rect(465, 463, 30, 30)


while True:
    game.resize_images()
    game.show_background(screen)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() # shutdown game completely

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            if pizza_hitbox.collidepoint(position):
                game.cookies += 1 + (game.cps / 10)
            if button_general_area.collidepoint(position):
                for i in button_array:
                    if i.hitbox.collidepoint(position):
                        i.buy()
                        i.print_button(screen)
            if plus_button.collidepoint(position) and game.time_scale < 99:
                game.cps = game.cps**(1/game.time_scale)
                if game.time_scale < 2:
                    game.time_scale += .1
                game.cps = game.cps**game.time_scale
            if minus_button.collidepoint(position) and game.time_scale != 1:
                game.cps = game.cps**(1/game.time_scale)
                if game.time_scale != .1:
                    game.time_scale -= .1
                game.cps = game.cps**game.time_scale
    timer += clock.get_time()
    if timer >= 200:
        timer = 0
        game.compile_cookies(200)

    if game.active:
        game.show_pizza(screen)
        game.print_cookie_text(screen)
        game.print_header(screen)
        game.print_time_scale(screen)
        for i in button_array:
            i.print_button(screen)


    pygame.display.update()
    clock.tick(60)