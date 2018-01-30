#!C:\Python27\python.exe
#!/usr/bin/env python
#-*- coding: utf-8 -*-
import cgi,cgitb
cgitb.enable()
import sys
import time
from naoqi import ALProxy


def main(robotIP):
    
    postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)


    postureProxy.goToPosture("StandInit", 1.0)


if __name__ == "__main__":
    form = cgi.FieldStorage()
    IPNAO =  form.getvalue('IPNAO')
    if len(sys.argv) <= 1:
        print "Usage python alrobotposture.py robotIP (optional default: 127.0.0.1)"
    else:
        robotIp = sys.argv[1]

    main(IPNAO)