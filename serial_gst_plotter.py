# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 12:28:39 2020

@author: Ксения
"""


import serial
import time
import serial.tools.list_ports as lp


def get_comports_list():
    ports=list(lp.comports(include_links=False))
    for p in ports:
        print(p.device)
    return ports



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


com = serial.Serial('COM3', baudrate=115200, timeout=0.02)





s=read_write_gst(com, "fil_test:start\r")


print(s)
com.close()