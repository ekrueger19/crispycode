import setup
import RoboPiLib as RPL

#tunes the motres

falala = 2
lala = 0
toodledoo = 100
dingywink = 2000

RPL.servoWrite(lala, dingywink)
RPL.servoWrite(falala, toodledoo)

while raw_input("> ") == "a":
    RPL.servoWrite(lala, toodledoo)
    RPL.servoWrite(falala, dingywink)
    print "fast"
while raw_input("> ") == "b":
    RPL.servoWrite(lala, 600)
    RPL.servoWrite(falala, 1500)
    print "slow"
while raw_input("> ") == "c":
    RPL.servoWrite(lala, 700)
    RPL.servoWrite(falala, 1400)
    print "slow backwards"
while raw_input("> ") == "d":
    RPL.servoWrite(lala, 1000)
    RPL.servoWrite(falala, 1000)
    print "fast backwards"
while raw_input("> ") == "q":
    RPL.servoWrite(lala, 0)
    RPL.servoWrite(falala, 0)
    print "done"
continue
