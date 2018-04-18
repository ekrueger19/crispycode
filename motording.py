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
    toodledoo = 100
    toodledoo = toodledoo + 50
    dingywink = 2000
    dingywink = dingywink - 50
    RPL.servoWrite(lala, toodledoo)
    RPL.servoWrite(falala, dingywink)
