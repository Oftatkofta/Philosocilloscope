__author__ = 'jens_e'
import serial
import math
from time import sleep

ser = serial.Serial('/dev/cu.usbmodemfd121',9600,timeout=1)

origo=(127.5,127.5)
radius=128


def coordgen(pointnum, radius, origo):
    for i in range(0,360,360/pointnum):
        alpha=math.radians(i)
        x=int(radius*math.cos(alpha)+origo[0])
        y=int(radius*math.sin(alpha)+origo[1])
        ser.write(str(x)+','+str(y)+',')
        sleep(0.01)

def coordgen2(pointnum, radius, origo):
    for i in range(0,360,360/pointnum):
        alpha=math.radians(i)
        x=int(radius*math.cos(alpha)+origo[0])
        y=int(radius*math.sin(alpha)+origo[1])
        ser.write(bin(x))
        ser.write(bin(y))


coordgen2(15, radius ,origo)
