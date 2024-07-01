import serial
import re
import cProfile
import threading
import time
# Connects to the Arduino.
def connect_arduino(port='/dev/ttyUSB0', baud_rate=9600):    
    try:
        ser = serial.Serial(port, baud_rate)
        return ser
    except Exception as e:
        print(f"Error connecting to Arduino: {e}")
        return None

# Sends data to the Arduino.
def send_data(data):
    ser = connect_arduino()
    if ser is not None:
        try:
            ser.write(data.encode())
        except Exception as e:
            print(f"Failed to send data: {e}")

def read_raw_data(ser):
    if ser is not None:
        try:
            while True:
                if ser.in_waiting >= 26:
                    # time.sleep(0.1);
                    print(ser.readline())
                    return str(ser.readline())
        except Exception as e:
            print((f"Failed to read data: {e}"));

def read_buffer():
    ser = connect_arduino()
    for i in range(10):            
        ser.readline()        
        print(ser.in_waiting)

def echoMeasured():

    try:
        values = extract_messages();
        measured_values = values[3:]
        return measured_values;
    except:
        pass


def extract_messages():
    ser = connect_arduino();
    arduino_recieved_raw = str(read_raw_data(ser))


    try:
        string_pattern = r'!([^#]*)#'
        formatted_str_list = re.findall(string_pattern, arduino_recieved_raw);
        formatted_string = formatted_str_list[0]
        values = [int(formatted_string[i:i+4].strip()) for i in range(0,len(formatted_string),4)]
        return values;
    except Exception as e:
        # Handle case where $ or # is not found
        pass
        print(f"Message format not found. Failed to extract data: {e}")

ser = connect_arduino()
threading.Thread(target=read_raw_data(ser)).start()
