from random import random
import scipy.io
import os
import matplotlib.pyplot as plt
import numpy as np
import serial
import time
'''
a function
input: matrice 1 * n
scale all data between 0 to 255
output: matrice 1 * n
'''

def scale(signal):
    # min = 0
    mx = float(max(signal))
    signal = abs(signal)
    ret = []
    for sig in signal:
        ret.append((float(sig) / mx) * 255)
    return ret

# note that you should pass a valid integer
def sandewich(x):
    x = float(x) / 127.0
    if x <= 1:
        return int(x * 25) + 65
    else: 
        x = x - 1
        return int(x * 25) + 97

'''
input : An array of (0, 255)

output : An array of [65, 90] + [97, 122]
'''
def toString(signal):
    ret = ""
    # signal = signal / 2
    for sig in signal:
        if sig < 130:
            ret = ret + chr(int(sig / 5) + 65)
        else:
            ret = ret + chr(int(sig / 5) + 71)
    return ret

def randomChoose(signal, part):
    ln = len(signal)
    ln /= part
    ln = int(ln)
    ret = []
    for i in range(0, ln):
        ret.append(signal[i * 200 + int(random()) % 200])
    return ret




file_name = "cheers.wav"

file_path = os.path.join("", file_name)

sr, signal = scipy.io.wavfile.read(file_path)
time = len(signal) / sr
y = scale(signal)

y = randomChoose(y, 200)
# sr /= 200
# t = np.arange(len(y)) / float(sr)
# arrange(3) / sr = [1 / sr, 2 / sr, 3 / sr]
# show on the plot
'''
plt.figure()
plt.plot(t, y)
plt.show()
'''

# sending nhe data to the arduino

sent = toString(y)
print(sent)
com = serial.Serial("COM3", 9600)
com.timeout = 1
com.write(sent.encode())
'''
for sig in y:
    sent = str(int(sig)) + ','
    com.write(sent.encode())
    time.sleep(.9)
    #print(com.readline().decode("ascii"))
    print(sig)
'''
com.close()