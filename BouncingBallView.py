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
   light_ambient = [1.0, 0.0, 1.0, 1.0] #RGBA values
   light_diffuse = [1.0, 0.0, 0.0, 1.0]
   light_specular = [1.0, 1.0, 1.0, 1.0]
   # light_position is NOT default value
   light_position = [1.0, 1.0, 1.0, 0.0] #x , y, z postion of the light source and last is the movement of the light source.

   glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient) #light, pname, param
   glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
   glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
   glLightfv(GL_LIGHT0, GL_POSITION, light_position)

   glEnable(GL_LIGHTING) #prepare OpenGL to perform lighting calculations
   glEnable(GL_LIGHT0) #To enable lights from a single source
   glEnable(GL_DEPTH_TEST) #to enable a write to the depth buffer (z-buffer)

def display():
   global time

   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #clear buffer to preset values

   glLoadIdentity() #replaces the current matrix with the identity matrix

   spherePos = BouncingBallModel.updateObject('glutSolidSphere',time)

   glPushMatrix() #pushes the current matrix stack down by one, duplicating the current matrix.
   glTranslatef(spherePos[0], spherePos[1], spherePos[2]) # produces a translation by (x, y, z )
   glutSolidSphere(radius, 40, 40) #(radius, slices and stack)
   glPopMatrix() #pop the current matrix stack

   glutSwapBuffers() #swaps the buffers of the current window if double buffered

   glFlush() #force execution of GL commands in finite time
   time = time + .25
   if spherePos[1]<=-9:
      time=0
   print time/10

def reshape(w, h):
   global left,right,bottom,top

   glViewport(0, 0, w, h) #specifies the affine transformation of x and y from normalized device coordinates to window coordinates, (x,y,w,h)
   glMatrixMode (GL_PROJECTION)  #changes the current matrix to the projection matrix
   glLoadIdentity() #replaces the current matrix with the identity matrix

   if w > h:
      left = -20
      right = 20
      bottom = -20 * h/w
      top = 20 * h/w
   else:
      left = 20 * w/h
      right = 20 * w/h
      bottom = -20
      top = 20

   glOrtho(left,right,bottom,top, -10.0, 10.0) #multiply the current matrix with an orthographic matrix, (left,rifht,bottom,top,nearVal,farVal)

   BouncingBallModel.setScreenBoundries(left + radius, right - radius, bottom + radius, top - radius)  # check the boundary
   glMatrixMode(GL_MODELVIEW) #specify which matrix is current matrix
   glLoadIdentity() #replaces the current matrix with the identity matrix

def Timer(value):
   glutPostRedisplay() #marks the current window as needing to be redisplayed
   glutTimerFunc(refresh, Timer, 0) #registers a timer callback to be triggered in a specified number of milliseconds.

if __name__ == '__main__':

   glutInit(sys.argv)
   glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH) # double buffer window, rgb color mode, window with a depth buffer
   glutInitWindowSize (screenWidth, screenHeight) #initialize the size of the display window
   glutCreateWindow('Bouncing Ball') # Name of the display window
   init() # init method call to set up the lighting effect
   glutReshapeFunc(reshape) #sets the reshape callback for the current window
   glutDisplayFunc(display) #sets the display callback for the current window
   glutTimerFunc(0, Timer, 0) #registers a timer callback to be triggered in a specified number of milliseconds. ,( unsigned int msecs,void (*func)(int value), value)
   glutKeyboardFunc(BouncingBallController.keyEvent) #keyboard event reader
   glutSpecialFunc(BouncingBallController.specialKeyEvent) #arrows keys event reader to control the ball movement
   glutMouseFunc(BouncingBallController.onClick) #mouse event reader
   #glutPassiveMotionFunc(BouncingBallController.onClick)
   BouncingBallModel.addObjects('glutSolidSphere', [0,0,0], 0, [0.0,0.1,0])

   print "Instructions:"
   print "~ To pause or restart the ball press the space bar"
   print "~ To decrease the speed in the x direction, press the left arrow"
   print "~ To increase the speed in the x direction, press the right arrow"
   print "~ To increase the speed in the y direction, press the up arrow"
   print "~ To decrease the speed in the x direction, press the down arrow"
   print "~OR USE YOUR MOUSE POINTER CLICK TO MANIPULATE THE REBOUND DIRECTION"
   glutMainLoop() #enters the GLUT event processing loop. This routine should be called at most once in a GLUT program.

