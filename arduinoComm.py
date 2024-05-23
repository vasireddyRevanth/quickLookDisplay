import serial
import re

# Connects to the Arduino.
def connect_arduino(port='/dev/ttyUSB1', baud_rate=9600):    
    try:
        ser = serial.Serial(port, baud_rate)
        return ser
    except Exception as e:
        print(f"Error connecting to Arduino: {e}")
        return None

# Sends data to the Arduino.
def send_data(ser, data):
    if ser is not None:
        try:
            ser.write(data.encode())
        except Exception as e:
            print(f"Failed to send data: {e}")

def read_raw_data(ser):
    if ser is not None:
        try:
            while True:
                if ser.in_waiting >0:
                    return ser.readline();
        except Exception as e:
            print((f"Failed to read data: {e}"));

def echoMeasured():
    try:
        values = extract_messages();
        measured_values = values[3:]
        return measured_values;
    except:
        pass

def extract_messages():
    ser = connect_arduino()
    arduino_recieved_raw = read_raw_data(ser)
    
    try:
        # Assuming read_raw_data already returns a string suitable for regex
        string_pattern = r'([^#]*)#'
        formatted_str_list = re.findall(string_pattern, arduino_recieved_raw)
        
        if formatted_str_list:
            formatted_string = formatted_str_list[0]
            values = [int(formatted_string[i:i+4].strip()) for i in range(0, len(formatted_string), 4)]
            return values
        else:
            print("No formatted string found.")
            return []
    except Exception as e:
        print(f"Message format not found. Failed to extract data: {e}")
        return []


def extract_messages():
    ser = connect_arduino();
    arduino_recieved_raw = str(read_raw_data(ser));
    try:
        string_pattern = r'!([^#]*)#'
        formatted_str_list = re.findall(string_pattern, arduino_recieved_raw);
        formatted_string = formatted_str_list[0]
        values = [int(formatted_string[i:i+4].strip()) for i in range(0,len(formatted_string),4)]
        return values;
    except Exception as e:
        # Handle case where $ or # is not found
        print(f"Message format not found. Failed to extract data: {e}")
