#include <Servo.h>

Servo steerServo;  // Steering Servo - Range: 0 -> 180
int ESC_Arduino_Pin = 11; 


void setup() {
  Serial.begin(9600); // Initialize serial communication at 9600 bps
  pinMode(ESC_Arduino_Pin, OUTPUT); // Set pin 11 as an output ///<----------NEED ANOTHER PWM PIN 
  steerServo.attach(9);  // attaches the servo on pin 9 to the servo object
}


//check if first character is the symbol "S" -> Speed, "T" -> Turn Vehicle, go to their respective functions to execute, wether it be speed control OR Turning Controls. 
//COMMAND FORMAT: S200 -> Set speed of car to 200 / 256 , T90 -> Turn car to drive straight (90/180)
void loop() {
  if (Serial.available() > 0) { // Check if data is available to read
    String inputString = Serial.readStringUntil('\n'); // Read the incoming data until a newline character is received
    
    int pwmValue = inputString.substring(1).toInt(); // Convert the string to an integer
    
    
    switch ( inputString[0]) { //Check first char for what command type it is 
    case 'S': //-------------CONTROLS THE SPEED OF THE CAR -------------
      Serial.println("SPEED ATTEMPT MADE");
      if (pwmValue >= 0 && pwmValue <= 255) { // Check if the value is within the valid PWM range
        analogWrite(ESC_Arduino_Pin, pwmValue); // Output PWM signal on pin 9 with the specified value
        
        //steerServo.write(pwmValue-10); //Goes from 0 to 180, apparently
        //delay(15); //as recommended by the library 
        Serial.println("PWM value set to: " + String(pwmValue)); //For Debugging Purposes ONLY 
      } else {
        Serial.println("Invalid PWM value. Please enter a number between 0 and 255."); //For Debugging Purposes ONLY  + Needed to make sure if something ELSE is sent, the program does NOT CRASH
      }//end of IF-ELSE statement
            
      break;
    case 'T'://----------------CONTROLS THE TURNING OF THE CAR-------------
      Serial.println("TURN ATTEMP MADE"); 
      if (pwmValue >= 0 && pwmValue <= 180) { // Check if the value is within the valid PWM range
        //analogWrite(9, pwmValue); // Output PWM signal on pin 9 with the specified value
        
        steerServo.write(pwmValue-10); //Goes from 0 to 180, apparently
        delay(15); //as recommended by the library 
        Serial.println("PWM value set to: " + String(pwmValue)); //For Debugging Purposes ONLY 
      } else {
        Serial.println("Invalid PWM value. Please enter a number between 0 and 255."); //For Debugging Purposes ONLY  + Needed to make sure if something ELSE is sent, the program does NOT CRASH
      }//end of IF-ELSE statement 


      
      break;
    default:
      Serial.print("SOMETHING BROKE!"); // statements
      break;
    }//end of switch 
  }//end of IF statement 

  delay(20); //attempting to put in 20ms delay in hopes that the arduino will slow down and be more responsive to commands (instead of trying to play "catch-up" [assuming thats what it is doing]) 

  
   
}// end of loop()
