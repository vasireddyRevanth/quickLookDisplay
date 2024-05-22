import serial

# Connects to the Arduino.
def connect_arduino(port='COM3', baud_rate=9600):    
    try:
        ser = serial.Serial(port, baud_rate)
        return ser
    except Exception as e:
        print(f"Error connecting to Arduino: {e}")
        return None

# Sends data to the Arduino.
def send_data(ser, data):
    if ser is not None:
        ser.write(data.encode())

# Reads data from the Arduino.
def read_data(ser):
    if ser is not None:
        while True:
            if ser.in_waiting > 0:
                return ser.readline().decode('utf-8').strip()
    return None