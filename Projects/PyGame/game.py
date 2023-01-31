import pygame
import sys
import random

class Game:
    def __init__(self, jerma_img, background_img):
        self.active = True
        self.jerma = pygame.image.load(jerma_img).convert_alpha()
        self.background = pygame.image.load(background_img).convert_alpha()
        self.jerma_pos = [250, 250]

    def show_jerma(self, screen):
        screen.blit(self.jerma, self.jerma_pos)
    def show_background(self, screen):
        screen.blit(self.background, (0,0))