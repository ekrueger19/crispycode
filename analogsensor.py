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
    if RPL.analogRead(analogR) > 300:
        print "so far away"
    if 100 < RPL.analogRead(analogR) <= 300:
        print "very close, or oh so far away..."
    if RPL.analogRead(analogR) <= 100:
        print "there aint nothing"
