import curses
import time
import random

# Game constants
DELAY = 0.1
MAX_WIDTH = 60
MAX_HEIGHT = 20
ROAD_CHAR = "="
PLAYER_CHAR = ">"
OBSTACLE_CHAR = "#"

# Initialize curses
stdscr = curses.initscr()
curses.curs_set(0)
stdscr.timeout(0)

# Create the game window
win = curses.newwin(MAX_HEIGHT, MAX_WIDTH, 0, 0)
win.keypad(1)
win.nodelay(1)

# Initialize game variables
player_x = MAX_WIDTH // 2
player_y = MAX_HEIGHT - 1
obstacles = []
score = 0

# Function to draw the player, obstacles, and score
def draw():
    win.clear()
    win.addch(player_y, player_x, PLAYER_CHAR)
    for obstacle in obstacles:
        win.addch(obstacle[0], obstacle[1], OBSTACLE_CHAR)
    win.addstr(0, 2, "Score: " + str(score))
    win.refresh()

# Main game loop
while True:
    # Get user input
    key = win.getch()

    # Quit the game if 'q' is pressed
    if key == ord('q'):
        break

    # Move the player
    if key == curses.KEY_LEFT and player_x > 0:
        player_x -= 1
    elif key == curses.KEY_RIGHT and player_x < MAX_WIDTH - 1:
        player_x += 1

    # Update obstacles and check for collisions
    if len(obstacles) > 0:
        for obstacle in obstacles:
            if obstacle[0] == player_y and obstacle[1] == player_x:
                break
        else:
            if obstacles[0][0] == MAX_HEIGHT - 1:
                obstacles.pop(0)
                score += 1
            else:
                obstacles[0][0] += 1

    # Generate new obstacles randomly
    if random.randint(0, 10) > 7:
        obstacles.append([0, random.randint(0, MAX_WIDTH - 1)])

    # Draw the game
    draw()

    # Delay the game
    time.sleep(DELAY)

# End the game
curses.endwin()
