import setup
import RoboPiLib as RPL
import time

motorR = 2
motorL = 0

while True:
    while RPL.digitalRead(16) == 1:
        RPL.servoWrite(motorL, 1000)
        RPL.servoWrite(motorR, 2000)
        print "nothing"

    while RPL.digitalRead(16) == 0:
        RPL.servoWrite(motorL, 500)
        RPL.servoWrite(motorR, 500)
