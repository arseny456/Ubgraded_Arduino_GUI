#define LED_R 9
#define LED_G 10
#define LED_R 11

String message;


void setup() {
  Serial.begin(115200);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(9,OUTPUT);
}

void loop() {
//  Serial.println("some text"
  while(Serial.available()){
    char inByte = Serial.read();

    message += inByte;
    if (inByte == "\n"){
      if (message == "ON")digitalWrite(LED_R,HIGH);
      if (message == "OFF")digitalWrite(LED_R,LOW);
      message = "";
    }
    

//    if (inByte >= '0' && inByte <='9'){
//      message += inByte;
//      
//    }else if(inByte == '\n'){
//      analogWrite(LED_R, message.toInt());
//      message = "";
//    }
//  }
}
}
