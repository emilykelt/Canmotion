import digitalio
import board
import time
import bmp280
import radio
import tmp36

print("Program Running.")

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

radio.send("VEGCANTATION Test Message")
print("Radio message Sent")

led.value = True
time.sleep(1.5)
led.value = False

# ^ change?

time_count = 0

# main loop
while True:

    # ^ change to while true

    temperature = bmp280.read_temperature()
    pressure = bmp280.read_pressure()
    adc_temp = tmp36.read_temperature()

    time_count += 1

    print(str(time_count),
          "VEGCANTATION T:{:.2f} P: {:.0f} ADC-T:{:5.2f}".format(temperature, pressure, adc_temp))

    radio.send(str(time_count) +
               "VEGCANTATION T:{:.2f} P: {:.0f} ADC-T:{:5.2f}".format(temperature, pressure, adc_temp))

    time.sleep(1)   # change to reduce traffic?

