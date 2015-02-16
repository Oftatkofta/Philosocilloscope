/* The arrays store the pin numbers making up the X and Y bytes LSB->MSB
 */
byte Xpins[] = {
  2, 3, 4, 5, 6, 7, 8, 9
};
byte Ypins[] = {
  12, 13, A5, A4, A3, A2, A1, A0
};
int d;
bool coordinateX[8];
bool coordinateY[8];
int shapeX[128];
int shapeY[128];


void setup() {
  //Serial.begin(115200);
  d = 0;

  // for loop to initialize each pin as an output:
  for (int i = 0; i < 8; i++)  {
    pinMode(Xpins[i], OUTPUT);
    pinMode(Ypins[i], OUTPUT);
  }
    for (int i = 0; i < sizeof(shapeX - 1); i++) {
      float x = (128*cos(i) + 127);
      float y = (128*sin(i) + 127);
      shapeY[i] = (int)y;
      shapeX[i] = (int)x;
    }

}

void loop() {

  if (d > sizeof(shapeX) - 1) {
    d = 0;
  }

  DigitToBinArray(shapeX[d], coordinateX);
  DigitToBinArray(shapeY[d], coordinateY);
  painter(coordinateX, Xpins, coordinateY, Ypins);


  delay(1);
     //Serial.println(shapeX);
  //  Serial.print(" ");
  //  for (int i = 0; i < 8; i++) {
  //    Serial.print(shapeX[i]);
  //    Serial.print("=");
  //    Serial.print(coordinateX[i]);
  //    Serial.print(" ");
  //  }
  //  Serial.println();
  //tester(Xpins, Ypins);
  d++;
}



void tester(byte pinArrayX[], byte pinArrayY[]) {
  for (int i = 7; i > -1; i--) {
    digitalWrite(pinArrayX[i], HIGH);
    digitalWrite(pinArrayY[i], HIGH);
  }
  //delay(timer);
  for (int i = 7; i > -1; i--) {
    digitalWrite(pinArrayX[i], LOW);
    digitalWrite(pinArrayY[i], LOW);
  }
}
void DigitToBinArray(int d, boolean array[]) {
  //Function that generates a 8-bit array from an int (LSB->MSB, like the DAC pins)

  d = d % 256; //Make sure that d does not overflow our 8-bit DAC
  for (int i = 0; i < 8; i++) {
    if (d % 2 == 1) {
      array[i] = 1;
    } else {
      array[i] = 0;
    }
    d = d / 2;
  }
}

void painter(bool coordinateX[], byte pinArrayX[], bool coordinateY[], byte pinArrayY[]) {

  for (int i = 0; i < 8; i++) {
    if (coordinateX[i]) {
      digitalWrite(pinArrayX[i], HIGH);
    }
    else {
      digitalWrite(pinArrayX[i], LOW);
    }

    if (coordinateY[i]) {
      digitalWrite(pinArrayY[i], HIGH);
    }
    else {
      digitalWrite(pinArrayY[i], LOW);
    }
  }
  //delayMicroseconds(10);
}

void painter2(bool coordinateX[], byte pinArrayX[], bool coordinateY[], byte pinArrayY[]) {

  for (int i = 0; i < 8; i++) {
    if (coordinateX[i]) {
      digitalWrite(pinArrayX[i], HIGH);
    }
    else {
      digitalWrite(pinArrayX[i], LOW);
    }

    if (coordinateY[i]) {
      digitalWrite(pinArrayY[i], HIGH);
    }
    else {
      digitalWrite(pinArrayY[i], LOW);
    }
  }
  //delayMicroseconds(10);
}

