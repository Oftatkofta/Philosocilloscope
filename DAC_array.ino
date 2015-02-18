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
byte shapeX[] = {255, 255, 255, 254, 254, 253, 252, 251, 250, 249, 247, 246, 244, 242, 240, 238, 236, 233, 231, 228, 225, 222, 219, 216, 213, 209, 206, 202, 199, 195, 191, 187, 183, 179, 175, 171, 167, 162, 158, 154, 149, 145, 140, 136, 131, 127, 123, 118, 114, 109, 105, 100, 96, 92, 87, 83, 79, 75, 71, 67, 63, 59, 55, 52, 48, 45, 41, 38, 35, 32, 29, 26, 23, 21, 18, 16, 14, 12, 10, 8, 7, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 7, 8, 10, 12, 14, 16, 18, 21, 23, 26, 29, 32, 35, 38, 41, 45, 48, 52, 55, 59, 63, 67, 71, 75, 79, 83, 87, 92, 96, 100, 105, 109, 114, 118, 123, 127, 131, 136, 140, 145, 149, 154, 158, 162, 167, 171, 175, 179, 183, 187, 191, 195, 199, 202, 206, 209, 213, 216, 219, 222, 225, 228, 231, 233, 236, 238, 240, 242, 244, 246, 247, 249, 250, 251, 252, 253, 254, 254, 255, 255};
byte shapeY[] = {127, 131, 136, 140, 145, 149, 154, 158, 162, 167, 171, 175, 179, 183, 187, 191, 195, 199, 202, 206, 209, 213, 216, 219, 222, 225, 228, 231, 233, 236, 238, 240, 242, 244, 246, 247, 249, 250, 251, 252, 253, 254, 254, 255, 255, 255, 255, 255, 254, 254, 253, 252, 251, 250, 249, 247, 246, 244, 242, 240, 238, 236, 233, 231, 228, 225, 222, 219, 216, 213, 209, 206, 202, 199, 195, 191, 187, 183, 179, 175, 171, 167, 162, 158, 154, 149, 145, 140, 136, 131, 127, 123, 118, 114, 109, 105, 100, 96, 92, 87, 83, 79, 75, 71, 67, 63, 59, 55, 52, 48, 45, 41, 38, 35, 32, 29, 26, 23, 21, 18, 16, 14, 12, 10, 8, 7, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 7, 8, 10, 12, 14, 16, 18, 21, 23, 26, 29, 32, 35, 38, 41, 45, 48, 52, 55, 59, 63, 67, 71, 75, 79, 83, 87, 92, 96, 100, 105, 109, 114, 118, 123};


void setup() {
  //Serial.begin(115200);
  d = 0;

  // for loop to initialize each pin as an output:
  for (int i = 0; i < 8; i++)  {
    pinMode(Xpins[i], OUTPUT);
    pinMode(Ypins[i], OUTPUT);
  }
//    for (int i = 0; i < sizeof(shapeX - 1); i++) {
//      float x = (128*cos(i) + 127);
//      float y = (128*sin(i) + 127);
//      shapeY[i] = (int)y;
//      shapeX[i] = (int)x;
//      delay(1);
//    }

}

void loop() {

  if (d > sizeof(shapeX) - 1) {
    d = 0;
  }

  DigitToBinArray(shapeX[d], coordinateX);
  DigitToBinArray(shapeY[d], coordinateY);
  painter(coordinateX, Xpins, coordinateY, Ypins);


  //delay(1);
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

