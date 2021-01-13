# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 13:52:38 2020

@author: SantiagoCaroZ
"""
import time
import RPi.GPIO as GPIO
pin_velocidad=27
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_velocidad,GPIO.IN)

time_start=time.time()
TIME=[]
VEL=[]
radio=1 #metros
numero_huecos=6
angulo=360/numero_huecos
i=0
while True:
    GPIO.wait_for_edge(pin_velocidad,GPIO.RISING)
    i+=1
    print(i)
    pulso=GPIO.input(pin_velocidad)
    
#     pulso=int(input("p:"))# CAMBIAR POR 
#     if (pulso==0):
#         TIME.append(time.time()-time_start)
#         if (len(TIME)>=10):
#             TIME.pop(0)
#     
#         if(len(TIME)>=2):
#             for i in range(len(TIME)-1):
#                 dt=TIME[i+1]-TIME[i]
#                 VEL.append(angulo/dt)
#                 if (len(VEL)>=10):
#                     VEL.pop(0)
#         
#             vel=sum(VEL)/len(VEL)*radio
#             print(vel)
            
   