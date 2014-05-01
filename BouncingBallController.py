#!/usr/bin/env python

import math
import BouncingBallModel
from OpenGL.GLUT import *

pause = False

def keyEvent(key, x, y):
    #Press the space bar to pause or unpause the boucning ball
    print `x`+"x ho yo"
    if key == chr(32):
        BouncingBallModel.setPause(not BouncingBallModel.pause)


def onClick(button,state, x, y):
    #Press the space bar to pause or unpause the boucning ball
    if button == GLUT_LEFT_BUTTON:
        centerx= BouncingBallModel.objects['glutSolidSphere']['position'][0]
        centery=BouncingBallModel.objects['glutSolidSphere']['position'][1]
        xnew=(x-675)/33.75
        ynew=(333.33-y)/33.75
        print xnew,ynew
        acceleratex=centerx-xnew
        acceleratey=centery-ynew
        testradsquare=acceleratex**2+acceleratey**2
        testradius=math.sqrt(testradsquare)
        print testradius
        if testradius<2:
            BouncingBallModel.changeVelocity('glutSolidSphere',BouncingBallModel.objects['glutSolidSphere']['velocity'][0]+acceleratex/5,0)
            BouncingBallModel.changeVelocity('glutSolidSphere',BouncingBallModel.objects['glutSolidSphere']['velocity'][1]+acceleratey/5,1)



def specialKeyEvent(key,x,y):
    #Left arrow to decrease x velocity
    if key == GLUT_KEY_LEFT:
        BouncingBallModel.changeVelocity('glutSolidSphere', BouncingBallModel.objects['glutSolidSphere']['velocity'][0] - .8, 0)
    #Right arrow to increase x velocity
    elif key == GLUT_KEY_RIGHT:
        BouncingBallModel.changeVelocity('glutSolidSphere', BouncingBallModel.objects['glutSolidSphere']['velocity'][0] + .8, 0)
    #Up arrow to increase y velocity
    elif key == GLUT_KEY_UP:
        BouncingBallModel.changeVelocity('glutSolidSphere', BouncingBallModel.objects['glutSolidSphere']['velocity'][1] + .8, 1)
    #Down arrow to decrease y velocity
    elif key == GLUT_KEY_DOWN:
        BouncingBallModel.changeVelocity('glutSolidSphere', BouncingBallModel.objects['glutSolidSphere']['velocity'][1] - .5, 1)

'''def specialMouseKeyEvent(x,y,centerx,centery,radius):'''

