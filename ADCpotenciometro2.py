import Adafruit_ADS1x15
import time

adc=Adafruit_ADS1x15.ADS1115()
GAIN=1#Para leer valores entre 0 y 4.096
i=1
while i==1:
    value=adc.read_adc(0,gain=GAIN)
    #value1=adc.read_adc(3, gain=GAIN)
    time.sleep(0.5)
    value=240/26368*value-120
    #print(value,value1)
    print(int(value))