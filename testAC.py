import serial 
from arduinoComm import extract_messages, echoMeasured

while True:
    print(echoMeasured())
# Open the serial port 


