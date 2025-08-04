from prosthesis import *

# Create the motor instance
name = Motor()
prevposi = 0 
# Perform initial setup on the motor
initial(name)

# Prompt for the number of cycles
num_cycles = int(input("Enter the number of cycles: "))

# Execute the motor control routine for the given number of cycles
for i in range(num_cycles):
    # Request the angle for the current cycle
    angle_input = int(input(f"Cycle {i + 1} - Enter the angle: "))
    torque = int(input(f"Cycle {i + 1} - Enter the torque: "))
    name.angle = angle_input
    name.torque = torque

    # currentposi = name.actualPos - prevposi
    
    # Start the motor with the specified parameters
    start(name)

    #40 angle and 1100 as torque for ps motor 
    #20 angle and 900 as torque for RU motor 
    #20 angle and 600 as torque for fe motor
    
    # Output the motor telemetry data
    print(f"Cycle {i + 1} - Actual Position: {name.actualPos}")
    print(f"Cycle {i + 1} - Actual Velocity: {name.actualVel}")
    print(f"Cycle {i + 1} - Acceleration: {name.acceleration}")
    print(f"Cycle {i + 1} - Deceleration: {name.deceleration}")
    print(f"Cycle {i + 1} - Velocity: {name.velocity}")
    print(f"Cycle {i + 1} - MasterEncoder: {name.encvalue}")
    print(f"Cycle {i + 1} - IncEncoder: {name.encvalue1}")
    print(f"Cycle {i + 1} - direction: {name.direction}")
    print(f"Cycle {i + 1} - torque: {name.torque}")
    print(f"Cycle {i + 1} - currentposi: {name.actualPos - prevposi}")
    prevposi = name.actualPos
    

