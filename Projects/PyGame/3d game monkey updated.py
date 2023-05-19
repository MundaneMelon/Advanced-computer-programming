import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import objloader

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

# Load the monkey head object
monkey = objloader.OBJ("monkey.obj")

# Initialize rotation variables
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

    # Draw the monkey head as wireframe
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)  # Enable wireframe mode
    glBegin(GL_TRIANGLES)
    for face in monkey.faces:
        for vertex in face:
            glVertex3fv(monkey.vertices[vertex])
    glEnd()
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)  # Disable wireframe mode

    # Update rotation
    rotation_x += 0.5
    rotation_y += 0.3

    # Swap the buffers
    pygame.display.flip()
    pygame.time.wait(10)

# Quit the game
pygame.quit()
