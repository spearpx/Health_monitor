### Health_monitor
Simple Health Monitor System using Heart Beat sensor and Temperature sensor.</br>

**Introduction**</br>
This project aims to provide the user with the details of the heartbeat and temperature. Raspberry Pi 3 is used for connecting all the sensors and communicaing the data to user through mqtt client. </br>

**Hardware used** 

**1. Raspberry Pi 3**

Raspberry Pi 3 is a development board in PI series. It can be considered as a single board computer that works on LINUX operating system. The board not only has tons of features it also has terrific processing speed making it suitable for advanced applications. PI board is specifically designed for hobbyist and engineers who are interested in LINUX systems and IoT (Internet of Things). </br></br>
Where is Raspberry Pi 3 used? </br>
Raspberry pi platform is most used after ADRUINO. Although overall applications of PI are less it is most preferred when developing advanced applications. Also the RASPBERRY PI is an open source platform where one can get a lot of related information so you can customize the system depending on the need. Here are few examples where RASPBERRY PI 3 is chosen over other microcontrollers and development boards: </br>
1. Where the system processing is huge. Most ARDUINO boards all have clock speed of less than 100MHz, so they can perform functions limited to their capabilities. They cannot process high end programs for applications like Weather Station, Cloud server, gaming console etc. With 1.2GHz clock speed and 1 GB RAM, Raspberry pi can perform all those advanced functions.</br>
2. Where wireless connectivity is needed. RASPBERRY PI 3 has wireless LAN and Bluetooth facility by which you can setup WIFI HOTSPOT for internet connectivity. For Internet of Things this feature is best suited.</br>
3. Raspberry pi has dedicated port for connecting touch LCD display which is a feature that completely omits the need of monitor. </br>
4. RASPBERRY PI also has dedicated camera port so one can connect camera without any hassle to the PI board. </br>
5. RASPBERRY PI also has PWM outputs for application use. There are many other features like HD steaming which further promote the use of RASPBERRY PI.</br>


**2. DS18B20 Temperature Sensor**

DS18B20 Sensor Specifications</br>
• Programmable Digital Temperature Sensor</br>
• Communicates using 1-Wire method</br>
• Operating voltage: 3V to 5V </br>
• Temperature Range: -55°C to +125°C </br>
• Accuracy: ±0.5°C</br>
• Output Resolution: 9-bit to 12-bit (programmable)</br>
• Unique 64-bit address enables multiplexing </br>
• Conversion time: 750ms at 12-bit</br>
• Programmable alarm options</br>
• Available as To-92, SOP and even as a waterproof sensor</br></br>

Where to use DS18B20 Sensor?</br> The DS18B20 is a 1-wire programmable Temperature sensor from maxim integrated. It is widely used to measure temperature in hard environments like in chemical solutions, mines or soil etc. The constriction of the sensor is rugged and also can be purchased with a waterproof option making the mounting process easy. It can measure a wide range of temperature from -55°C to +125° with a decent accuracy of ±5°C. Each sensor has a unique address and requires only one pin of the MCU to transfer data so it a very good choice for measuring temperature at multiple points without compromising much of your digital pins on the microcontroller.</br>


**3. MCP3008 ADC**


Features:</br>
• 10-bit resolution.</br>
• ± 1 LSB max DNL.</br>
• ± 1 LSB max INL.</br>
• 4 (MCP3004) or 8 (MCP3008) input channels.</br>
• Analog inputs programmable as single-ended or pseudo-differential pairs.</br>
• On-chip sample and hold.</br>
• SPI serial interface (modes 0,0 and 1,1).</br>
• Single supply operation: 2.7V - 5.5V.</br>
• 200 ksps max. sampling rate at VDD = 5V.</br>
• 75 ksps max. sampling rate at VDD = 2.7V.</br>
• Low power CMOS technology.</br>
• 5 nA typical standby current, 2 μA max.</br>
• 500 μA max. active current at 5V.</br>
• Industrial temp range: -40°C to +85°C.</br>
• Available in PDIP, SOIC and TSSOP packages.</br>


