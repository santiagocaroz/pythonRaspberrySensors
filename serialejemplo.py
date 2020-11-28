# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 11:14:19 2020

@author: SantiagoCaroZ
"""
import serial

pc=serial.Serial("COM7",9600)
vel=0
while True:
    instruction=pc.read().decode()
    #print(instruction)
    
    if (instruction=="M"):    
        #print("Y")
        grado=pc.read(3).decode()
        print("Grado: "+grado)
        
 
    elif(instruction=="A"):
        vel+=2
        pc.write(str(int(vel/100%10)).encode())
        pc.write(str(int(vel/10%10)).encode())
        pc.write(str(int(vel/1%10)).encode())
        
        print("Vel: "+pc.read(3).decode())
        
 
        
        
        