import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluPerspective

def draw_triangle():
    glBegin(GL_TRIANGLES)
    glVertex3f(-1, -1, 0)
    glVertex3f(1, -1, 0)
    glVertex3f(0, 1, 0)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_triangle()
    glutSwapBuffers()

def main():
    pygame.init()
    display_size = (800, 600)
    pygame.display.set_mode(display_size, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display_size[0] / display_size[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        display()
        pygame.time.wait(10)

if __name__ == "__main__":
    glutInit()
    main()
