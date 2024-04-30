from vpython import *
from time import *
import numpy as np
import math




scene.range=5
toRad=2*np.pi/360
toDeg=1/toRad
scene.forward=vector(-1,-1,-1)

scene.width=600
scene.height=600

xarrow=arrow(lenght=2, shaftwidth=.1, color=color.red,axis=vector(1,0,0))
yarrow=arrow(lenght=2, shaftwidth=.1, color=color.green,axis=vector(0,1,0))
zarrow=arrow(lenght=4, shaftwidth=.1, color=color.blue,axis=vector(0,0,1))

frontArrow=arrow(length=4,shaftwidth=.1,color=color.purple,axis=vector(1,0,0))
upArrow=arrow(length=1,shaftwidth=.1,color=color.magenta,axis=vector(0,1,0))
sideArrow=arrow(length=2,shaftwidth=.1,color=color.orange,axis=vector(0,0,1))

bBoard=cylinder(length=3,opacity=.8,pos=vector(0,0,0,),axis=vector(0,1,0))

myObj=compound([bBoard])

with open("output.csv") as readfile:    #** prepares to read data from text file **
    line = readfile.readline().rstrip('\n')         #**gets data from each line**
    while line: #repeats for every line
        splitPacket=line.split(",")
        roll=float(splitPacket[7])*toRad
        pitch=(float(splitPacket[8])-45)*toRad
        yaw=float(splitPacket[9])*toRad+np.pi
        print("Roll=",roll*toDeg," Pitch=",pitch*toDeg,"Yaw=",yaw*toDeg)
        rate(50)
        k=vector(cos(yaw)*cos(pitch), sin(pitch),sin(yaw)*cos(pitch))
        y=vector(0,1,0)
        s=cross(k,y)
        v=cross(s,k)
        vrot=v*cos(roll)+cross(k,v)*sin(roll)

        frontArrow.axis=k
        sideArrow.axis=cross(k,vrot)
        upArrow.axis=vrot
        myObj.axis=k
        myObj.up=vrot
        sideArrow.length=2
        frontArrow.length=4
        upArrow.length=1

        sleep(0.5)
        line = readfile.readline().rstrip('\n') 