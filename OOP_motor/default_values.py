# These hardcodings could be in some outer txt file instead
class DefaultValues:

    def get_default_wait_time(self):
        return float(0.01)
    def get_default_number_steps_per_revolution(self):
        return int(128)
    def get_default_change_direction_times(self):
        return int(2)
    
    # sequencer uses 4 steps, from sequencegenerator.py
    # [1,0,0,0]
    # [0,1,0,0]
    # [0,0,1,0]
    # [0,0,0,1]

    def get_default_sequencer_step_count(self):
        return int(4)

    #GPIO pins
    def get_default_step_pins(self):
        return [27,22,23,24]

    
