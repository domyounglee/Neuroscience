from numpy import linspace, empty
from pylab import *
import matplotlib.pyplot as plt

import numpy as np
import math 


def Izh(a,b,c,d):

    dt = 0.01
    Nt = (int)(300.0/dt)
    t= empty(Nt,float)

    I =  0

    point=[]

    Vm =empty(Nt,float)
    Um =empty(Nt,float)

    t[0] = 0.0



    Vm[0]=-70.0
    Um[0]=(0.2)*(-70.0)


    def V(v,w,I):
       y = 0.04*(v**2) + 5*v + 140 - w + I
       return(y)

    def U(v,w,a,b):
       y = a*(b*v-w)
       return(y)

    for i in range(Nt-1):

        if i == (int)(Nt/6):
            I = 10
        if i == (int)(5*Nt/6):
            I = 0
            
        
        t[i+1] = t[i] + dt

       
        Vm[i+1] = Vm[i] + dt*V(Vm[i],Um[i],I)
        Um[i+1] = Um[i] + dt*U(Vm[i],Um[i],a,b)

        if Vm[i+1] > 30:
            Vm[i+1] = c
            Um[i+1] = Um[i+1] + d

    for i in range(0,Nt):
          point.append((t[i],Vm[i]))

    return point





Fast_spiking = Izh(0.1,0.2,-65,2)
Regular_spking = Izh(0.02,0.2,-65,8)
Chattering_spking = Izh(0.02,0.2,-50,2)

   

fig = plt.figure()

plt.rc("font",size=9)

ax1=fig.add_subplot(221); ax1.plot([p[0] for p in Fast_spiking], [p[1] for p  in Fast_spiking])
plt.title("Fastspiking ")

ax2=fig.add_subplot(223); ax2.plot([p[0] for p in Regular_spking], [p[1] for p in Regular_spking])
plt.title("Regularspiking")

ax2=fig.add_subplot(224); ax2.plot([p[0] for p in Chattering_spking], [p[1] for p in Chattering_spking])
plt.title("Chatteringspking")

plt.show()

   

    
    
   
