
from __future__ import print_function
import wiringpi as wiringpi
import time
from shapes import *

"""
MR = GPIO18, pin12; Master Clear, active low
DS = GPIO17, pin11; Serial data input
OE = GPIO27, pin13; Output Enable, active low
ST_CP = GPIO22, pin15; latch 22pF ceramic capacitor to GND
SH_CP = GPI23, pin16; clock

"""
GPIOflag = True

if not GPIOflag:
    print("Using physical pin numbers")
    wiringpi.wiringPiSetup() #physical pin numbering
    masterResetPin = 12
    outputEnablePin = 13
    serialDataPin = 11
    latchPin = 15
    clockPin = 16

if GPIOflag:
    print("Using GPIO pin numbers")
    wiringpi.wiringPiSetupGpio()
    masterResetPin = 18
    outputEnablePin = 27
    serialDataPin = 17
    latchPin = 22
    clockPin = 23

channels_in_use = [masterResetPin, outputEnablePin, serialDataPin, latchPin, clockPin]

for channel in channels_in_use:
    wiringpi.pinMode(channel, 1)  # Set pins to OUTPUT
    wiringpi.digitalWrite(channel, 0)
    print("channel: ", channel, " set up.")

def reset():
   wiringpi.digitalWrite(masterResetPin, 1)
   wiringpi.delay(1)
   wiringpi.digitalWrite(masterResetPin, 1)

def latch():
    wiringpi.digitalWrite(latchPin, 1)
    #time.sleep(0.01)
    #wiringpi.delayMicroseconds(10)
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
        wiringpi.delayMicroseconds(10)
        wiringpi.digitalWrite(clockPin, 1)
        wiringpi.digitalWrite(clockPin, 0)

    latch()

def shiftShape(shape):
    for p in shape.get_points():
        shiftOut(p)

def shiftShape2(shape):
    for p in shape.get_points():
        shiftOut2(p)

def shiftOut2(Point):
    x=Point.get_constrained_x()
    y=Point.get_constrained_y()
    wiringpi.shiftOut(serialDataPin,clockPin,1,y)
    wiringpi.shiftOut(serialDataPin,clockPin,1,x)
    latch()

reset()


p0=Point(0,0)
p1=Point(0,255)
p2=Point(255,255)
p3=Point(255,0)
pc=Point(127,127)
l=Shape(pc)

ppl=100
try:
    print("In the main loop...")
    l=Line(p0, p1, ppl)
    l+=Line(p1, p2, ppl)
    l+=Line(p2, p3, ppl)
    l+=Line(p3, p0, ppl)
    l+=Line(p0, p2, ppl)
    l+=Line(p1, p3, ppl)
    while True:
        #for i in xrange(0, 256):
        #    shiftOut2(Point(i,i))
        #    l+=s
        shiftShape2(l)
        #shiftShape2(l)

except KeyboardInterrupt:
    wiringpi.digitalWrite(outputEnablePin, 1)
    reset()
    print("Exiting...")
