import RPi.GPIO as GPIO
import time
import numpy as np
import serial
import Adafruit_ADS1x15
pc=serial.Serial("/dev/ttyACM0",9600)

#Inicialización Servo
servoPin=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin,GPIO.OUT)
servo=GPIO.PWM(servoPin,50) #Servo con Pulse Cycle 20 ms=50Hz
servo.start(12)

#Inicialización ADC
adc=Adafruit_ADS1x15.ADS1115()
GAIN=1#Para leer valores entre 0 y 4.095V


while True:
    
    instruction=pc.read().decode() #Lectura de la instrucción deseada
    #print(instruction)
    
    if (instruction=="M"):
        grado=pc.read(3).decode()
        print("Grado: "+grado)
        pulso=int(grado)*11/180+1
        servo.ChangeDutyCycle(pulso)
   
    elif(instruction=="A"):
        valueADC=adc.read_adc(0,gain=GAIN)
        angle=valueADC
        pc.write(str(int(angle/100%10)).encode())
        pc.write(str(int(angle/10%10)).encode())
        pc.write(str(int(angle/1%10)).encode())
        print("ADC: "+pc.read(5).decode())
        
    elif(instruction=="F"):
        valueADC2=adc.read_adc(2,gain=GAIN)
        flex=valueADC2
        pc.write(str(int(flex/10000%10)).encode())
        pc.write(str(int(flex/1000%10)).encode())
        pc.write(str(int(flex/100%10)).encode())
        pc.write(str(int(flex/10%10)).encode())
        pc.write(str(int(flex/1%10)).encode())
        
        print("Flex: "+pc.read(5).decode())
        
        


