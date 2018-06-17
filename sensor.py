#this code is good if the digital sensors are set up to measure the blind spots
# of the camera
import RoboPiLib as RPL
import setup
import time

#setting up pins
fr =
bl =
fl =
br =

while True:
    while RPL.digitalRead(fr) == 1:
        print " - "
        if RPL.digitalRead(fr) == 0:
            print "something in front right"
    while RPL.digitalRead(fr) == 0:
        print "something in front right"
        if RPL.digitalRead(fr) == 1:
            print " - "
    while RPL.digitalRead(fl) == 1:
        print " - "
        if RPL.digitalRead(fl) == 0:
            print "something in front left"
    while RPL.digitalRead(fl) == 0:
        print "something in front left"
        if RPL.digitalRead(fl) == 1:
            print " - "
    while RPL.digitalRead(bl) == 0:
        print "something in back left"
        if RPL.digitalRead(bl) == 1:
            print " - "
    while RPL.digitalRead(bl) == 1:
        print " - "
        if RPL.digitalRead(bl) == 0:
            print "something in back left"
    while RPL.digitalRead(br) == 1:
        print " - "
        if RPL.digitalRead(br) == 0:
            print "something in back right"
    while RPL.digitalRead(br) == 0:
        print "something in back right"
        if RPL.digitalRead(br) == 1:
            print " - "
