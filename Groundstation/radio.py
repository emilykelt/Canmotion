import digitalio
import board
import busio
import adafruit_rfm9x

spi = busio.SPI(clock=board.GP2, MOSI=board.GP3, MISO=board.GP4)
cs = digitalio.DigitalInOut(board.GP6)
reset = digitalio.DigitalInOut(board.GP7)

rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 433.0)

print("Radio Ready")

def send(message):
    rfm9x.send(message)

# groundstation, recieving:

def try_read():
    return rfm9x.receive(timeout=1.0)

def rssi():
    return rfm9x.rssi

