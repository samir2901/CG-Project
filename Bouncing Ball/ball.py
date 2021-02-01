from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global anim, x, y, dx, dy


##############
def setpixel(xcoordinate, ycoordinate):
    glBegin(GL_POINTS)
    glVertex2f(xcoordinate, ycoordinate)
    glEnd()
    glFlush()


def drawCircle(xc, yc, x, y):
    setpixel(xc + x, yc + y)
    setpixel(xc - x, yc + y)
    setpixel(xc + x, yc - y)
    setpixel(xc - x, yc - y)
    setpixel(xc + y, yc + x)
    setpixel(xc - y, yc + x)
    setpixel(xc + y, yc - x)
    setpixel(xc - y, yc - x)


def bresenhamCircle(xc, yc, r):
    x, y = 0, r
    Pk = 3 - 2 * r
    drawCircle(xc, yc, x, y)

    while y >= x:
        x = x + 1

        if Pk > 0:
            y = y - 1
            Pk = Pk + 4 * (x - y) + 10

        else:
            Pk = Pk + 4 * x + 6

        drawCircle(xc, yc, x, y)


