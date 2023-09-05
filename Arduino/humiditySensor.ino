/* This is a simple arduino code that I wrote, so it can measure humidity */

const int humiditySensorPin = A0;

void setup() {
    Serial.begin(9600);
  pinMode(humiditySensorPin, INPUT);

}

void loop() {
  if (analogRead(humiditySensorPin) > 750) {
    Serial.println("[+] Umidade abaixo do nível ideal!\n");
  };

  if (analogRead(humiditySensorPin) >= 450 && analogRead(humiditySensorPin) <= 750) {
      Serial.println("[+] Umidade no nível ideal!\n");
  };

  if (analogRead(humiditySensorPin) < 450 ) {
    Serial.println("[+] Umidade acima do nível!\n");
  };

    /* switch (analogRead(humiditySensorPin)) {
    case analogRead(humiditySensorPin) > 750:
      Serial.println("[+] Umidade abaixo do nível ideal!\n);
      break;
    case (analogRead(humiditySensorPin) >= 450 && analogRead(humiditySensorPin) <= 750:
      Serial.println("[+] Umidade no nível ideal!\n");
      break;
    case analogRead(humiditySensorPin) < 450):
      Serial.println("[+] Umidade acima do nível ideal!\n");
      break;
    default:
      Serial.println("Sorry, I'm finding some issues with your input...");
      break;
  }; */

  delay(1500);

}