#!C:\Python27\python.exe
# -*- encoding: UTF-8 -*-
#!/usr/bin/env python
import cgi,cgitb
cgitb.enable() 
print "Content-Type: text/plain;charset=utf-8"
print

import sys
import almath
import motion
import argparse
import time
from naoqi import ALProxy

def main(robotIP, PORT=9559):
    
    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

    # Wake up robot
    motionProxy.wakeUp()

    # Send robot to Pose Init
    postureProxy.goToPosture("StandInit", 0.5)
    # Example showing how to use positionInterpolations
    frame = motion.FRAME_ROBOT
    useSensorValues = False
    isEnabled = False
    motionProxy.wbEnable(isEnabled)


    # aller vers le sol et prendre le stylo
    axisMaskList = [motion.AXIS_MASK_ALL,motion.AXIS_MASK_ALL,motion.AXIS_MASK_ALL]
    timeList    = [[2.0],
                    [2.0],[2.0]] # seconds

    effectorList = []
    pathList     = []

    effectorList.append("LArm")
    currentPos = motionProxy.getPosition("LArm", frame, useSensorValues)
    targetPos  = almath.Position6D(currentPos)
    targetPos.z -= 0.09
    targetPos.y-=0.1
    targetPos.x+=0.06
    pathList.append(list(targetPos.toVector()))
    
    effectorList.append("Head")
    currentPos = motionProxy.getPosition("Head", frame, useSensorValues)
    targetPos  = almath.Position6D(currentPos)
    targetPos.wy+=0.6
    pathList.append(list(targetPos.toVector()))


    effectorList.append("Torso")
    currentPos = motionProxy.getPosition("Torso", frame, useSensorValues)
    targetPos  = almath.Position6D(currentPos)
    targetPos.z -= 0.06
    targetPos.wy-=0.1
    pathList.append(list(targetPos.toVector()))
    handName  = 'LHand'
    motionProxy.openHand(handName) 
    motionProxy.positionInterpolations(effectorList, frame, pathList,
                                 axisMaskList, timeList)

    motionProxy.closeHand(handName) 
    # se redresser et déposer le stylo
    axisMaskList = [motion.AXIS_MASK_ALL,motion.AXIS_MASK_ALL]
    timeList    = [[2.0],[2.0]] # seconds

    effectorList = []
    pathList     = []
    effectorList.append("Torso")
    currentPos = motionProxy.getPosition("Torso", frame, useSensorValues)
    targetPos  = almath.Position6D(currentPos)
    targetPos.z += 0.06
    pathList.append(list(targetPos.toVector()))

    
    effectorList.append("Head")
    currentPos = motionProxy.getPosition("Head", frame, useSensorValues)
    targetPos  = almath.Position6D(currentPos)
    targetPos.wy-=0.6
    pathList.append(list(targetPos.toVector()))
    
    motionProxy.positionInterpolations(effectorList, frame, pathList,
                              axisMaskList, timeList)

     
    
    #déposer le stylo

    axisMaskList = [motion.AXIS_MASK_ALL,motion.AXIS_MASK_ALL]
    timeList    = [[3.0],[1.0]] # seconds

    effectorList = []
    pathList     = []
    effectorList.append("LArm")
    currentPos = motionProxy.getPosition("LArm", frame, useSensorValues)
    targetPos  = almath.Position6D(currentPos)

    targetPos.x=0
    targetPos.y=0.3
    targetPos.z=0.5
    pathList.append(list(targetPos.toVector()))
    
    effectorList.append("Head")
    currentPos = motionProxy.getPosition("Head", frame, useSensorValues)
    targetPos  = almath.Position6D(currentPos)
    targetPos.wz+=0.6
    pathList.append(list(targetPos.toVector()))
    

    motionProxy.positionInterpolations(effectorList, frame, pathList,
                                 axisMaskList, timeList)
    handName  = 'LHand'
    motionProxy.openHand(handName)


    #Go to rest position
    postureProxy.goToPosture("StandInit", 0.5)

if __name__ == "__main__":

    form = cgi.FieldStorage()
    IPNAO =  form.getvalue('IPNAO')
    main(IPNAO,9559)
    if (len(sys.argv) < 3):
        print "Usage python albehaviormanager_example.py robotIP behaviorName"
    sys.exit(1)

    main(sys.argv[1], sys.argv[2])