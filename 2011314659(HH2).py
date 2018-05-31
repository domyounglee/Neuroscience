from numpy import linspace, empty
from pylab import *
import matplotlib.pyplot as plt
import numpy as np
import math

def F(x):
    if abs(x)<0.00002: z=1
    else: z=x/(exp(x)-1)
    return z



g=empty(3,float)
E=empty(3,float)
Alpha=empty(3,float)
Beta=empty(3,float)
x=empty(3,float)
tau=empty(3,float)
x_0=empty(3,float)
gnmh=empty(3,float)
I=empty(3,float)
x_plot=empty(8000,float)
y_plot=empty(8000,float)

Freq=empty(21,float)
intcurr=empty(21,float)

#Maximal conductances
g[0]=36
g[1]=120
g[2]=0.3

#Battery voltage 
E[0]=-77
E[1]=50
E[2]=-55


x[0]=0
x[1]=0
x[2]=2


#initialization of some variables
I_ext=0
V=-65
t_rec=0

#timestep for integration
dt=0.01
for i in range(0,21):
    intcurr[i]=i
    for t in range(-3000,8000):  
        Peak = []
        if t==1000:      
             I_ext= i#external current is 15mA #
        if t==7000:     
             I_ext=0

        Alpha[0]=0.1*F((-50-V)/10)
        Alpha[1]=F((-35-V)/10)
        Alpha[2]=0.07*(math.exp((-V-60)/20))

        Beta[0]=0.125*(math.exp((-V-60)/80))
        Beta[1]=4*(math.exp((-V-60)/18))
        Beta[2]=1/exp((-3-0.1*V)+1)

        for j in range(0,3):
            tau[j]=1/(Alpha[j]+Beta[j])
            x_0[j]=(Alpha[j]*tau[j])
            x[j]=((1-dt/tau[j])*x[j])+dt*x_0[j]/tau[j]

        gnmh[0]=g[0]*(x[0]**4)
        gnmh[1]=g[1]*(x[1]**3)*x[2]
        gnmh[2]=g[2]

        for k in range(0,3):
            I[k]=gnmh[k]*(V-E[k])

        V=V+dt*(I_ext-sum(I))

        if t>=0:
            t_rec=t_rec+1
            x_plot[t]=t
            y_plot[t]=V

    for j in range(1,7998):

       if y_plot[j+1]>y_plot[j] and y_plot[j+2]<y_plot[j+1] and y_plot[j+1]>0 :
          Peak.append(y_plot[j+1])

       

    a = len(Peak)

    Freq[i]= a/0.06





plot1 = plt.plot(intcurr,Freq,'o')

plt.ylim(-2,120)
plt.title("Firing freq")
plt.xlabel("External current(mA)")
plt.ylabel("Firing freq(Hz)")

show()


    
