import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now
close = RPL.digitalRead(16)
motorL = 0
motorR = 2

RPL.servoWrite(0, 1000)
RPL.servoWrite(2, 2000)

while True:
    future = time.time() + 1
    while RPL.digitalRead(16) == 0:
        while time.time() < future:
            RPL.servoWrite(motorL, 1000)
            RPL.servoWrite(motorR, 2000)
        while time.time() >= future:
            RPL.servoWrite(motorR, 0)
            RPL.servoWrite(motorL, 0)
    while RPL.digitalRead(16) == 1:
        RPL.servoWrite(0, 1000)
        RPL.servoWrite(2, 2000)
