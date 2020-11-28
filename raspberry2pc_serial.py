import RPi.GPIO as GPIO
import time
import numpy as np
import serial
import Adafruit_ADS1x15
#pc=serial.Serial("/dev/ttyACM0",9600)
pc=serial.Serial("/dev/ttyS0",9600,timeout=1)
while True:
    pc.write("ok".encode())