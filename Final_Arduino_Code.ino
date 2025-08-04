// Define motor driver pins for Motor 1 (90-degree rotation)
const int motor1In1 = 9;   // Motor 1 IN1
const int motor1In2 = 8;   // Motor 1 IN2
const int motor1ENA = 10;  // Motor 1 ENA (PWM for speed)

// Define motor driver pins for Motor 2 (75-degree rotation)
const int motor2In1 = 7;   // Motor 2 IN1
const int motor2In2 = 6;   // Motor 2 IN2
const int motor2ENA = 5;   // Motor 2 ENA (PWM for speed)

// Define motor driver pins for Motor 3 (45-degree rotation)
const int motor3In1 = 4;   // Motor 3 IN1
const int motor3In2 = 3;   // Motor 3 IN2
const int motor3ENA = 2;   // Motor 3 ENA (PWM for speed)

// Variables to store motor speeds (0-255)
int motor1Speed = 0;
int motor2Speed = 0;
int motor3Speed = 0;

// Time required for rotations (milliseconds)
const int motor1RotationTime90 = 400; // Motor 1 - 90 degrees
const int motor2RotationTime75 = 275; // Motor 2 - 75 degrees
const int motor3RotationTime45 = 150; // Motor 3 - 45 degrees

void setup() {
  pinMode(motor1In1, OUTPUT);
  pinMode(motor1In2, OUTPUT);
  pinMode(motor1ENA, OUTPUT);

  pinMode(motor2In1, OUTPUT);
  pinMode(motor2In2, OUTPUT);
  pinMode(motor2ENA, OUTPUT);

  pinMode(motor3In1, OUTPUT);
  pinMode(motor3In2, OUTPUT);
  pinMode(motor3ENA, OUTPUT);

  Serial.begin(9600);
  Serial.println("Triple Motor Control with 90, 75, and 45 Degree Rotations");
  Serial.println("Commands:");
  Serial.println("  P<speed> - Motor 1 Forward 90 degrees at <speed> (0-255)");
  Serial.println("  SU<speed> - Motor 1 Reverse 90 degrees at <speed> (0-255)");
  Serial.println("  F<speed> - Motor 2 Forward 75 degrees at <speed> (0-255)");
  Serial.println("  E<speed> - Motor 2 Reverse 75 degrees at <speed> (0-255)");
  Serial.println("  R<speed> - Motor 3 Forward 45 degrees at <speed> (0-255)");
  Serial.println("  U<speed> - Motor 3 Reverse 45 degrees at <speed> (0-255)");
  Serial.println("  S - Stop all motors");
}

void loop() {
  if (Serial.available() > 0) {
    // Read the full command string
    String command = Serial.readStringUntil('\n');
    command.trim(); // Remove leading/trailing whitespace

    // Process commands
    if (command.startsWith("P")) {
      int speed = command.substring(2).toInt();
      if (speed >= 0 && speed <= 255) {
        Serial.print("Motor 1 Forward 90 degrees at Speed: ");
        Serial.println(speed);
        moveMotorForward(motor1In1, motor1In2, motor1ENA, speed, motor1RotationTime90);
      } else {
        Serial.println("Invalid speed for Motor 1!");
      }
    } else if (command.startsWith("SU")) {
      int speed = command.substring(2).toInt();
      if (speed >= 0 && speed <= 255) {
        Serial.print("Motor 1 Reverse 90 degrees at Speed: ");
        Serial.println(speed);
        moveMotorReverse(motor1In1, motor1In2, motor1ENA, speed, motor1RotationTime90);
      } else {
        Serial.println("Invalid speed for Motor 1!");
      }
    } else if (command.startsWith("F")) {
      int speed = command.substring(2).toInt();
      if (speed >= 0 && speed <= 255) {
        Serial.print("Motor 2 Forward 75 degrees at Speed: ");
        Serial.println(speed);
        moveMotorForward(motor2In1, motor2In2, motor2ENA, speed, motor2RotationTime75);
      } else {
        Serial.println("Invalid speed for Motor 2!");
      }
    } else if (command.startsWith("E")) {
      int speed = command.substring(2).toInt();
      if (speed >= 0 && speed <= 255) {
        Serial.print("Motor 2 Reverse 75 degrees at Speed: ");
        Serial.println(speed);
        moveMotorReverse(motor2In1, motor2In2, motor2ENA, speed, motor2RotationTime75);
      } else {
        Serial.println("Invalid speed for Motor 2!");
      }
    } else if (command.startsWith("R")) {
      int speed = command.substring(2).toInt();
      if (speed >= 0 && speed <= 255) {
        Serial.print("Motor 3 Forward 45 degrees at Speed: ");
        Serial.println(speed);
        moveMotorForward(motor3In1, motor3In2, motor3ENA, speed, motor3RotationTime45);
      } else {
        Serial.println("Invalid speed for Motor 3!");
      }
    } else if (command.startsWith("U")) {
      int speed = command.substring(2).toInt();
      if (speed >= 0 && speed <= 255) {
        Serial.print("Motor 3 Reverse 45 degrees at Speed: ");
        Serial.println(speed);
        moveMotorReverse(motor3In1, motor3In2, motor3ENA, speed, motor3RotationTime45);
      } else {
        Serial.println("Invalid speed for Motor 3!");
      }
    } else if (command.equals("S")) {
      Serial.println("Stopping all motors");
      stopMotor(motor1In1, motor1In2, motor1ENA);
      stopMotor(motor2In1, motor2In2, motor2ENA);
      stopMotor(motor3In1, motor3In2, motor3ENA);
    } else {
      Serial.println("Invalid command! Use P, SU, F, E, R, U, or S.");
    }
  }
}

// Function to move motor forward for a fixed duration
void moveMotorForward(int in1, int in2, int ena, int speed, int duration) {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  analogWrite(ena, speed);
  delay(duration);
  stopMotor(in1, in2, ena);
}

// Function to move motor in reverse for a fixed duration
void moveMotorReverse(int in1, int in2, int ena, int speed, int duration) {
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  analogWrite(ena, speed);
  delay(duration);
  stopMotor(in1, in2, ena);
}

// Function to stop a motor
void stopMotor(int in1, int in2, int ena) {
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  analogWrite(ena, 0);
}
