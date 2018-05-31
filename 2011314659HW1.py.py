from numpy import linspace, empty
from pylab import *
import matplotlib.pyplot as plt

def velx(t):
   y = Vx
   return(y)

def velye(t):
   y = Vy - (Ge*t)
   return(y)


def velym(t):
   y = Vy - (Gm*t)
   return(y)

Vx = 10.0
Vy = 10.0
Ge = 9.8
Gm = 3.3 
dt = 0.1
Nt = (int)(10.0/dt)
t = empty(Nt,float)
Xe = empty(Nt,float)
Ye = empty(Nt,float)
Xm = empty(Nt,float)
Ym = empty(Nt,float)
t[0] = 0.0
Xe[0] = 0.0
Ye[0] = 0.0
Xm[0] = 0.0
Ym[0] = 0.0 

for i in range(Nt-1):
   t[i+1] = t[i] + dt
   
   velx2 = velx(t[i]) + (dt*velx(t[i+1]))
       
   Xe[i+1] = Xe[i] + (dt*velx(t[i]))
   Ye[i+1] = Ye[i] + (dt*velye(t[i]))
   


for i in range(Nt-1):
   t[i+1] = t[i] + dt

   velx2 = velx(t[i]) + (dt*velx(t[i+1]))
  
   Xm[i+1] = Xm[i] + (dt*velx(t[i]))
   Ym[i+1] = Ym[i] + (dt*velym(t[i]))




plot(Xm,Ym,'k')



plot1 = plt.plot(Xe,Ye,'o',label = 'On Earth')
plot2 = plt.plot(Xm,Ym,'b--',label = 'On Mars')
#Set a limit on plot-range
plt.xlim(0.0,100)
plt.ylim(0.0,20)
plt.title("Assignment 1")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc='upper right')
plt.show()
