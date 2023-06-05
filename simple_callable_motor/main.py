import argparse
from drive import move_forward, move_backward
import RPi.GPIO as GPIO

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--cmd', nargs='+', help='Motor commands')
args = parser.parse_args()

# Define motor functions
fw = move_forward
bw = move_backward

if __name__ == '__main__':
    try:
        # Process motor commands
        i = 0
        while i < len(args.cmd):
            action = args.cmd[i]
            i += 1
            steps = []
            while i < len(args.cmd) and args.cmd[i].isdigit():
                steps.append(int(args.cmd[i]))
                i += 1
            if action == 'fw':
                for s in steps:
                    fw(s)
            elif action == 'bw':
                for s in steps:
                    bw(s)
    finally:
        GPIO.cleanup()
