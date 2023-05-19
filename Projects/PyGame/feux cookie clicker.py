import pygame
import sys

# Initialize Pygame
pygame.init()

# Game constants
WIDTH = 800
HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cookie Clicker Clone")
clock = pygame.time.Clock()

# Game variables
cookies = 0
cookie_multiplier = 1
click_power = 1

# Building variables
building_prices = [10, 100, 1000]  # Prices for each building
building_counts = [0, 0, 0]  # Number of each building
building_cookies_per_sec = [0.1, 1, 10]  # Cookies generated per second for each building

# Load images
cookie_image = pygame.image.load("images/pizza.png")

# Resize images
cookie_image = pygame.transform.scale(cookie_image, (100, 100))

# Set the initial position of the cookie
cookie_rect = cookie_image.get_rect()
cookie_rect.center = (WIDTH // 2, HEIGHT // 2)

# Create font objects
font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 24)

# Function to draw text on the screen
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

# Function to buy a building
def buy_building(building_index):
    global cookies, cookie_multiplier
    price = building_prices[building_index]
    if cookies >= price:
        cookies -= price
        building_counts[building_index] += 1
        cookie_multiplier += 0.1

# Game loop
running = True
while running:
    # Keep the loop running at the right speed
    clock.tick(FPS)

    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the cookie is clicked
            if cookie_rect.collidepoint(event.pos):
                cookies += click_power * cookie_multiplier
            # Check if a building button is clicked
            for i, button_rect in enumerate(building_buttons_rects):
                if button_rect.collidepoint(event.pos):
                    buy_building(i)

    # Update
    cookie_rect.center = (WIDTH // 2, HEIGHT // 2)

    # Calculate the total cookies per second from buildings
    total_cookies_per_sec = sum(building_cookies_per_sec[i] * building_counts[i] for i in range(len(building_counts)))

    # Increment the cookie count based on the total cookies per second
    cookies += total_cookies_per_sec / FPS

    # Draw / Render
    screen.fill(WHITE)
    screen.blit(cookie_image, cookie_rect)

    # Draw the number of cookies
    draw_text(f"Cookies: {int(cookies)}", font, BLACK, 20, 20)

    # Draw the click power
    draw_text(f"Click Power: {click_power}", small_font, BLACK, 20, 70)

    # Draw the cookie multiplier
    draw_text(f"Cookie Multiplier: x{cookie_multiplier:.1f}", small_font, BLACK, 20, 120)

    # Draw the building information
    draw_text("Buildings:", font, BLACK, 20, 180)
    for i in range(len(building_counts)):
        building_name = f"Building {i+1}"
        building_count = building_counts[i]
        building_price = building_prices[i]
        cookies_per_sec = building_cookies_per_sec[i] * building_count
        draw_text(f"{building_name}: {building_count}", small_font, BLACK, 40, 220 + i * 50)
        draw_text(f"Price: {building_price}", small_font, BLACK, 40, 250 + i * 50)
        draw_text(f"Cookies/Sec: {cookies_per_sec}", small_font, BLACK, 40, 280 + i * 50)

    # Draw the building buttons
    building_buttons_rects = []
    for i in range(len(building_prices)):
        button_rect = pygame.Rect(40, 220 + i * 50, 150, 30)
        pygame.draw.rect(screen, BLACK, button_rect, 2)
        building_buttons_rects.append(button_rect)
        draw_text("Buy", small_font, BLACK, 115, 235 + i * 50)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
sys.exit()
