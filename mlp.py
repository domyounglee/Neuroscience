from numpy import linspace, empty , matrix, random
from pylab import *
import matplotlib.pyplot as plt

import numpy as np
import math
import random

N_i =2
N_h =2
N_o =1

trial= empty(10000,float)
t= empty(10000,float)
w_h= np.random.random((2,2)) ; w_o= np.random.random((2,2)) #I didnt subtract 0.5

r_i= np.matrix('0 1 0 1 ; 0 0 1 1')
r_d= np.matrix('0 1 1 0')

rand = random.random()


for k in range(10000):

    t[k]=k

    rand = random.random()
    i = math.ceil(4*rand)
        
    r_h= 1./(1+exp(-w_h*(r_i[:,i-1])))
    r_o= 1./(1+exp(-w_o*r_h))
    delta_o = multiply(multiply(r_o,(1-r_o)),(r_d[:,i-1]-r_o))
    delta_h= multiply(multiply(r_h,(1-r_h)),((w_o.T)*delta_o))

    w_o = w_o +0.6*(r_h*(delta_o.T)).T #I changed the learning rate to 0.6
    w_h = w_h +0.6*(r_i[:,i-1]*(delta_h.T)).T

    "test all pattern"
    r_o_test=1./(1+exp(-w_o*(1./(1+exp(-w_h*r_i)))))

    r_o_test2=(r_o_test[0]+r_o_test[1])*0.5

    trial[k]=0.5*(np.sum(multiply(r_o_test2-r_d,r_o_test2-r_d)))

a = r_o_test2

zerout = a.tolist()

peel = zerout[0]

print a 


for i in range(4):
    if peel[i]>0.7:
        peel[i]=1
    else:
        peel[i]=0


print peel
        
        

plot1 = plt.plot(t,trial,'m')

plt.title("MLP")
plt.xlabel("Trainingsteps")
plt.ylabel("training error")

show()




