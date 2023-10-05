# groundstation code
import digitalio
import board
import time
import radio

print("Program Running.")

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

led.value = True
time.sleep(1.5)
led.value = False

packet_count = 0

while True:
    radio_message = radio.try_read()

    if radio_message is not None:
        print("Radio RX {:d} {:s}".format(packet_count, str(radio_message, 'ascii')))
        print("RSSI: {:3d}db".format(radio.rssi()))
        packet_count = packet_count + 1
