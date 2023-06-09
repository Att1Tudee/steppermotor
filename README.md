## _steppermotor_

# TEAC 14769070-00

>_The scripts utilizes old steppermotor from floppydisk drive that I wanted to make work with raspberry pi 3._  
>_The physical stuff is pretty DIY, I used old 9-pin internal motherboard cable from old computer and the pins from internal usb-module._    
>_I used a PCB circuit with 12v power source and 4 NPN transistors that are connected to RP3, those NPN's are cutting grounds_  
>_from the motor. There's two programs, one can be used for demonstrating a CNC machine as for given inputs directly, other program can be used to pass directions via cmdline._  


# _wiring explained_
The pins arranged in script equal into this sequence array
```sh
StepPins = [27,22,23,24]

Seq[0] = [1,0,0,0]  
Seq[1] = [0,1,0,0]  
Seq[2] = [0,0,1,0]  
Seq[3] = [0,0,0,1]  
```

- GPIO27 = seq0 = yellow on motor  
- GPIO22 = seq1 = white  
- GPIO23 = seq2 = blue  
- GPIO24 = seq3 = red  
 
2 browns are +12V  

This is how the motor seems to work for me when controlling motor via cutting ground.  

## To run the script
You need to have python3 installed.

```sh
python3 main.py
```

[![My video of testing steppermotor](https://img.youtube.com/vi/rUI71POV53M/0.jpg)](https://www.youtube.com/watch?v=rUI71POV53M)


