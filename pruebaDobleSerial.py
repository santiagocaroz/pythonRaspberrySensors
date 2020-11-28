import serial
psoc=serial.Serial("/dev/ttyACM0",9600)
arduino=serial.Serial("/dev/ttyACM1",9600)
pc=serial.Serial("/dev/ttyS0",9600,timeout=1)
while True:
    instruction=psoc.read(5).decode()
    pc.write(("psoc: "+instruction+"\r\n").encode())
    print("psoc: "+instruction)
    instruction2=arduino.read(4).decode()
    print("arduino: "+instruction2)
    pc.write(("arduino: "+instruction2+"\r\n").encode())
    
