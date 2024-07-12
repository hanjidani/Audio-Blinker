String in;
const int light = 8;
void setup() {
 Serial.begin(38400);
 pinMode(light, OUTPUT);
}
long brightness;
int fuck(String s){
  int len = s.length();
  int ret = 0;
  for(int i = 0; i < len; i++)
    ret = ret * 10 + (s[i] - '0');
  return ret;
}
void loop() {
  /*if(Serial.available() > 0){
    in = Serial.readStringUntil(',');
    brightness = fuck(in);
    //Serial.print(brightness);
    //if(brightness != 0)
    //  analogWrite(LED_BUILTIN, brightness);
    if(brightness == 1) digitalWrite(light, HIGH);
    if(brightness == 0) digitalWrite(light, LOW);
  }*/
  while(Serial.available() > 0){
    in = Serial.readString();
    
  }
  Serial.flush();
  delay(800);
  //analogWrite(LED_BUILTIN, 0);
}
