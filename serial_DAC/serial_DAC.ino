byte Xpins[] = {
  2, 3, 4, 5, 6, 7, 8, 9 //LSB->MSB
};
byte Ypins[] = {
  12, 13, A5, A4, A3, A2, A1, A0 //LSB->MSB
};
//int d;

//byte shapeX[] = {123};
//byte shapeY[] = {123};
int x = 0;
int y = 0;



void setup() {
  Serial.begin(9600);

  // for loop to initialize each pin as an output:
  for (int i = 0; i < 8; i++)  {
    pinMode(Xpins[i], OUTPUT);
    pinMode(Ypins[i], OUTPUT);

  }
}
void loop() {
  if (Serial.available() > 0){
    x = Serial.parseInt();
    y = Serial.parseInt();
    if (Serial.read() == '\n') {
    Serial.print(x,y);
  }
  }
  painter3(x, y, Xpins, Ypins);
 
}

void painter3(int coordinateX, int coordinateY, byte pinArrayX[], byte pinArrayY[]) {
  for (int i = 0; i < 8; i++) {

    if (bitRead(coordinateX, i)) {
    digitalWrite(pinArrayX[i], HIGH);
    }
    else {
      digitalWrite(pinArrayX[i], LOW);
    }

    if (bitRead(coordinateY, i)) {
    digitalWrite(pinArrayY[i], HIGH);
    }
    else {
      digitalWrite(pinArrayY[i], LOW);
    }
  }
}
