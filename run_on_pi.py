from __future__ import print_function
try:
    import RPi.GPIO as GPIO
    dryrunFlag = False
except ImportError:
    print('no GPIO, dry run')
    dryrunFlag = True
import time
from coordinate import *

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



    #time.sleep(15)



#print GPIO.RPI_INFO
#reset()
po=Point(0,0)
pt=Point(255,255)
pc=Point(127,127)
l=Shape(po)
for i in xrange(0,1000):
    p1=Point(0,i)
    p2=Point(i,0)
    b=Bezier(po,p1,p2,pt,19)
    l+=b
for p in l.get_points():
    shiftOut(p)
        #time.sleep(0.01)

#reset()
#s=imageToShape("testimage.tif")
#for p in s.get_points():
#    shiftOut(p)

if not dryrunFlag:
    print("Cleaning up GPIO")
    GPIO.cleanup(channels_in_use)
