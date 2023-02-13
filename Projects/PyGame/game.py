import pygame
import sys
import random

class Game:
    def __init__(self, jerma_img, background_img, pizza_img):
        self.active = True
        self.jerma = pygame.image.load(jerma_img).convert_alpha()
        self.background = pygame.image.load(background_img).convert_alpha()
        self.pizza = pygame.image.load(pizza_img).convert_alpha()
        self.jerma_pos = [250, 250]
        self.cookies = 0

    def show_jerma(self, screen):
        screen.blit(self.jerma, self.jerma_pos)
    def show_pizza(self, screen):
        screen.blit(self.pizza, (10,10))

    def show_background(self, screen):
        screen.blit(self.background, (0,0))

    def resize_images(self):
        self.jerma = pygame.transform.scale(self.jerma, (10, 10))
        self.pizza = pygame.transform.scale(self.pizza, (200, 200))

    def jiggle_pizza(self):
        self.pizza = pygame.transform.scale(self.pizza, (210, 210))

    def update_jerma(self):
        self.jerma_pos = (pygame.mouse.get_pos()[0] -5, pygame.mouse.get_pos()[1])