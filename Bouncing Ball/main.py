from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from ball import bresenhamCircle
import sys

global anim, x, y, dx, dy

# initial position of the ball
x = 0
y = 0

# Direction vector of the balls trajectory
dx = dy = 1

# Dimensions of screen
width = height = 500
axrng = 25

# No animation to start
anim = 0


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-axrng, axrng, -axrng, axrng)
    glPointSize(5.0)
    glColor3f(1.0, 0.0, 0.0)


def idle():
    # We animate only when anim == 1, or
    # the ball doesn't move
    if anim == 1:
        glutPostRedisplay()


def bounce():
    global x, y, dx, dy
    glClear(GL_COLOR_BUFFER_BIT)

    x += 0.5 * dx
    y += 0.5 * dy

    # Moving the ball location based on x and y axes positions

    bresenhamCircle(x, y, 5)

    # Collision detection
    if x >= axrng or x <= -axrng:
        dx = -1 * dx
    if y >= axrng or y <= -axrng:
        dy = -1 * dy

    glFlush()


def keyboard(key, x, y):
    ''' Allows us to quit by pressing 'Esc' or 'q'
        We can animate by "a" and stop by "s"   '''

    global anim
    if key == chr(27):
        sys.exit()

    if key == "a":
        anim = 1

    if key == "s":
        anim = 0

    if key == "q":
        sys.exit()


if __name__ == "__main__":

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowPosition(100, 100)
    glutInitWindowSize(width, height)
    glutCreateWindow("Bouncing Ball")

    glutDisplayFunc(bounce)
    glutKeyboardFunc(keyboard)
    glutIdleFunc(idle)

    init()
    glutMainLoop()
