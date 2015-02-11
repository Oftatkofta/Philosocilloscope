/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.
 
  This example code is in the public domain.
 */
 #include "LedControl.h"
 
 
// Pin 13 has an LED connected on most Arduino boards.
// give it a name:

LedControl lc=LedControl(2,4,3,1);


int led = 11;
int i = 0;
int incoming1 = 0;
int incoming2 = 0;
// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT);
  Serial.begin(9600);
    lc.shutdown(0,false);
  /* Set the brightness to a medium values */
  lc.setIntensity(0,8);
  /* and clear the display */
  lc.clearDisplay(0);
}

void print_binary(int d) {
   d = d % 256;
   Serial.print(d % 2);
   d = d/2;
   Serial.print(d % 2);
   d = d/2;
   Serial.print(d % 2);
   d = d/2;
   Serial.print(d % 2);
   d = d/2;
   Serial.print(d % 2);
   d = d/2;
   Serial.print(d % 2);
   d = d/2;
   Serial.print(d % 2);
   d = d/2;
   Serial.print(d % 2);
   d = d/2;
   Serial.print(d % 2);
   d = d/2;
   Serial.println("");
}

unsigned long delaytime=250;

void display_number(int number) {
  int j;
  lc.clearDisplay(0);
  for(j = 0;j < 8;j++) {
    lc.setDigit(0,j,number%10,false);
    Serial.print(number%10);
    number /= 10;
    delay(delaytime);
    
  }
  Serial.println("");
}

// the loop routine runs over and over again forever:
void loop() {
  if(Serial.available() > 0) {
    incoming1 = Serial.read();
    //incoming2 = Serial.read();
    analogWrite(led, incoming1);
    display_number(incoming1);
  //digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(50);  // wait for a second
  }
  //print_binary(i);
  
  //digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  //delay(250);               // wait for a second
}
