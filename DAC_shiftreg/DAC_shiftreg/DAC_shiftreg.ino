int clockpin = 6;
int latch = 5;
int datapin = 7;

void setup() {
  pinMode(clockpin, OUTPUT);
  pinMode(datapin, OUTPUT);
  pinMode(latch, OUTPUT);
}

void loop() {

  for (int i = 0; i < 16; i++) {
    digitalWrite(datapin, HIGH);
    digitalWrite(clockpin, HIGH);
    digitalWrite(clockpin, LOW);
    if (i == 7) {
      digitalWrite(latch, HIGH);
      digitalWrite(latch, LOW);
    }
  }

  digitalWrite(latch, HIGH);
  digitalWrite(latch, LOW);

  for (int i = 0; i < 16; i++) {
    digitalWrite(datapin, LOW);
    digitalWrite(clockpin, HIGH);
    digitalWrite(clockpin, LOW);

    if (i == 7) {
      digitalWrite(latch, HIGH);
      digitalWrite(latch, LOW);
    }
  }
  digitalWrite(latch, HIGH);
  digitalWrite(latch, LOW);
}
