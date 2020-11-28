import RPi.GPIO as GPIO
import time
import numpy as np

servoPin=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin,GPIO.OUT)

servo=GPIO.PWM(servoPin,50) #Servo con Pulse Cycle 20 ms=50Hz
servo.start(12)

#try:
    #while True:
"""
pulse=np.arange(12,0.5,-0.5)
for i in pulse:
    servo.ChangeDutyCycle(i)
    time.sleep(0.5)
    grado=180/11*(i-1)
    print(grado)
for i in np.flip(pulse):
    servo.ChangeDutyCycle(i)
    time.sleep(0.5)
    grado=180/11*(i-1)
    print(grado)
servo.stop()

"""
while True:
    grado=float(input("Ingrese angulo del servo: "))
    pulso=grado*11/180+1
    
    servo.ChangeDutyCycle(pulso)


"""
except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()
"""
    