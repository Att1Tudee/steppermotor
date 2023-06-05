import RPi.GPIO as GPIO
import time

# Define the GPIO pins for the stepper motor
IN1 = 27
IN2 = 22
IN3 = 23
IN4 = 24

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Define the step sequence for the stepper motor
step_sequence = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],        
    [0, 0, 1, 0],    
    [0, 0, 0, 1],
]

# Define the delay between each step
delay = 0.01

# Define the maximum number of steps to move
MAX_STEPS = 9162

# Define the counter variable to keep track of the steps taken
step_count = 0

def move_forward(steps):
    global step_count
    step_count = 0
    while step_count < steps and step_count < MAX_STEPS:
        for step in step_sequence:
            GPIO.output(IN1, step[0])
            GPIO.output(IN2, step[1])
            GPIO.output(IN3, step[2])
            GPIO.output(IN4, step[3])
            time.sleep(delay)
            step_count += 1

def move_backward(steps):
    global step_count
    step_count = 0
    while step_count < steps and step_count < MAX_STEPS:
        for step in reversed(step_sequence):
            GPIO.output(IN1, step[0])
            GPIO.output(IN2, step[1])
            GPIO.output(IN3, step[2])
            GPIO.output(IN4, step[3])
            time.sleep(delay)
            step_count += 1

# Clean up the GPIO pins when the program is finished
GPIO.cleanup()
