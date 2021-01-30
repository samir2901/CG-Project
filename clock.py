from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from datetime import datetime
from cg_algo import mid_point_circle, bresenham_line


def lerp(var, minVar, maxVar, minLimit, maxLimit):
    '''
    Linearly interpolates the value of var from minVar-maxVar to minLimit-maxLimit
    '''
    deltaVar = maxVar - minVar
    deltaLimit = maxLimit - minLimit

    value = float(var - minVar)/float(deltaVar) * float(deltaLimit) + minLimit
    return value


def clock_timer(value):
    glutPostRedisplay()
    glutTimerFunc(1000, clock_timer, 0)


def draw_clock(WIDTH, HEIGHT):
    center = (WIDTH//2, HEIGHT//2)
    # Drawing circle
    glColor3f(1.0,0.0,0.0)
    mid_point_circle(center, 200)

    # Extract current time.
    now = datetime.now()
    hr = now.hour
    minute = now.minute
    sec = now.second

    secAngle = lerp(sec,0,60,0,360)
    minuteAngle = lerp(minute,0,60,0,360)
    hourAngle = lerp(hr%12,0,12,0,360)

    # Drawing clock arms
    # Seconds arm
    glPushMatrix()
    glTranslate(center[0],center[1],0)
    glRotate(-secAngle,0,0,1)
    glColor3f(1.0,0.0,1.0)
    bresenham_line((0,0),(0,190))
    glPopMatrix()


    # Minutes arm
    glPushMatrix()
    glTranslate(center[0],center[1],0)
    glRotate(-minuteAngle,0,0,1)
    glColor3f(1.0,1.0,1.0)
    bresenham_line((0,0),(0,170))
    glPopMatrix()


    # Hour arm
    glPushMatrix()
    glTranslate(center[0],center[1],0)
    glRotate(-hourAngle,0,0,1)
    glColor3f(0.0,1.0,0.0)
    bresenham_line((0,0),(0,150))
    glPopMatrix()
