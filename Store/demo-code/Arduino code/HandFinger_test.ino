
#include <Servo.h>

String readvoice;

Servo servo[5];
bool rightFingure[]={1,1,1,0,0};
int angle=0;

void setup()
{
  Serial.begin(9600);
  for (int i = 0; i < 5; i++) {
    servo[i].attach(i + 3);
  }
  for(int i=0; i<5; i++){
    if(i<3)
      servo[i].write(0);
    else 
      servo[i].write(180);
  }
}


void loop()
{
  for(int j=0; j<3; j++){
    for(int i=0; i<5; i++){
      moveServo(i,90,00);
    }
    delay(1000);
    for(int i=0; i<5; i++){
      if(rightFingure[i]==1)moveServo(i,0,00);
      else moveServo(i,180,00);
    }
    delay(1000);
  }
  for(int i=0; i<3; i++){
      if(rightFingure[i]==1)moveServo(i,0,00);
      else moveServo(i,180,00);
    }
  for(int j=0; j<5; j++){
    moveServo(4,180,0);
    for(int i=0; i<5; i++){
      moveServo(i,90,0);
      if(i-1>=0){
        if(rightFingure[i-1]==1)moveServo(i-1,0,0);
        else moveServo(i-1,180,0); 
      }
      delay(500);
    }
  }
  /**while (Serial.available() != 0)
  {
    delay(10);
    char c = Serial.read();
    readvoice += c;
  }

  if (readvoice.length() > 0)
  {
    Serial.println("Voice found");
    Serial.println(readvoice);

    if (readvoice == "*hi#")
    {
      Serial.println("Hello");
      takePosition();
    }
    else if (readvoice == "*move all#" || readvoice == "*all#")
    {
      allMove();
    }
    else if (readvoice == "*move 1#")
    {
      moveServo(0, 180, 500);
      moveServo(0, 0, 500);
    }
    else if (readvoice == "*move middle#")
    {
      moveServo(1, 180, 500);
      moveServo(1, 0, 500);
    }


    Serial.println(readvoice);
    readvoice = "";
  }
  for (int i = 0; i < 5; i++) {
    moveServo(i, 70, 2000);
  }**/

}

void moveServo(int servoNumber, int Position, int Delay) {
  servo[servoNumber].write(Position);
  delay(Delay);
}
void takePosition()
{
  for (int i = 0; i < 5; i++) {
    servo[i].write(0);
  }
}


void allMove()
{
  for (int i = 0; i < 5; i++)
  {
    servo[i].write(90);
  }
  delay(1000);
  for (int i = 0; i < 5; i++)
  {
    servo[i].write(180);
  }
  delay(1000);
}
