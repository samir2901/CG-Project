from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *


def drawPoints(xc, yc, x, y):
    glVertex2i(xc + x, yc + y)
    glVertex2i(xc - x, yc + y)
    glVertex2i(xc + x, yc - y)
    glVertex2i(xc - x, yc - y)
    glVertex2i(xc + y, yc + x)
    glVertex2i(xc - y, yc + x)
    glVertex2i(xc + y, yc - x)
    glVertex2i(xc - y, yc - x)


def mid_point_circle(center, radius):
    x = 0
    y = radius
    p = 1 - radius
    glBegin(GL_POINTS)
    drawPoints(center[0],center[1],x,y)
    while x <= y:
        x += 1
        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * (x - y) + 1
        drawPoints(center[0],center[1],x,y)
    glEnd()
    glFlush()


def drawLineLow(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    if x1 > x2:
        x, y = x2, y2
        x2, y2 = x1, y1
        x1, y1 = x, y
    x, y = x1, y1
    p = 2*dy - dx
    glBegin(GL_POINTS)
    glVertex2i(x,y)
    while x<=x2:
        x += 1
        if p < 0:
            p += 2 * dy
        else:
            if (dy/dx) > 0:
                y += 1
            else:
                y -= 1
            p += 2*(dy - dx)
        glVertex2i(x,y)
    glEnd()
    glFlush()


def drawLineHigh(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    if y1 > y2:
        x, y = x2, y2
        x2, y2 = x1, y1
        y1, y1 = x, y
    x, y = x1, y1
    p = 2*dx - dy
    glBegin(GL_POINTS)
    glVertex2i(x,y)
    while y<=y2:
        y += 1
        if p < 0:
            p = p + 2*dy
        else:
            if (dy/dx) > 0:
                x += 1
            else:
                x -= 1
            p = p + (2 * dy - 2 * dx)
        glVertex2i(x,y)
    glEnd()
    glFlush()


def bresenham_line(start, dest):
    if(abs(dest[1]-start[1]) == 0):
        x = min(start[0], dest[0])
        glBegin(GL_POINTS)
        while x<max(start[0],dest[0]):
            x+=1
            glVertex2i(x,start[1])
        glEnd()
        glFlush()
    elif(abs(dest[0]-start[0]) == 0):
        y = min(start[1],dest[1])
        glBegin(GL_POINTS)
        while y<max(start[1],dest[1]):
            y+=1
            glVertex2i(start[0],y)
        glEnd()
        glFlush()
    elif(abs(dest[1]-start[1]) <= abs(dest[0]-start[0])):
        drawLineLow(start[0],start[1],dest[0],dest[1])
    else:
        drawLineHigh(start[0],start[1],dest[0],dest[1])
