#IMPORTS
import digitalio
import board
import time
import radio

#DATA STRUCTURES

#parralel 1D arrays (better to use other data structure but you guys know how to use this bc of higher)
packets = []    #represents time as 1 packet is sent every second
temp_d = [] #digital tempurature
pressure = []
temp_a = [] #analogue temp

#to store calculations
altitude = []

#--TODO 
#needs to be revamped with functional programming, and store variables of each data thing
#check pressure units are correct

#CHECK PROGRAM IS RUNNING
print("Program Running.")

#LED to check that circuit connections are running
led = digitalio.DigitalInOut(board.GP25)    #update if pin changes
led.direction = digitalio.Direction.OUTPUT

led.value = True
time.sleep(1.5)
led.value = False


#RECIEVE DATA
packet_count = 0

while True:
    radio_message = radio.try_read()

    if radio_message is not None:
        message ="{:d} {:s}".format(packet_count, str(radio_message, 'ascii')))
        print(message)
        #print("RSSI: {:3d}db".format(radio.rssi())) #--signal strength indicator. uncomment for testing.
        packet_count = packet_count + 1

        #READING DATA INTO ARRAYS
        packets.append(int(message.partition("C")[0])) #adds packet to array

        #not the most efficient but it gets it done
        for i in range(len(message)):
            if message[i] == ":":

                #TODO test these 2 lines to make sure they work
                parts = message.split(i)
                data_value = parts[1].split()[0] if len(parts) > 1 and len(parts[1].split()) > 0 else None      #make sure that this works
                
                datatype = message[i-1]

                if datatype == "T":
                    temp_d.append(data_value)
                elif datatype == "P":
                    pressure.append(data_value)
                    P = data_value

                    #CALCULATE ALTITUDE
                    # altitude calculation with international barometric formula
                    p0 = 1013.25 #hPa 
                    altitude.append(44330 * [1-(P/p0)^(1/5.255)]) #where P is pressure from sensor and p0 is reference pressure at sea level

                elif datatype == "C":
                    temp_a.append(data_value)

                #add more code when we have new data values

            

