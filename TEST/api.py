#!/Python27/python.exe
from naoqi import *
tts = ALProxy("ALTextToSpeech", "169.254.189.104", 9559)
tts.say("Hello, world!")