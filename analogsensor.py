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

analogR = 1

rgo = 2000
lgo = 1000

while True:
    while RPL.analogRead(analogR) > 500:
        print "middle"
    while RPL.analogRead(analogR) < 500:
        while RPL.digitalRead(19) == 0:
            print "close"
        while RPL.digitalRead(19) == 1:
            print "far"
