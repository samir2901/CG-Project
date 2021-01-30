from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from datetime import datetime
from MidPointCircle import midPointCircle
from BresenhamLine import BresenhamLine

def lerp(var, minVar, maxVar, minLimit, maxLimit):
    '''
    Linearly interpolates the value of var from minVar-maxVar to minLimit-maxLimit
    '''
    deltaVar = maxVar - minVar
    deltaLimit = maxLimit - minLimit

    value = float(var - minVar)/float(deltaVar) * float(deltaLimit) + minLimit
    return value


secAngle = 0
minuteAngle = 0
hourAngle = 0

def clock(value):
    global secAngle, minuteAngle
    now = datetime.now()
    hr = now.hour
    minute = now.minute
    sec = now.second
    secAngle = lerp(sec,0,60,0,360)
    minuteAngle = lerp(minute,0,60,0,360)
    hourAngle = lerp(hr%12,0,12,0,360)
    glutPostRedisplay()
    glutTimerFunc(1000,clock,0)

def drawClock():
    center = (640//2,480//2)
    #drawing circle
    glColor3f(1.0,0.0,0.0)
    midPointCircle(center, 200)

    now = datetime.now()
    hr = now.hour
    minute = now.minute
    sec = now.second
    secAngle = lerp(sec,0,60,0,360)
    minuteAngle = lerp(minute,0,60,0,360)
    hourAngle = lerp(hr%12,0,12,0,360)

    #draw lines
    #seconds line
    glPushMatrix()
    glTranslate(center[0],center[1],0)
    glRotate(-secAngle,0,0,1)
    glColor3f(1.0,0.0,1.0)
    BresenhamLine((0,0),(0,190))
    glPopMatrix()


    #minutes line
    glPushMatrix()
    glTranslate(center[0],center[1],0)
    glRotate(-minuteAngle,0,0,1)
    glColor3f(1.0,1.0,1.0)
    BresenhamLine((0,0),(0,170))
    glPopMatrix()


    #hour line
    glPushMatrix()
    glTranslate(center[0],center[1],0)
    glRotate(-hourAngle,0,0,1)
    glColor3f(0.0,1.0,0.0)
    BresenhamLine((0,0),(0,150))
    glPopMatrix()