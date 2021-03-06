from numpy import linspace, empty
from pylab import plot,show
import matplotlib.pyplot as plt

#define constants

C_m = 1.0
g_L = 1.0
tau_syn = 1.0
E_syn = 10.0
dt = 0.01
t_pre = 1.5
t_delay = 0.1

#build arrays

numbin = (int)(10.0/dt)
t = empty(numbin,float)
g_syn = empty(numbin,float)
I_syn = empty(numbin,float)
v_m = empty(numbin,float)
g_syn_f = empty(numbin,float)

#Initializing variables
t[0] = 0.0
g_syn[0.0]= 0.0
I_syn[0.0] = 0.0
v_m[0.0] = 0.0
g_syn_f[0.0] = 0.0

#Numerical intergration using Euler Scheme
#Further studies required in order to apply improved Euler scheme. Currently, 
#it is not fucntioning as I desire.

for i in range(numbin-1):
	t[i+1] = t[i] + dt
	#Generating Delta function-like behavior
	if abs(t[i+1] - t_pre - t_delay)<0.001:
		g_syn[i] = 1.0
	#When t is sufficiently close to signal-fire-time, this function
	#generates a pulse of intensity of 1. 
	g_syn[i+1] = g_syn[i] - (dt/tau_syn)*(g_syn[i])
	I_syn[i+1] = g_syn[i+1] * (v_m[i] - E_syn)
	v_m[i+1] = v_m[i] - (dt/C_m)*(g_L*v_m[i]+I_syn[i+1])

#Plotting the results. 
#For plot1 ; RP = Resting Potential
plot1 = plt.plot(t,v_m, label='Potential diff. w.r.t RP')
plot2 = plt.plot(t,g_syn*5,'r--',label ='Conductance')
plot2 = plt.plot(t,I_syn/5,'k:',label = 'Current generated by two channels')
plt.title("Assignment 2")
plt.xlabel("Time")
plt.legend(loc='upper right')
show()

