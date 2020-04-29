from bokeh.plotting import curdoc, figure
import serial
import time
#bokeh serve --show serial_plotter.py


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

def update():
    global i
    com = serial.Serial('COM3', baudrate=115200, timeout=0.02)
    time.sleep(0.01)
    s=read_while_LF(com, 100)
    s=s[:-2]
    y =float(s)

    r.data_source.stream({'x': [i], 'y': [y]})
    i += 1
    com.close()
    time.sleep(0.01)


com = serial.Serial('COM3', baudrate=115200, timeout=0.02)
time.sleep(0.01)
instruction = "tracking:start\r".encode('utf-8')
com.write(instruction)

i = 0
p = figure()
r = p.circle([], [])
curdoc().add_root(p)
curdoc().add_periodic_callback(update, 100)
com.close()