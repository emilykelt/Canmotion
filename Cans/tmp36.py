import board
import analogio
adc = analogio.AnalogIn(board.GP26)

def read_temperature():
    adc_raw = adc.value
    adc_voltage = (adc_raw * 3.3)/65536
    temperature = (adc_voltage - 0.5) * 100
    # print("raw = {:5d} volts = {:5.2f}".format(adc_raw, adc_voltage, temperature))
    return temperature
