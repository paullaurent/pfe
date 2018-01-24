#!C:\Python27\python.exe
# -*- encoding: UTF-8 -*-
#!/usr/bin/env python
print "Content-type: text/html"

print "<html><body></body></html>"
import cgi,cgitb
cgitb.enable()
import sys
import time
from weather import Weather
from naoqi import ALProxy



def main(robotIP, behaviorName):
  # Create proxy to ALBehaviorManager
  managerProxy = ALProxy("ALBehaviorManager", robotIP, 9559)

  getBehaviors(managerProxy)
  launchAndStopBehavior(managerProxy, behaviorName)
  defaultBehaviors(managerProxy, behaviorName)
  managerProxy = ALProxy("ALTextToSpeech", robotIP, 9559)
  weather = Weather()
  location = weather.lookup_by_location('tours')
  condition = location.condition()
  print(condition.text())
  if (condition.text()=="Sunny" or condition.text()=="Clear"):
    phrase="Aujourd'hui il fait trai beau"
  elif(condition.text()=="Cloudy" or condition.text()=="Partly cloudy" or condition.text()=="Mostly cloudy"):
      phrase="Aujourd'hui le ciel est couvert"
  elif(condition.text()=="Showers" or condition.text()=="Scattered showers"):
      phrase="Aujourd'hui il pleut"
  elif(condition.text()=="Windy"):
      phrase="Aujourd'hui il y a beaucoup de vent"
  elif(condition.text()=="Smoky" or condition.text()=="Foggy" ):
      phrase="Aujourd'hui il y a du brouillard"
  else:
      phrase="Aujourd'hui le temps est vraiment incertain"
        
  managerProxy.say(phrase)
  
  

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
    main(IPNAO,"Stand/Gestures/This_2")
    if (len(sys.argv) < 3):
        print "Usage python albehaviormanager_example.py robotIP behaviorName"
    sys.exit(1)

    main(sys.argv[1], sys.argv[2])