#!C:\Python27\python.exe
#!/usr/bin/env python
import sys

from naoqi import ALProxy
from naoqi import *
import cgi,cgitb
import sys
print 'Content-type: text/html'
print 

cgitb.enable()


sys.path.append('C:/Python27/Lib/site-packages')
tts = ALProxy("ALRobotPosture", "192.168.43.177", 9559)
tts.goToPosture("StandInit", 1.0)

