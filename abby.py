import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now

doit = raw_input("> ")

# MAKE A CODE!
# input a Password
#

lock = 800
step1 = 1300
step2 = 1700
unlock = 3000

#need: make incriments of openness- p1 will only open a bit and p2 more etc

while True:
    RPL.servoWrite(0,lock)
    print "Do you want to unlock a safe? Riddle me this:"
    print "Why don't you like sand?"

    p1 = raw_input("> ")
    if p1 == "course":
        RPL.servoWrite(0,step1)
    else:
        RPL.servoWrite(0,lock)
        print "It's over Anakin"
        break

    p2 = raw_input("> ")
    if p2 == "rough":
        RPL.servoWrite(0,step2)
    else:
        RPL.servoWrite(0,lock)
        print "It's over Anakin"
        break


    p3 = raw_input("> ")
    if p3 == "irritating":
        RPL.servoWrite(0,unlock)
        print "General Kenobi, you are a bold one."

    else:
        RPL.servoWrite(0,lock)
        print "It's over Anakin"
        break
