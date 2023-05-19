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

faces = (
    (0, 1, 2),   # Bottom face
    (0, 2, 3),   # Right face
    (0, 3, 4),   # Back face
    (0, 4, 1),   # Left face
    (1, 2, 3, 4)  # Front face
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
    glTranslatef(0.0, -0.5, -5.0)  # Translate to the center of the pyramid
    glRotatef(rotation_x, 1, 0, 0)
    glRotatef(rotation_y, 0, 1, 0)

    # Draw the pyramid
    glBegin(GL_TRIANGLES)
    for face in faces:
        glColor3fv(colors[faces.index(face) % len(colors)])  # Assign color to each face
        for vertex in face:
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
