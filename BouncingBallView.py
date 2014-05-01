#!/usr/bin/python

import sys
import BouncingBallModel
import BouncingBallController
from OpenGL.GLUT import *
from OpenGL.GL import *

refresh = 30
time = 0
screenWidth = 1350
screenHeight = 700
radius = 2
left = 0.0
right = 0.0
bottom = 0.0
top = 0.0

# Initialize material property and light source.
def init():
   light_ambient = [0.0, 1.0, 1.0, 0.0]
   light_diffuse = [1.0, 1.0, 1.0, 1.0]
   light_specular = [1.0, 1.0, 1.0, 1.0]
   # light_position is NOT default value
   light_position = [0.25, 1.0, 1.0, 0.0]

   glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
   glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
   glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
   glLightfv(GL_LIGHT0, GL_POSITION, light_position)

   glEnable(GL_LIGHTING)
   glEnable(GL_LIGHT0)
   glEnable(GL_DEPTH_TEST)

def display():
   global time

   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

   glLoadIdentity()

   spherePos = BouncingBallModel.updateObject('glutSolidSphere',time)

   glPushMatrix()
   glTranslatef(spherePos[0], spherePos[1], spherePos[2])
   glutSolidSphere(radius, 40, 40)
   glPopMatrix()

   glutSwapBuffers()

   glFlush()
   time = time + .25

def reshape(w, h):
   global left,right,bottom,top

   glViewport(0, 0, w, h)
   glMatrixMode (GL_PROJECTION)
   glLoadIdentity()

   if w > h:
      left = -20
      right = 20
      bottom = -20 * h/w #10.37
      top = 20 * h/w
   else:
      left = 20 * w/h
      right = 20 * w/h
      bottom = -20
      top = 20

   glOrtho(left,right,bottom,top, -10.0, 10.0)

   BouncingBallModel.setScreenBoundries(left + radius, right - radius, bottom + radius, top - radius)
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()

def Timer(value):
   glutPostRedisplay()
   glutTimerFunc(refresh, Timer, 0)

if __name__ == '__main__':

   glutInit(sys.argv)
   glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
   glutInitWindowSize (screenWidth, screenHeight)
   glutCreateWindow('Bouncing Ball')
   init()
   glutReshapeFunc(reshape)
   glutDisplayFunc(display)
   glutTimerFunc(0, Timer, 0)
   glutKeyboardFunc(BouncingBallController.keyEvent)
   glutSpecialFunc(BouncingBallController.specialKeyEvent)
   glutMouseFunc(BouncingBallController.onClick)
   BouncingBallModel.addObjects('glutSolidSphere', [0,0,0], 0, [0.0,0.1,0])

   print "Instructions:"
   print "~ To pause or restart the ball press the space bar"
   print "~ To decrease the speed in the x direction, press the left arrow"
   print "~ To increase the speed in the x direction, press the right arrow"
   print "~ To increase the speed in the y direction, press the up arrow"
   print "~ To decrease the speed in the x direction, press the down arrow"
   glutMainLoop()
   #

