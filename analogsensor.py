# analog

import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now

motorL = 0
motorR = 2

right = 17
front = 16
left = 19

analogR = 5

rgo = 2000
lgo = 1000

while True:
    print RPL.analogRead(analogR)

#    if RPL.analogRead(analogR) > 300:
#        print "ay"
