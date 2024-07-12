import serial
import time

com = serial.Serial("COM3", 9600)
com.timeout = 1

#while True:
i = input("Type on to turn the light on and off to turn the light off: \n").strip()
if i == "done":
    print("tamaam")
    #break
com.write(i.encode())
time.sleep(0.5)

com.close()