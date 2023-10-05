#importing libraries and files

import digitalio
import board
import time
import bmp280
import radio
import tmp36

#to validate that the code is running correctly
print("Program Running.")

#turn on LED to see if Pico is working
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

led.value = True
time.sleep(1.5)
led.value = False

#send test message to make sure radio is working
radio.send("CANMOTION Test Message")
print("Radio message Sent")

time_count = 0

# main loop
while True:


    temperature = bmp280.read_temperature()
    pressure = bmp280.read_pressure()
    adc_temp = tmp36.read_temperature()

    time_count += 1

    print(str(time_count),
          "CANMOTION T:{:.2f} P: {:.0f} ADC-T:{:5.2f}".format(temperature, pressure, adc_temp))

    radio.send(str(time_count) +
               "CANMOTION T:{:.2f} P: {:.0f} ADC-T:{:5.2f}".format(temperature, pressure, adc_temp))

    time.sleep(1)   # TODO - look at cansat spec and see if it needs changed

