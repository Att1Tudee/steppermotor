class SequenceGenerator:
    def __init__(self, step_count):
        self.step_count = step_count
        self.seq =  [i for i in range(0, step_count)]

        # This is how the steppermotor uses the coil steps
        
        self.seq[0] = [1,0,0,0]
        self.seq[1] = [0,1,0,0]
        self.seq[2] = [0,0,1,0]
        self.seq[3] = [0,0,0,1]

    def get_sequence(self):
        return self.seq
