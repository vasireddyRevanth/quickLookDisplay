import serial 
from arduinoComm import echoMeasured, read_buffer, extract_messages
from datetime import datetime
import cProfile
import threading


T =60;
try:
    while T>0:
        print(echoMeasured(), datetime.now().strftime("%H:%M:%S"));
        # cProfile.run('echoMeasured()');
        T-=1;


except KeyboardInterrupt:
    print("\nCaught KeyboardInterrupt")

    # Open the serial port 


