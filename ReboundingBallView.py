#!/usr/bin/python

import sys
import ReboundingBallModel
import ReboundingBallController
from OpenGL.GLUT import *
from OpenGL.GL import *

filename='score'
refresh = 30
time = 0
best = 0
screenWidth = 1350
screenHeight = 690
radius = 2
left = 0.0
right = 0.0
bottom = 0.0
top = 0.0
PROMPT='SOME PROMPT'
i=0

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

def score():
   f=open(filename,'rU')
   score=f.read()
   return float(score.split()[0])

def storebest(bestscore):
   f=open(filename,'w')
   print bestscore
   f.write(`bestscore`)

def display():
   global time
   global best
   global i


   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #clear buffer to preset values

   glLoadIdentity() #replaces the current matrix with the identity matrix

   spherePos = ReboundingBallModel.updateObject('glutSolidSphere',time)

   glPushMatrix() #pushes the current matrix stack down by one, duplicating the current matrix.
   glTranslatef(spherePos[0], spherePos[1], spherePos[2]) # produces a translation by (x, y, z )
   glutSolidSphere(radius, 40, 40) #(radius, slices and stack)
   glPopMatrix() #pop the current matrix stack
#####################################################################

#####################################################################

   if i==0:
      best=score()
      print best
      i=i+1
   if ReboundingBallModel.pause==False:
      time = time + .25
   if spherePos[1]<=-8.96:
      if time/10>best:
         best=time/10
         storebest(best)
      time=0

   glClearColor(0.0, 0.0, 0.0, 0.0)
   #glClear(GL_COLOR_BUFFER_BIT)
   glColor4f(1.0, 1.0, 1.0, 0.0)
   #glMatrixMode(GL_PROJECTION)
   #glLoadIdentity()
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()
   glTranslate(-1.0, 1.0, 0.0)
   scale = 0.01
   glScale(scale, -scale*screenWidth/screenHeight,2.0)
   glTranslate(00, 0.0, 0.0)
   y = -400
   x= 1450
   timestr=("current time in air", `time/10` , "best",`best`)

   for s in timestr:
     glRasterPos(x, y)
     y=y+25
     for c in s:
         glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(c))
######################################################################

######################################################################

   glutSwapBuffers() #swaps the buffers of the current window if double buffered

   glFlush() #force execution of GL commands in finite time
   #print time/10
   #print spherePos[1]

def reshape(w, h):
   global left,right,bottom,top

   glViewport(0, 0, w, h) #specifies the affine transformation of x and y from normalized device coordinates to window coordinates, (x,y,w,h)
   glMatrixMode (GL_PROJECTION) #changes the current matrix to the projection matrix
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

   glOrtho(left,right,bottom,top, -100, 100) #multiply the current matrix with an orthographic matrix, (left,rifht,bottom,top,nearVal,farVal)

   ReboundingBallModel.setScreenBoundries(left+ radius , right - radius, bottom + radius, top - radius) # check the boundary
   glMatrixMode(GL_MODELVIEW) #specify which matrix is current matrix
   glLoadIdentity() #replaces the current matrix with the identity matrix

def Timer(value):
   glutPostRedisplay() #marks the current window as needing to be redisplayed
   glutTimerFunc(refresh, Timer, 0) #registers a timer callback to be triggered in a specified number of milliseconds.

if __name__ == '__main__':
   glutInit(sys.argv)
   glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH) # double buffer window, rgb color mode, window with a depth buffer
   glutInitWindowSize (screenWidth, screenHeight) #initialize the size of the display window
   glutCreateWindow('Rebounding Ball') # Name of the display window
   init() # init method call to set up the lighting effect
   glutReshapeFunc(reshape) #sets the reshape callback for the current window
   ReboundingBallModel.addObjects('glutSolidSphere', [0,0,0], 0, [0.0,0.1,0])
   glutDisplayFunc(display) #sets the display callback for the current window
   glutTimerFunc(0, Timer, 0) #registers a timer callback to be triggered in a specified number of milliseconds. ,( unsigned int msecs,void (*func)(int value), value)
   #glutKeyboardFunc(ReboundingBallController.keyEvent) #keyboard event reader
   #glutSpecialFunc(ReboundingBallController.specialKeyEvent) #arrows keys event reader to control the ball movement
   glutMouseFunc(ReboundingBallController.onClick) #mouse event reader
   #glutPassiveMotionFunc(ReboundingBallController.onClick)


   print "Instructions:"
   print "~ To pause or restart the ball press the space bar"
   print "~OR USE YOUR MOUSE POINTER CLICK TO MANIPULATE THE REBOUND DIRECTION"
   print "~stay as long as u can in the air."
   glutMainLoop() #enters the GLUT event processing loop. This routine should be called at most once in a GLUT program.
