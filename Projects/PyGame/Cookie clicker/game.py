import pygame
import sys
import random


class Game:
    def __init__(self, pizza_img):
        self.active = True
        self.pizza = pygame.image.load(pizza_img).convert_alpha()
        self._cookies = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.time_scale_font = pygame.font.Font('freesansbold.ttf', 28)
        self.text = self.font.render(str(int(self.cookies)), True, (136, 0, 204))
        self._cps = 0
        self._cool_cookie_number = 1
        self._button_array = []
        self.time_scale = 1.0

    # Getters and setters
    @property
    def button_array(self):
        return self._button_array

    @button_array.setter
    def button_array(self, value):
        self._button_array = value

    @property
    def cps(self):
        return self._cps

    @cps.setter
    def cps(self, value):
        self._cps = value

    @property
    def cookies(self):
        return self._cookies

    @cookies.setter
    def cookies(self, value):
        self._cookies = value

    @property
    def cool_cookie_number(self):
        return self._cool_cookie_number

    def set_cool_cookie_number(self):
        result = 1
        for i in self.button_array:
            result += (i.cps * i.count) / 5
        self._cool_cookie_number = result

    def show_pizza(self, screen):
        screen.blit(self.pizza, (25, 65))

    def show_background(self, screen):
        screen.fill((238, 204, 255))

    def resize_images(self):
        self.pizza = pygame.transform.scale(self.pizza, (200, 200))

    def print_cookie_text(self, screen):
        self.text = self.font.render(return_comma_str(str(int(self.cookies))), True, (136, 0, 204))
        screen.blit(self.text, (10, 300))
        temp_text = self.font.render("cookies", True, (136, 0, 204))
        screen.blit(temp_text, (10, 330))
        temp = str(round(self.cps, 1))
        temp_decimal = ""
        if temp != 0:
            for i in range(0, len(temp)-1):
                if temp[i:i+1] == ".":
                    temp_decimal = temp[i::]
                    temp = return_comma_str(temp[0:i])

        temp_text = self.font.render(f"{temp}{temp_decimal}", True, (136, 0, 204))
        screen.blit(temp_text, (10, 420))
        temp_text = self.font.render("cookies/sec", True, (136, 0, 204))
        screen.blit(temp_text, (10, 450))

    def print_header(self, screen):
        screen.blit(self.font.render("purple cookie clicker", True, (0, 0, 0)), (10, 10))

    def compile_cookies(self, milliseconds):
        self.cookies += self.cps / (1000 / milliseconds)

    def print_time_scale(self, screen):
        temp_text = self.time_scale_font.render(f"time scale:", True, (0,0,0))
        screen.blit(temp_text, (225,462))
        temp_text = self.time_scale_font.render(str(self.time_scale)[0:3], True, (0,0,0))
        screen.blit(temp_text, (420,463))
        pygame.draw.rect(screen, (158,158,158), pygame.Rect(383, 463, 30, 30))
        pygame.draw.rect(screen, (158,158,158), pygame.Rect(465, 463, 30, 30))
        screen.blit(self.time_scale_font.render("+", True, (0,0,0)), (471,463))
        screen.blit(self.time_scale_font.render("-", True, (0,0,0)), (392,464))

class Upgrade():
    def __init__(self, game, price, name, cps, button_num):
        self.price = price
        self.name = name
        self.cps = cps
        self.count = 0
        self.button_num = button_num
        self.game = game
        self.name_font = pygame.font.Font('freesansbold.ttf', 21)
        self.hitbox = pygame.Rect(290, 60 + (65 * self.button_num), 205, 60)
        self.active = False
        self.toggle = False

    def print_button(self, screen):
        if self.game.cookies >= self.price / 10:
            self.toggle = True
        if self.game.cookies >= self.price:
            self.active = True
        else:
            self.active = False
        if self.toggle:
            if self.active:
                white_box_color = (255, 255, 255)
                text_color = (0, 0, 0)
            else:
                white_box_color = (128, 128, 128)
                text_color = (175, 0, 0)

            height = 60 + (65 * self.button_num)
            # Black box
            thing = pygame.Rect(285, height - 5, 215, 70)
            pygame.draw.rect(screen, (0, 0, 0), thing)

            # White box
            pygame.draw.rect(screen, white_box_color, self.hitbox)
            # Name/price
            name_text = self.name_font.render(self.name, True, text_color)
            cost_text = self.name_font.render( \
                f"{return_comma_str(str(int(self.price)))}", True, text_color)
            amount_text = self.name_font.render(f"{return_comma_str(str(self.count))}", True, \
                                                (0, 0, 0))
            screen.blit(name_text, (300, height + 10))
            screen.blit(cost_text, (300, height + 30))
            screen.blit(amount_text, (435, height + 10))

    def buy(self):
        if self.game.cookies >= int(self.price):
            # Subtract cookies
            self.game.cookies -= int(self.price)
            # Add 1 to count
            self.count += 1
            # add appropriate amount to cps
            temp = self.game.cps ** (1/self.game.time_scale)
            temp += self.cps
            self.game.cps = temp ** self.game.time_scale
            # increase price by percent
            self.price = int(self.price * (1 + .15))

def return_comma_str(str):
    str = str[::-1]
    result = ''
    count = 0
    while len(str) > 0:
        if count != 3:
            count += 1
            result += str[0:1]
            str = str[1::]
        elif count == 3 and len(str) > 0:
            count = 0
            result += ','
    return result[::-1]
