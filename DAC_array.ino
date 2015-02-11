/* The arrays store the pin numbers making up the X and Y bytes LSB->MSB
 */
byte Xpins[] = {
  2, 3, 4, 5, 6, 7, 8, 9 };       
byte Ypins[] = {
  12, 13, A5, A4, A3, A2, A1, A0};
int d;
byte coordinateX[8];
byte coordinateY[8];
int shapeX[] = {0, 37, 127, 219, 255, 219, 127, 37};
int shapeY[] = {127, 37, 0, 37, 127, 219, 255, 219};


void setup() {
//  Serial.begin(9600);
  d = 0;
  
// for loop to initialize each pin as an output:
  for (int i = 0; i < 8; i++)  {
    pinMode(Xpins[i], OUTPUT);
    pinMode(Ypins[i], OUTPUT); 
  }
}

void loop() {

  if (d > sizeof(shapeX)-1) {
    d=0;  }

  DigitToBinArray(shapeX[d], coordinateX);
  DigitToBinArray(shapeY[d], coordinateY);
  painter(coordinateX, Xpins, coordinateY, Ypins);
  d++;
  
  delay(1);
  // delay(200);
  // Serial.print(d);
  // Serial.print(" ");
  // for (int i = 0; i < 8; i++){
  // Serial.print(coordinateX[i]);
  // }
  // Serial.println();
  //tester(Xpins, Ypins);
}



void tester(byte pinArrayX[], byte pinArrayY[]){
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
void DigitToBinArray(int d, byte array[]){
  //Function thar generates a 8-bit array from an int (LSB->MSB, like the DAC pins)

  d = d % 256; //Make sure that d does not overflow our 8-bit DAC
  for (int i = 0; i < 8; i++){
    array[i]= d%2;
    d = d/2;
  }
}

void painter(byte coordinateX[], byte pinArrayX[], byte coordinateY[], byte pinArrayY[]){

  for (int i = 0; i < 8; i++){
    if (coordinateX[i] == 1){
      digitalWrite(pinArrayX[i], HIGH);
    }
    else{
      digitalWrite(pinArrayX[i], LOW);
    }

    if (coordinateY[i] == 1){
      digitalWrite(pinArrayY[i], HIGH);
    }
    else{
      digitalWrite(pinArrayY[i], LOW);
    } 
  }
  //delayMicroseconds(10);
}



