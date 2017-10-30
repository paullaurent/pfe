#!C:\Python27\python.exe
#!/usr/bin/env python
from naoqi import *
import cgi,cgitb
cgitb.enable()
import sys
print "Content-type: text/html\n\n"
print
print"""
<html>"""
#sys.path.append('C:/Python27/Lib/site-packages')
form = cgi.FieldStorage()
variable = ""
value = ""

for key in form.keys():
    variable = str(key)
    value = str(form.getvalue(variable))

if value=="hello":
     tts = ALProxy("ALTextToSpeech", "192.168.43.177", 9559)
     tts.say("Hello, world!")

cgi.escape("fin")
print"""
</html>
"""