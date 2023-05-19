import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)

# Set up the 3D perspective
glViewport(0, 0, WIDTH, HEIGHT)
glMatrixMode(GL_PROJECTION)
gluPerspective(45, WIDTH / HEIGHT, 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
glEnable(GL_DEPTH_TEST)

# Initialize pyramid variables
vertices = (
    (0, 1, 0),     # Top vertex
    (-1, -1, 1),   # Bottom-left vertex
    (1, -1, 1),    # Bottom-right vertex
    (1, -1, -1),   # Top-right vertex
    (-1, -1, -1)   # Top-left vertex
)

edges = (
    (0, 1),   # Connects top vertex with bottom-left vertex
    (0, 2),   # Connects top vertex with bottom-right vertex
    (0, 3),   # Connects top vertex with top-right vertex
    (0, 4),   # Connects top vertex with top-left vertex
    (1, 2),   # Connects bottom-left vertex with bottom-right vertex
    (2, 3),   # Connects bottom-right vertex with top-right vertex
    (3, 4),   # Connects top-right vertex with top-left vertex
    (4, 1)    # Connects top-left vertex with bottom-left vertex
)

colors = (
    (0.976, 0.651, 0.651),  # Coral
    (0.804, 0.922, 0.796),  # Pale green
    (0.824, 0.651, 0.918),  # Lavender
    (0.863, 0.847, 0.941)   # Light purple
)

# Initialize pyramid rotation
rotation_x = 0
rotation_y = 0

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Set up the modelview matrix
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5.0)
    glRotatef(rotation_x, 1, 0, 0)
    glRotatef(rotation_y, 0, 1, 0)

    # Draw the pyramid
    glBegin(GL_LINES)
    for edge in edges:
        glColor3fv(colors[edges.index(edge) % len(colors)])  # Fix indexing of colors
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    # Update pyramid rotation
    rotation_x += 0.5
    rotation_y += 0.3

    # Swap the buffers
    pygame.display.flip()
    pygame.time.wait(10)

# Quit the game
pygame.quit()
