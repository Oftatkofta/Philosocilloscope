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
MR = GPIO18, 12; Master Clear, active low
DS = GPIO17, 11; Serial data input
OE = GPIO27, 13; Output Enable, active low
ST_CP = GPIO22, 15; latch
SH_CP = GPIO4, 7; clock
"""
if not dryrunFlag:
    GPIO.setmode(GPIO.BOARD)
    masterResetPin = 12
    outputEnablePin = 13
    serialDataPin = 11
    latchPin = 15
    clockPin = 7
    GPIO.setwarnings(False) #For ease of debugging
    GPIO.setup(masterResetPin, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(outputEnablePin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup([serialDataPin, latchPin, clockPin], GPIO.OUT, initial=GPIO.LOW)
    channels_in_use = [masterResetPin, outputEnablePin, serialDataPin, latchPin, clockPin]

def latch():
    GPIO.output(latchPin, 1)
    GPIO.output(latchPin, 0)

def shiftOut(Point):
    """
    Sends point coodinates out to an 8-bit DAC. X as high byte, Y as low byte.

    Args:
        Point: Point object

    Returns: None

    """
    x=Point.get_constrained_x()
    y=Point.get_constrained_y()
    binary_representation = bin(x)[2:].zfill(8)+bin(y)[2:].zfill(8)



    print("shifting: ", binary_representation)
    for bit in binary_representation:
        GPIO.output(clockPin, 1)
        GPIO.output(serialDataPin, int(bit))
        GPIO.output(clockPin, 0)
    latch()



    #time.sleep(15)



#print GPIO.RPI_INFO

def funkyFunction(npoints):
    p0 = Point(0,0)
    p1 = Point(0,255)
    p2 = Point(255, 255)
    p3 = Point(255, 0)

    p4 = Point(0,127)
    p5 = Point(127,255)
    p6 = Point(255, 127)
    p7 = Point(127,0)


    l1 = Line(p1,p2,npoints)
    l2 = Line(p0,p3,npoints)
    l3 = Line(p0,p1,npoints)
    l4 = Line(p3,p2,npoints)

    l=l1+l2+l3+l4

    return l

square = funkyFunction(20)

for i in range(10000):
    for p in square.get_points():
        shiftOut(p)
        time.sleep(0.001)

if not dryrunFlag:
    print("Cleaning up GPIO")
    GPIO.cleanup(channels_in_use)
