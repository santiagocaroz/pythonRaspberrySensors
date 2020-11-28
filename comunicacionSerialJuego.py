# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 21:49:01 2020

@author: Santiago Caro
"""

import RPi.GPIO as GPIO
import time
import numpy as np
import serial
import Adafruit_ADS1x15

pc=serial.Serial("/dev/ttyACM0",9600)
vel=0
flex=0
ang=0

#Inicializacion servo
servoPin=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin,GPIO.OUT)
servo=GPIO.PWM(servoPin,50) #Servo con Pulse Cycle 20 ms=50Hz
servo.start(12)

#Inicialización ADC
adc=Adafruit_ADS1x15.ADS1115()
GAIN=1#Para leer valores entre 0 y 4.095V


while True:
    instruction=pc.read().decode()
    print(instruction)
    valueADC=adc.read_adc(0,gain=GAIN)
    
    if (instruction=="S"):
        vel+=31
        flex+=37
        ang=int(valueADC*240/26368)
        pc.write(("V"+str(len(str(vel)))+str(vel)+"A"+str(len(str(ang)))+str(ang)+"F"+str(len(str(flex)))+str(flex)+"/").encode())
        
        
    elif(instruction=="M"):
        grado=pc.read(3).decode()
        print("Grado: "+grado)
        pulso=int(grado)*11/180+1
        #pc.write("Y".encode())
        servo.ChangeDutyCycle(pulso)
        
# instruction=pc.read().decode()
# print(instruction)

# if (instruction=="S"):
#     vel+=111
#     flex+=37
#     cad+=123
#     # pc.write(("V"+len(str(vel))+str(vel)+"F"+len(str(flex))+str(flex)+"C"+len(str(cad))+str(cad).encode()))
#     pc.write(("V"+str(len(str(vel)))+str(vel)).encode())

# while True:
#     print(pc.read().decode())