import csv
import re

# Read data from text file
with open('data.txt', 'r') as file:
    data = file.readlines()

# Process each line and extract numbers
rows = []
for line in data:
    # Extract numerical values using regular expressions
    numbers = re.findall(r'[-+]?\d*\.\d+|\d+', line)
    rows.append(numbers)

# Write data to CSV file
with open('output.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(rows)

print("CSV file generated successfully.")

#1 CANMOTION T:20.63 P: 996 ADC:-50.00/ x:0.06 y:-0.05 z:-0.01/ r:355.69 p:-0.63 y:-1.50/A x:-0.09 y:0.21 z:9.53
#1- time 2- digital temperature 3- pressure 4- analogue temperature 5,6&7 - gyro 8,9&10 - eulder (roll pitch yaw) 11,12&13 are acceleration



