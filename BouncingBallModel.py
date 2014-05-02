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
    bottom = b+0.02
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


        #parameters to govern the motion's simulation
        gravity=0.02
        frictionfactor=13
        absorbrebound=0.18
        #print v[0]
        #print y
        #print "bottom="+`bottom`

      #if direction=='up':
        v[1]=v[1]-gravity
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

        elif y < bottom+0.02:
            y = bottom+0.02
            v[1] = -v[1]-absorbrebound
            if v[0]!=0:
                v[0]=v[0]-v[0]/frictionfactor
            else:
                v[0]=0

        #print v[0]

    objects[obj]['position'] = [x,y,z]
    #print objects[obj]['position']

    return objects[obj]['position']
    #
