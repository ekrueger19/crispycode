import setup
import RoboPiLib as RPL

#tunes the motres

lala = 2
falala = 0
toodledoo = 100
dingywink = 2000

RPL.servoWrite(lala, dingywink)
RPL.servoWrite(falala, toodledoo)

while raw_input("> ") == "a":
    RPL.servoWrite(lala, dingywink)
    RPL.servoWrite(falala, toodledoo)
    print "fast"
while raw_input("> ") == "b":
    x = 100
    x = x + 100
    y = 2000
    y = y - 100
    RPL.servoWrite(lala, x)
    RPL.servoWrite(falala, y)
