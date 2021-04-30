class TrafficLight{
  int redLight,orangeLight,greenLight;
  public:
  TrafficLight(int r, int g){
    redLight=r;
    orangeLight=19;//some unused pin
    greenLight=g;
    pinSetup();
  }
  TrafficLight(int r, int o, int g){
    redLight=r;
    orangeLight=o;
    greenLight=g;
    pinSetup();
  }
  void pinSetup(){
    pinMode(redLight,OUTPUT);
    pinMode(orangeLight,OUTPUT);
    pinMode(greenLight,OUTPUT);
  }
  void red(){
    digitalWrite(redLight,HIGH);
    digitalWrite(orangeLight,LOW);
    digitalWrite(greenLight,LOW);
  }
  void orange(){
    digitalWrite(redLight,LOW);
    digitalWrite(orangeLight,HIGH);
    digitalWrite(greenLight,LOW);
  }
  void green(){
    digitalWrite(redLight,LOW);
    digitalWrite(orangeLight,LOW);
    digitalWrite(greenLight,HIGH);
  }
};

void setup() {
      Serial.begin(9600);
      Serial.print("hello");
    
     
}
char rx_byte= 0;
int seqNo=1;

TrafficLight kalimati(10,9,8),thapathali(7,6,5),ratnapark(4,3,2),kalimatizeb(13,14),thapathalizeb(15,16),ratnaparkzeb(11,12);



void loop() {

  if (Serial.available() > 0) {    // is a character available?
    rx_byte = Serial.read();   // get the character
    Serial.print(rx_byte);
    // check if a number was received
    if ((rx_byte >= '0') && (rx_byte <= '9')) {
      Serial.print("Number received: ");
      Serial.println(rx_byte);
      kalimati.red();
      thapathali.red();
      ratnapark.red();
      delay(3000);
    }
  }
    
   // end: if (Serial.available() > 0)
    if(seqNo==1){
        Serial.println("seq 1 activated");
        kalimati.red();//        digitalWrite(10,HIGH); // red 1
        thapathali.green();// digitalWrite(5,HIGH); // green 2
        ratnapark.red();//digitalWrite(4,HIGH); // RED 3
        ratnapark.orange();//digitalWrite(3,HIGH); // ORANGE 3
        kalimatizeb.green();//digitalWrite(14,HIGH); // Z1/G HIGH AS BOTH 1 AND 3 RED
      // digitalWrite(13,LOW); // Z1/R.
        delay(300);
        //digitalWrite(14,LOW); // Z1/G LOW
        kalimatizeb.red();// digitalWrite(13,HIGH); // Z1/R HIGH
       // digitalWrite(3,LOW); //O3 LOW ORANGE HO HAI
       // digitalWrite(4,LOW); //R3 LOW
       // digitalWrite(5,LOW); //G2 LOW
        thapathali.orange();//digitalWrite(6,HIGH); // ORANGE 2
        ratnapark.green();//digitalWrite(2,HIGH); // GREEN  3
        delay(600);
       // digitalWrite(6,LOW); // O2 LOW
    }
    else if(seqNo==2){
      Serial.println("seq 2 activated");
        // FOR 2nd SEQUENCE 
//        digitalWrite(9,HIGH); // ORANGE 1 high
        kalimati.orange();
        thapathali.red();// digitalWrite(7,HIGH); // red 2 high
        thapathalizeb.green();//digitalWrite(16,HIGH);// Z2/G HIGH AS 2 AND 1 RED
        //digitalWrite(15,LOW); // Z2/R LOW
        delay(600);
       // digitalWrite(16,LOW); // Z2/G LOW
        thapathalizeb.red();//digitalWrite(15,HIGH);// Z2/R HIGH
       // digitalWrite(9,LOW);// O1 LOW
       // digitalWrite(10,LOW);//R1 LOW
       // digitalWrite(2,LOW); // G3 LOW
       kalimati.green();//   digitalWrite(8,HIGH);// G1 HIGH
      
        ratnapark.orange();//digitalWrite(3,HIGH);// O3 HIGH
        delay(900);
        //digitalWrite(7,LOW);// R2 LOW
        //digitalWrite(3,LOW);// O3 LOW
    }
    else{
      Serial.println("seq 3 activated");
       // FOR 3RD SEQUENCE 
        thapathali.red();//digitalWrite(7,HIGH); //R2 HIGH
        thapathali.orange();//digitalWrite(6,HIGH); //O2 HIGH
        ratnapark.red();//digitalWrite(4,HIGH); // R3 HIGH
        ratnaparkzeb.green();//digitalWrite(12,HIGH); // Z3/G HIGH AS 2 AND 3 RED
       //digitalWrite(11,LOW); //Z3/R LOW
        delay(600);
        //digitalWrite(12,LOW); // Z3/G LOW
        ratnaparkzeb.red();//digitalWrite(11,HIGH); // Z3/R HIGH
       // digitalWrite(7,LOW);// R2 LOW
       // digitalWrite(6,LOW);//02 LOW
        //digitalWrite(8,LOW);// G1 LOW
        kalimati.orange();//digitalWrite(9,HIGH);//O1 HIGH
        thapathali.green();//digitalWrite(5,HIGH);// G2 HIGH
        delay(900);
       // digitalWrite(9,LOW);//O1 LOW*/
    }
    seqNo+=1;
    seqNo=seqNo%3;
  
}
