# Write your code here :-)
 #importing libraries and files

import digitalio
import board
import time
import bmp280
import radio
import tmp36
import bno055



#to validate that the code is running correctly
print("Program Running.")

#turn on LED to see if Pico is working
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

#read/write
switch = digitalio.DigitalInOut(board.GP19)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

led.value = True

#send test message to make sure radio is working
stringyo = "CANMOTION Test " + str(switch.value)
radio.send(stringyo)
print("Radio message Sent")

time_count = 0

# main loop
while True:


    temperature = bmp280.read_temperature()
    pressure = bmp280.read_pressure()
    adc_temp = tmp36.read_temperature()
    data = bno055.read_sensor_data()
    time_count += 1
    stringy = "CANMOTION T:{:.2f} P: {:.0f} ADC:{:5.2f}/ x:{:.2f} y:{:.2f} z:{:.2f}/ r:{:.2f} p:{:.2f} y:{:.2f}/A x:{:.2f} y:{:.2f} z:{:.2f}".format(temperature, pressure, adc_temp,data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8] )
    print(str(stringy))

    radio.send(stringy)

    if switch.value == 0: #only if the pico is allowed to write
        File = open('data.txt', 'w') #prepares to add data to the file
        File.write(stringy+"\n")  #(they are written to a new file)
        File.close()  #this line closes the file

    time.sleep(1)   # TODO - look at cansat spec and see if it needs changed

