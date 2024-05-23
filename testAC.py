import serial 
from arduinoComm import extract_messages, echoMeasured
from datetime import datetime

try:
    while True:
        print(echoMeasured(),datetime.now().strftime("%H:%M:%S"));
except KeyboardInterrupt:
    print("\nCaught KeyboardInterrupt")

    # Open the serial port 


