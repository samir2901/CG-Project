from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from clock import draw_clock, clock_timer

WIDTH = 640
HEIGHT = 480

def init(width,height):
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(0,width,0,height)


def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPointSize(2.5)
    draw_clock(WIDTH, HEIGHT)
    glutSwapBuffers()


if __name__ == "__main__":

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)

    glutInitWindowSize(WIDTH, HEIGHT)
    wind = glutCreateWindow("Analog Clock")
    init(WIDTH, HEIGHT)

    glutDisplayFunc(display)
    glutTimerFunc(1000, clock_timer, 0)

    glutMainLoop()
