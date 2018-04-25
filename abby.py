import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now


# MAKE A CODE!
# input a Password
#

lock = 800
step1 = 1300
step2 = 1700
unlock = 3000
donde = 1

# idea- make it so that if you get it wrong you go back, not just end

while True:
    RPL.servoWrite(0,lock)
    donde = 1
    print "Do you want to unlock a safe? Riddle me this:"
    print "Why don't you like sand?"

    if donde == 1:
        one()
    if donde == 2:
        two()
    if donde == 3:
        three()

    def one():
        p1 = raw_input("> ")
        if p1 == "course":
            RPL.servoWrite(0,step1)
            donde = donde + 1
        elif p1 == "You're going down a path I can't follow":
            print "Ironic."
            break
        else:
            RPL.servoWrite(0,lock)
            print "It's over Anakin"
            donde = 1

    def two():
        p2 = raw_input("> ")
        if p2 == "rough":
            RPL.servoWrite(0,step2)
            donde = donde + 1
        else:
            RPL.servoWrite(0,lock)
            print "It's over Anakin"
            donde = 1

    def three():
        p3 = raw_input("> ")
        if p3 == "irritating":
            RPL.servoWrite(0,unlock)
            print "General Kenobi, you are a bold one."
            break
        else:
            RPL.servoWrite(0,lock)
            print "It's over Anakin"
            donde = 1
