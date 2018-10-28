//This code has the infrastructure for 

// Drive system constants
#define PWMA  6   // Motor 1 (LEFT)
#define A_IN1   7
#define A_IN2   8
#define D_IN5   9
#define D_IN6   10

#define CW  1
#define CCW 0

int dVal5 = 0;
int dVal6 = 0;
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// State definitions
#define state_Default 0 //drive straight
#define state_TurnRight 1
#define state_TurnLeft 2

int state = state_Default;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(PWMA, OUTPUT);
  pinMode(A_IN1, OUTPUT);
  pinMode(A_IN2, OUTPUT);
  pinMode(D_IN5, INPUT);
  pinMode(D_IN6, INPUT);
  analogWrite(PWMA, 0.2*255);
  digitalWrite(A_IN1, LOW);
  digitalWrite(A_IN2, LOW);
  //Starts in default state
  state = state_Default;
}


// the loop function runs over and over again forever
void loop() {
  switch (state){
    case state_Default:   //default is to go straight
         handleDefault();
         dVal5 = digitalRead(D_IN5);
         dVal6 = digitalRead(D_IN6);
         if (dVal6 == HIGH && dVal5 == LOW) {
         state = state_TurnRight;
         delay(1000);// for testing- will add time from decision making
         }
         else if (dVal6 == LOW && dVal5 == HIGH){
          state = state_TurnLeft;
         delay(1000);// for testing- will add time from decision making
         }
         else if (dVal6 == LOW && dVal5 == LOW){
          state = state_Default;
          delay(1000);// for testing- will add time from decision making
         }
         break;
    case state_TurnRight:
         handleTurnRight();
         delay(1000);// for testing- will add time from decision making
         state= state_Default;
         break;
    case state_TurnLeft:
         handleTurnLeft();
         delay(1000);// for testing- will add time from decision making
         state = state_Default;
         break;
  }
}


//Function definitions
void handleDefault(void){
  digitalWrite(A_IN1, LOW);
  digitalWrite(A_IN2, LOW);
}

void handleTurnRight(void){
  digitalWrite(A_IN1, HIGH);
  digitalWrite(A_IN2, LOW);
  
}

void handleTurnLeft(void){
  digitalWrite(A_IN1, LOW);
  digitalWrite(A_IN2, HIGH);
}


