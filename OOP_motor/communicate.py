class Communicate:        
        def wrong_input(self):
            print("Wrong value. If you want to use default value hit enter without any input")
        def print_wait_time(self, wait_time):                
                print(f"Using wait_time {wait_time}")                
        def print_number_steps_per_rev(self, number_steps_per_rev):
                print(f"Using number_steps_per_rev {number_steps_per_rev}")
        def print_change_direction_times(self, change_direction_times):        
                print(f"Using change_direction_times {change_direction_times}")
        def print_setting_up_gpio_pins(self, step_pins):
                print(f"Setting up GPIO pins {step_pins}")
        def print_number_of_steps_and_sign(self, number_of_steps, sign):
                print(f"number_of_steps {number_of_steps} and sign {sign}")
        def print_motor_stop(self):
                print("Motor stopped.")
               