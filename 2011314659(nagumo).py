from numpy import linspace, empty
from pylab import *
import matplotlib.pyplot as plt
import numpy as np
import math 


f = open("Peak.txt",'w')

dt = 0.01
Nt = (int)(200.0/dt)
t= empty(Nt,float)

I =  empty(Nt,float)

Peak = []

Vm =empty(Nt,float)
Um =empty(Nt,float)


t[0] = 0.0

I=0.5

Vm[0]=0.0
Um[0]=0.0


a= 0.7
b= 0.8
tau= 12.5

def V(v,w,I):
   y = v - (v**3)/3 - w + I
   return(y)

def U(v,w,a,b,tau):
   y = (v+a-(b*w))/(tau)
   return(y)

for i in range(Nt-1):

    
    
    t[i+1] = t[i] + dt

   
    Vm[i+1] = Vm[i] + dt*V(Vm[i],Um[i],I)
    Um[i+1] = Um[i] + dt*U(Vm[i],Um[i],a,b,tau)

    data = "%f \n" %Vm[i]
    f.write(data)
    
   

for j in range(Nt-3):

   if Vm[j+1]>Vm[j] and Vm[j+2]<Vm[j+1] :
      Peak.append(Vm[j+1])

   

a = len(Peak)

print  "The number of peaks are %i" %a


f.close()


plot1 = plt.plot(t,Vm,'m')

plt.title("nagumo")
plt.xlabel("Time")
plt.ylabel("Voltage")

show()

   

    
    
   
