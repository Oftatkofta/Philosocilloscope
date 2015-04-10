byte Xpins[] = {
  2, 3, 4, 5, 6, 7, 8, 9 //LSB->MSB
};
byte Ypins[] = {
  12, 13, A5, A4, A3, A2, A1, A0 //LSB->MSB
};

int d;

byte shape[30];
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
    if (d > sizeof(shape) - 2) {
    d = 0;

  }
  if (Serial.available() > 0){
    Serial.readBytes(shape,30);
    //x = Serial.parseInt();
    //y = Serial.parseInt();
    //if (Serial.read() == '\n') {
    //Serial.print(x,y); }
  } 
  painter3(shape[d], shape[d+1], Xpins, Ypins);
 d+=2;
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
