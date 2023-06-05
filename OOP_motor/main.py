#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from communicate import Communicate
from set_values import SetValues
from default_values import DefaultValues
from sequencegenerator import SequenceGenerator
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# setting defaults

c=Communicate()
values = DefaultValues()
motor_on_duty = SetValues(values.get_default_wait_time(), values.get_default_number_steps_per_revolution(), values.get_default_change_direction_times())
motor_on_duty.get_wait_time()
motor_on_duty.get_steps()
motor_on_duty.get_rotations()

step_pins = values.get_default_step_pins()
step_count = values.get_default_sequencer_step_count()
seq_gen = SequenceGenerator(step_count)
seq = seq_gen.get_sequence()
for pin in step_pins:        
        GPIO.setup(pin,GPIO.OUT)                
        GPIO.output(pin, False)        
c.print_setting_up_gpio_pins(step_pins)

# I just gotta leave this functionality here, can't drive it from elsewhere just for now

def steps(number_of_steps):
        step_counter = 0
        if number_of_steps<0: sign=-1
        else: sign=1
        number_of_steps=sign*number_of_steps
        c.print_number_of_steps_and_sign(number_of_steps, sign)
        for i in range(number_of_steps):
                for pin in range(4):
                        xpin = step_pins[pin]
                        if seq[step_counter][pin]!=0:
                                GPIO.output(xpin, True)
                        else:
                                GPIO.output(xpin, False)
                step_counter += sign
        # If we reach the end of the sequence
        # start again
                if (step_counter==step_count):
                        step_counter = 0
                if (step_counter<0):
                        step_counter = step_count-1
                # Wait before moving on
                time.sleep(float(motor_on_duty.wait_time))

# Start main loop
if __name__ == '__main__' :
    try:
        for i in range(int(motor_on_duty.change_direction_times)):    
                steps(int(motor_on_duty.number_steps_per_revolution))
                time.sleep(0.2)
                steps(-int(motor_on_duty.number_steps_per_revolution))
                time.sleep(0.2)     

        c.print_motor_stop()
        for pin in step_pins:
                GPIO.output(pin, False)

    finally:
        GPIO.cleanup()