import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now

motor = 0

right = 17
front = 16
left = 19

lgo = 100
lslow = 600


doit = raw_input("> ")

while True:
    doit = raw_input("> ")
    if doit = "a"
        RPL.servoWrite(0,800)
    if doit = "d"
        RPL.servoWrite(0,3000)
