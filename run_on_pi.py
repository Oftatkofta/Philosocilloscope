from __future__ import print_function
try:
    import RPi.GPIO as GPIO
    dryrunFlag = False
except ImportError:
    print('no GPIO, dry run')
    dryrunFlag = True
import time
from shapes import *
import random

"""
MR = GPIO18, pin12; Master Clear, active low
DS = GPIO17, pin11; Serial data input
OE = GPIO27, pin13; Output Enable, active low
ST_CP = GPIO22, pin15; latch 22pF ceramic capacitor to GND
SH_CP = GPI23, pin16; clock

"""

if not dryrunFlag:
    GPIO.setmode(GPIO.BOARD)
    masterResetPin = 12
    outputEnablePin = 13
    serialDataPin = 11
    latchPin = 15
    clockPin = 16
    GPIO.setwarnings(False) #For ease of debugging
    GPIO.setup(masterResetPin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(outputEnablePin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup([serialDataPin, latchPin, clockPin], GPIO.OUT, initial=GPIO.LOW)
    channels_in_use = [masterResetPin, outputEnablePin, serialDataPin, latchPin, clockPin]
    GPIO.output(masterResetPin, 1)

def reset():
    GPIO.output(masterResetPin, 0)
    #time.sleep(0.00001)
    GPIO.output(masterResetPin, 1)
    #GPIO.output(outputEnablePin, 0)

def latch():
    GPIO.output(latchPin, 1)
    #time.sleep(0.001)
    GPIO.output(latchPin, 0)

def shiftOut(Point):
    """
    Sends point coodinates out to an 8-bit DAC. X as high byte, Y as low byte.

    Args:
        Point: Point object

    Returns: None

    """
    #reset()
    x=Point.get_constrained_x()
    y=Point.get_constrained_y()
    binary_representation = bin(x)[2:].zfill(8)+bin(y)[2:].zfill(8)


   
    #print("shifting: ", binary_representation)
    for bit in binary_representation:
        GPIO.output(serialDataPin, int(bit))
        #time.sleep(0.00001)
        GPIO.output(clockPin, 1)
        #time.sleep(0.001)
        #latch()
        #GPIO.output(serialDataPin, int(bit))
        GPIO.output(clockPin, 0)
    
    latch()

def shiftShape(shape):
    for p in shape.get_points():
        shiftOut(p)




#print GPIO.RPI_INFO
#reset()
p0=Point(0,0)
p1=Point(0,255)
p2=Point(255,255)
p3=Point(255,0)
pc=Point(127,127)
l=Shape(pc)
reset()
#for i in xrange(2,255):
    #p1=Point(0,i)
    #p2=Point(i,0)
    #b=Bezier(po,p1,pt,p2, 30)
    #t=Circle(p1, i/2,i)
    #l=b+t
    #t=Square(pc, i/2, i/2, 128)
    #shiftShape(t)
        #time.sleep(0.01)

#reset()
#s=imageToShape("testimage.tif")
#for p in s.get_points():
#    shiftOut(p)
ppl=25
try:
    l=Square(pc,200,200,25)
    l+=Line(p0, p1, ppl)
    l+=Line(p1, p2, ppl)
    l+=Line(p2, p3, ppl)
    l+=Line(p3, p0, ppl)
    l+=Line(p0, p2, ppl)
    l+=Line(p1, p3, ppl)
    
    while True:
        #for i in xrange(2, 256, 4):
        #    s = Square(pc, i, i, (i/16+4))
        #    l+=s 
        shiftShape(l)
        #r=random.randint(126,128)
        #l.translate(Point(r,r))

except KeyboardInterrupt:
    print("Exiting...")
    if not dryrunFlag:
        print("Cleaning up GPIO")
        GPIO.cleanup(channels_in_use)
