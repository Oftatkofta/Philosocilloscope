from __future__ import print_function
try:
    import wiringpi
    dryrunFlag = False
except ImportError:
    print('no GPIO, dry run')
    dryrunFlag = True
import time
from shapes import *

"""
MR = GPIO18, pin12; Master Clear, active low
DS = GPIO17, pin11; Serial data input
OE = GPIO27, pin13; Output Enable, active low
ST_CP = GPIO22, pin15; latch 22pF ceramic capacitor to GND
SH_CP = GPI23, pin16; clock

"""
if not dryrunFlag:
    wiringpi.wiringPiSetup() #physical pin numbering
    masterResetPin = 12
    outputEnablePin = 13
    serialDataPin = 11
    latchPin = 15
    clockPin = 16
    channels_in_use = [masterResetPin, outputEnablePin, serialDataPin,
                       latchPin, clockPin]

    for channel in channels_in_use:
        wiringpi.pinMode(channel, 1)  # Set pins to 1 ( OUTPUT )
        wiringpi.digitalWrite(channel, 0)

    wiringpi.digitalWrite(masterResetPin, 1)

def latch():
    wiringpi.digitalWrite(latchPin, 1)
    wiringpi.digitalWrite(latchPin, 0)

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

    for bit in binary_representation:
        wiringpi.digitalWrite(serialDataPin, int(bit))
        wiringpi.digitalWrite(clockPin, 1)

        wiringpi.digitalWrite(clockPin, 0)

    latch()

def shiftShape(shape):
    for p in shape.get_points():
        shiftOut(p)

p0=Point(0,0)
p1=Point(0,255)
p2=Point(255,255)
p3=Point(255,0)
pc=Point(127,127)
l=Shape(pc)

ppl=9
try:
    l=Line(p0, p1, ppl)
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

except KeyboardInterrupt:
    print("Exiting...")
