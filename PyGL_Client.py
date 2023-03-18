#!/usr/bin/env python
# Written by: Alice Williams

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import PyGL_Draw
import sys

class Client:
    """GL window management"""
    def init_gl(self):
        # https://learnopengl.com/Advanced-OpenGL/Depth-testing
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glViewport(0, 0, 500, 500)
        glLoadIdentity()
        #glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
        gluPerspective(45.0, float(500)/float(500), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    def display(self):
        glClearColor(0.75, 0.75, 0.75, 0.75)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0,0.0,-6.0)
        glColor3f(1.0, 0.0, 3.0)
        glRotatef(self.x_axis, 1.0, 0.0, 0.0)
        glRotatef(self.y_axis, 0.0, 1.0, 0.0)
        glRotatef(self.z_axis, 0.0, 0.0, 1.0)
        PyGL_Draw.cube()
        self.x_axis = self.x_axis - 0.30
        self.z_axis = self.z_axis - 0.30
        glutSwapBuffers()

    def reshape(self, width, height):
        glViewport(0, 0, width, height)

    def keyboard(self, *args):
        # key events
        if self.window and args[0] == b'\x1b':
            glutDestroyWindow(self.window)

    def mouse(self, button, state, x, y):
        # mouse events
        pass

    def __init__(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
        glutInitWindowSize(500, 500)
        glutInitWindowPosition(0, 0)
        self.window = glutCreateWindow("pygl devbox")
        self.init_gl()
        glutReshapeFunc(self.reshape)
        glutMouseFunc(self.mouse)
        glutKeyboardFunc(self.keyboard)
        glutDisplayFunc(self.display)
        glutIdleFunc(self.display)
        self.x_axis = 0.0
        self.y_axis = 0.0
        self.z_axis = 0.0
        self.direction = 1


def main():
    Client()
    glutMainLoop()


if __name__ == "__main__":
    main()
