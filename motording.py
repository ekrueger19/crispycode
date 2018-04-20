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
    print x
    y = 2000
    y = y - 100
    print y
    RPL.servoWrite(lala, x)
    RPL.servoWrite(falala, y)
while raw_input("> ") == "c":
    food = x
    food = food + 50
    print food
    ugh = y
    ugh = ugh - 50
    print ugh
    RPL.servoWrite(lala, food)
    RPL.servoWrite(falala, ugh)
