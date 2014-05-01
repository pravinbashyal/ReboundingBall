#!/usr/bin/env python

import math
import BouncingBallView

objects = {}
left = 0.0
right = 0.0
bottom = 0.0
top = 0.0
pause = False

def addObjects(objName, position, time, velocity):
    obj = {'position':position,'time':time,'velocity':velocity}
    objects[objName] = obj

def setScreenBoundries(l,r,b,t):
    global left,right,bottom,top

    left = l
    right = r
    bottom = b
    top = t

def setPause(p):
    global pause
    pause = p

def changeVelocity(obj, v, dir):
    objects[obj]['velocity'][dir] = v

def updateObject(obj,t):

    # set new time
    objects[obj]['time'] = t

    v = objects[obj]['velocity']
   # print v

    x = objects[obj]['position'][0]
    y = objects[obj]['position'][1]
    z = objects[obj]['position'][2]

    #calculate new position based on velocity
    if not pause:
        x = x + v[0]
        y = y + v[1]
        z = z + v[2]

        #print v[0]
        #print y
        #print "bottom="+`bottom`

      #if direction=='up':
        v[1]=v[1]-0.06
        #print v[1]


        if x > right:
            x = right
            v[0] = -v[0]
        elif x < left:
            x = left
            v[0] = -v[0]

        if y > top:
            y = top
            v[1] = -v[1]
       #     direction='down'

        elif y < bottom:
            y = bottom
            v[1] = -v[1]-0.3
            if v[0]!=0:
                v[0]=v[0]-v[0]/9
            else:
                v[0]=0

    objects[obj]['position'] = [x,y,z]
    print objects[obj]['position']

    return objects[obj]['position']
    #
