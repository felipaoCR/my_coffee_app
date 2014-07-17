int output1 = 13;  //These are the duinos outputs, which are
int output2 = 6;  //considered as the relay´s inputs, feel free to pick whatever duino´s pin you like

void setup()
{
  pinMode(output1, OUTPUT);
  pinMode(output2, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  if(Serial.available()>0)       //If data is received, then send a +5 volts input to the power switch tail
    {
      digitalWrite(output1, HIGH);
      digitalWrite(output2, HIGH);
    }
  else
    {
      digitalWrite(output1, LOW);  //If not, then do nothing
      digitalWrite(output2, LOW);
    }  
} 
