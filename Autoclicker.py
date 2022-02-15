import math
import random
import time
from tokenize import String
from turtle import delay
import pyautogui as mouse

maxRandPos = 10
print("pon el numero de clicks aca")
totalClicks = int(input())
print("minutos pa demoraste")
totalTime = int(input())*60
timePerClick = totalTime/totalClicks
(2)

x,y = mouse.position()
print("x: " + str(x) + " y: " + str(y))
for i in range(totalClicks):
    mouse.moveTo(x + maxRandPos * ((random.random()-0.5) * 2), y + maxRandPos * ((random.random()-0.5) * 2) )
    # mouse.moveTo(x,y)
    mouse.click()
    time.sleep(timePerClick + (random.random()-0.5) * 0.01)
