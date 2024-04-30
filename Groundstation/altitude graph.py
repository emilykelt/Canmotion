import numpy as np 
import matplotlib.pyplot as plt 

#CALCULATE ALTITUDE
# altitude calculation with international barometric formula
p0 = 1013.25 #hPa 

#TODO: calculate pressure and make pressure graph

altitudes = []
with open("output.csv") as readfile:    #** prepares to read data from text file **
        line = readfile.readline().rstrip('\n')         #**gets data from each line**
        while line: #repeats for every line
            items = line.split(",")
            pressure = float(items[2])
            altitude = (44330 * (1-(pressure/p0)**(1/5.255))) #where P is pressure from sensor and p0 is reference pressure at sea level
            altitudes.append(altitude)
            line = readfile.readline().rstrip('\n') 

# data to be plotted
x = np.arange(1, len(altitudes)+1) 
y = np.array(altitudes)
 
# plotting
plt.title("Altitude of Can's Descent") 
plt.xlabel("Time(s)") 
plt.ylabel("Altitude (m)") 
plt.plot(x, y, color ="green") 
plt.show()