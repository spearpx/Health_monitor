#this is the end code for the data collection and output of the sensors
import pulse
import temp


tempread=temp.read_temp_c
pulseread=pulse.bpm

print(f'Pulse Rate is : {pulseread}') if pulseread !=0 else print("No Pulse detected!")
print(f'Temperature is : {pulseread}') if tempread !=0 else print("No Temperature detected!")







