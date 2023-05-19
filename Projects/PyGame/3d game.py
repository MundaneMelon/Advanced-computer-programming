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

# Initialize prism variables
vertices = (
    (1, -1, -0.5),
    (1, 1, -0.5),
    (-1, 1, -0.5),
    (-1, -1, -0.5),
    (1, -1, 0.5),
    (1, 1, 0.5),
    (-1, 1, 0.5),
    (-1, -1, 0.5)
)

edges = (
    (0, 1, 2, 3),
    (4, 5, 6, 7),
    (0, 1, 5, 4),
    (1, 2, 6, 5),
    (2, 3, 7, 6),
    (3, 0, 4, 7)
)

colors = (
    (0.792, 0.875, 0.906),  # Light blue
    (0.847, 0.749, 0.847),  # Lavender
    (0.800, 0.922, 0.796),  # Pale green
    (0.980, 0.875, 0.651),  # Peach
    (0.961, 0.769, 0.651),  # Light orange
    (0.863, 0.847, 0.941)   # Light purple
)

# Initialize prism rotation
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

    # Draw the prism
    glBegin(GL_QUADS)
    for face in edges:
        glColor3fv(colors[edges.index(face)])
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    # Update prism rotation (slower speed)
    rotation_x += 0.2
    rotation_y += 0.1

    # Swap the buffers
    pygame.display.flip()
    pygame.time.wait(10)  # Increase the waiting time to slow down the rotation

# Quit the game
pygame.quit()
