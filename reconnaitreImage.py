#!C:\Python27\python.exe
#!/usr/bin/env python
#-*- coding: utf-8 -*-
import cgi,cgitb
cgitb.enable()
import sys
from naoqi import ALProxy
import os
import time


count=1
res=""
period = 2
moduleName = "pythonModule"
NAO_IP = "192.168.43.116"  # Replace here with your NaoQi's IP address.
PC_IP = "192.168.43.113"   # Replace here with your computer IP address
PORT = 9559
memValue = "PictureDetected" # ALMemory variable where the ALVisionRecognition module outputs its results.


# create python module
class myModule(ALModule):
  """python class myModule test auto documentation"""

  def pictureChanged(self, strVarName, value, strMessage):
    """callback when data change"""
    global count
    count = count-1
    global res
    res=value[1][0][0][0]
    #return value

broker = ALBroker("pythonBroker", PC_IP,9999, NAO_IP,9559)
pythonModule = myModule(moduleName)

# Create a proxy to ALMemory
try:
  memoryProxy = ALProxy("ALMemory", NAO_IP, PORT)
except RuntimeError,e:
  print "Error when creating ALMemory proxy:"
  exit(1)


# Have the python module called back when picture recognition results change.
try:
  memoryProxy.subscribeToEvent(memValue, moduleName, "pictureChanged")
  
except RuntimeError,e:
  print "Error when subscribing to micro event"
  exit(1)


# Let the picture recognition run for a little while (will stop after 'count' calls of the callback).
# You can check the results using a browser connected on your Nao, then
# Advanced -> Memory -> type PictureDetected in the field
while count>0:
  time.sleep(1)


# unsubscribe modules
memoryProxy.unsubscribeToEvent(memValue, moduleName)
#recoProxy.unsubscribe(moduleName)
managerProxy = ALProxy("ALTextToSpeech", NAO_IP, 9559)        
managerProxy.say("c\'est un" + res)