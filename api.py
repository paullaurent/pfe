#!C:\Python27\python.exe
#!/usr/bin/env python
from naoqi import *
import cgi,cgitb
cgitb.enable()
import sys
print "Content-type: text/html\n\n"
print
#sys.path.append('C:/Python27/Lib/site-packages')
postureProxy = ALProxy("ALFaceDetection", "192.168.43.177", 9559)
postureProxy.learnFace("Paul")
