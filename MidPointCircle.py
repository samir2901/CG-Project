from OpenGL.GL import *

def drawPoints(xc, yc, x, y):
    glVertex2i(xc + x, yc + y)
    glVertex2i(xc - x, yc + y)
    glVertex2i(xc + x, yc - y)
    glVertex2i(xc - x, yc - y)
    glVertex2i(xc + y, yc + x)
    glVertex2i(xc - y, yc + x)
    glVertex2i(xc + y, yc - x)
    glVertex2i(xc - y, yc - x)

def midPointCircle(center, radius):
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
        
