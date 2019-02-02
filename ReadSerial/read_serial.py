import serial
import time

def process_value(val):
    # Do something with plotly here
    if val != b'':
        split = val.decode('utf8').split(' ')
        if len(split) == 3 and len(split[-1]) > 0:
            print(' '.join(split)[:-1])


s0 = serial.Serial('/dev/ttyACM0', 115200, timeout=0)
s1 = serial.Serial('/dev/ttyACM1', 115200, timeout=0)


while True:
    val0, val1 = (s0.readline(), s1.readline())
    process_value(val0)
    process_value(val1)
    # throw out values that have piled up during processing
    # Todo: think about threading?
    (s0.flushInput(), s1.flushInput())
