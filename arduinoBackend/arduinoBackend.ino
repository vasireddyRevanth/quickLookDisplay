#define BAUD_RATE 9600
#define SERIAL_PORT_NAME "/dev/ttyUSB1"

#define ANALOG_PORT_X A0
#define ANALOG_PORT_Y A1
#define ANALOG_PORT_Z A2

long int xSensor = 0;
long int zSensor = 0; 
long int ySensor = 0; 
int inByte = 0;

// PWM PINS : D3 ; D5 ; D6 ; D9 ; D10 ; D11

void setup() {
  Serial.begin(BAUD_RATE);
}

void loop() {
if (Serial.available() > 0) {
    // get incoming byte:
    inByte = Serial.read();
    if(inByte == '?'){
      char buff [200];
      xSensor = analogRead(ANALOG_PORT_X) / 4;
      // read second analog input, divide by 4 to make the range 0-255:
      ySensor = analogRead(ANALOG_PORT_Y) / 4;
      // read switch, map it to 0 or 255L
      zSensor = analogRead(ANALOG_PORT_Z) / 4;
      long int set1 = 1, set2 = 2, set3 = 3;
      sprintf(buff, "$%4ld%4ld%4ld%4ld%4ld%4ld#", set1, set2, set3, xSensor, ySensor, zSensor);
      Serial.println(buff);
    }

  }
}