import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now

motorR = 2
motorL = 0
# lsens = 23
# fsens = 16

# motorR forward = 1000
# motorL forward = 2000


# Okay so this is good but I think we need to do a thing to actually make it...
# ...turn into a gap because right now it's just turning away from a wall

RPL.servoWrite(motorR,2000)
RPL.servoWrite(motorL,100)

while RPL.digitalRead(23) == 0:
  RPL.servoWrite(motorR,2000)
  RPL.servoWrite(motorL,100)
  print "--------"
  if RPL.digitalRead(23) == 1:
     RPL.servoWrite(motorR,2000)
     RPL.servoWrite(motorL,0)
     future = time.time() + 2
     RPL.servoWrite(motorR,2000)
     RPL.servoWrite(motorL,0)
     print "gap"
     if time.time() > future:
         RPL.servoWrite(motorR, 2000)
         RPL.servoWrite(motorL, 100)
         print "!!!!!!!!"
