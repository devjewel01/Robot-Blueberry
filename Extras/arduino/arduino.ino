  #include <Wire.h> 
  #include <LiquidCrystal_I2C.h>

  LiquidCrystal_I2C lcd(0x27,20,4);
  void QR()
  {
    lcd.setCursor(4,3);
    lcd.print("Quanta Robotics!");
  }
  int column[16]={34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49};
  //               0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
  int atob[4][4]={{0,1,2,3},{4,5,6,7},{8,9,10,11},{12,13,14,15}};
  int atod[4][4]={{0,4,8,12},{1,5,9,13},{2,6,10,14},{3,7,11,15}};
  int btoa[4][4]={{3,2,1,0},{7,6,5,4},{11,10,9,8},{15,14,13,12}};
  int btoc[4][4]={{3,7,11,15},{2,6,10,14},{1,5,9,13},{0,4,8,12}};
  int ctob[4][4]={{15,11,7,3},{14,10,6,2},{13,9,5,1},{12,8,4,0}};
  int ctod[4][4]={{15,14,13,12},{11,10,9,8},{7,6,5,4},{3,2,1,0}};
  int dtoc[4][4]={{12,13,14,15},{8,9,10,11},{4,5,6,7},{0,1,2,3}};
  int dtob[4][4]={{12,8,4,0},{13,9,5,1},{14,10,6,2},{15,11,7,3}};
  int layer[4]={50,51,52,53};
  void setup() {
    Serial.begin(9600);
    for(int i = 0; i<16; i++)
      pinMode(column[i], OUTPUT);
    for(int i = 0; i<4; i++)
      pinMode(layer[i], OUTPUT);
    for(int i = 0; i<4; i++){
      for(int j=0; j<4; j++){
        atob[i][j] = column[atob[i][j]];
        atod[i][j] = column[atod[i][j]];
        btoa[i][j] = column[btoa[i][j]];
        btoc[i][j] = column[btoc[i][j]];
        ctob[i][j] = column[ctob[i][j]];
        ctod[i][j] = column[ctod[i][j]];
        dtoc[i][j] = column[dtoc[i][j]];
        dtob[i][j] = column[dtob[i][j]];
      }
    }
    
    lcd.init();
    lcd.backlight();
    lcd.clear();
    lcd.setCursor(3,0);
    lcd.print("Welcome to");
    lcd.setCursor(1,1);
    lcd.print("Robot Blueberry");
    QR();
  }
  int count=0;

  void loop()
  {
    count=count%6;
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
        f2();f2();f2();
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
    else {
      if(count==0){f1();}
      else if(count==1){layerByLayer();layerByLayer();layerByLayer();}
      else if(count==2) {flickerOn();flickerOn();flickerOn();}
      else if(count==3){ f2();f2(); }
      else if(count==4){ f3(); f3(); f3();}
      else if(count==5){ f4(); f4(); f4();}
      count+=1;
    }

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

