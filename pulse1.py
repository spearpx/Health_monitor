import pulse
import time
import smbus

#### Getting the temperature Data #########

bus = smbus.SMBus(1)

ADDRESS = 0x48

def reading1():
 a= bus.read_byte(ADDRESS)
 return a


### Printing it ########

while 1:
 temp = pulse.bpm
 temp = float(temp)
 
 print(temp:)
