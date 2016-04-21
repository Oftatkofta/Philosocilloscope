import RPi.GPIO as GPIO

"""
MR = GPOI18, 12; Master Clear, active low
DS = GPIO17, 11; Serial data input
OE = GPIO27, 13; Output Enable, active low
ST_CP = GPIO22, 15; latch
SH_CP = GPIO4, 7; clock
"""

GPIO.setmode(GPIO.BOARD)
masterClearPin = 12
outputEnablePin = 13
serialDataPin = 11
latchPin = 15
clockPin = 7

GPIO.setup(masterClearPin, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(outputEnablePin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup([serialDataPin, latchPin, clockPin], GPIO.OUT, initial=GPIO.LOW)

#print GPIO.RPI_INFO


GPIO.cleanup()