Where to use it? </br> There are some devices like Raspberry pi which don’t have hardware for analog to digital converter and therefore they can’t read analog inputs. So, you need a circuit for this conversion. For such devices, you can use the MCP3008 chip. This chip uses an SPI interface for communication. In Raspberry Pi, only four GPIO pins are required. So, you can get 8 additional analog inputs by using this chip. Sensors use analog outputs. Therefore, many devices need an ADC converter to read these outputs. The MCP3008 can be used for converting these analog signals into digital signals.


**4. Pulse sensor or heart beat sensor**


Pulse Sensor Features and Specifications</br> 
• Biometric Pulse Rate or Heart Rate detecting sensor</br> 
• Plug and Play type sensor </br>
• Operating Voltage: +5V or +3.3V</br>
• Current Consumption: 4mA</br>
• Inbuilt Amplification and Noise cancellation circuit.</br>
• Diameter: 0.625”</br>
• Thickness: 0.125” Thick</br>


How Pulse Sensor Works?</br>
The working of the Pulse/Heart beat sensor is very simple. The sensor has two sides, on one side the LED is placed along with an ambient light sensor and on the other side we have some circuitry. This circuitry is responsible for the amplification and noise cancellation work. The LED on the front side of the sensor is placed over a vein in our human body. This can either be your Finger tip or you ear tips, but it should be placed directly on top of a vein. Now the LED emits light which will fall on the vein directly. The veins will have blood flow inside them only when the heart is pumping, so if we monitor the flow of blood we can monitor the heart beats as well. If the flow of blood is detected then the ambient light sensor will pick up more light since they will be reflect ted by the blood, this minor change in received light is analysed over time to determine our heart beats.</br>

**Circuit Diagram**</br>


![](https://github.com/spearpx/Health_monitor/blob/spearpx-patch-2/pulse%20sensor%20image.jpg)

Circuit diagram of pulse sensor connected to Raspberry Pi 3 along with MCP3008 ADC</br>


![](https://github.com/spearpx/Health_monitor/blob/spearpx-patch-2/Temp%20sensor%20image.jpg)

Circuit diagram of temperature sensor connected to Raspberry Pi 3 </br>


**Working of the project**</br>
• Raspberry pi3 is used as medium that interacts with both sensors and output device (App).</br>
• The temperature sensor does not require ADC, however it requires resistor connected across Vcc and sensor output.</br>
• The temperature sensor output is connected to one of the GPIO pins of Raspberry pi, for communication it uses only one wired interface.</br>
• Pulse sensor communicates through ADC(MCP3008), the data pin is connected to channel 0 of MCP3008.</br>
• The analog output from Pulse sensor is converted into digital through ADC and interfaced with Raspberry pi.</br>
• ADC(MCP3008) uses SAR(Successive approximation) technique to get accurate pulse readings.</br>
• Raspberry pi communicates with mobile application by using MQTT client.</br>
• A MQTT broker connects Raspberry pi to the cloud and cloud to mobile.</br>
• The sensor output is sent to cloud through a channel and the mobile app receives the data from subscribing the channel that contains the sensor output.</br>
• To collect the data for ML code is written to include the data into a csv file created locally.</br>
• The csv file is used for various applications of ML.</br>

**Conclusion**

This is a simple project that handles with the sensors, CPU and mobile application. It is user friendly and hence any person of any age can use it. With further developments in hardware structure this device can be carried out anywhere. And mobile app is also a prototype, when developed the UI and usability of the app can be improved.
##
**Note**: All the files of this project are not available in this repository due to technical failures at the author's side resulting in loss of android studio files, since the process of restoration of files is difficult, any user can  utilise the existing files and complete the work as a challange by refering to the "working of the project" and suggest the changes when and where required. For further querries contact  Aravind V A (aravindva@hotmail.com).

