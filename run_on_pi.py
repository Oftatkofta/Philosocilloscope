import RPi.GPIO as GPIO

"""
MR = GPOI18; Master Clear, active low
DS = GPIO17; Serial data input
OE = GPIO27; Output Enable, active low
ST_CP = GPIO22; latch
SH_CP = GPIO4; clock
"""

GPIO.setmode(GPIO.BOARD)
masterClearPin = 18
outputEnablePin = 27
serialDataPin = 17
latchPin = 22
clockPin = 4

GPIO.setup(masterClearPin, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(outputEnablePin, GPIO.OUT, initial=GPIO.LOW)

print GPIO.RPI_INFO


GPIO.cleanup()
