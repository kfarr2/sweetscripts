// we're gonna try something new here.
int scannow=0,scandir=0;
int incoming = 0;

unsigned int table[][4]={
    {0x000, 0x000, 0x000, 0x0000},
};

void setup() {      
  Serial.begin(9600);  
  for(int a=2;a<=13;a++){
    pinMode(a, OUTPUT); 
  }
}

void loop() {
  // Read input from serial?
  // feed data to pins
  if(Serial.available() > 0) {
    incoming = Serial.parseInt();
    translate(incoming);   
    Serial.println(incoming);
  }    

}

// error code (e.g. 404) gets passed in and is displayed
//
void translate(int error_code) {
  unsigned int rate_delay = 0x05ff;
  switch(error_code)
  {
    case 200:
    {
      output_to_led(0x000, 0x000, 0x101, rate_delay);
      break; 
    }
    case 301:
    {
      output_to_led(0x010, 0x000, 0x485, rate_delay);
      break; 
    }
    case 302:
    {
      output_to_led(0x012, 0x000, 0x485, rate_delay);      
      break; 
    }
    case 404:
    {
      output_to_led(0x945, 0x000, 0x945, rate_delay);
      break; 
    }
    default:
    {
      output_to_led(0x000, 0x010, 0x000, rate_delay);
      break; 
    }
    
  }
}

void output_to_led(unsigned int one, unsigned int two, unsigned int three, unsigned int four){
  unsigned int table[][4] = {
    { one, two, three, four },
  };
  for(int b=0;b<(table[0][3]>>8);b++)
    {
      for(int c=0;c<30;c++)// This loop repeated the cycle of pins output; you can modify the c to change the brightness 
      {
        digitalWrite(2,(table[0][c%3]&0x1));
        digitalWrite(4,(table[0][c%3]&0x2));   
        digitalWrite(7,(table[0][c%3]&0x4));
        digitalWrite(8,(table[0][c%3]&0x8));
        digitalWrite(9,(table[0][c%3]&0x10));   
        digitalWrite(10,(table[0][c%3]&0x20)); 
        digitalWrite(11,(table[0][c%3]&0x40));
        digitalWrite(12,(table[0][c%3]&0x80));   
        digitalWrite(13,((table[0][c%3]&0x100)>>1));
        if(c%3==0)
          analogWrite(3,(0xff-(table[0][3]&0xff)));  
        else if(c%3==1)
          analogWrite(5,(0xff-(table[0][3]&0xff)));        
        else if(c%3==2)
          analogWrite(6,(0xff-(table[0][3]&0xff)));        
        delay(2); 
        digitalWrite(3,1); 
        digitalWrite(5,1);
        digitalWrite(6,1); 
        
      }
      
    }
}
