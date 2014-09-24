'''
@ytang 09/23/2014
This in-class exercise is importing the velocity versus time data "velocities.txt", and using trapezoidal method to integrate v over t
to find the area, which is the displacement delta_x. 
'''

import numpy as np
import pylab as pl

data = np.loadtxt('velocities.txt', float) #make sure the data type is floating point

#get the row and column numbers
row, col = data.shape

N=row  #N is the number of data points
a = data[0,0] #get the first element in the x axis
b = data[-1,0] #get the last element in the x axis

spacing = (b - a)/float(N)

S = 0.5*(data[0,1]+data[-1,1]) #0.5*(f(a)+f(b))

for counter in range(1, N-1): #the first and last points have alread been considered
   
    S += data[counter,1] #sum(f(a+kh)), f(a+kh) is given in the data already

S *= spacing

print "The integral equals: %f"  %S
print "Number of steps: %d"  %N 

#to check what's the data look like
pl.plot(data[:,0], data[:,1], marker='o')
pl.xlabel('t')
pl.ylabel('Vx')
pl.show()
