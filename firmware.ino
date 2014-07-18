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
  if(Serial.available()>0)       //If data is available on input buffer, and data on buffer isn't NONE, send a 
    {                           // HIGH +5 volts signal to power switch tail
      if(Serial.read()!=-1)
      {
      
      digitalWrite(output1, HIGH);
      digitalWrite(output2, HIGH);
      delay(3000);                 //This delay goes according to your write serial function delay in the sudo_make_coffee.py code
                                  //I set a three seconds delay to give the write python function enough time to send data
      }                           //and fill the incoming buffer in the arduino (Since my write delay lasts for a sec).
    }                             //That way there will be always data in the input buffer, as long as your python code sends some data.
  else
    {
      digitalWrite(output1, LOW);  //Because of the delay, it'll last at least around ten to fifteen seconds for the arduino to 
      digitalWrite(output2, LOW); // stop sending HIGH signals to the relays in the power switch tail
    }  
} 
