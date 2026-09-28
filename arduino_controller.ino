void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
Serial.begin(9600);
}


void loop() {
if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
command.trim();


if (command == "ON") {
digitalWrite(LED_BUILTIN, HIGH);
}


if (command == "OFF") {
digitalWrite(LED_BUILTIN, LOW);
}
}


int water = analogRead(A0);
Serial.println(water);


delay(500);
}
