//Source: https://www.youtube.com/watch?v=UZKxUFkwCc8
#define RCPin 2
volatile long StartTime = 0; 
volatile long CurrentTime = 0;
volatile long Pulses = 0; 
int PulseWidth = 0; 
 

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); 
  pinMode(RCPin, INPUT_PULLUP); 
  attachInterrupt(digitalPinToInterrupt(RCPin), PulseTimer, CHANGE); //registers the change on both RISING and FALLING edges, needed to figure out rise-fall time <3 // ALSO sets it up as a hardware interrupt to ensure accurate data capture VS waiting for the print statement from finishing (this is a great thing!) 
  
}//end of setup()

void loop() {
  if(Pulses < 2000){ // 2000 is the start of the only real pulses we care about :)  
    PulseWidth = Pulses; 
  }//end of IF statement

  //Serial.println(Pulses); 
  Serial.println(PulseWidth); 
}//end of loop()



void PulseTimer(){ 
  CurrentTime = micros(); 
  if(CurrentTime > StartTime){ 
    Pulses = CurrentTime - StartTime; 
    StartTime = CurrentTime; 
  }//end of IF statement
  
}//end of PulseTimer() 
