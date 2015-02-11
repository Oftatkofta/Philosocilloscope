
import serial

ser = serial.Serial('/dev/ttyACM3',9600)

def send(bytes):
  byte1 = bytes % 256
  #byte2 = (bytes / 256) %256
  #print byte1,byte2 
  ser.write(chr(byte1))
  #ser.write(chr(byte2))
  return ser.readline()
