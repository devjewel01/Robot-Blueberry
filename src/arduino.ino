#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,20,4);
void QR()
{
  lcd.setCursor(4,3);
  lcd.print("Quanta Robotics!");
}
int column[16]={22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37};
int atob[4][4]={{22,23,24,25},{26,27,28,29},{30,31,32,33},{34,35,36,37}};
int atod[4][4]={{22,26,30,34},{23,27,31,35},{24,28,32,36},{25,29,33,37}};
int btoa[4][4]={{25,24,23,22},{29,28,27,26},{33,32,31,30},{37,36,35,34}};
int btoc[4][4]={{25,29,33,37},{24,28,32,36},{23,27,31,35},{22,26,30,34}};
int ctob[4][4]={{37,33,29,25},{36,32,28,24},{35,31,27,23},{34,30,26,22}};
int ctod[4][4]={{37,36,35,34},{33,32,31,30},{29,28,27,26},{25,24,23,22}};
int dtoc[4][4]={{34,35,36,37},{30,31,32,33},{26,27,28,29},{22,23,24,25}};
int dtob[4][4]={{34,30,26,22},{35,31,27,23},{36,32,28,24},{37,33,29,25}};
int layer[4]={38,39,40,41};
void setup() {
  Serial.begin(9600);
  for(int i = 0; i<16; i++)
    pinMode(column[i], OUTPUT);

  for(int i = 0; i<4; i++)
    pinMode(layer[i], OUTPUT);
  
  lcd.init();
  lcd.backlight();
  lcd.clear();
  lcd.setCursor(3,0);
  lcd.print("Welcome to");
  lcd.setCursor(1,1);
  lcd.print("Robot Blueberry");
  QR();
}

void loop()
{
  if(Serial.available() > 0)
  {
    String data = Serial.readStringUntil('\n');
    if(data == "listening")
    {
      lcd.clear();
      lcd.setCursor(4,1);
      lcd.print("I am Listening");
      f3();
    }
    else if(data == "speaking")
    {
      lcd.clear();
      lcd.setCursor(4,1);
      lcd.print("I am Speaking");
      f2();
    }
    else if(data=="on"){
        f1();
    }
    else if(data=="color"){
        layerByLayer();
    }
    else
    {
      lcd.clear();
      lcd.setCursor(1,0);
      lcd.print("Call me Buleberry");
      QR();
      f4();
    }
    Serial.print("You sent me: ");
    Serial.println(data);
  }
  else flickerOn();

}
void flickerOn()
{
  int i = 150;
  while(i != 0)
  {
    turnEverythingOn();
    delay(i);
    turnEverythingOff();
    delay(i);
    i-= 5;
  }
}
void f4(){
  for(int d=100; d>=0; d-=5){
    for(int lyr=0; lyr<4; lyr++){
      digitalWrite(layer[lyr],0);
      for(int i=0; i<=lyr; i++){
        for(int j=0; j<=lyr; j++){
          digitalWrite(atob[i][j],1);
          digitalWrite(atod[i][j],1);
        }
      }
      delay(d);
    }
    for(int lyr=3,lp=0; lyr>=0; lyr--,lp++){
      digitalWrite(layer[lyr],1);
      for(int i=0; i<=lp; i++){
        for(int j=0; j<=lp; j++){
          digitalWrite(atob[i][j],0);
          digitalWrite(atod[i][j],0);
        }
      }
      delay(d);
    }
    for(int lyr=3,lp=0; lyr>=0; lyr--,lp++){
      digitalWrite(layer[lyr],0);
      for(int i=0; i<=lp; i++){
        for(int j=0; j<=lp; j++){
          digitalWrite(btoa[i][j],1);
          digitalWrite(btoc[i][j],1);
        }
      }
      delay(d);
    }
    for(int lyr=0; lyr<4; lyr++){
      digitalWrite(layer[lyr],1);
      for(int i=0; i<=lyr; i++){
        for(int j=0; j<=lyr; j++){
          digitalWrite(dtob[i][j],0);
          digitalWrite(dtoc[i][j],0);
        }
      }
      delay(d);
    }
  }
}
void f3(){
  for(int i=0; i<4; i++)digitalWrite(layer[i], 1);
  for(int k=3; k>=0; k--){
    for(int j=3; j>=k; j--)digitalWrite(layer[j], 0);
    for(int i=0; i<16; i+=4){
    for(int j=0; j<4; j++)
      digitalWrite(column[i+j],1);
      delay(200);
      for(int j=0; j<4; j++)
        digitalWrite(column[i+j],0);
    }
    for(int i=0; i<4; i++){
      for(int j=0; j<4; j++){
        digitalWrite(column[i+4*j],1);
      }
      delay(200);
      for(int j=0; j<4; j++){
        digitalWrite(column[i+4*j],0);
      }
    }
  }
}
void f2(){
  for(int i=0; i<4; i++){
    digitalWrite(layer[i], 0);
  }
  for(int i=0; i<16; i+=4){
    for(int j=0; j<4; j++)
      digitalWrite(column[i+j],1);
    delay(200);
    for(int j=0; j<4; j++)
      digitalWrite(column[i+j],0);
  }
  for(int i=0; i<4; i++){
    for(int j=0; j<4; j++){
      digitalWrite(column[i+4*j],1);
    }
    delay(200);
    for(int j=0; j<4; j++){
      digitalWrite(column[i+4*j],0);
    }
  }
}
void f1(){
  for(int i=0; i<4; i++){
    digitalWrite(layer[i], 0);
  }
  for(int j=0; j<15; j++){
    for(int i=0; i<16-j; i++){
      for(int k=i; k<min(16,i+j); k++)
        digitalWrite(column[k],1);
      delay(100);
      for(int k=i; k<min(16,i+j); k++)
        digitalWrite(column[k],0);
    }
  }
}
void layerByLayer(){
  for(int i=0; i<4; i++){
    digitalWrite(layer[i], 1);
  }
  
  for(int i=0; i<4; i++){
    
    digitalWrite(layer[i],0);
    for(int j=0; j<16; j++){
      digitalWrite(column[j], 1);
    }
    delay(500);
    for(int j=0; j<16; j++){
      digitalWrite(column[j], 0);
    }
    digitalWrite(layer[i],1);
  }
}
void turnEverythingOn() {
  for(int i=0; i<4; i++){
    digitalWrite(layer[i],0);
  }
  for(int i=0; i<16; i++)
    digitalWrite(column[i],1);
}
void turnEverythingOff() {
  for(int i=0; i<4; i++){
    digitalWrite(layer[i],1);
  }
  for(int i=0; i<16; i++)
    digitalWrite(column[i],0);
}
