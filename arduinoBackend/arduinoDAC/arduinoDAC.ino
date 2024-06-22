#define BAUD_RATE 9600
#define SERIAL_PORT_NAME "/dev/ttyUSB0"

#define ANALOG_PORT_X A0
#define ANALOG_PORT_Y A1
#define ANALOG_PORT_Z A2

#define WORDSEL_PIN 2
#define DATA_PIN 4
#define BITCLK_PIN 7

#define ledPin LED_BUILTIN

long int xSensor = 0;
long int zSensor = 0; 
long int ySensor = 0; 
int inByte = 0;
int ledState = LOW;

long int leftDACVal =0x2434; 
long int rightDACVal =0x5678; 

// PWM PINS : D3 ; D5 ; D6 ; D9 ; D10 ; D11

void setup() {
  Serial.begin(BAUD_RATE);

  pinMode(ledPin, OUTPUT);
  pinMode(WORDSEL_PIN, OUTPUT);
  pinMode(DATA_PIN, OUTPUT);
  pinMode(BITCLK_PIN, OUTPUT);


}

void loop() {

  Serial.println("-x-x-x-x");

  digitalWrite(WORDSEL_PIN, LOW);
  delayMicroseconds(10); // Delay for the duration of the bit clock low pulse

  // Send the first 24 bits of the Left Value
  for (int i = 23; i >= 0; i--) {
    digitalWrite(BITCLK_PIN, HIGH);

    digitalWrite(DATA_PIN, (leftDACVal >> i) & 0x01);
   
    xSensor = analogRead(ANALOG_PORT_X) / (4*255);
    ySensor = analogRead(ANALOG_PORT_Y) / (4*255);
    Serial.println(xSensor);

    delayMicroseconds(10);
    digitalWrite(BITCLK_PIN, LOW);
    delayMicroseconds(10);
  }

  digitalWrite(WORDSEL_PIN, HIGH);
  delayMicroseconds(10);

  Serial.println("-x-x-x-x");

  // Send the first 24 bits of the rightValue
  for (int i = 23; i >= 0; i--) {
    digitalWrite(BITCLK_PIN, HIGH);
    digitalWrite(DATA_PIN, (rightDACVal >> i) & 0x01);

    xSensor = analogRead(ANALOG_PORT_X) / (4*255);
    ySensor = analogRead(ANALOG_PORT_Y) / (4*255);
    Serial.println(xSensor);

    delayMicroseconds(10);
    digitalWrite(BITCLK_PIN, LOW);
    delayMicroseconds(10);
  }
  Serial.println("-x-x-x-x");

  delay(100000);

}