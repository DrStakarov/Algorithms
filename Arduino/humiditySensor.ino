/* This is a simple arduino code that I wrote, so it can measure humidity */

const int humiditySensorPin = A0;

void setup() {
  Serial.begin(9600);
  pinMode(humiditySensorPin, INPUT);

}

void loop() {

    /* Missing conditions here */
  Serial.println(analogRead(humiditySensorPin));
  delay(1000);

}