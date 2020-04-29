# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 12:28:39 2020

@author: Ксения
"""


import serial
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
import random



def read_while_LF(com, timeout_ms=500):
    read_data =""
    delay_ms=10
    attempts=int(timeout_ms/delay_ms)
    for i in range(attempts):      
         byte=com.read(size = 1).decode('utf-8')
         time.sleep(0.01)
         read_data+=byte
         if byte == '\n':
             break

    return read_data

def read_write_gst(com, instruction):    

    write_data=instruction.encode('utf-8')
    com.write(write_data)
    recieved = []
    while(1):
        read_data=read_while_LF(com)
        if(read_data == ""):
            break
        recieved.append(read_data)

    return recieved

def animate(x, y):
    x_data = []
    y_data = []
    x_data.append(x)
    y_data.append(y)
    
    plt.cla()
    plt.plot(x, y)
    plt.legend(loc='upper_left')


com = serial.Serial('COM3', baudrate=115200, timeout=0.02)
instruction = "tracking:start\r".encode('utf-8')
com.write(instruction)

x=[]
y=[]
x = 0
fig, ax = plt.subplots(1, 1)
points = ax.plot(x,y)
plt.show(False)
plt.draw()
plt.pause(0.05)
while(1):
    x.append(x+1)
    s=read_while_LF(com, 500)
    y.append(s[:-2])
    points.set_data(x, y)



com.close()