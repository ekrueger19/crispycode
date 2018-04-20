import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now

doit = raw_input("> ")

while True:
    doit = raw_input("> ")
    if doit == "a":
        RPL.servoWrite(0,800)
    if doit == "d":
        RPL.servoWrite(0,3000)
