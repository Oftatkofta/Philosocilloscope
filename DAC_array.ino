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
byte shapeX[] = {255, 249, 231, 202, 167, 127, 87, 52, 23, 5, 0, 5, 23, 52, 87, 127, 167, 202, 231, 249, 249};
byte shapeY[] = {127, 167, 202, 231, 249, 255, 249, 231, 202, 167, 127, 87, 52, 23, 5, 0, 5, 23, 52, 87, 249};
void setup() {
  //Serial.begin(115200);
  d = 0;

  // for loop to initialize each pin as an output:
  for (int i = 0; i < 8; i++)  {
    pinMode(Xpins[i], OUTPUT);
    pinMode(Ypins[i], OUTPUT);
  }

}

void loop() {

  if (d > sizeof(shapeX) - 1) {
    d = 0;

  }

  //  DigitToBinArray(shapeX[d], coordinateX);
  //  DigitToBinArray(shapeY[d], coordinateY);
  //  painter(coordinateX, Xpins, coordinateY, Ypins);
  painter2(shapeX[d], Xpins, shapeY[d], Ypins);
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

}

void painter2(int Xcord, byte pinArrayX[], int Ycord, byte pinArrayY[]) {

  //Make sure that we not overflow our 8-bit DAC
  int x = Xcord % 256;
  int y = Ycord % 256;

  for (int i = 0; i < 8; i++) {

    if (x % 2 == 1) {
      digitalWrite(pinArrayX[i], HIGH);
    } else {
      digitalWrite(pinArrayX[i], LOW);
    }
    x = x / 2;
    if (y % 2 == 1) {
      digitalWrite(pinArrayY[i], HIGH);
    } else {
      digitalWrite(pinArrayY[i], LOW);
    }
    y = y / 2;
  }
}
//delayMicroseconds(10);


