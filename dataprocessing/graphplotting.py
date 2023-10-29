import pandas as pd
import matplotlib.pyplot as plt
import io
#As is, this code will produce three graphs, Resultant_X_Acceleration against Time, as well Resultant_Y_Acceleration and Resultant_Z_Acceleration against Time. This isn't on example.csv but using the resultant vector program should give the required data.
#(Also creates a table but we'll have that anyways as it is the same as the .csv)
#I don't know how to plot the three lines on the same graph, if anyone knows how to then feel free to do so. Also feel free to use any loops to make this more efficient. Can't be bothered doing it myself.
#Could also do with fixing ymin and ymax to be the same for all three graphs, maybe will do later.
#This code requires a .csv file (see lines 11-13) with the exact variable names as in line 4.
#This code also requires some extensions. I personally installed Anaconda to get these as I couldn't get them from the extensions tab on VS.

#Note: This file needs changed. Copy paste the location of the .csv and leave in the form (Remember to change \ to /):
#table_1 = pd.read_csv(r'C:/Users/username/Desktop/example.csv')
table_1 = pd.read_csv(r'')

# Get the headers
print(table_1.head())

# Convert values to numpy arrays to graph
x = table_1['Time'].to_numpy()
y = table_1['Resultant_X_Acceleration'].to_numpy()
# Graph dimensions
xmin = x.min()
xmax = x.max()
ymin = y.min() - 5
ymax = y.max() + 5

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis
plt.plot(x,y) # make it scatterplot or line graph. (x,y,ro) for scattergraph

y = table_1['Resultant_Y_Acceleration'].to_numpy()

xmin = x.min()
xmax = x.max()
ymin = y.min() - 5
ymax = y.max() + 5

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis
plt.plot(x,y,color='red') # make it scatterplot or line graph. (x,y,ro) for scattergraph

y = table_1['Resultant_Z_Acceleration'].to_numpy()

xmin = x.min()
xmax = x.max()
ymin = y.min() - 5
ymax = y.max() + 5

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis
plt.plot(x,y,color='green') # make it scatterplot or line graph. (x,y,ro) for scattergraph

plt.show()
