#!C:\Python27\python.exe
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgi
import cgitb
cgitb.enable()

print "Content-Type: text/plain;charset=utf-8"
print

from naoqi import ALProxy
import time
import sys
def main(robotIP, behaviorName,nbObjets,masculin,nomObjet):
  # Create proxy to ALBehaviorManager

    #speechProxy = ALProxy("ALTextToSpeech", robotIP, 9559)
    managerProxy = ALProxy("ALBehaviorManager", robotIP, 9559)
    launchAndStopBehavior(managerProxy, behaviorName)
    defaultBehaviors(managerProxy, behaviorName)
    managerProxy = ALProxy("ALTextToSpeech", robotIP, 9559)
    
    if (nbObjets==0):
        if masculin:
            managerProxy.say("Un"+ nomObjet)
        else:
            managerProxy.say("Une"+ nomObjet)
    else:
        managerProxy.say(str(nbObjets)+ nomObjet)
        
    
        
  
  

def getBehaviors(managerProxy):
  ''' Know which behaviors are on the robot '''

  names = managerProxy.getInstalledBehaviors()
  print "Behaviors on the robot:"
  print names

  names = managerProxy.getRunningBehaviors()
  print "Running behaviors:"
  print names

def launchAndStopBehavior(managerProxy, behaviorName):
  ''' Launch and stop a behavior, if possible. '''

  # Check that the behavior exists.
  if (managerProxy.isBehaviorInstalled(behaviorName)):

    # Check that it is not already running.
    if (not managerProxy.isBehaviorRunning(behaviorName)):
      # Launch behavior. This is a blocking call, use post if you do not
      # want to wait for the behavior to finish.
      managerProxy.post.runBehavior(behaviorName)
      time.sleep(0)
    else:
      print "Behavior is already running."

  else:
    print "Behavior not found."
    return

  names = managerProxy.getRunningBehaviors()
  print "Running behaviors:"
  print names

  # Stop the behavior.
  if (managerProxy.isBehaviorRunning(behaviorName)):
    managerProxy.stopBehavior(behaviorName)
    time.sleep(1.0)
  else:
    print "Behavior is already stopped."

  names = managerProxy.getRunningBehaviors()
  print "Running behaviors:"
  print names

def defaultBehaviors(managerProxy, behaviorName):
  ''' Set a behavior as default and remove it from default behavior. '''

  # Get default behaviors.
  names = managerProxy.getDefaultBehaviors()
  print "Default behaviors:"
  print names

  # Add behavior to default.
  managerProxy.addDefaultBehavior(behaviorName)

  names = managerProxy.getDefaultBehaviors()
  print "Default behaviors:"
  print names

  # Remove behavior from default.
  managerProxy.removeDefaultBehavior(behaviorName)

  names = managerProxy.getDefaultBehaviors()
  print "Default behaviors:"
  print names


if __name__ == "__main__":
    form = cgi.FieldStorage()
    IPNAO =  form.getvalue('IPNAO')
    nbObjets=form.getvalue('nbObjets')
    nomObjet=form.getvalue('nomObjet')
    if form.getvalue('masculin')=="true":
      masculin=True
    else:
      masculin=False
    main(IPNAO,"Stand/Gestures/CountOne_1",nbObjets,masculin,nomObjet)
    if (len(sys.argv) < 3):
        print "Usage python albehaviormanager_example.py robotIP behaviorName"
    sys.exit(1)

    main(sys.argv[1],sys.argv[2])