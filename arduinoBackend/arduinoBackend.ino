#define BAUD_RATE 9600
#define SERIAL_PORT_NAME "COM3"

void setup() {

 Serial.begin(BAUD_RATE);
  
Serial.println("Arduino is ready!");
}

void loop() {
 if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    
 
    Serial.print("Received: ");
    Serial.println(data);
    
 }
}