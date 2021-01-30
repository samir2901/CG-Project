from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from Clock import *

def init(width,height):
    glClearColor(0.0,0.0,0.0,1.0)        
    gluOrtho2D(0,width,0,height)    
    


def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    
    drawClock()    
    
    glutSwapBuffers()     

glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)

width = 640
height = 480

glutInitWindowSize(width,height)
wind = glutCreateWindow("OpenGL")
init(width,height)
glutDisplayFunc(display)
glutTimerFunc(1000,clock,0)
glutMainLoop()
