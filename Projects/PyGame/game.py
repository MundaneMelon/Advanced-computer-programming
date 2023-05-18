import pygame
import sys
import random

class Game:
    def __init__(self, jerma_img, background_img, pizza_img):
        self.active = True
        self.jerma = pygame.image.load(jerma_img).convert_alpha()
        self.background = pygame.image.load(background_img).convert_alpha()
        self.pizza = pygame.image.load(pizza_img).convert_alpha()
        self.pizza_hitbox = pygame.Rect(50,145,200,200)
        self.cookies = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render(str(self.cookies), True, (136, 0, 204))

    def show_pizza(self, screen):
        screen.blit(self.pizza, (50,145))
    def show_background(self, screen):
        # screen.blit(self.background, (0,0))
        screen.fill((238, 204, 255))
    def resize_images(self):
        self.jerma = pygame.transform.scale(self.jerma, (10, 10))
        self.pizza = pygame.transform.scale(self.pizza, (200, 200))
    def jiggle_pizza(self):
        self.pizza = pygame.transform.scale(self.pizza, (210, 210))
    def print_cookie_text(self, screen):
        self.text = self.font.render(str(self.cookies), True, (136, 0, 204))
        screen.blit(self.text, (10, 450))
    def print_header(self, screen):
        screen.blit(self.font.render("SUGAR COOKIE CLICKER", True, (0,0,0)), (10,20))
    def mouse_inputs(self):
        position = pygame.mouse.get_pos()
        if self.pizza_hitbox.collidepoint(position):
            self.cookies += 1