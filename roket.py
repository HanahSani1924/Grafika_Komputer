from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def BODY():
    glBegin(GL_POLYGON)
    glColor3ub(225,225, 225)
    glVertex2f(40, 80)  #a
    glVertex2f(20, 40)  #b
    glVertex2f(7, -40)  #c
    glVertex2f(72, -40) #d
    glVertex2f(60, 40 ) #e
    glEnd()

def LEFT_WING():
    glBegin(GL_QUADS)
    glColor3ub(150, 0, 0)
    glVertex2f(-7, -65) #f
    glVertex2f(-7, -47) #g
    glVertex2f(12, 10)  #h
    glVertex2f(5, -40)  #i
    glEnd()

def RIGHT_WING():
    glBegin(GL_QUADS)
    glColor3ub(150, 0, 0)
    glVertex2f(68, 10)  #j
    glVertex2f(87, -47) #k
    glVertex2f(87, -65) #l
    glVertex2f(75, -40) #m
    glEnd()

def WINDOW():
    glBegin(GL_QUADS)
    glColor3ub(0, 30, 180)
    glVertex2f(28, 31)  #n
    glVertex2f(52, 31)  #o
    glVertex2f(52, 8)   #p
    glVertex2f(28, 8)   #q
    glEnd()

def NOS1():
    glBegin(GL_QUADS)
    glColor3ub(75, 75, 75)
    glVertex2f(12, -40)  #a
    glVertex2f(68, -40)  #b
    glVertex2f(68, -56)  #c
    glVertex2f(12, -56)  #d
    glEnd()

def NOS2():
    glBegin(GL_QUADS)
    glColor3ub(255, 85, 0)
    glVertex2f(48, -68)  #e
    glVertex2f(32, -68)  #n
    glVertex2f(32, -56)  #o
    glVertex2f(48, -56)  #p
    glEnd()



def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    glTranslated(200,250,0)

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    BODY()
    LEFT_WING()
    RIGHT_WING()
    WINDOW()
    NOS1()
    NOS2()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA) 
glutInitWindowSize(500, 500) 
glutInitWindowPosition(0, 0) 
wind = glutCreateWindow("karakter roket")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop() 