import setup
import RoboPiLib as RPL
import time
from PIL import image

def picture(x1, x2):
    if x1 > x2:
        RPL.servoWrite(0, 0)
    if x1 < x2:
        RPL.servoWrite(2, 0)
    else:
        RPL.servoWrite(1, 0)

while True:
    wget -o http://192.168.21.181/jpg/image.jpg
    im = image.open("http://192.168.21.181/jpg/image.jpg")
    pix_val = list(m.getdata())
    pix_val_flat = [x for sets in pix_val for x in sets]

x1 = location of the most different pixel pair on top
x2 = location of the most different pixel pair on bottom

pix1 = most different pixel pair on top
pix2 = most different pixel pair on top
