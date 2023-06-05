from communicate import Communicate
from default_values import DefaultValues

# set value functions
c=Communicate()

class SetValues:
    def __init__(self, wait_time, number_steps_per_revolution, change_direction_times):        
        self.wait_time = wait_time
        self.number_steps_per_revolution = number_steps_per_revolution
        self.change_direction_times = change_direction_times
        
    def get_wait_time(self):
        while True:        
            default_value_for_wait_time = DefaultValues()    
            input_for_wait_time = input(f"Wait time between steps({default_value_for_wait_time.get_default_wait_time()}=default):")
            if not input_for_wait_time:                    
                    c.print_wait_time(self.wait_time)         
                    return float(self.wait_time)                    
            try:
                    self.wait_time = float(input_for_wait_time)                
                    return float(self.wait_time)
            except ValueError:                
                    c.wrong_input()
        
    def get_steps(self):
        while True:
            default_value_for_number_steps_per_revolution = DefaultValues()
            input_for_number_steps_per_revolution = input(f"Steps per revolution({default_value_for_number_steps_per_revolution.get_default_number_steps_per_revolution()}=default):")
            if not input_for_number_steps_per_revolution:
                    c.print_number_steps_per_rev(self.number_steps_per_revolution)
                    return self.number_steps_per_revolution
            try:
                    self.number_steps_per_revolution = int(input_for_number_steps_per_revolution)
                    return self.number_steps_per_revolution
            except ValueError:
                    c.wrong_input()
        
    def get_rotations(self):
        while True:
            default_value_for_default_change_direction_times = DefaultValues()
            input_for_change_direction_times = input(f"Times to change direction({default_value_for_default_change_direction_times.get_default_change_direction_times()}=default):")
            if not input_for_change_direction_times:
                    c.print_change_direction_times(self.change_direction_times)
                    return self.change_direction_times
            try:        
                    self.change_direction_times = int(input_for_change_direction_times)
                    return self.change_direction_times                    
            except ValueError:
                    c.wrong_input()           